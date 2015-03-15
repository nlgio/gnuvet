
class  IWrapper:#
    """helper to access rows from  a Table in the db, the Tablename is by definition
      the class name with one 's' appended, no schema support """
    pk=None #The Column Name of the primary key
    def get(cls, pkval, cn=None):
        """retrieve a row from the db and wrap it into our class,
          might yield to multiple instances in ram of the same row
        """
    def pkey(cls ):
        """return the name of the primary key column of our wrapped table"""
    def findall(cls, cond=None, orderby=1):
        """retrieve all rows from the db from our table which meet given cond,
         and wrap each into our class"""
    
    def reload(self ):
        """re-fetch the row from the db"""
    def update(self, **kw):
        "save modified values from kw into the row, afterwards update the obj"
        #doesnt check if we overwrite an meanwhile committed version
        #implementation doesnt have to read back from db until triggers are in use
    def insert(self ):
        "insert the obj as a row into our table and save the primary key given from the db"
        #the implementation might omitt the fallback of "insert into with default values"
        #doenst have to read back from db
    def delete(self):
        "delete the row from our table"
    
#from sqlite3_orm import DAL as Wrapper
from pgpsycopg2_orm import DAL as Wrapper

from datetime import date, datetime, timedelta

#staff=[]


class Appointment(Wrapper):
    "Scheduled Appointment with a Client"
    pk='app_id'
    def getClient(self ):
        return Client.get(self.app_cid)
    def lbshort(self ):
        return '%u %s %-12s %s' % ( self.app_cid, str(self.app_dt)[:16], self.getClient().c_sname, self.app_text )
def getTodaysAppointments():
    #return Appointment.findall("app_dt = date('now')", orderby = 'app_dt,1')
    return Appointment.findall('app_dt::date=now()::date', orderby='app_dt,1' )
    pass

#class Encounter(Wrapper): pass
class Symptom(Wrapper):
    pk='sy_id'
    def lbshort(self ):
        return '%u %s' % ( self.sy_id, self.symptom or '')
    
class Ch(Wrapper):
    "Clinical Record (EMR) tracks Activites to Patient - might trigger Invoice Lines"
    pk='ch_id'
    def lbshort(self ):
        return '%3u %s %-12s %s /%s' % ( self.ch_id, str(self.ch_date)[:16],
                              self.getSymptom().sy_short,
                                    self.ch_descr or '',
                                    self.ch_staff )
    def getSymptom(self ):
        return Symptom.get(self.ch_symp )
    def getPatient(self ):
        return Patient.get(self.ch_pid )
    def update(self, **kw):
        Wrapper.update(self, **kw)
        self.reload()
        self.ensureConsultAccLineFor()
        
    def ensureConsultAccLineFor(self):
        #now make sure there is an encounter fee for
        ## if another client  takes the charge  the record has to be inserted before ##
        ## each patient gets seperated fee, means client has to pay twice if he brings in two
        p = self.getPatient()
        for il in p.getAccLinesFor( 'acc_prid in (select pr_id from products where pr_type=6)' ):
            if il.acc_date.date() == self.ch_date.date() or il.acc_details.endswith( self.ch_date.strftime('%Y-%m-%d') ) :
                #ok there is one @@check if outside normal hours is expected
                if il.acc_qty >0:
                    return

        cp_code = 'constd'
        if self.ch_date.date().weekday() in ( 5,6) or self.ch_date.hour not in range(9,18): #@@other holidays
            cp_code='conooh4'
        cp = Product.get(cp_code, 'pr_short')
        details = '%s %s' % ( self.getSymptom().symptom, self.ch_date.strftime('%Y-%m-%d') )
        p.getClient().addAccLineFor( cp.pr_id , 1, details, acc_pid= p.p_id
                                     #, acc_date = self.ch_date
                                     )
        #@@broadcaster.broadcast('Fee was added')
        
class Addresse(Wrapper):
    "Postal Address"
    pk='addr_id'
    def validate(self):
        return 1
    def fmt3Lines(self):
        return '%s %s\n%s\n%s' % ( self.housen,self.street,self.city,self.postcode)
    
Address=Addresse

class PType(Wrapper):
    pk='pt_id'
    def lbshort(self ):
        return '%u %s' % (self.pt_id, self.pt_name)
class VAT(Wrapper):
    pk='vat_id'
    
from decimal import Decimal
class Product(Wrapper):
    "Service or Goods to be chargeable"
    pk='pr_id'
    def getVAT(self):
        return Decimal(100)*VAT.get(self.pr_vat).vat_rate
    vat=property(getVAT)
    
    def getType(self ):
        return PType.get(self.pr_type)
    def lbshort(self ):
        return '%u %s %.2f' % ( self.pr_id,self.pr_name, self.pr_nprice )

class Acc(Wrapper):
    "Invoice Line to be payed or refunded"
    pk='acc_id'
    def getLineTotal(self ):
        return self.acc_qty * self.acc_npr #* (1+ self.acc_vat/100.0 )
    def getProduct(self ):
        return Product.get(self.acc_prid)
    getItem=getProduct
    
    def isDraft(self ):
        return self.acc_inv is None #@@or Invoice.get(self.acc_inv).isDraft()
    #def getEMR(self ):
    #    return Ch.get(self.acc_ch)
    def getClient(self ):
        return Client.get(self.acc_cid)
    def getInvoice(self ):
        if self.acc_inv:
            return Invoice.get(self.acc_inv)
    def getPatient(self ):
        if self.acc_pid:
            return Patient.get(self.acc_pid )
    def lbshort(self):
        return '%u %-12s %s %3d %-12s %s' % ( self.acc_id, getattr(self.getPatient(),'p_name','')[:12], str(self.acc_date)[:10],self.acc_qty,self.getProduct().pr_short, self.acc_details or '')
AccLine=Acc

class Invoice(Wrapper):
    pk='invoice_id'
    def __init__(self, **kw):
        self.stmt_date=None
        Wrapper.__init__(self, **kw)
        
    def isDraft(self ):
        return self.stmt_date is None
    def getClient(self ):
        return Client.get(self.c_id )
        #might be not the same as the lines!
    def getFilename(self ):
        return '%u_%u.pdf' % (self.c_id,self.invoice_id)
    def getLines(self ):
        return Acc.findall('/*acc_cid=%u and*/ acc_inv=%u' % (self.c_id,self.invoice_id))
    def close(self ):
        assert self.stmt_date is None
        cli = self.getClient()
        #@@assert valid billing address
        those = self.getLines()
        assert len(those)
        total=sum([ il.getLineTotal() for il in those ])
        stmtDate = date.today() + timedelta(days=cli.toc)
        self.update(stmt_date=stmtDate, excl_vat=total ) #.strftime('%d.%m.%Y') )

        #did i ever mentioned transactions;-)
        if total >=0:
            cli.addPaym(total,'Invoice %u' % self.invoice_id,paytyp=0)
        else:
            cli.addPaym(total,'Credit Note %u' % self.invoice_id,paytyp=0 )
    def getLineTotal(self):
        return sum([ il.getLineTotal() for il in self.getLines() ])
    total=property(getLineTotal)

def fmt_yq(ts ):
    y = ts.strftime('%Y')
    m = int( ts.strftime('%m') )
    return '%s%u' % (y,1 + (m-1) // 3 )
    
     
def assignLines(cli ):
    #assign all new lines to an open invoice
    ##at the end of an quarter just loop over all clients and close the invoice with lines
    found=list()
    for line in cli.getAccLines():
        if line.acc_date.date() > date.today():
            break
        #if len(found)>0 and fmt_yq(line.acc_date) > fmt_yq(found[-1].acc_date): #quarter left
        #    break
        if line.isDraft():
            found.append(line)

    if len(found)==0: return #nothing to do
    inv=cli.getOpenInvoice()
    #total=0
    last_acc_date = date(2000,1,1)
    for line in found:
        assert line.isDraft()
        line.update(acc_inv=inv.invoice_id)
        #total += line.getLineTotal() #..if your policy is about cutting by amount
        last_acc_date = max(last_acc_date, line.acc_date.date() )
    inv.update(ref='Encounters until %s' % last_acc_date.strftime('%Y-%m-%d') )
    return inv
    
class PayMode(Wrapper):
    pk='pay_id'
    def lbshort(self ):
        return '%u %s' % ( self.pay_id, self.pay_mode )
PaymType=PayMode
class Paym(Wrapper):
    "Payment Record"
    pk='paym_id'
    def getType(self ):
        return PaymType.get(self.paytyp)
    def isDraft(self ):
        #return self.pay_date > date.today()- timedelta(days=7)
        return True

    def lbshort(self ):
        return '%3u %s %-8s %8.2f %s' % ( self.paym_id, self.pay_date, self.getType().pay_mode, self.pay_amount, self.pay_ref )
    def getAmountForSaldo(self):
        return self.pay_amount
    
class Client(Wrapper):
    pk='c_id'
    def _getFullname(self):
        return '%s, %s %s' % ( self.c_sname, self.c_fname, self.c_mname )
    fullname=property(_getFullname)
    
    def getLastEncDate(self ):
        return self.c_last
        #@@find all patients last emr date
    def lbshort(self ):
        return '%u %s %s' %(self.c_id,self.c_sname, self.c_fname ) #self.getAddress().city )
    def getAllPatients(self ):
        return Patient.findall('p_cid= %u' % self.c_id, orderby='dob,1')
    def addPatient(self, name, **kw ):
        new = Patient(p_cid=self.c_id, p_name=name,
                      #dob = date.today(),
                      **kw
                      #p_reg=date.today(), #@@db defaults
                      #p_last=datetime.now(),
                      #breed=1,
                      
                      )
        new.insert()
        return new
    
    def getAddress(self):
        if self.c_address:
            return Address.get(self.c_address)
    billingAddress=getAddress
    def setAddress(self, a ):
        "set the given address object to be the current postal address of the client to be used"
        #@@object must already be inserted
        self.update(c_address= a.addr_id )
    def addAddress(self, **kw):
        new = Address( **kw)
        new.insert()
        return new
    def getInvoices(self ):
        return Invoice.findall('c_id=%u' % self.c_id)
    def getOpenInvoice(self):
        "get the first draft invoice or create one if necessary "
        for inv in self.getInvoices():
            if inv.isDraft():
                return inv
        new = Invoice(c_id=self.c_id)
        new.insert()
        return new
    addInvoice = getOpenInvoice
    
    def addAccLineFor(self, pr_id,qty=1, details=None, **kw ):
        "add a line about what should be charged, patient is optional"
        pr = Product.get(pr_id)
        inv = self.getOpenInvoice()
        new=AccLine(acc_cid = self.c_id, acc_prid=pr_id,
                    acc_qty=qty,
                    acc_npr= pr.pr_nprice,
                    acc_details = details or '',
                    acc_inv = inv.invoice_id, #2015-04-15
                    **kw
                    )
        new.insert()
        return new
    def getAccLines(self):
        return AccLine.findall('acc_cid = %u' % self.c_id, orderby='acc_inv,acc_date,1' )
    
    def addPaym(self, amount, ref, **kw): #amount, ref, typ=1 ):
        "add Payments from Client or Liabilities / Refunds"
        new = Paym(pay_cid=self.c_id, pay_amount=amount, pay_ref = ref, **kw) #paytyp=typ )
        new.insert()
        return new
    def getPayments(self):
        "Payments and Liabilites"
        return Paym.findall('pay_cid=%u' % self.c_id, orderby='pay_date,1' )
        
    def outstAmount(self ):
        "outstanding Amount as of today"
        #return( "select /* outstAmount */ sum(pay_ampount) from payms where pay_cid=%u and pay_date <= date('now') " , self.c_id )
        return sum([p.getAmountForSaldo() for p in self.getPayments() if p.pay_date <= date.today() ] )

    def addSchedApp(self, dt, subj, **kw ):
        assert dt.date() >= date.today()
        new=Appointment( app_cid = self.c_id, app_dt=dt, app_text=subj, **kw)
        new.insert()
        return new
    def cancelAppoint(self, this ):
        this.delete()
        
class Client_Combo(Wrapper):
    #A view helps in our lookups
    def lbshort(self ):
        return Client.get(self.c_id).lbshort()

class Weight(Wrapper):
    pk='w_id'
    def lbshort(self ):
        return '%.3f (kg) on %s' % ( self.weight, self.w_date ) #.strftime('%d-%b-%Y') )
class Specie(Wrapper):
    pk='spec_id'
    def lbshort(self ):
        return '%u %s' % ( self.spec_id, self.spec_name )
    def getReqVaccinations(self ):
        found={}
        for rec in  Vaccination.findall('vac_spec=%u' % self.spec_id ):
            found[rec.getType().vt_type ]=None
        return found.keys()
    
class Breed(Wrapper):
    pk='breed_id'
    def lbshort(self ):
        return '%u %s' % ( self.breed_id, self.breed_name )
    def getSpecies(self ):
        return Specie.get(self.b_spec )
class Chronic(Wrapper):
    pk='chr_id'


def fmtAge( delta ):
    y,remd=  divmod(delta.days, 365 ) #mx.DateTIme was delta.day
    return '%ua %um' % ( y,remd//30 )

class VType(Wrapper):
    pk='vt_id'
    def lbshort(self ):
        return '%u %s' % ( self.vt_id, self.vt_type )
class Vaccination(Wrapper):
    pk='vac_id'
    def getType(self ):
        return VType.get(self.vac_type)
    def lbshort(self ):
        '%u %s' %  (self.vac_id, self.vac_type ) #self.validity
    def getProduct(self ):
        return Product.get(self.vac_prid) #vac_sid
    
class Patient(Wrapper):
    pk='p_id'
    def age(self ):
        d = self.deceased or date.today()
        return d - self.dob
        
    def lbshort(self ):
        return '%s %-12s (%s)' % ( self.p_id,  self.p_name[:12] , self.getClient().c_sname )

    def getAccLinesFor(self, where=None ):
        return AccLine.findall('acc_pid = %u and %s' % (self.p_id,where or '1=1'), orderby='acc_inv,acc_date,1' )
    def getClient(self):
        return Client.get(self.p_cid)
    def getChronics(self ):
        those = list()
        for i,el in enumerate(Chronic.findall() ):
            if self.chr % 2**i:
                those.append( el.chr_name )
        return those
    def getWeights(self):
        return Weight.findall('w_pid=%u' % self.p_id, orderby='w_date' )
    def addWeight(self, kg, **kw):
        m=Weight(w_pid=self.p_id , weight=kg, **kw)
        m.insert()
        return m
    def getWeight(self):
        measures = [None] +self.getWeights()
        return measures[-1]
    def getBreed(self ):
        return Breed.get(self.breed )

    def addEMR(self, **kw ):
        new = Ch( ch_pid = self.p_id, **kw )
        new.insert()
        return new
    def getEMR(self ):
        return Ch.findall('ch_pid = %u' % self.p_id , orderby='ch_date,1')
    
if __name__=='__main__':
    #from sqlite3_orm import get_conn
    #conn=get_conn('gnuv39049.db')
    from pgpsycopg2_orm import get_conn
    conn=get_conn('host=raspberrypi dbname=gnuvet user=nl')
    
    #db = pg.DB('gnuvet')
    p=Patient.get(62)
    print p, p.p_name
    c = Client.get(3)
    print c, c.__dict__
    for cp in  c.getAllPatients():
        print cp, cp.p_name
    #conn.close()

    
    for it in Ch.findall('ch_pid=100'):
        #print it
        #conn.execute('begin')
        it.ensureConsultAccLineFor()
        #conn.execute('commit')

        
    for cli in Client.findall('c_id=100'):
        #conn.execute('begin')
        
        inv = assignLines(cli)
        if inv:
            inv.close()
        #conn.execute('commit')
    conn.close()
    