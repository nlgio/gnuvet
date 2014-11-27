"""Client window."""
# TODO:
# add buttons for patient: New MarkAsRIP
#     ChangeOwner only from patient window
#  and resp Actions/functions
#  and resp button connections...

from datetime import date
from decimal import Decimal as D
from psycopg2 import OperationalError
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QAction, QMainWindow, QMenu
import gv_qrc
from keycheck import Keycheck
from util import ch_conn, gprice, money, querydb # ch_conn so far unused
from client_ui import Ui_Client

class Client(QMainWindow):
    """The client window, from which to choose a patient and such."""
    # signals:
    gvquit   = pyqtSignal(bool)
    helpsig  = pyqtSignal(str)
    savestate = pyqtSignal(str)

    # vars:
    db_err = changes = shutdown = False

    def __init__(self, parent=None, cid=0):
        super(Client, self).__init__(parent)
        self.conns  = {} # pyqt bug, disconnect() w/o arg can segfault
        self.sigs   = {}
        self.cid = cid
        self.w = Ui_Client()
        self.w.setupUi(self)
        keych = Keycheck(self)
        self.installEventFilter(keych)
        #    LOCAL VARIABLES
        #    ACTIONS
        closeA = QAction(self.tr('Close &Window'), self)
        closeA.setAutoRepeat(0)
        closeA.setShortcut(self.tr('Ctrl+W'))
        closeA.setStatusTip(self.tr('Close this window'))
        self.dbA = QAction(self.tr('&Reconnect to database'), self)
        self.dbA.setAutoRepeat(0)
        self.dbA.setShortcut(self.tr('Ctrl+R'))
        self.dbA.setStatusTip(self.tr('Try to reconnect to database'))
        aboutA = QAction(self.tr('About &Gnuvet'), self)
        aboutA.setAutoRepeat(0)
        aboutA.setStatusTip(self.tr('GnuVet version info'))
        helpA = QAction(self.tr('&Help'), self)
        helpA.setAutoRepeat(0)
        helpA.setShortcut(self.tr('F1'))
        helpA.setStatusTip(self.tr('context sensitive help'))
        quitA = QAction(self.tr('&Quit GnuVet'), self)
        quitA.setAutoRepeat(0)
        quitA.setShortcut(self.tr('Ctrl+Q'))
        quitA.setStatusTip(self.tr('Quit GnuVet'))
        self.editA = QAction(self.tr('&Edit Client'), self)
        self.editA.setAutoRepeat(0)
        self.editA.setShortcut(self.tr('Ctrl+E'))
        self.editA.setStatusTip(self.tr('Edit client record'))
        self.mrgA = QAction(self.tr('&Merge Client'), self)
        self.mrgA.setAutoRepeat(0)
        self.mrgA.setStatusTip(
            self.tr('Merge this client\'s accounts if you have more than one'))
        self.newpatA = QAction(self.tr('&Patient'), self)
        self.newpatA.setAutoRepeat(0)
        self.newpatA.setShortcut(self.tr('Ctrl+P'))
        self.newpatA.setStatusTip(self.tr("Add a patient to this client"))
        self.newsaleA = QAction(self.tr('S&ale'), self)
        self.newsaleA.setAutoRepeat(0)
        self.newsaleA.setShortcut(self.tr('Ctrl+A'))
        self.newsaleA.setStatusTip(self.tr('Enter patient-unrelated sale'))
        self.newpayA = QAction(self.tr('Pa&yment'), self)
        self.newpayA.setAutoRepeat(0)
        self.newpayA.setShortcut(self.tr('Ctrl+Y'))
        self.newpayA.setStatusTip(self.tr('Take payment'))
        self.rippatA = QAction(
            self.tr('&Mark patient deceased'), self)
        self.rippatA.setAutoRepeat(0)
        self.rippatA.setShortcut(self.tr('Ctrl+K'))
        self.rippatA.setStatusTip(self.tr('Mark selected patient as deceased'))
        # ...
        #    MENUES
        taskM = QMenu(self.w.menubar)
        taskM.setTitle(self.tr('&Task'))
        self.w.menubar.addAction(taskM.menuAction())
        newM = QMenu(self.w.menubar)
        newM.setTitle(self.tr('&New'))
        self.w.menubar.addAction(newM.menuAction())
        helpM = QMenu(self.w.menubar)
        helpM.setTitle(self.tr('&Help'))
        self.w.menubar.addAction(helpM.menuAction())
        #    SUBMENUES
        taskM.addAction(self.dbA)
        taskM.addSeparator()
        taskM.addAction(self.editA)
        taskM.addAction(self.mrgA)
        taskM.addAction(self.rippatA)
        taskM.addSeparator()
        taskM.addAction(closeA)
        taskM.addAction(quitA)
        taskM.setSeparatorsCollapsible(1)
        newM.addAction(self.newpatA)
        newM.addAction(self.newsaleA)
        newM.addAction(self.newpayA)
        helpM.addAction(helpA)
        helpM.addSeparator()
        helpM.addAction(aboutA)
        #    ACTION CONNECTIONS
        closeA.triggered.connect(self.close)
        self.editA.triggered.connect(self.editc)
        helpA.triggered.connect(self.help_self)
        quitA.triggered.connect(self.gv_quitconfirm)
        self.mrgA.triggered.connect(self.merge)
        self.newpatA.triggered.connect(self.addpat)
        self.newsaleA.triggered.connect(self.sale)
        self.newpayA.triggered.connect(self.payment)
        self.rippatA.triggered.connect(self.rip)
        #    PARENT CONNECTIONS
        if parent: # devel if
            if parent.gaia == 'gaia':
                self.gaia = parent
            else:
                self.gaia = parent.gaia
            self.dbA.triggered.connect(self.gaia.db_connect)
            aboutA.triggered.connect(self.gaia.about)
            self.gaia.gvquit.connect(self.gv_quit)
            self.gaia.dbstate.connect(self.db_state)
            ## self.savestate.connect(self.gaia.state_write)
            self.helpsig.connect(self.gaia.gv_help)
            self.db = self.gaia.db
            self.staffid = self.gaia.staffid
            self.options = self.gaia.options
        else:
            import dbmod
            dbh = dbmod.Db_handler('enno')
            self.db = dbh.db_connect()
            self.staffid = 1
            from options import defaults as options
            self.options = options
        #    BUTTON CONNECTIONS
        self.w.cancelPb.clicked.connect(self.close)
        #    INIT # hierwei ck old files
        #ch_conn(self, 'enter', self.keych.enter, self.w.mainPb.click)
        #self.w.mainPb.clicked.connect(self.whatever)
        self.dbA.setVisible(0)
        self.dbA.setEnabled(0)
        try:
            self.curs = self.db.cursor()
        except (OperationalError, AttributeError) as e: # no db connection
            print('db.cursor(): {}'.format(e))
            self.db_state(e)
            return
        logname = 'no login' # neu
        lname = querydb(
            self,
            'select stf_logname from staff where stf_id=%s', (self.staffid,))
        if lname is None:  return # db error
        logname = lname[0][0]
        self.w.lLb.setText(logname)
        self.cli_data()
        self.get_pats()

    def addpat(self):
        print('client.addpat not yet implemented')
        self.origin.sae_pat(cid=self.cid, act='a') # hierwei
        
    def cli_data(self):
        """Collect client data including associated patients."""
        res = querydb(
            self,
            'select t_title,c_sname,c_mname,c_fname,housen,street,village,city,'
            'region,postcode,c_telhome,c_telwork,c_mobile1,c_mobile2,c_email,'
            'baddebt,c_reg,c_last,c_anno from clients,titles,addresses where '
            't_id=c_title and c_address=addr_id and c_id=%s',
            (self.cid,))
        if res is None:  return # db error
        for e in res:
            name = ' '.join([e[0], e[1]])
            if e[2]:
                name = ', '.join([name, e[2]])
            name = ' '.join([name, e[3]])
            self.w.nameLb.setText(name)
            self.w.addr1Lb.setText(', '.join([s for s in e[4:6] if s]))
            self.w.addr2Lb.setText(', '.join([s for s in e[6:8] if s]))
            self.w.addr3Lb.setText(e[9])
            self.w.telhomeLb.setText(self.tr('Home: ') + e[10])
            self.w.telworkLb.setText(self.tr('Work: ') + e[11])
            self.w.mobile1Lb.setText(e[12])
            self.w.mobile2Lb.setText(e[13])
            self.w.emailLb.setText(e[14])
            self.w.bdPix.setVisible(e[15])
            self.w.regdateLb.setText(e[16].strftime('%d.%m.%y'))
            self.w.ldateLb.setText(e[17].strftime('%d.%m.%y'))
            if e[18]: # devel if
                self.w.annotxtLb.setText(e[18])
            else:
                self.w.annotxtLb.setText(
                    'This is our first client, being the first sentient being '
                    'to have brought patients to our GnuVet practice.')
        tables = querydb( # hierwei ck dependencies of tables for creation!
            self,
            "select tablename from pg_tables where tablename='acc{}'".format(
                self.cid))
        if tables == None:  return # db error
        if not tables[0][0]:
            suc = querydb(
                self,
                'create table acc{}(acc_id serial primary key,acc_pid integer '
                'not null references patients,acc_prid integer not null '
                'references prod{},acc_npr numeric(9,2) not null,acc_vat '
                'integer not null references vats,acc_paid boo not null '
                'default false'.format(self.cid,self.pid))
        cbal = D('0.00')
        pats = querydb(
            self,
            'select p_id from patients where p_cid=%s', (self.cid,))
        if pats is None:  return # db error
        pats = [e[0] for e in pats]
        for p in pats:
            ## hierwei: error if no accN table!
            addend = querydb(
                self,
                'select acc_npr,vat_rate,count from acc{0},prod{1},vats '
                'where acc_vat=vat_id and acc_prid=prod{1}.id and acc_pid='
                '%s and acc_paid is null'.format(self.cid, p), (p,))
            if addend is None:  return # db error
            for e in addend:
                cbal += money(gprice(e[0], e[1]), e[2])
        self.w.balanceLb.setText(str(cbal))
        
    def closeEvent(self, ev):
        if self.gaia:
            self.gaia.xy_decr()

    def dbdep_enable(self, yes=True):
        """En- or disable db dependent actions."""
        for action in (self.editA, self.mrgA, self.payA, self.saleA):
            action.setEnabled(yes)
        self.dbA.setVisible(not yes)
        self.dbA.setEnabled(not yes)
        
    def db_state(self, msg=''):
        """Actions to be taken on db loss or gain."""
        self.dberr = msg and True or False
        self.w.no_dbconn.setVisible(self.dberr)
        self.dbstate.emit(not self.dberr)
        self.dbdep_enable(not self.dberr)
        if not hasattr(self, 'warnw'):
            from warn import Warning
        self.warnw = Warning(self, self.tr('GnuVet: Db Error'), msg)
        if not self.isVisible(): # ?
            self.warnw.closed.connect(self.show)

    def editc(self):
        pass

    def get_pats(self):
        """Collect this client's patients."""
        res = querydb(
            self,
            'select p_name,xbreed,breed_abbr,breed_name,sex,neutd,case when '
            "b1.bcol is not null then b1.bcol else '' end||case when b2.bcol "
            "is not null then '-'||b2.bcol else '' end||case when b3.bcol is "
            "not null then '-'||b3.bcol else '' end,dob,dobest,vicious,rip "
            'from patients,breeds,colours,basecolours b1,basecolours b2,'
            'basecolours b3 where p_cid=%s and breed=breed_id and colour='
            'col_id and b1.bcol_id=col1 and b2.bcol_id=col2 and b3.bcol_id='
            'col3 order by p_name', (self.cid,))
        if res is None:  return # db error
        if not res:
            self.w.plist.append_row(
                [self.tr('No patients on this clients record')])
            self.w.plist.set_colwidth(0, self.w.plist.width())
            return
        pheader = map(self.tr,
                      ['Name', 'Breed', 'Sex', 'Colour', 'dob', 'vic', 'rip'])
        self.w.plist.set_headers(pheader)
        for e in res:
            self.w.plist.append_row([
                e[0],
                e[1] and e[2] + '-X' or e[2], # breed
                e[4]+(e[5] is None and '-n?' or e[5] and '-n' or ''), #sex
                e[6], # colour
                e[8] and '({})'.format(e[7].strftime('%d.%m.%y')) or
                e[7].strftime('%d.%m.%y'), # dob
                e[9] and 'v' or '',
                e[10] and 'rip' or ''])
            self.w.plist.cell(len(self.w.plist.lrows)-1, 1).setToolTip(e[3])
        self.w.plist.set_colwidth(0, 100)
        self.w.plist.set_colwidth(1, 100)
        self.w.plist.set_colwidth(2, 100)
        self.w.plist.set_colwidth(3, 200)
        self.w.plist.set_colwidth(4, 100)
        self.w.plist.set_colwidth(5, 50)
        self.w.plist.set_colwidth(6, 50)
        self.w.plist.setFocus()

    def gv_quit(self, quitnow=False):
        """Signal children if quitting GnuVet or not."""
        self.shutdown = quitnow
        self.gvquit.emit(quitnow)
        if quitnow:
            self.close()
    
    def gv_quitconfirm(self):
        if self.gaia:
            self.gaia.gv_quitconfirm()
        else:
            exit()
        
    def help_self(self):
        self.helpsig.emit('client.html')

    def merge(self):
        print('client.merge not yet implemented')

    def payment(self):
        print('client.payment not yet implemented')
        
    def rip(self):
        print('client.rip not yet implemented')

    def sale(self):
        print('client.sale not yet implemented')
        
if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    a = QApplication([])
    ding = Client(None, 2)
    ding.show()
    exit(a.exec_())
