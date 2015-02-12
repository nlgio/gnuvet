"""Payment dialog -- to be called from client only."""
# TODO:
# check for things like card or cheque payment only be booked as payed when
# payment is confirmed

from decimal import Decimal
##from datetime import date, datetime # ?
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import (QMainWindow, QAction)
from payment_ui import Ui_Payment
from util import ch_conn

class Payment(QMainWindow):
    def __init__(self, parent=None, totbalv=0, curbalv=0):
        super(Payment, self).__init__(parent)
        self.w = Ui_Payment()
        self.w.setupUi(self)
        self.conns = {} # qt disconnect bug
        self.sigs  = {}
        closeA = QAction(self)
        closeA.setShortcut('Ctrl+W')
        self.addAction(closeA)
        closeA.triggered.connect(self.close)
        ## self.w.paymentSb.valueChanged.connect(self.change)
        ch_conn(self, 'valchanged', self.w.paymentSb.valueChanged, self.change)
        for rb in (
            'cashRb', 'dcardRb', 'ccardRb', 'cheqRb', 'transRb', 'directRb'):
            getattr(self.w, rb).toggled.connect(self.radiocheck)
        self.w.buttonBox.rejected.connect(self.close)
        self.devel()

    def devel(self):
        self.totbalv = Decimal('80.63')
        self.curbalv = Decimal('80.63')
        self.w.totbal.setText(str(self.totbalv))
        self.w.curbal.setText(str(self.curbalv))

    def change(self, val): # hierwei to change
        dif = Decimal(str(val)) - self.curbalv
        if dif < 0:
            self.w.change.setText('0.00')
        else:
            self.w.change.setText(str(dif))
            
    def radiocheck(self):
        if self.w.cashRb.isChecked():
            self.w.changeLb.show()
            self.w.change.show()
            ## self.w.paymentSb.valueChanged.connect(self.change)
            ch_conn(
                self, 'valchanged', self.w.paymentSb.valueChanged, self.change)
        else:
            self.w.changeLb.hide()
            self.w.change.hide()
            ch_conn(self, 'valchanged')
            
if __name__ == '__main__':
    from PyQt4.QtGui import QApplication, QShortcut
    a = QApplication([])
    w = Payment(None)
    w.show()
    exit(a.exec_())

## unpaid:
##     select sum(acc_npr*(1+vat_rate)) from acc{},vats where acc_vat=vat_id and not acc_paid
## outstanding:
##     select sum(acc_npr*(1+vat_rate)) from acc{},vats where acc_vat=vat_id and acc_paid is null
# acc_paid: default false.  null: paid but payment not confirmed.
