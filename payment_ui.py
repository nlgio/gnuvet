# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment.ui'
#
# Created: Wed Jul 20 08:49:38 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import (QApplication, QDialogButtonBox, QLabel, QRadioButton,
                         QComboBox, QDoubleSpinBox)
from PyQt4.QtCore import Qt, QString

class Ui_Payment(object):
    def setupUi(self, Payment):
        Payment.resize(400, 300)
        self.balpatLb = QLabel(Payment)
        self.balpatLb.setGeometry(20, 12, 153, 15)
        self.balcliLb = QLabel(Payment)
        self.balcliLb.setGeometry(20, 40, 144, 15)
        self.baltotLb = QLabel(Payment)
        self.baltotLb.setGeometry(20, 70, 126, 15)
        self.balpat = QLabel(Payment)
        self.balpat.setGeometry(230, 12, 121, 20)
        self.balpat.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.balcli = QLabel(Payment)
        self.balcli.setGeometry(230, 40, 121, 20)
        self.balcli.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.baltot = QLabel(Payment)
        self.baltot.setGeometry(230, 70, 121, 20)
        self.baltot.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cashRb = QRadioButton(Payment)
        self.cashRb.setGeometry(60, 100, 120, 20)
        self.cashRb.setChecked(True)
        self.cardRb = QRadioButton(Payment)
        self.cardRb.setGeometry(210, 100, 120, 20)
        self.cheqRb = QRadioButton(Payment)
        self.cheqRb.setGeometry(60, 130, 120, 20)
        self.bankRb = QRadioButton(Payment)
        self.bankRb.setGeometry(210, 130, 102, 20)
        self.invoiceLb = QLabel(Payment)
        #self.invoiceLb.setGeometry(90, 153, 80, 15)
        self.invoiceLb.setGeometry(20, 164, 80, 15)
        self.invoiceDd = QComboBox(Payment)
        #self.invoiceDd.setGeometry(190, 150, 120, 21)
        self.invoiceDd.setGeometry(222, 161, 151, 21)
        self.paymentLb = QLabel(Payment)
        self.paymentLb.setGeometry(20, 193, 57, 15)
        self.paymentSb = QDoubleSpinBox(Payment)
        self.paymentSb.setGeometry(222, 190, 151, 22)
        self.paymentSb.setAlignment(
            Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.paymentSb.setMaximum(9999.99)
        self.changeLb = QLabel(Payment)
        self.changeLb.setGeometry(20, 220, 52, 15)
        self.change = QLabel(Payment)
        self.change.setGeometry(230, 220, 121, 20)
        self.change.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.buttonBox = QDialogButtonBox(Payment)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setGeometry(30, 250, 341, 32)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.invoiceLb.setBuddy(self.invoiceDd)
        self.paymentLb.setBuddy(self.paymentSb)

        self.retranslateUi(Payment)

    def retranslateUi(self, Payment):
        Payment.setWindowTitle(QApplication.translate(
            "Payment", "GnuVet: Payment", None, 1))
        self.balpatLb.setText(QApplication.translate(
            "Payment", "Current Balance Patient:", None, 1))
        self.balcliLb.setText(QApplication.translate(
            "Payment", "Current Balance Client:", None, 1))
        self.baltotLb.setText(QApplication.translate(
            "Payment", "Total Balance Client:", None, 1))
        self.paymentLb.setText(QApplication.translate(
            "Payment", "&Payment:", None, 1))
        self.changeLb.setText(QApplication.translate(
            "Payment", "Change:", None, 1))
        self.balpat.setText(QApplication.translate(
            "Payment", "0.00", None, 1))
        self.balcli.setText(QApplication.translate(
            "Payment", "0.00", None, 1))
        self.baltot.setText(QApplication.translate(
            "Payment", "0.00", None, 1))
        self.change.setText(QApplication.translate(
            "Payment", "0.00", None, 1))
        self.cashRb.setText(QApplication.translate(
            "Payment", "&Cash", None, 1))
        self.cardRb.setText(QApplication.translate(
            "Payment", "C&redit card", None, 1))
        self.cheqRb.setText(QApplication.translate(
            "Payment", "C&heque", None, 1))
        self.bankRb.setText(QApplication.translate(
            "Payment", "&Transfer", None, 1))
        self.invoiceLb.setText(QApplication.translate(
            "Payment", "&Invoice:", None, 1))
        
