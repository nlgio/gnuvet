# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saepat.ui'
#
# Created: Sat Nov 27 00:27:21 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

# todo:
# poss set tooltip for individual Dd item via itemIcon -- no.
# check (tab)order
# sort out cliLb and cliNameLb/in add/edit

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QApplication, QCheckBox, QComboBox, QDateEdit, QFont,
                         QFrame, QGridLayout, QGroupBox, QLabel, QLineEdit,
                         QPixmap, QPlainTextEdit, QPushButton, QRadioButton,
                         QSpacerItem,QSpinBox,QTableWidget,QWidget)
from gtable import Gtable

class Ui_Saepat(object):
    def setupUi(self, Saepat):
        Saepat.resize(870, 626)
        Saepat.setMinimumSize(870, 626)
        self.centralwidget = QWidget(Saepat)
        self.menubar = Saepat.menuBar()
        self.lLb = QLabel(Saepat)
        self.lLb.setGeometry(Saepat.width()-90, 1, 80, 19)
        self.lLb.setAlignment(Qt.AlignRight|Qt.AlignBottom)
        self.statusbar = Saepat.statusBar()
        self.statusbar.setSizeGripEnabled(False)
        self.no_dbconn = QLabel(self.statusbar)
        font = QFont()
        font.setBold(1)
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
        self.qPix.setGeometry(182, 214, 32, 32)
        self.qPix.setPixmap(QPixmap(":/images/question.png"))
        self.noMLb = QLabel(self.noMFr)
        self.noMLb.setGeometry(230, 100, 421, 261)
        #self.noMLb.setAutoFillBackground(False)
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
        self.plist = Gtable(self.matchFr, scrollh=0, resizecols=True)
        self.plist.setGeometry(0, 34, 850, 455)
        self.plist.setMinimumSize(850, 455)
        self.matchFr.hide()
        # search add edit frame
        self.saeFr = QFrame(self.centralwidget)
        self.saeFr.setGeometry(10, 10, 850, 521)
        self.saeFr.setMinimumSize(850, 491)
        self.saeFr.setAutoFillBackground(True)
        self.saeFr.setFrameShape(QFrame.StyledPanel)
        self.saeFr.setFrameShadow(QFrame.Raised)
        self.pnameLe = QLineEdit(self.saeFr)
        self.pnameLe.setGeometry(30, 18, 271, 21)
        self.pnameLe.setMaxLength(80)
        self.pnameLb = QLabel(self.saeFr)
        self.pnameLb.setGeometry(30, 41, 84, 15)
        self.pnameLb.setTextFormat(Qt.PlainText)
        self.pnameLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.breedDd = QComboBox(self.saeFr)
        self.breedDd.setGeometry(30, 72, 271, 21)
        self.breedDd.setEditable(1)
        self.breedDd.lineEdit().setMaxLength(80)
        self.breedLb = QLabel(self.saeFr)
        self.breedLb.setGeometry(30, 95, 85, 15)
        self.breedLb.setTextFormat(Qt.PlainText)
        self.breedLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.xbredCb = QCheckBox(self.saeFr)
        self.xbredCb.setGeometry(312, 73, 88, 20)
        self.specDd = QComboBox(self.saeFr)
        self.specDd.setGeometry(30, 126, 201, 21)
        self.specDd.setEditable(1)
        self.specDd.lineEdit().setMaxLength(80)
        self.specLb = QLabel(self.saeFr)
        self.specLb.setGeometry(30, 149, 98, 15)
        self.specLb.setTextFormat(Qt.PlainText)
        self.specLb.setTextInteractionFlags(Qt.NoTextInteraction)
        # patient colour
        self.colDd = QComboBox(self.saeFr)
        self.colDd.setGeometry(450, 18, 240, 21)
        self.colDd.setEditable(1)
        self.colDd.lineEdit().setMaxLength(80)
        self.colLb = QLabel(self.saeFr)
        self.colLb.setGeometry(450, 41, 89, 15)
        self.colLb.setTextFormat(Qt.PlainText)
        self.colLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.mixedcolCb = QCheckBox(self.saeFr)
        self.mixedcolCb.setGeometry(702, 18, 104, 20)
        self.mixedcolCb.hide()
        self.sexDd = QComboBox(self.saeFr)
        self.sexDd.setGeometry(450, 72, 120, 21)
        self.sexLb = QLabel(self.saeFr)
        self.sexLb.setGeometry(450, 95, 71, 15)
        self.sexLb.setTextFormat(Qt.PlainText)
        self.sexLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.neuteredCb = QCheckBox(self.saeFr)
        self.neuteredCb.setGeometry(593, 74, 82, 20)
        self.neutBox = QGroupBox(self.saeFr)
        self.neutBox.setGeometry(601, 76, 204, 121)
        # intact
        self.neutnoRb = QRadioButton(self.neutBox)
        self.neutnoRb.setGeometry(17, 20, 39, 20)
        # neutered state unknown
        self.neutunRb = QRadioButton(self.neutBox)
        self.neutunRb.setGeometry(79, 20, 79, 20)
        # neutered, date unknown
        self.neutduRb = QRadioButton(self.neutBox)
        self.neutduRb.setGeometry(17, 53, 141, 20)
        # neutered date
        self.neutdateRb = QRadioButton(self.neutBox)
        self.neutdateRb.setGeometry(17, 86, 48, 20)
        self.neutDe = QDateEdit(self.neutBox)
        self.neutDe.setGeometry(77, 87, 110, 21)
        self.neutDe.setCalendarPopup(1)
        self.viciousCb = QCheckBox(self.saeFr)
        self.viciousCb.setGeometry(450, 127, 67, 20)
        # patient deceased
        self.ripCb = QCheckBox(self.saeFr)
        self.ripCb.setGeometry(450, 160, 43, 20)
        # patient chip
        self.idLe = QLineEdit(self.saeFr)
        self.idLe.setGeometry(30, 200, 190, 21)
        self.idLe.setMaxLength(20)
        self.idLb = QLabel(self.saeFr)
        self.idLb.setGeometry(30, 223, 16, 15)
        self.idLb.setTextFormat(Qt.PlainText)
        self.idLb.setTextInteractionFlags(Qt.NoTextInteraction)
        # pet passport
        self.petpassLe = QLineEdit(self.saeFr)
        self.petpassLe.setGeometry(290, 200, 180, 21)
        self.petpassLe.setMaxLength(20)
        self.petpassLb = QLabel(self.saeFr)
        self.petpassLb.setGeometry(290, 223, 80, 15)
        self.annoTe = QPlainTextEdit(self.saeFr)
        self.annoTe.setGeometry(30, 249, 210, 91)
        self.annoTe.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.annoTe.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.annoTe.setTabChangesFocus(True)
        self.annoLb = QLabel(self.saeFr)
        self.annoLb.setGeometry(30, 342, 117, 15)
        self.annoLb.setTextFormat(Qt.PlainText)
        self.annoLb.setTextInteractionFlags(Qt.NoTextInteraction)
        # patient age <=>
        self.agespecDd = QComboBox(self.saeFr)
        self.agespecDd.setGeometry(290, 249, 90, 21)
        self.agespecLb = QLabel(self.saeFr)
        self.agespecLb.setGeometry(290, 272, 83, 15)
        self.agespecLb.setTextFormat(Qt.PlainText)
        self.agespecLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.ageSb = QSpinBox(self.saeFr)
        self.ageSb.setGeometry(390, 249, 55, 21)
        self.ageLb = QLabel(self.saeFr)
        self.ageLb.setGeometry(390, 272, 24, 15)
        self.ageLb.setTextFormat(Qt.PlainText)
        self.ageLb.setTextInteractionFlags(Qt.NoTextInteraction)
        # patient age unit
        self.ageuDd = QComboBox(self.saeFr)
        self.ageuDd.setGeometry(454, 249, 86, 21)
        self.ageuLb = QLabel(self.saeFr)
        self.ageuLb.setGeometry(454, 272, 53, 15)
        self.ageuLb.setTextFormat(Qt.PlainText)
        self.ageuLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.dobDe = QDateEdit(self.saeFr)
        self.dobDe.setGeometry(570, 249, 110, 21)
        self.dobDe.setCalendarPopup(1)
        self.dobLb = QLabel(self.saeFr)
        self.dobLb.setGeometry(570, 272, 79, 15)
        self.dobLb.setTextFormat(Qt.PlainText)
        self.dobLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.dobestCb = QCheckBox(self.saeFr)
        #self.dobestCb.setGeometry(690, 249, 87, 20)
        self.dobestCb.setGeometry(690, 249, 87, 20)
        # patient age spec unit
        self.agesuDd = QComboBox(self.saeFr)
        self.agesuDd.setGeometry(690, 249, 90, 21)
        self.agesuLb = QLabel(self.saeFr)
        self.agesuLb.setGeometry(690, 272, 53, 15)
        self.locDd = QComboBox(self.saeFr)
        self.locDd.setGeometry(290, 319, 441, 21)
        self.locDd.setEditable(1)
        self.locDd.lineEdit().setMaxLength(80)
        self.locLb = QLabel(self.saeFr)
        self.locLb.setGeometry(290, 342, 101, 15)
        self.locLb.setTextFormat(Qt.PlainText)
        self.locLb.setTextInteractionFlags(Qt.NoTextInteraction)
        # patient reg'd <=>
        self.regspecDd = QComboBox(self.saeFr)
        self.regspecDd.setGeometry(30, 373, 90, 21)
        self.regspecLb = QLabel(self.saeFr)
        self.regspecLb.setGeometry(30, 397, 83, 15)
        self.regDe = QDateEdit(self.saeFr)
        self.regDe.setGeometry(130, 373, 110, 21)
        self.regDe.setCalendarPopup(1)
        self.regLb = QLabel(self.saeFr)
        self.regLb.setGeometry(130, 397, 67, 15)
        self.regLb.setTextFormat(Qt.PlainText)
        self.regLb.setTextInteractionFlags(Qt.NoTextInteraction)
        # patient insurance
        self.insDd = QComboBox(self.saeFr)
        self.insDd.setGeometry(290, 373, 250, 21)
        self.insDd.setEditable(1)
        self.insDd.lineEdit().setMaxLength(80)
        self.insLb = QLabel(self.saeFr)
        self.insLb.setGeometry(290, 397, 110, 15)
        self.insLb.setTextFormat(Qt.PlainText)
        self.insLb.setTextInteractionFlags(Qt.NoTextInteraction)
        # patient seen date [new]
        self.seenCb = QCheckBox(self.saeFr)
        self.seenCb.setGeometry(560, 374, 55, 15)
        self.seenDe = QDateEdit(self.saeFr)
        self.seenDe.setGeometry(625, 373, 140, 21)
        self.seenDe.setCalendarPopup(1)
        self.seenDe.setEnabled(0)
        self.seenCb.clicked.connect(self.seenDe.setEnabled)
        line = QFrame(self.saeFr)
        line.setGeometry(30, 420, 791, 20)
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        # client specs
        self.csnameLe = QLineEdit(self.saeFr)
        self.csnameLe.setGeometry(30, 460, 210, 21)
        self.csnameLe.setMaxLength(80)
        self.csnameLb = QLabel(self.saeFr)
        self.csnameLb.setGeometry(30, 483, 95, 15)
        self.csnameLb.setTextFormat(Qt.PlainText)
        self.csnameLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.cfnameLe = QLineEdit(self.saeFr)
        self.cfnameLe.setGeometry(259, 460, 210, 21)
        self.cfnameLe.setMaxLength(80)
        self.cfnameLb = QLabel(self.saeFr)
        self.cfnameLb.setGeometry(259, 483, 102, 15)
        self.cfnameLb.setTextFormat(Qt.PlainText)
        self.cfnameLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.clientLb = QLabel(self.saeFr)
        self.clientLb.setGeometry(30, 460, 441, 21) # geo ok?
        # find all|live|rip
        self.pfindDd = QComboBox(self.saeFr)
        self.pfindDd.setGeometry(570, 460, 74, 22)
        self.pfindLb = QLabel(self.saeFr)
        self.pfindLb.setGeometry(532, 463, 29, 15)
        self.pfindLb.setTextFormat(Qt.PlainText)
        self.pfindLb.setTextInteractionFlags(Qt.NoTextInteraction)
        # detailed/short search
        self.detailedCb = QCheckBox(self.saeFr)
        self.detailedCb.setGeometry(690, 460, 124, 20)
        # error frame
        self.errFr = QFrame(self.centralwidget)
        self.errFr.setGeometry(250, 159, 360, 240)
        self.errFr.setMinimumSize(360, 240)
        self.errFr.setMaximumSize(360, 240)
        self.errFr.setAutoFillBackground(True)
        self.errFr.setFrameShape(QFrame.StyledPanel)
        self.errFr.setFrameShadow(QFrame.Raised)
        self.warnPix = QLabel(self.errFr)
        self.warnPix.setGeometry(33, 75, 40, 39)
        self.warnPix.setText("")
        self.warnPix.setPixmap(QPixmap(":/images/warning.png"))
        self.errLb = QLabel(self.errFr)
        self.errLb.setGeometry(95, 46, 221, 101)
        self.errLb.setTextFormat(Qt.RichText)
        self.errLb.setWordWrap(True)
        self.errLb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.errOk = QPushButton(self.errFr)
        self.errOk.setGeometry(127, 190, 107, 24)
        self.errFr.hide()
        # buttonbox
        self.buttonBox = QWidget(self.centralwidget)
        self.buttonBox.setGeometry(177, 540, 505, 42)
        self.gridlayout = QGridLayout(self.buttonBox)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.mainPb = QPushButton(self.buttonBox)
        self.mainPb.setMinimumSize(107, 24)
        self.mainPb.setAutoDefault(False)
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
        Saepat.setCentralWidget(self.centralwidget)
        # BUDDIES
        self.pnameLb.setBuddy(self.pnameLe)
        self.breedLb.setBuddy(self.breedDd)
        self.specLb.setBuddy(self.specDd)
        self.colLb.setBuddy(self.colDd)
        self.sexLb.setBuddy(self.sexDd)
        self.idLb.setBuddy(self.idLe)
        self.petpassLb.setBuddy(self.petpassLe)
        self.annoLb.setBuddy(self.annoTe)
        self.regspecLb.setBuddy(self.regspecDd)
        self.regLb.setBuddy(self.regDe)
        self.agespecLb.setBuddy(self.agespecDd)
        self.ageLb.setBuddy(self.ageSb)
        self.ageuLb.setBuddy(self.ageuDd)
        self.dobLb.setBuddy(self.dobDe)
        self.agesuLb.setBuddy(self.agesuDd)
        self.locLb.setBuddy(self.locDd)
        self.insLb.setBuddy(self.insDd)
        self.csnameLb.setBuddy(self.csnameLe)
        self.cfnameLb.setBuddy(self.cfnameLe)
        self.pfindLb.setBuddy(self.pfindDd)
        self.retranslateUi(Saepat)

    def retranslateUi(self, Saepat):
        self.sortbyLb.setText(
            QApplication.translate("Saepat", "order by", None, 1))
        self.sbydateRb.setText(
            QApplication.translate("Saepat", "Last &Seen", None, 1))
        self.sbynameRb.setText(
            QApplication.translate("Saepat", "&Name", None, 1))
        self.breedLb.setText(
            QApplication.translate("Saepat", "Patient &Breed", None, 1))
        self.xbredCb.setText(
            QApplication.translate("Saepat", "C&rossbred", None, 1))
        self.specLb.setText(
            QApplication.translate("Saepat", "&Patient Species", None, 1))
        self.specDd.setWhatsThis(QApplication.translate(
            "Saepat", "Grouping of Breeds rather than \'species\' in the "
            "scientific sense.", None, 1))
        self.mixedcolCb.setText(
            QApplication.translate("Saepat", "&mixed colour", None, 1))
        self.mixedcolCb.setToolTip(
            QApplication.translate("Saepat", "Search for chosen colour in any "
                                   "combination", None, 1))
        self.sexLb.setText(
            QApplication.translate("Saepat", "Patient Se&x", None, 1))
        self.agespecDd.setToolTip(
            QApplication.translate("Saepat", "< search younger than\n= search "
                                   "± 1 unit\n> search older than", None, 1))
        # above does not cause the 'load glyph failed QFontEngine' Error
        self.agespecDd.setWhatsThis(QApplication.translate(
            "Saepat", "With this you can search for Age ranges.  If you set "
            "this to \"=\" it will search for Age ranges plus/minus one of the "
            "given Age Units", None, 1))
        self.agespecDd.addItem("")
        self.agespecDd.addItem("<")
        self.agespecDd.addItem("=")
        self.agespecDd.addItem(">")
        self.ageLb.setText(QApplication.translate("Saepat", "&Age", None, 1))
        self.ageuLb.setText(
            QApplication.translate("Saepat", "Age &Unit", None, 1))
        self.ageuDd.addItem(QApplication.translate("Saepat", "years", None, 1))
        self.ageuDd.addItem(QApplication.translate("Saepat", "months", None, 1))
        self.ageuDd.addItem(QApplication.translate("Saepat", "weeks", None, 1))
        self.ageuDd.addItem(QApplication.translate("Saepat", "days", None, 1))
        self.agesuLb.setText(QApplication.translate("Saepat","± &unit",None, 1))
        self.agesuDd.addItem(QApplication.translate("Saepat", "year", None, 1))
        self.agesuDd.addItem(QApplication.translate("Saepat", "month", None, 1))
        self.agesuDd.addItem(QApplication.translate("Saepat", "week", None, 1))
        self.agesuDd.addItem(QApplication.translate("Saepat", "day", None, 1))
        self.pfindDd.addItem(QApplication.translate("Saepat", "All", None, 1))
        self.pfindDd.addItem(QApplication.translate("Saepat", "Live", None, 1))
        self.pfindDd.addItem(QApplication.translate("Saepat", "RIP", None, 1))
        self.agespecLb.setText(
            QApplication.translate("Saepat", "Age Specif&ier", None, 1))
        self.pnameLb.setText(
            QApplication.translate("Saepat", "&Patient Name", None, 1))
        self.dobLb.setText(
            QApplication.translate("Saepat", "Date of &Birth", None, 1))
        self.neuteredCb.setText(
            QApplication.translate("Saepat", "neutere&d", None, 1))
        self.colLb.setText(
            QApplication.translate("Saepat", "Patient C&olour", None, 1))
        self.dobestCb.setText(
            QApplication.translate("Saepat", "&estimated", None, 1))
        self.cfnameLb.setText(
            QApplication.translate("Saepat", "Client &Forename", None, 1))
        self.viciousCb.setText(
            QApplication.translate("Saepat", "&vicious", None, 1))
        self.seenCb.setText(
            QApplication.translate("Saepat", "&seen:", None, 1))
        self.ripCb.setText(
            QApplication.translate("Saepat", "&RIP", None, 1))
        self.dobDe.setDisplayFormat(
            QApplication.translate("Saepat", "dd.MM.yyyy", None, 1))
        self.neutBox.setTitle(
            QApplication.translate("Saepat", "neutere&d", None, 1))
        self.neutdateRb.setText(
            QApplication.translate("Saepat", "&yes:", None, 1))
        self.neutduRb.setText(
            QApplication.translate("Saepat", "&yes, date unknown", None, 1))
        self.neutnoRb.setText(
            QApplication.translate("Saepat", "n&o", None, 1))
        self.neutunRb.setText(
            QApplication.translate("Saepat", "&unknown", None, 1))
        self.neutDe.setDisplayFormat(
            QApplication.translate("Saepat", "dd.MM.yyyy", None, 1))
        self.locLb.setText(
            QApplication.translate("Saepat", "Patient Lo&cation", None, 1))
        self.insLb.setText(
            QApplication.translate("Saepat", "Patient &Insurance", None, 1))
        self.idLb.setText(
            QApplication.translate("Saepat", "&ID", None, 1))
        self.petpassLb.setText(
            QApplication.translate("Saepat", "&Pet Passport", None, 1))
        self.annoLb.setText(
            QApplication.translate("Saepat", "Patient &Annotation", None, 1))
        self.regLb.setText(
            QApplication.translate("Saepat", "&Registered", None, 1))
        self.regDe.setDisplayFormat(
            QApplication.translate("Saepat", "dd.MM.yyyy", None, 1))
        self.regspecDd.setToolTip(
            QApplication.translate("Saepat", "< search prior to\n= search "
                                   "± 1 month\n> search after", None, 1))
        self.regspecDd.setWhatsThis(QApplication.translate(
            "Saepat", "With this you can search for the Registration Date. If "
            "you set this to \"=\" it will search for the given date plusminus "
            "one month, otherwise after or prior to the given date.", None, 1))
        self.regspecDd.addItem("")
        self.regspecDd.addItem("<")
        self.regspecDd.addItem("=")
        self.regspecDd.addItem(">")
        self.regspecLb.setText(
            QApplication.translate("Saepat", "&Reg.Spec", None, 1))
        self.detailedCb.setText(
            QApplication.translate("Saepat", "&Detailed Search", None, 1))
        self.pfindLb.setText(
            QApplication.translate("Saepat", "&Find:", None, 1))
        self.backPb.setText(
            QApplication.translate("Saepat", "&back to Search", None, 1))
        self.cancelPb.setText(
            QApplication.translate("Saepat", "Cancel", None, 1))
        self.cancelPb.setShortcut(
            QApplication.translate("Saepat", "Esc", None, 1))
        self.errOk.setText(
            QApplication.translate("Saepat", "OK", None, 1))
        self.no_dbconn.setText(
            QApplication.translate('Saepat', 'No db connection...', None, 1))

if __name__ == '__main__':
    from PyQt4.QtGui import QMainWindow, QShortcut
    import gv_qrc
    a = QApplication([])
    b = Ui_Saepat()
    w = QMainWindow()
    b.setupUi(w)
    QShortcut('Ctrl+W', w, quit)
    w.show()
    exit(a.exec_())
