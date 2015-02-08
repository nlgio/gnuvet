# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment.ui'
#
# Created: Sun Feb  8 13:57:36 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtCore import Qt # Alignment, alas
from PyQt4.QtGui import (QApplication, QCheckBox, QDialogButtonBox, 
                         QDoubleSpinBox, QLabel, QRadioButton, )

def tl(txt=''):
    return QApplication.translate("Payment", txt, None, 1)

class Ui_Payment(object):
    def setupUi(self, Payment):
        Payment.resize(431, 300)
        self.buttonBox = QDialogButtonBox(Payment)
        self.buttonBox.setGeometry(40, 240, 341, 32)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.curbalLb = QLabel(Payment)
        self.curbalLb.setGeometry(20, 10, 111, 16)
        self.totbalLb = QLabel(Payment)
        self.totbalLb.setGeometry(20, 30, 111, 16)
        self.paymentLb = QLabel(Payment)
        self.paymentLb.setGeometry(20, 73, 57, 15)
        self.paymentSb = QDoubleSpinBox(Payment)
        self.paymentSb.setGeometry(112, 70, 151, 22)
        self.paymentSb.setAlignment(AlignRight|AlignTrailing|AlignVCenter)
        self.changeLb = QLabel(Payment)
        self.changeLb.setGeometry(20, 100, 52, 15)
        self.curbal = QLabel(Payment)
        self.curbal.setGeometry(140, 10, 101, 20)
        self.curbal.setAlignment(AlignRight|AlignTrailing|AlignVCenter)
        self.totbal = QLabel(Payment)
        self.totbal.setGeometry(140, 30, 101, 20)
        self.totbal.setAlignment(AlignRight|AlignTrailing|AlignVCenter)
        self.change = QLabel(Payment)
        self.change.setGeometry(120, 100, 121, 20)
        self.change.setAlignment(AlignRight|AlignTrailing|AlignVCenter)
        self.cashRb = QRadioButton(Payment)
        self.cashRb.setGeometry(310, 40, 54, 20)
        self.cashRb.setChecked(True)
        self.cardRb = QRadioButton(Payment)
        self.cardRb.setGeometry(310, 70, 91, 20)
        self.cheqRb = QRadioButton(Payment)
        self.cheqRb.setGeometry(310, 130, 71, 20)
        self.bankRb = QRadioButton(Payment)
        self.bankRb.setGeometry(310, 160, 81, 20)
        self.cardRb_2 = QRadioButton(Payment)
        self.cardRb_2.setGeometry(310, 100, 91, 20)
        self.bankRb_2 = QRadioButton(Payment)
        self.bankRb_2.setGeometry(310, 190, 101, 20)
        self.label = QLabel(Payment)
        self.label.setGeometry(310, 10, 101, 16)
        self.printCb = QCheckBox(Payment)
        self.printCb.setGeometry(20, 130, 100, 19)
        self.paymentLb.setBuddy(self.paymentSb)

        self.retranslateUi(Payment)

    def retranslateUi(self, Payment):
        Payment.setWindowTitle(tl("Payment", "GnuVet: Payment", None))
        self.curbalLb.setText(tl("Payment", "Current Balance:", None))
        self.totbalLb.setText(tl("Payment", "Total Balance:", None))
        self.paymentLb.setText(tl("Payment", "&Payment:", None))
        self.changeLb.setText(tl("Payment", "Change:", None))
        self.curbal.setText(tl("Payment", "0.00", None))
        self.totbal.setText(tl("Payment", "0.00", None))
        self.change.setText(tl("Payment", "0.00", None))
        self.cashRb.setText(tl("Payment", "&Cash", None))
        self.cardRb.setText(tl("Payment", "&Debit Card", None))
        self.cheqRb.setText(tl("Payment", "C&heque", None))
        self.bankRb.setText(tl("Payment", "&Transfer", None))
        self.cardRb_2.setText(tl("Payment", "C&redit Card", None))
        self.bankRb_2.setText(tl("Payment", "D&irect Debit", None))
        self.label.setText(tl("Payment", "Payment Mode:", None))
        self.printCb.setText(tl("Payment", "Pri&nt invoice", None))

if __name__ == "__main__":
    import sys
    from PyQt4.QtGui import QMainWindow, QShortcut
    a = QApplication([])
    a.setStyle('plastique')
    w = QMainWindow()
    b = Ui_Payment()
    b.setupUi(Payment)
    QShortcut('Ctrl+W', w, quit)
    w.show()
    exit(a.exec_())
