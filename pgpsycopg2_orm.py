#!/usr/bin/python
# -*- coding:latin1 -*-
# lightweight transient orm

import psycopg2
conn = None
debug=1

    

class DAL(object):
    #implements IWrapper
    pk=None
    def _pkey(cls ):
        return cls.pk
    pkey=classmethod(_pkey)
    
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def _get(cls, val, cn=None ):
        try:
            me, = cls.findall('%s=%%s' % (cn or cls.pk,),val )
            return me
        except ValueError: #row not found
            return None
    get=classmethod(_get)

    def reload(self ):
        c = conn.cursor()
        val = self.__dict__[self.pk]
        sql = 'select * from %ss where %s = %u ' % (self.__class__.__name__, self.pk, val )
        if debug: print sql
        c.execute(sql)
        row = c.fetchone()
        cnames = [x[0] for x in c.description ]
        kw = dict(zip(cnames,row))
        self.__dict__.update( kw)
        
    def _findall(cls, where=None, *args, **kw ):
        res = list()
        c = conn.cursor()
        sql = 'select * from %ss where %s order by %s' % (cls.__name__, where or '1=1',
                kw.get('orderby','1') )
        if debug: print sql,args
        c.execute(sql, args)
        cnames = [x[0] for x in c.description ] 
        for row in c.fetchall():
            kw = dict(zip(cnames,row) )
            obj = cls(**kw)
            res.append(obj)
        return res
        
    findall = classmethod(_findall)
    
    def update(self, **kw):
        keys,values=list(),list()
        for k,v in kw.items():
            if k == 'oid' or k.startswith('_'): # or k==self.pk :
                #we allow update of pkey 
                continue
            try:
                if hasattr(self,k) and unicode(v) == unicode(self.__dict__[k]): #unchanged..
                    continue
            except:
                print "failed comparison against old value for %s" % k
                
            keys.append('%s= %%s ' % k)
            values.append(v)
        if len(keys)==0: return #nothing to update
        
        values.append( getattr(self,self.pk) )


        c = conn.cursor()
        
        sql = 'update %ss set %s where %s = %%s ' % ( self.__class__.__name__,
                ','.join(keys), self.pk )
        if debug: print sql,values
        c.execute(sql, values)
        
        self.__dict__.update(kw)
        
    def insert(self ):
        keys,values = list(),list()
        for k,v in self.__dict__.items():
            if k == 'oid' or k.startswith('_'):
                continue
            keys.append(k)
            values.append(v)
        
        c = conn.cursor()
        
        sql = 'insert into %ss (%s) values (%s) returning %s' % (self.__class__.__name__,
                                                        ','.join(keys),
                                                        ','.join( map(lambda x:'%s',keys) ),
                                                                 self.pk
                                                        )
        if debug: print sql,values
        c.execute(sql,values)
        setattr(self, self.pk, c.fetchone()[0] )
        
        #problem: object has evtl not all attributes from the db record, refetch?
        #self.reload()
        
    def delete(self ):
        c = conn.cursor()
        sql = 'delete from %ss where %s = %%s' % (self.__class__.__name__, self.pk)
        pkval = getattr(self, self.pk)
        if debug:print sql, (pkval,)
        c.execute(sql, (pkval,) )

    #tr handling
    def rollback(self):
        conn.rollback()
    begin=rollback
    def commit(self):
        conn.commit()

import broker


def get_conn(dsn):
    global conn
    '''prepare and register a connection'''
    conn = psycopg2.connect(dsn)
    conn.set_isolation_level( psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    #conn.set_client_encoding('UTF8')
    print "connected"
    broker.Register('conn',conn)
    return conn
        

    
if __name__=='__main__':
    pass
