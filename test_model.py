#pyunit.sf.net
import unittest

#Mock
import model
#from decimal import Decimal
from datetime import date, datetime, timedelta


#make sure appointments get not overlapped
#there is an consul. fee for each ch record
#the consul. fee is according to the datetime
#verify address verification
#client adds address, is not the default one if not explicity said
#every accline is on an invoice
#after vat change the vat part of accline is still the same
#cannot add/remove/unlink lines on already closed invoices
#look at the case where accline.invoice.client is not the same as accline.patient.client
#if there are 2 open invoices check that the first one is returned
#make sure outst Amount doesnt include future-dated payments
#check the age calculation

from gen_testrecs import genCode

class ExampleTeatCase(unittest.TestCase):
    def setUp(self):
        self.cli=model.Client(c_sname= genCode('T'), c_reg = date.today() )
        self.cli.insert()
        self.inv1  = self.cli.addInvoice(ref='B1')
        self.inv2  = self.cli.addInvoice(ref='B2')
        
        
    def tearDown(self):
        pass
    
        
    def test1(self):
        self.assertEquals( self.inv1.invoice_id, self.inv2.invoice_id )
        
    
    def test2(self ):
        pass
        
class Example2Case(unittest.TestCase):
    def setUp(self):
        pass
        
        
    def tearDown(self):
        pass
    
        
    
    
    def test2(self ):
        pass
        
def suite():
    #suite1 = unittest.makeSuite(xTestCase)
    #suite2 = unittest.makeSuite(xTestCase)
    #return unittest.TestSuite( (suite1, suite2) )
    pass

if __name__=='__main__':
    from sqlite3_orm import get_conn
    #get_conn('gnuv39049.db')
    get_conn(':memory:')
    unittest.main()
    #unittest.TextTestRunner().run( suite() )

    
