#!/usr/bin/python
# -*- coding:latin1 -*-
# lightweight transient orm
#2015-03-13 if compare against old value take into consideration that attribute might not exist

import sqlite3
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
        c = conn.cursor()
        sql = 'select * from %ss where %s = ? ' % (cls.__name__, cn or cls.pk )
        if debug: print sql,(val,)
        c.execute(sql, (val,) )
        row = c.fetchone()
        return cls(**row )
        
        
    get=classmethod(_get)

    def reload(self ):
        c = conn.cursor()
        val = self.__dict__[self.pk]
        sql = 'select * from %ss where %s = %u ' % (self.__class__.__name__, self.pk, val )
        if debug: print sql
        c.execute(sql)
        row = c.fetchone()
        self.__dict__.update( row)
        
    def _findall(cls, where=None, *args, **kw ):
        c = conn.cursor()
        sql = 'select * from %ss where %s order by %s' % (cls.__name__, where or '1=1',
                kw.get('orderby','1') )
        if debug: print sql,args
        c.execute(sql, args)
        return [ cls(**row) for row in c.fetchall() ]
    
    findall = classmethod(_findall)
    
    def update(self, **kw):
        keys,values=list(),list()
        for k,v in kw.items():
            if k == 'rowid' or k.startswith('_'): # or k==self.pk :
                #we allow update of pkey 
                continue
            try:
                if hasattr(self,k) and unicode(v) == unicode(self.__dict__[k]): #unchanged..
                    continue
            except:
                print "failed comparison against old value for %s" % k
            keys.append('%s=?' % k)
            values.append(v)
        if len(keys)==0: return #nothing to update
        
        values.append( getattr(self,self.pk) )


        c = conn.cursor()
        
        sql = 'update %ss set %s where %s = ? ' % ( self.__class__.__name__,
                ','.join(keys), self.pk )
        if debug: print sql,values
        c.execute(sql, values)
        
        self.__dict__.update(kw)
        
    def insert(self ):
        keys,values = list(),list()
        for k,v in self.__dict__.items():
            if k == 'rowid' or k.startswith('_'):
                continue
            keys.append(k)
            values.append(v)
        
        c = conn.cursor()
        
        sql = 'insert into %ss (%s) values (%s) ' % (self.__class__.__name__,
                                                        ','.join(keys),
                                                        ','.join( '?' * len(keys) )
                                                        )
        if debug: print sql,values
        c.execute(sql,values)
        setattr(self, self.pk, c.lastrowid)
        
        #problem: object has evtl not all attributes from the db record, refetch?
        #self.reload()
        
    def delete(self ):
        c = conn.cursor()
        sql = 'delete from %ss where %s = ?' % (self.__class__.__name__, self.pk)
        pkval = getattr(self, self.pk)
        if debug:print sql, (pkval,)
        c.execute(sql, (pkval,) )

    #tr handling
    def begin(self):
        conn.execute('begin ')
    def rollback(self):
        conn.execute('rollback')
    def commit(self):
        conn.execute('commit')

import broker


def get_conn(fn):
    global conn
    '''prepare and register a connection'''
    conn = sqlite3.connect(fn , #'files/data.db',
                         detect_types = sqlite3.PARSE_DECLTYPES,
                         isolation_level=None #autocommit
                         )
    conn.row_factory=sqlite3.Row
    broker.Register('conn',conn)
    return conn
        

    
if __name__=='__main__':
    pass
