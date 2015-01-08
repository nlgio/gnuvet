# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saecli.ui'
#
# Created: Sun Feb  6 01:03:03 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

# todo

# from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QApplication, QCheckBox, QComboBox,
                         QDateEdit,QFont,QFrame,QGridLayout,QLabel,QLineEdit,
                         QPixmap, QPlainTextEdit, QPushButton, QRadioButton,
                         QSpacerItem, QSpinBox, QWidget)
from gtable import Gtable

class Ui_Saecli(object):
    def setupUi(self, Saecli):
        Saecli.resize(870, 626)
        Saecli.setMinimumSize(870, 626)
        self.centralwidget = QWidget(Saecli)
        self.menubar = Saecli.menuBar()
        self.lLb = QLabel(Saecli)
        self.lLb.setGeometry(Saecli.width()-90, 5, 80, 19)
        self.lLb.setAlignment(Qt.AlignRight)
        self.statusbar = Saecli.statusBar()
        self.statusbar.setSizeGripEnabled(False)
        self.no_dbconn = QLabel(self.statusbar)
        font = QFont()
        font.setBold(1)
        font.setWeight(75)
        self.no_dbconn.setFont(font)
        self.statusbar.addPermanentWidget(self.no_dbconn)
        self.no_dbconn.hide()
        # no match frame
        self.noMFr = QFrame(self.centralwidget)
        self.noMFr.setGeometry(10, 10, 850, 521)
        self.noMFr.setMinimumSize(850, 491)
        self.noMFr.setAutoFillBackground(True)
        self.noMFr.setFrameShape(QFrame.StyledPanel)
        self.noMFr.setFrameShadow(QFrame.Raised)
        self.qPix = QLabel(self.noMFr)
        self.qPix.setGeometry(182, 214, 32, 32) # was 250, 192, 32, 32
        self.qPix.setPixmap(QPixmap(":/images/question.png"))
        self.noMLb = QLabel(self.noMFr)
        self.noMLb.setGeometry(230, 100, 421, 261) # was 303, 194, 245, 66
        #self.noMLb.setAutoFillBackground(True)
        self.noMLb.setAlignment(Qt.AlignCenter)
        self.noMLb.setTextFormat(Qt.RichText)
        self.noMLb.setWordWrap(True)
        self.noMFr.hide()
        # match[es] frame: list
        self.matchFr = QFrame(self.centralwidget)
        self.matchFr.setGeometry(10, 10, 850, 521)
        self.matchFr.setMinimumSize(850, 491)
        self.matchFr.setAutoFillBackground(True)
        self.matchFr.setFrameShape(QFrame.StyledPanel)
        self.matchFr.setFrameShadow(QFrame.Raised)
        self.matchnLb = QLabel(self.matchFr)
        self.matchnLb.setGeometry(10, 7, 231, 19)
        self.matchnLb.setTextFormat(Qt.PlainText)
        self.sortbyLb = QLabel(self.matchFr)
        self.sortbyLb.setGeometry(251, 8, 53, 19)
        self.sbydateRb = QRadioButton(self.matchFr)
        self.sbydateRb.setGeometry(425, 6, 90, 25)
        self.sbynameRb = QRadioButton(self.matchFr)
        self.sbynameRb.setGeometry(325, 6, 90, 25)
        self.clist = Gtable(self.matchFr, scrollh=0, resizecols=True)
        self.clist.setGeometry(0, 34, 850, 455)
        self.clist.setMinimumSize(850, 455)
        self.matchFr.hide()
        # search add edit frame
        self.saeFr = QFrame(self.centralwidget)
        self.saeFr.setGeometry(10, 10, 850, 521)
        self.saeFr.setMinimumSize(850, 491)
        self.saeFr.setAutoFillBackground(True)
        self.saeFr.setFrameShape(QFrame.StyledPanel)
        self.saeFr.setFrameShadow(QFrame.Raised)
        self.ctitleDd = QComboBox(self.saeFr)
        self.ctitleDd.setGeometry(52, 29, 57, 21)
        self.ctitleLb = QLabel(self.saeFr)
        self.ctitleLb.setGeometry(52, 53, 60, 19)
        self.snameLe = QLineEdit(self.saeFr)
        self.snameLe.setGeometry(135, 29, 210, 21)
        self.snameLe.setMaxLength(80)
        self.snameLb = QLabel(self.saeFr)
        self.snameLb.setGeometry(135, 53, 99, 19)
        self.fnameLe = QLineEdit(self.saeFr)
        self.fnameLe.setGeometry(365, 29, 210, 21)
        self.fnameLe.setMaxLength(80)
        self.fnameLb = QLabel(self.saeFr)
        self.fnameLb.setGeometry(365, 53, 105, 19)
        self.mnameLe = QLineEdit(self.saeFr)
        self.mnameLe.setGeometry(595, 29, 210, 21)
        self.mnameLe.setMaxLength(25)
        self.mnameLb = QLabel(self.saeFr)
        self.mnameLb.setGeometry(595, 53, 141, 19)
        self.baddebtCb = QCheckBox(self.saeFr)
        self.baddebtCb.setGeometry(52, 92, 45, 23)
        self.bdPix = QLabel(self.saeFr)
        self.bdPix.setGeometry(81, 94, 17, 20)
        self.bdPix.setPixmap(QPixmap(":/images/redflag.png"))
        self.housenLe = QLineEdit(self.saeFr)
        self.housenLe.setGeometry(135, 89, 210, 21)
        self.housenLe.setMaxLength(80)
        self.housenLb = QLabel(self.saeFr)
        self.housenLb.setGeometry(135, 113, 140, 19)
        self.streetLe = QLineEdit(self.saeFr)
        self.streetLe.setGeometry(365, 89, 210, 21)
        self.streetLe.setMaxLength(80)
        self.streetLb = QLabel(self.saeFr)
        self.streetLb.setGeometry(365, 113, 40, 19)
        self.villageLe = QLineEdit(self.saeFr)
        self.villageLe.setGeometry(595, 89, 210, 21)
        self.villageLe.setMaxLength(80)
        self.villageLb = QLabel(self.saeFr)
        self.villageLb.setGeometry(595, 113, 42, 19)
        self.cityLe = QLineEdit(self.saeFr)
        self.cityLe.setGeometry(135, 150, 210, 21)
        self.cityLe.setMaxLength(80)
        self.cityLb = QLabel(self.saeFr)
        self.cityLb.setGeometry(135, 174, 24, 19)
        self.regionLe = QLineEdit(self.saeFr)
        self.regionLe.setGeometry(365, 150, 210, 21)
        self.regionLe.setMaxLength(80)
        self.regionLb = QLabel(self.saeFr)
        self.regionLb.setGeometry(365, 174, 43, 19)
        self.postcodeLe = QLineEdit(self.saeFr)
        self.postcodeLe.setGeometry(595, 150, 210, 21) # -17
        self.postcodeLe.setMaxLength(10)
        self.postcodeLb = QLabel(self.saeFr)
        self.postcodeLb.setGeometry(595, 174, 59, 19)
        self.line1 = QFrame(self.saeFr)
        self.line1.setGeometry(30, 197, 791, 20) # 821
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.telhomeLe = QLineEdit(self.saeFr)
        self.telhomeLe.setGeometry(30, 234, 210, 21)
        self.telhomeLe.setMaxLength(30)
        self.telhomeLb = QLabel(self.saeFr)
        self.telhomeLb.setGeometry(30, 258, 61, 19)
        self.telworkLe = QLineEdit(self.saeFr)
        self.telworkLe.setGeometry(260, 234, 210, 21)
        self.telworkLe.setMaxLength(30)
        self.telworkLb = QLabel(self.saeFr)
        self.telworkLb.setGeometry(260, 258, 61, 19)
        self.mobile1Le = QLineEdit(self.saeFr)
        self.mobile1Le.setGeometry(30, 296, 210, 21)
        self.mobile1Le.setMaxLength(30)
        self.mobile1Lb = QLabel(self.saeFr)
        self.mobile1Lb.setGeometry(30, 320, 61, 19)
        self.mobile2Le = QLineEdit(self.saeFr)
        self.mobile2Le.setGeometry(260, 296, 210, 21)
        self.mobile2Le.setMaxLength(30)
        self.mobile2Lb = QLabel(self.saeFr)
        self.mobile2Lb.setGeometry(260, 320, 61, 19)
        self.emailLe = QLineEdit(self.saeFr)
        self.emailLe.setGeometry(260, 360, 210, 21)
        self.emailLe.setMaxLength(80)
        self.emailLb = QLabel(self.saeFr)
        self.emailLb.setGeometry(260, 384, 43, 19)
        self.pnameLe = QLineEdit(self.saeFr)
        self.pnameLe.setGeometry(611, 234, 210, 21)
        self.pnameLe.setMaxLength(30)
        self.pnameLb = QLabel(self.saeFr)
        self.pnameLb.setGeometry(611, 258, 87, 19)
        self.annoTe = QPlainTextEdit(self.saeFr)
        self.annoTe.setGeometry(611, 296, 210, 85)
        self.annoTe.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.annoTe.setTabChangesFocus(True)
        self.annoLb = QLabel(self.saeFr)
        self.annoLb.setGeometry(611, 384, 70, 19)
        self.regspecDd = QComboBox(self.saeFr)
        self.regspecDd.setGeometry(30, 440, 65, 21)
        self.regspecLb = QLabel(self.saeFr)
        self.regspecLb.setGeometry(30, 464, 60, 15)
        self.regDe = QDateEdit(self.saeFr)
        self.regDe.setGeometry(105, 440, 110, 21)
        self.regDe.setCalendarPopup(True)
        self.regLb = QLabel(self.saeFr)
        self.regLb.setGeometry(105, 464, 67, 15)
        self.regLb.setTextFormat(Qt.PlainText)
        self.lastspecDd = QComboBox(self.saeFr)
        self.lastspecDd.setGeometry(260, 440, 65, 21) # +175
        self.lastspecLb = QLabel(self.saeFr)
        self.lastspecLb.setGeometry(260, 464, 60, 15)
        self.lastDe = QDateEdit(self.saeFr)
        self.lastDe.setGeometry(335, 440, 110, 21)
        self.lastLb = QLabel(self.saeFr)
        self.lastLb.setGeometry(335, 464, 67, 15)
        self.balspecDd = QComboBox(self.saeFr)
        self.balspecDd.setGeometry(611, 440, 65, 21) # +175
        self.balspecLb = QLabel(self.saeFr)
        self.balspecLb.setGeometry(611, 464, 60, 15)
        self.balSb = QSpinBox(self.saeFr)
        self.balSb.setGeometry(686, 440, 110, 21)
        self.balLb = QLabel(self.saeFr)
        self.balLb.setGeometry(686, 464, 100, 15)
        # error frame
        self.errFr = QFrame(self.centralwidget)
        self.errFr.setGeometry(250, 159, 360, 240)
        self.errFr.setMinimumSize(360, 240)
        self.errFr.setMaximumSize(360, 240)
        self.errFr.setAutoFillBackground(True)
        self.errFr.setFrameShape(QFrame.StyledPanel)
        self.errFr.setFrameShadow(QFrame.Raised)
        self.warnPix = QLabel(self.errFr)
        self.warnPix.setGeometry(33, 95, 40, 39)
        self.warnPix.setPixmap(QPixmap(":/images/warning.png"))
        self.errLb = QLabel(self.errFr)
        self.errLb.setGeometry(95, 66, 221, 101)
        self.errLb.setTextFormat(Qt.RichText)
        self.errLb.setWordWrap(True)
        self.errOk = QPushButton(self.errFr)
        self.errOk.setGeometry(130, 190, 107, 24)
        # buttonbox
        self.buttonBox = QWidget(self.centralwidget)
        self.buttonBox.setGeometry(177, 540, 505, 42)
        self.gridlayout = QGridLayout(self.buttonBox)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.mainPb = QPushButton(self.buttonBox)
        self.mainPb.setMinimumSize(107, 24)
        self.mainPb.setAutoDefault(0)
        self.mainPb.setDefault(True)
        self.gridlayout.addWidget(self.mainPb, 0, 0, 1, 1)
        self.secondPb = QPushButton(self.buttonBox)
        self.secondPb.setMinimumSize(107, 24)
        self.gridlayout.addWidget(self.secondPb, 0, 1, 1, 1)
        spacerItem = QSpacerItem(51, 20, 7, 1) # exp, min
        self.gridlayout.addItem(spacerItem, 0, 2, 1, 1)
        self.backPb = QPushButton(self.buttonBox)
        self.backPb.setMinimumSize(107, 24)
        self.gridlayout.addWidget(self.backPb, 0, 3, 1, 1)
        self.cancelPb = QPushButton(self.buttonBox)
        self.cancelPb.setMinimumSize(107, 24)
        self.gridlayout.addWidget(self.cancelPb, 0, 4, 1, 1)
        Saecli.setCentralWidget(self.centralwidget)
        # buddies
        self.ctitleLb.setBuddy(self.ctitleDd)
        self.snameLb.setBuddy(self.snameLe)
        self.mnameLb.setBuddy(self.mnameLe)
        self.fnameLb.setBuddy(self.fnameLe)
        self.housenLb.setBuddy(self.housenLe)
        self.streetLb.setBuddy(self.streetLe)
        self.villageLb.setBuddy(self.villageLe)
        self.cityLb.setBuddy(self.cityLe)
        self.regionLb.setBuddy(self.regionLe)
        self.postcodeLb.setBuddy(self.postcodeLe)
        self.telhomeLb.setBuddy(self.telhomeLe)
        self.telworkLb.setBuddy(self.telworkLe)
        self.mobile1Lb.setBuddy(self.mobile1Le)
        self.mobile2Lb.setBuddy(self.mobile2Le)
        self.regspecLb.setBuddy(self.regspecDd)
        self.regLb.setBuddy(self.regDe)
        self.emailLb.setBuddy(self.emailLe)
        self.pnameLb.setBuddy(self.pnameLe)
        self.annoLb.setBuddy(self.annoTe)
        self.lastspecLb.setBuddy(self.lastspecDd)
        self.lastLb.setBuddy(self.lastDe)
        self.balspecLb.setBuddy(self.balspecDd)
        self.balLb.setBuddy(self.balSb)
        self.retranslateUi(Saecli)

    def retranslateUi(self, Saecli):
        self.noMLb.setText(
            QApplication.translate("Saecli", "No matching client record found!"
                                   "\n\nDo you want to register a new account\n"
                                   "with your entries?", None, 1))
        self.sortbyLb.setText(
            QApplication.translate("Saecli", "order by", None, 1))
        self.sbydateRb.setText(
            QApplication.translate("Saecli", "Last &Seen", None, 1))
        self.sbynameRb.setText(
            QApplication.translate("Saecli", "&Name", None, 1))
        self.cancelPb.setText(
            QApplication.translate("Saecli", "Cancel", None, 1))
        self.cancelPb.setShortcut(
            QApplication.translate("Saecli", "Esc", None, 1))
        self.fnameLb.setText(
            QApplication.translate("Saecli", "Client &Forename", None, 1))
        self.mnameLb.setText(
            QApplication.translate("Saecli", "Client &Middle Name(s)", None, 1))
        self.housenLb.setText(
            QApplication.translate("Saecli", "H&ouse Name/Number", None, 1))
        self.streetLb.setText(
            QApplication.translate("Saecli", "&Street", None, 1))
        self.villageLb.setText(
            QApplication.translate("Saecli", "&Village", None, 1))
        self.cityLb.setText(
            QApplication.translate("Saecli", "&City", None, 1))
        self.regionLb.setText(
            QApplication.translate("Saecli", "&Region", None, 1))
        self.postcodeLb.setText(
            QApplication.translate("Saecli", "&Postcode", None, 1))
        self.mobile2Lb.setText(
            QApplication.translate("Saecli", "Mobile &2", None, 1))
        self.snameLb.setText(
            QApplication.translate("Saecli", "C&lient Surname", None, 1))
        self.ctitleLb.setText(
            QApplication.translate("Saecli", "T&itle", None, 1))
        self.mobile1Lb.setText(
            QApplication.translate("Saecli", "Mobile &1", None, 1))
        self.telworkLb.setText(
            QApplication.translate("Saecli", "Tel &Work", None, 1))
        self.telhomeLb.setText(
            QApplication.translate("Saecli", "&Tel Home", None, 1))
        self.regLb.setText(
            QApplication.translate("Saecli", "&Registered", None, 1))
        self.regDe.setDisplayFormat(
            QApplication.translate("Saecli", "dd.MM.yyyy", None, 1))
        self.regspecDd.setToolTip(
            QApplication.translate("Saecli", "< search prior to\n= search ± 1 "
                                   "month\n> search after", None, 1))
        self.regspecDd.setWhatsThis(QApplication.translate(
            "Saecli", "With this you can search for the Registration Date. If "
            "you set this to \"=\" it will search for the given date plusminus "
            "one month, otherwise after or prior to the given date.", None, 1))
        self.regspecDd.addItem("")
        self.regspecDd.addItem("<")
        self.regspecDd.addItem("=")
        self.regspecDd.addItem(">")
        self.regspecLb.setText(
            QApplication.translate("Saecli", "&R.Spec.", None, 1))
        self.emailLb.setText(
            QApplication.translate("Saecli", "em&ail", None, 1))
        self.pnameLb.setText(
            QApplication.translate("Saecli", "Animal &Name", None, 1))
        self.annoLb.setText(
            QApplication.translate("Saecli", "&Annotation", None, 1))
        self.baddebtCb.setToolTip(
            QApplication.translate("Saecli", "Bad Debtor", None, 1))
        self.baddebtCb.setText(
            QApplication.translate("Saecli", "&BD", None, 1))
        self.lastspecLb.setText(
            QApplication.translate("Saecli", "&L.Spec.", None, 1))
        self.lastDe.setDisplayFormat(
            QApplication.translate("Saecli", "dd.MM.yyyy", None, 1))
        self.lastspecDd.setToolTip(
            QApplication.translate("Saecli", "< search prior to\n= search ± 1 "
                                   "month\n> search after", None, 1))
        self.lastspecDd.setWhatsThis(QApplication.translate(
            "Saecli", "With this you can search for the date the Client has "
            "been last seen. If "
            "you set this to \"=\" it will search for the given date plusminus "
            "one month, otherwise after or prior to the given date.", None, 1))
        self.lastspecDd.addItem("")
        self.lastspecDd.addItem("<")
        self.lastspecDd.addItem("=")
        self.lastspecDd.addItem(">")
        self.lastLb.setText(
            QApplication.translate("Saecli", "&Last Seen", None, 1))
        self.balspecDd.addItem("")
        self.balspecDd.addItem("<")
        self.balspecDd.addItem(">")
        self.balspecLb.setText(
            QApplication.translate("Saecli", "&B.Spec.", None, 1))
        self.balLb.setText(
            QApplication.translate("Saecli", "Current &Balance", None, 1))
        self.errOk.setText('OK')
        self.no_dbconn.setText(
            QApplication.translate('Saecli', 'No db connection...', None, 1))

if __name__ == '__main__':
    from PyQt4.QtGui import QMainWindow, QShortcut
    import gv_rc
    a = QApplication([])
    b = Ui_Saecli()
    w = QMainWindow()
    b.setupUi(w)
    QShortcut('Ctrl+W', w, quit)
    w.show()
    exit(a.exec_())

