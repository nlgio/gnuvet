# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'products.ui'
#
# Created: Fri Aug  6 14:53:59 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

# TODO:
# eliminate palette things for styleSheet s. for instance gtable.py

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QApplication, QButtonGroup, QCheckBox, QComboBox,
                         QDateTimeEdit, QDoubleSpinBox, QFont, QFrame, QLabel,
                         QLineEdit, QRadioButton, QPushButton, QScrollArea,
                         QTextBrowser, QToolButton)
from gtable import Gtable
from tle import QTextLEdit
import gv_qrc

class Ui_Products(object):
    def setupUi(self, Products):
        Products.setMinimumSize(612, 435)
        Products.setMaximumSize(612, 436)
        Products.resize(612, 435)
        self.menubar = Products.menuBar()
        self.lLb = QLabel(Products)
        self.lLb.setGeometry(Products.width()-90, 0, 80, 19)
        self.lLb.setAlignment(Qt.AlignRight|Qt.AlignBottom)
        font = QFont()
        font.setBold(1)
        self.patLb = QLabel(Products)
        self.patLb.setGeometry(10, 35, 591, 19)
        self.patLb.setAlignment(Qt.AlignCenter)
        self.patLb.setFont(font)
        self.statusbar = Products.statusBar()
        self.statusbar.setSizeGripEnabled(False)
        self.no_dbconn = QLabel(self.statusbar)
        self.no_dbconn.setFont(font)
        self.statusbar.addPermanentWidget(self.no_dbconn)
        self.no_dbconn.hide()
        self.nomatchLb = QLabel(Products)
        self.nomatchLb.setGeometry(10, 65, 591, 261)
        self.nomatchLb.setAutoFillBackground(1)
        self.nomatchLb.setBackgroundRole(self.nomatchLb.palette().Base)
        self.nomatchLb.setMargin(3)
        self.nomatchLb.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.nomatchLb.hide()
        self.prodFr = QFrame(Products)
        self.prodFr.setGeometry(0, 55, 611, 361)
        self.prodFr.setAutoFillBackground(1)
        self.plist = Gtable(self.prodFr)
        self.plist.setGeometry(10, 10, 591, 261)
        self.vatLb = QLabel(self.prodFr)
        self.vatLb.setGeometry(35, 289, 50, 15)
        self.vatDd = QComboBox(self.prodFr)
        self.vatDd.setGeometry(90, 286, 165, 22)
        self.markupLb = QLabel(self.prodFr)
        self.markupLb.setGeometry(350, 289, 55, 15)
        self.markupDd = QComboBox(self.prodFr)
        self.markupDd.setGeometry(409, 286, 151, 22)
        self.srchLb = QLabel(self.prodFr)
        self.srchLb.setGeometry(10, 330, 55, 18)
        self.pLe = QLineEdit(self.prodFr)
        self.pLe.setGeometry(65, 327, 131, 24)
        self.pLe.setAcceptDrops(False)
        self.pLe.setMaxLength(80)
        self.amountFr = QFrame(Products)
        self.amountFr.setGeometry(0, 55, 611, 361)
        self.amountFr.setAutoFillBackground(1)
        self.prodLb = QLabel(self.amountFr)
        self.prodLb.setGeometry(129, 14, 371, 31)
        self.prodLb.setFont(font)
        self.prodLb.setFrameShape(QFrame.Panel)
        self.prodLb.setFrameShadow(QFrame.Raised)
        self.prodLb.setLineWidth(2)
        self.prodLb.setMidLineWidth(1)
        self.prodLb.setAlignment(Qt.AlignCenter)
        self.amountLb = QLabel(self.amountFr)
        self.amountLb.setGeometry(210, 60, 59, 18)
        self.amountSb = QDoubleSpinBox(self.amountFr)
        self.amountSb.setGeometry(278, 58, 71, 23)
        self.amountSb.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.amountSb.setDecimals(3)
        self.amountSb.setMaximum(250.0)
        self.amountSb.setValue(1.0)
        self.unitLb = QLabel(self.amountFr)
        self.unitLb.setGeometry(358, 60, 101, 21)
        self.priceLb = QLabel(self.amountFr)
        self.priceLb.setGeometry(114, 108, 64, 18)
        self.priceLb.setAlignment(Qt.AlignRight)
        self.priceSb = QDoubleSpinBox(self.amountFr)
        self.priceSb.setGeometry(182, 106, 101, 23)
        self.priceSb.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.priceSb.setDecimals(2)
        self.priceSb.setMaximum(9999.99)
        self.priceSb.setMinimum(-9999.99)
        self.avatLb = QLabel(self.amountFr)
        self.avatLb.setGeometry(296, 108, 39, 18)
        self.avatLb.setAlignment(Qt.AlignRight)
        self.avatDd = QComboBox(self.amountFr)
        self.avatDd.setGeometry(343, 106, 165, 22)
        self.sympLb = QLabel(self.amountFr)
        self.sympLb.setGeometry(138, 158, 102, 18)
        self.sympDd = QComboBox(self.amountFr)
        self.sympDd.setGeometry(248, 156, 241, 22)
        self.alertLb = QLabel(self.amountFr)
        self.alertLb.setGeometry(257, 158, 186, 18)
        self.line = QFrame(self.amountFr)
        self.line.setGeometry(132, 194, 361, 20)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.dateLb = QLabel(self.amountFr)
        self.dateLb.setGeometry(163, 223, 98, 18)
        self.pDte = QDateTimeEdit(self.amountFr)
        self.pDte.setGeometry(283, 221, 175, 21)
        self.pDte.setAccelerated(True)
        self.pDte.setCalendarPopup(True)
        self.tsysRb = QRadioButton(self.amountFr)
        self.tsysRb.setGeometry(153, 253, 104, 24)
        self.tsysRb.setChecked(True)
        self.tstopRb = QRadioButton(self.amountFr)
        self.tstopRb.setGeometry(283, 253, 90, 24)
        self.trunRb = QRadioButton(self.amountFr)
        self.trunRb.setGeometry(398, 253, 83, 24)
        self.amountFr.hide()
        self.histFr = QFrame(Products)
        self.histFr.setGeometry(0, 55, 611, 361)
        self.histFr.setAutoFillBackground(1)
        self.hTe = QTextLEdit(self.histFr, maxlen=1024)
        self.hTe.setGeometry(20, 10, 571, 151)
        self.hTe.setHorizontalScrollBarPolicy(1)
        self.hTe.setTabChangesFocus(1)
        self.hcharLb = QLabel(self.histFr)
        self.hcharLb.setGeometry(24, 165, 24, 14)
        font.setPointSize(7)
        font.setBold(0)
        self.hcharLb.setFont(font)
        self.hcharLb.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.pal = Products.palette()
        colButs = QButtonGroup(self.histFr)
        colButs.setExclusive(True)
        self.blkPb = QToolButton(self.histFr)
        self.blkPb.setGeometry(80, 165, 14, 14)
        self.blkPb.setCheckable(1)
        self.setcolours(self.blkPb, Qt.black)
        self.redPb = QToolButton(self.histFr)
        self.redPb.setGeometry(104, 165, 14, 14)
        self.redPb.setCheckable(1)
        self.setcolours(self.redPb, Qt.red)
        self.bluPb = QToolButton(self.histFr)
        self.bluPb.setGeometry(128, 165, 14, 14)
        self.bluPb.setCheckable(1)
        self.setcolours(self.bluPb, Qt.blue)
        colButs.addButton(self.blkPb, 1)
        colButs.addButton(self.redPb, 2)
        colButs.addButton(self.bluPb, 3)
        self.blkPb.setChecked(1)
        self.infLb = QLabel(self.histFr)
        self.infLb.setFont(font)
        self.infLb.setGeometry(162, 165, 190, 14)
        self.histFr.hide()
        self.instFr = QFrame(Products)
        self.instFr.setGeometry(0, 55, 611, 361)
        self.instFr.setAutoFillBackground(1)
        self.applDd = QComboBox(self.instFr)
        self.applDd.setGeometry(13, 10, 90, 22)
        self.noSb = QDoubleSpinBox(self.instFr)
        self.noSb.setGeometry(110, 10, 75, 22)
        self.noSb.setAlignment(Qt.AlignRight)
        self.noSb.setMaximum(999.99)
        self.noSb.setMinimum(0)
        self.unitDd = QComboBox(self.instFr)
        self.unitDd.setGeometry(192, 10, 88, 22)
        self.freqDd = QComboBox(self.instFr)
        self.freqDd.setGeometry(288, 10, 125, 22)
        self.periodDd = QComboBox(self.instFr)
        self.periodDd.setGeometry(420, 10, 180, 22)
        self.regionDd = QComboBox(self.instFr)
        self.regionDd.setGeometry(13, 43, 140, 22)
        self.forLb = QLabel(self.instFr)
        self.forLb.setGeometry(161, 44, 20, 22)
        self.forLb.setEnabled(0)
        self.durSb = QDoubleSpinBox(self.instFr)
        self.durSb.setGeometry(184, 43, 50, 22)
        self.durSb.setDecimals(0)
        self.durSb.setAlignment(Qt.AlignRight)
        self.durSb.setMinimum(0)
        self.durSb.setMaximum(99)
        self.durDd = QComboBox(self.instFr)
        self.durDd.setGeometry(241, 43, 120, 22)
        self.durDd.setEnabled(0)
        self.precDd = QComboBox(self.instFr)
        self.precDd.setGeometry(368, 43, 232, 22)
        for e in (self.applDd, self.freqDd, self.periodDd,
                   self.regionDd, self.durDd, self.precDd):
            e.addItem('', 0)
        self.codeLb = QLabel(self.instFr)
        self.codeLb.setGeometry(33, 140, 36, 15)
        self.codeLe = QLineEdit(self.instFr)
        self.codeLe.setGeometry(83, 138, 113, 21)
        self.freetxtTe = QTextLEdit(self.instFr, 300)
        self.freetxtTe.setTabChangesFocus(True)
        self.freetxtTe.setGeometry(13, 8, 590, 61)
        self.freetxtTe.hide()
        self.freetxtCb = QCheckBox(self.instFr)
        self.freetxtCb.setGeometry(33, 169, 79, 20)
        self.preview = QLabel(self.instFr)
        self.preview.setGeometry(238, 78, 361, 192)
        self.preview.setAutoFillBackground(1)
        self.preview.setFrameShape(1)
        self.preview.setBackgroundRole(self.codeLe.backgroundRole())
        self.preview.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.preview.setWordWrap(True)
        self.instFr.hide()
        self.confFr = QFrame(Products)
        self.confFr.setGeometry(0, 55, 611, 361)
        self.confFr.setAutoFillBackground(1)
        self.msgLb = QLabel(self.confFr)
        self.msgLb.setGeometry(20, 10, 571, 24)
        self.msgLb.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.confLb = QLabel(self.confFr)
        self.confLb.setGeometry(20, 54, 571, 24)
        self.confLb.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.instLb = QLabel(self.confFr)
        self.instLb.setGeometry(20, 88, 571, 181)
        self.instLb.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.instLb.setWordWrap(True)
        self.histShow = QTextLEdit(self.confFr)
        self.histShow.setGeometry(20, 130, 571, 133)
        self.histShow.setReadOnly(True)
        hspal = self.confFr.palette()
        hspal.setColor(0, 9, # pal.Active, pal.Base
                       hspal.color(0, 10)) # pal.Active, pal.Window
        hspal.setColor(2, 9, # pal.Inactive, pal.Base
                       hspal.color(0, 10)) # pal.Active, pal.Window
        self.histShow.setPalette(hspal)
        self.confFr.hide()
        self.bbox = QFrame(Products)
        self.bbox.setGeometry(215, 380, 360, 28)
        self.okPb = QPushButton(self.bbox)
        self.backPb = QPushButton(self.bbox)
        self.ccPb = QPushButton(self.bbox)
        self.okPb.setGeometry(0, 0, 70, 28)
        self.backPb.setGeometry(80, 0, 70, 28)
        self.ccPb.setGeometry(160, 0, 70, 28)
        self.skipPb = QPushButton(self.bbox)
        self.skipPb.setGeometry(250, 0, 100, 28)
        self.skipPb.hide()
        self.skipPb.setEnabled(False)
        self.srchLb.setBuddy(self.pLe)
        self.markupLb.setBuddy(self.markupDd)
        self.vatLb.setBuddy(self.vatDd)
        self.priceLb.setBuddy(self.priceSb)
        self.avatLb.setBuddy(self.avatDd)
        self.sympLb.setBuddy(self.sympDd)
        self.dateLb.setBuddy(self.pDte)
        self.amountLb.setBuddy(self.amountSb)
        self.codeLb.setBuddy(self.codeLe)

        self.retranslateUi(Products)

    def setcolours(self, button, colour):
        for group in (0, 2): # Active, Inactive
            for role in (1, ): # looks useful in plastique, messy in others
                self.pal.setColor(group, role, colour)
        button.setPalette(self.pal)
        
    def retranslateUi(self, Products):
        Products.setWindowTitle(QApplication.translate(
            "Products", "GnuVet: Select Product", None, 1))
        self.srchLb.setText(QApplication.translate(
            "Products", "&Search:", None, 1))
        self.vatLb.setText(QApplication.translate(
            "Products", "&VAT:", None, 1))
        self.vatDd.setToolTip(QApplication.translate(
            "Products", "Set VAT applicable for selected item.", None, 1))
        self.markupLb.setText(QApplication.translate(
            "Products", "&Markup:", None, 1))
        self.markupDd.setToolTip(QApplication.translate(
            "Products", "Set markup applicable for selected items.", None, 1))
        self.priceLb.setText(QApplication.translate(
            "Products", "gr. &price:", None, 1))
        self.avatLb.setText(QApplication.translate(
            "Products", "&VAT:", None, 1))
        self.tsysRb.setText(QApplication.translate(
            "Products", "s&ystem time", None, 1))
        self.tstopRb.setText(QApplication.translate(
            "Products", "timer &stop", None, 1))
        self.trunRb.setText(QApplication.translate(
            "Products", "timer &run", None, 1))
        self.sympLb.setText(QApplication.translate(
            "Products", "&Lead Symptom:", None, 1))
        self.dateLb.setText(QApplication.translate(
            "Products", "&Date and Time:", None, 1))
        self.amountLb.setText(QApplication.translate(
            "Products", "&Amount:", None, 1))
        self.alertLb.setText(QApplication.translate(
            "Products", "Please select Lead Symptom", None, 1))
        self.hcharLb.setText('1024')
        self.hcharLb.setToolTip(QApplication.translate(
            "Products", "Chars free in history field.\n[Note: Use of colours "
            "will eat lotsa chars due to markup]", None, 1))
        self.blkPb.setToolTip(QApplication.translate(
            "Products", "Set Text Colour: black", None, 1))
        self.redPb.setToolTip(QApplication.translate(
            "Products", "Set Text Colour: red", None, 1))
        self.bluPb.setToolTip(QApplication.translate(
            "Products", "Set Text Colour: blue", None, 1))
        self.infLb.setText(QApplication.translate(
            "Products", "Hit Ctrl+Enter or click OK when done", None, 1))
        self.forLb.setText(
            QApplication.translate("Products", 'for', None, 1))
        self.codeLb.setText(QApplication.translate(
            "Products", "&Code:", None, 1))
        self.freetxtCb.setText(QApplication.translate(
            "Products", "&Free Text", None, 1))
        self.confLb.setText(QApplication.translate(
            "Products", "<i>Please confirm:</i>", None, 1))
        self.okPb.setText(QApplication.translate(
            "Products", "OK", None, 1))
        self.backPb.setText(QApplication.translate(
            "Products", "&back", None, 1))
        self.ccPb.setText(QApplication.translate(
            "Products", "Cancel", None, 1))
        self.skipPb.setText(QApplication.translate(
            "Products", "&Skip printing", None, 1))

if __name__ == '__main__':
    a = QApplication([])
    a.setStyle('plastique')
    b = Ui_Products()
    from PyQt4.QtGui import QMainWindow, QShortcut
    Mf = QMainWindow()
    b.setupUi(Mf)
    QShortcut('Ctrl+W', Mf, quit)
    Mf.show()
    exit(a.exec_())
