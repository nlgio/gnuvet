# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weight.ui'
#
# Created: Tue May 31 08:35:25 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                         QDoubleSpinBox, QFrame, QLabel, QPushButton,)
from PyQt4.QtCore import Qt

class Ui_Weight(object):
    def setupUi(self, Weight):
        Weight.resize(500, 405)
        Weight.setMinimumSize(500, 405)
        Weight.setMaximumSize(1000, 405)
        self.lLb = QLabel(Weight)
        self.lLb.setGeometry(Weight.width()-90, 5, 80, 19)
        self.lLb.setAlignment(Qt.AlignRight)
        self.dLb = QLabel(Weight)
        self.dLb.setGeometry(20, 25, 50, 17)
        self.wDe = QDateTimeEdit(Weight)
        self.wDe.setGeometry(60, 22, 165, 22)
        self.wDe.setCalendarPopup(1)
        self.wSb = QDoubleSpinBox(Weight)
        self.wSb.setGeometry(250, 22, 102, 22)
        self.wSb.setRange(0.001, 9999) # no whales
        self.wLb = QLabel(Weight)
        self.wLb.setGeometry(360, 25, 22, 17)
        self.estCb = QCheckBox(Weight)
        self.estCb.setGeometry(398, 24, 100, 21)
        self.addPb = QPushButton(Weight)
        self.delPb = QPushButton(Weight)
        self.periodPb = QPushButton(Weight)
        self.printPb = QPushButton(Weight)
        self.closePb = QPushButton(Weight)
        self.addPb.setGeometry(130, 365, 60, 28)
        self.delPb.setGeometry(195, 365, 60, 28)
        self.periodPb.setGeometry(260, 365, 60, 28)
        self.printPb.setGeometry(325, 365, 60, 28)
        self.closePb.setGeometry(390, 365, 60, 28)
        self.dLb.setBuddy(self.wDe)
        self.wLb.setBuddy(self.wSb)
        self.confirm = QFrame(Weight)
        self.confirm.setFrameStyle(1)
        self.confirm.setGeometry(90, 105, 320, 200)
        self.confirm.setAutoFillBackground(1)
        self.confirmLb = QLabel(self.confirm)
        self.confirmLb.setGeometry(50, 45, 210, 17)
        self.confirmLb.setAlignment(Qt.AlignCenter)
        self.confirmPb = QPushButton(self.confirm)
        self.confirm_cancelPb = QPushButton(self.confirm)
        self.confirmPb.setGeometry(95, 110, 60, 28)
        self.confirm_cancelPb.setGeometry(160, 110, 60, 28)
        self.entrydelLb = QLabel(Weight)
        self.entrydelLb.setGeometry(20, 25, 60, 17)
        self.entrydelDd = QComboBox(Weight)
        self.entrydelDd.setGeometry(70, 22, 265, 23)
        self.entrydelPb = QPushButton(Weight)
        self.entrydelPb.setGeometry(355, 19, 60, 28)
        self.entrydel_cancelPb = QPushButton(Weight)
        self.entrydel_cancelPb.setGeometry(420, 19, 60, 28)
        self.datesel = QFrame(Weight)
        self.datesel.setFrameStyle(1)
        self.datesel.setGeometry(90, 105, 320, 200)
        self.datesel.setAutoFillBackground(1)
        self.loLb = QLabel(self.datesel)
        self.loLb.setGeometry(50, 40, 35, 17)
        self.loDd = QComboBox(self.datesel)
        self.loDd.setGeometry(90, 40, 165, 22)
        self.hiLb = QLabel(self.datesel)
        self.hiLb.setGeometry(50, 80, 35, 17)
        self.hiDd = QComboBox(self.datesel)
        self.hiDd.setGeometry(90, 80, 165, 22)
        self.loLb.setBuddy(self.loDd)
        self.hiLb.setBuddy(self.hiDd)
        self.entrydelLb.setBuddy(self.entrydelDd)
        self.dselPb = QPushButton(self.datesel)
        self.dsel_cancelPb = QPushButton(self.datesel)
        self.dselPb.setGeometry(90, 140, 60, 28)
        self.dsel_cancelPb.setGeometry(160, 140, 60, 28)
        self.retranslateUi(Weight)

    def retranslateUi(self, Weight):
        Weight.setWindowTitle(QApplication.translate(
            "Weight", "GnuVet: Patient Weight", None, 1))
        self.dLb.setText(QApplication.translate(
            "Weight", "&Date:", None, 1))
        self.wLb.setText(QApplication.translate(
            "Weight", "&kg", None, 1))
        self.estCb.setText(QApplication.translate(
            "Weight", "&estimated", None, 1))
        self.entrydelLb.setText(QApplication.translate(
            "Weight", "Entr&y", None, 1))
        self.addPb.setText(QApplication.translate("Weight", "&Add", None, 1))
        self.addPb.setToolTip(
            QApplication.translate("Weight", "Add entry as set above", None, 1))
        self.delPb.setText(QApplication.translate("Weight", "De&lete", None, 1))
        self.delPb.setToolTip(
            QApplication.translate("Weight", "Delete an entry", None, 1))
        self.periodPb.setText(
            QApplication.translate("Weight", "Pe&riod", None, 1))
        self.periodPb.setToolTip(QApplication.translate(
            "Weight", "Select time period to display", None, 1))
        self.printPb.setText(QApplication.translate(
            "Weight", "&Print", None, 1))
        self.closePb.setText(QApplication.translate(
            "Weight", "Close", None, 1))
        self.confirmPb.setText(
            QApplication.translate("Weight", "&Add", None, 1))
        self.confirm_cancelPb.setText(
            QApplication.translate("Weight", "&Cancel", None, 1))
        self.loLb.setText(QApplication.translate("Weight", "&from", None, 1))
        self.hiLb.setText(QApplication.translate("Weight", "&to", None, 1))
        self.dselPb.setText(QApplication.translate("Weight", "&Ok", None, 1))
        self.dsel_cancelPb.setText(
            QApplication.translate("Weight", "&Cancel", None, 1))
        self.entrydelPb.setText(
            QApplication.translate("Weight", "De&lete", None, 1))
        self.entrydel_cancelPb.setText(
            QApplication.translate("Weight", "&Cancel", None, 1))
