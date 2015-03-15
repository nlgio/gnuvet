#!/usr/bin/python
from random import sample, random, randint, choice

from string import letters, digits, upper
#from decimal import Decimal

import model

from datetime import date, datetime, timedelta

def genCode(desc):
    x= desc[:1] + ''.join(sample(digits,5))
    return upper(x)

def pseudo_now():
    #between 9-21h
    return datetime( randint(2010,2016),randint(1,12),randint(1,28),
                                       randint(9,21), randint(0,59), randint(0,59)
                                       )

sym_list = []
breed_list = []
class ClientGenerator( object ):
    def new(self, **kw):
        
        cli = model.Client(c_sname= genCode('T') )
        #give sometimes another postal address
        if choice((True,False)):
            a = cli.addAddress( postcode=randint(12,90), city=genCode('C'), street=genCode('S') )
            cli.c_address= a.addr_id
        cli.insert()
        #cli.update( c_address = a.addr_id )

        #at least one Patient
        cli.begin()
        for i in range( randint(0,4)):
            p = cli.addPatient( genCode( 'P' ),
                      breed = choice(breed_list),
                      dob = date(randint(1999,2011),randint(1,12),randint(1,28)),
                        sex=choice(['f','n']),
                      )
            #a handful of clinical records..
            
            for i in range(randint(0,20)):
                w=p.addWeight( randint(19,99 ), w_date = pseudo_now() )
                ch = p.addEMR(ch_symp = choice(sym_list),
                    ch_descr = ''.join(sample(letters,35)),
                    ch_date = pseudo_now(),
                    
                    )
                ch.ensureConsultAccLineFor() #2015-03-14
            if choice((True,False)):
                p.update( deceased = date.today() )
        cli.commit()
        
        #add some Payments and invoice lines
        cli.begin()
        for i in range(randint(0,12)):
            am = -random()*randint(9,400)
            ref = 'Test %s' % genCode('O')
            typ= randint(0,5)
            if typ==0:
                am=-am
            p=cli.addPaym(am, ref, paytyp=typ,
                          pay_date = date(randint(1999,2011),randint(1,12),randint(1,28)) )

        #prod_types = [ pt.pt_id for pt in model.PType.findall() ]
        prods = [ pr.pr_id for pr in model.Product.findall() ]
        for i in range(randint(21,99)):
            il=cli.addAccLineFor( choice(prods), randint(1,3), acc_date = pseudo_now() )

        cli.commit()
        return cli
    
    
    
def main():
    x = ClientGenerator()
    for i in range(68,70):
        it = x.new()
        print it.c_sname

            
if __name__=='__main__':
    #from sqlite3_orm import get_conn
    #get_conn('gnuv39049.db')
    from pgpsycopg2_orm import get_conn
    conn=get_conn('host=raspberrypi dbname=gnuvet user=nl')
    
    sym_list = [ s.sy_id for s in model.Symptom.findall() ]
    breed_list = [br.breed_id for br in model.Breed.findall() ]

    #model.slurp('files/ge2012')
    main()
    #addClientCredits()
    
    #print model.root
    #print model.root
    #model.dump('files/ge2012')
    
