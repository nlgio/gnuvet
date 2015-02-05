"""Payment dialog -- to be called from client only."""
# TODO:
# check for things like card or cheque payment only be booked as payed when
# payment is confirmed

from decimal import Decimal
##from datetime import date, datetime # ?
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import (QMainWindow, QAction)
from payment_ui import Ui_Payment

class Payment(QMainWindow):
    def __init__(self, parent=None, db=None, options={},
                 cid=0, pid=0, staffid=0): # these 3 nec?
        super(Payment, self).__init__(parent)
        self.db = db
        self.options = options
        self.cid = cid
        self.pid = pid
        self.staffid = staffid
        self.w = Ui_Payment()
        self.w.setupUi(self)
        closeA = QAction(self)
        closeA.setShortcut('Ctrl+W')
        self.addAction(closeA)
        closeA.triggered.connect(self.close)
        self.w.paymentSb.valueChanged.connect(self.calc)
        self.w.cashRb.toggled.connect(self.radiocheck)
        self.w.cardRb.toggled.connect(self.radiocheck)
        self.w.cheqRb.toggled.connect(self.radiocheck)
        self.w.bankRb.toggled.connect(self.radiocheck)
        self.w.buttonBox.rejected.connect(self.close)
        self.w.invoiceDd.addItem(self.tr("Oldest invoice(s)"), 0)
        self.w.invoiceDd.addItem(self.tr("Most recent invoice"), 1)
        self.devel()

    def devel(self):
        self.baltot = Decimal('80.63')
        self.balpat = Decimal('80.63')
        self.balcli = Decimal('80.63')
        self.w.baltot.setText(str(self.baltot))
        self.w.balcli.setText(str(self.balcli))
        self.w.balpat.setText(str(self.balpat))

    def calc(self, val):
        dif = Decimal(str(val)) - self.balpat
        if dif < 0:
            self.w.change.setText('0.00')
        else:
            self.w.change.setText(str(dif))
            
    def radiocheck(self):
        pass

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication, QShortcut
    from options import defaults as options
    a = QApplication([])
    w = Payment(None, [], options)
    w.show()
    exit(a.exec_())
