# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient.ui'
#
# Created: Fri Dec 17 14:00:29 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

# TODO:

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QApplication, QFont, QFrame, QLabel, QLineEdit,
                         QPixmap, QPushButton, QWidget)
from tle import QTextLEdit
from gtable import Gtable

class Ui_Patient(object):
    def setupUi(self, Patient):
        Patient.resize(957, 645)
        Patient.setMinimumSize(957, 645)
        Patient.setMaximumSize(958, 646)
        self.centralwidget = QWidget(Patient)
        self.menubar = Patient.menuBar()
        self.statusbar = Patient.statusBar()
        self.statusbar.setSizeGripEnabled(False)
        self.no_dbconn = QLabel(self.statusbar)
        font = QFont()
        font.setBold(True)
        self.no_dbconn.setFont(font)
        self.statusbar.addPermanentWidget(self.no_dbconn, 0)
        ## self.statusbar.
        self.no_dbconn.hide()
        self.lLb = QLabel(Patient)
        self.lLb.setGeometry(Patient.width()-90, 1, 85, 19)
        self.lLb.setAlignment(Qt.AlignRight|Qt.AlignBottom)
        self.sexLb = QLabel(self.centralwidget)
        self.sexLb.setGeometry(10, 50, 191, 19)
        self.ageLb = QLabel(self.centralwidget)
        self.ageLb.setGeometry(10, 70, 201, 19)
        self.chrLb = QLabel(self.centralwidget)
        self.chrLb.setGeometry(10, 304, 123, 19)
        self.weightPb = QPushButton(self.centralwidget)
        self.weightPb.setGeometry(10, 119, 201, 21)
        self.colourLb = QLabel(self.centralwidget)
        self.colourLb.setGeometry(10, 90, 251, 19)
        self.breedLb = QLabel(self.centralwidget)
        self.breedLb.setGeometry(10, 30, 201, 19)
        self.nameLb = QLabel(self.centralwidget)
        self.nameLb.setGeometry(10, 10, 235, 19)
        self.nameLb.setMinimumSize(40, 19)
        self.nameLb.setMaximumSize(235, 19)
        self.nameLb.setFont(font)
        self.ripLb = QLabel(self.centralwidget)
        self.ripLb.setGeometry(251, 10, 17, 20)
        self.ripLb.setPixmap(QPixmap(":/images/rip.png"))
        self.telwLb = QLabel(self.centralwidget)
        self.telwLb.setGeometry(615, 110, 131, 19)
        self.mobile2Lb = QLabel(self.centralwidget)
        self.mobile2Lb.setGeometry(760, 110, 131, 19)
        self.mobile1Lb = QLabel(self.centralwidget)
        self.mobile1Lb.setGeometry(760, 90, 131, 19)
        self.telhLb = QLabel(self.centralwidget)
        self.telhLb.setGeometry(615, 90, 131, 19)
        self.addr2Lb = QLabel(self.centralwidget)
        self.addr2Lb.setGeometry(615, 50, 241, 19)
        self.locLb = QLabel(self.centralwidget)
        self.locLb.setGeometry(330, 70, 251, 19)
        self.locLb.setAutoFillBackground(True)
        self.insLb = QLabel(self.centralwidget)
        self.insLb.setGeometry(330, 90, 251, 19)
        self.insLb.setAutoFillBackground(True)
        self.aLb = QLabel(self.centralwidget)
        self.aLb.setGeometry(10, 420, 81, 19)
        self.annoLb = QLabel(self.centralwidget)
        self.annoLb.setGeometry(10, 440, 251, 111)
        self.annoLb.setWordWrap(True)
        self.annoLb.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.idLb = QLabel(self.centralwidget)
        self.idLb.setGeometry(330, 10, 20, 19)
        self.identLb = QLabel(self.centralwidget)
        self.identLb.setGeometry(435, 10, 130, 19)
        self.petpassLb = QLabel(self.centralwidget)
        self.petpassLb.setGeometry(330, 30, 95, 19)
        self.petpassnoLb = QLabel(self.centralwidget)
        self.petpassnoLb.setGeometry(435, 30, 130, 19)
        self.warnLb = QLabel(self.centralwidget)
        self.warnLb.setGeometry(273, 10, 17, 20)
        self.warnLb.setPixmap(QPixmap(":/images/ltning.png"))
        self.bdLb = QLabel(self.centralwidget)
        self.bdLb.setGeometry(905, 10, 17, 20)
        self.bdLb.setPixmap(QPixmap(":/images/redflag.png"))
        self.cnameLb = QLabel(self.centralwidget)
        self.cnameLb.setGeometry(615, 10, 281, 19)
        self.cnameLb.setMinimumSize(0, 19)
        self.cnameLb.setMaximumSize(291, 19)
        self.cnameLb.setFont(font)
        self.vacLb = QLabel(self.centralwidget)
        self.vacLb.setGeometry(10, 184, 112, 19)
        self.vacPb = QPushButton(self.centralwidget)
        self.vacPb.setGeometry(160, 182, 80, 22)
        self.vachLb = QLabel(self.centralwidget)
        self.vachLb.setGeometry(10, 210, 230, 29)
        self.vachLb.setAutoFillBackground(True)
        self.vachLb.setTextFormat(Qt.RichText)
        self.vachLb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.vachLb.setWordWrap(True)
        self.chrhLb = QLabel(self.centralwidget)
        self.chrhLb.setGeometry(10, 324, 140, 29)
        self.chrhLb.setAutoFillBackground(True)
        self.chrhLb.setTextFormat(Qt.RichText)
        self.chrhLb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.htable = Gtable(self.centralwidget)
        self.htable.setGeometry(280, 140, 651, 411)
        self.htable.setMinimumSize(621, 411)
        self.addLb = QLabel(self.centralwidget)
        self.addLb.setGeometry(280, 564, 40, 19)
        self.addLe = QLineEdit(self.centralwidget)
        self.addLe.setGeometry(330, 563, 100, 21)
        self.addLe.setMaxLength(80)
        self.addchPb = QPushButton(self.centralwidget)
        self.addchPb.setGeometry(450, 562, 160, 24)
        self.addconsPb = QPushButton(self.centralwidget)
        self.addconsPb.setGeometry(630, 562, 160, 24)
        self.closePb = QPushButton(self.centralwidget)
        self.closePb.setGeometry(850, 562, 80, 24)
        self.addr1Lb = QLabel(self.centralwidget)
        self.addr1Lb.setGeometry(615, 30, 241, 19)
        self.postcodeLb = QLabel(self.centralwidget)
        self.postcodeLb.setGeometry(615, 70, 131, 19)
        self.pbalLb = QLabel(self.centralwidget)
        self.pbalLb.setGeometry(12, 560, 107, 18)
        self.pbalanceLb = QLabel(self.centralwidget)
        self.pbalanceLb.setGeometry(142, 560, 72, 18)
        self.pbalanceLb.setAlignment(
            Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbalLb = QLabel(self.centralwidget)
        self.cbalLb.setGeometry(12, 580, 107, 18)
        self.cbalanceLb = QLabel(self.centralwidget)
        self.cbalanceLb.setGeometry(142, 580, 72, 18)
        self.cbalanceLb.setAlignment(
            Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.savecFr = QFrame(self.centralwidget)
        self.savecFr.setGeometry(400, 230, 401, 231)
        self.savecFr.setAutoFillBackground(True)
        self.savecFr.setFrameShape(QFrame.StyledPanel)
        self.savecFr.setFrameShadow(QFrame.Raised)
        self.qLb = QLabel(self.savecFr)
        self.qLb.setGeometry(90, 97, 32, 32)
        self.qLb.setPixmap(QPixmap(":/images/question.png"))
        self.savecLb = QLabel(self.savecFr)
        self.savecLb.setGeometry(149, 103, 99, 18)
        self.savecFr.hide()
        self.lastLb = QLabel(self.centralwidget)
        self.lastLb.setGeometry(10, 157, 68, 18)
        self.lastLb.setTextFormat(Qt.PlainText)
        self.lastseenLb = QLabel(self.centralwidget)
        self.lastseenLb.setGeometry(90, 157, 64, 18)
        self.lastseenLb.setTextFormat(Qt.PlainText)
        Patient.setCentralWidget(self.centralwidget)
        self.newconsFr = QFrame(self.centralwidget)
        self.newconsFr.setGeometry(400, 230, 401, 231)
        self.newconsFr.setFrameShape(1)
        self.newconsFr.setAutoFillBackground(1)
        self.newconsqLb = QLabel(self.newconsFr)
        self.newconsqLb.setGeometry(70, 60, 32, 32)
        self.newconsqLb.setPixmap(QPixmap(":/images/question.png"))
        self.newconsLb = QLabel(self.newconsFr)
        self.newconsLb.setGeometry(130, 65, 160, 18)
        self.newcons_newPb = QPushButton(self.newconsFr)
        self.newcons_selPb = QPushButton(self.newconsFr)
        self.newcons_ccPb  = QPushButton(self.newconsFr)
        self.newcons_newPb.setGeometry(25, 140, 110, 24)
        self.newcons_selPb.setGeometry(145, 140, 110, 24)
        self.newcons_ccPb.setGeometry(265, 140, 110, 24)
        self.newcons_newPb.setDefault(1)
        self.newconsFr.hide()
        self.addLb.setBuddy(self.addLe)
        self.retranslateUi(Patient)

    def retranslateUi(self, Patient):
        Patient.setWindowTitle(
            QApplication.translate("Patient", "GnuVet: Patient", None, 1))
        self.ripLb.setToolTip(
            QApplication.translate("Patient", "deceased", None, 1))
        self.bdLb.setToolTip(
            QApplication.translate("Patient", "bad debtor", None, 1))
        self.chrLb.setText(
            QApplication.translate("Patient", "Chronic Conditions:", None, 1))
        self.weightPb.setToolTip(
            QApplication.translate(
                "Patient", "Click here to add new weight entry "
                "and/or display weight chart", None, 1))
        self.vacLb.setText(
            QApplication.translate("Patient", "Vaccinations due:", None, 1))
        self.vacPb.setText(
            QApplication.translate("Patient", "new &Vacc", None, 1))
        self.aLb.setText(
            QApplication.translate("Patient", "Annotations:", None, 1))
        self.idLb.setText(
            QApplication.translate("Patient", "ID", None, 1))
        self.petpassLb.setText(
            QApplication.translate("Patient", "Pet Passport", None, 1))
        self.warnLb.setToolTip(
            QApplication.translate("Patient", "vicious", None, 1))
        self.addLb.setText(
            QApplication.translate("Patient", "&Add:", None, 1))
        self.addchPb.setText(
            QApplication.translate("Patient", "Add &Text", None, 1))
        self.addchPb.setToolTip(
            QApplication.translate("Patient", "Add text to history", None, 1))
        self.addconsPb.setText(QApplication.translate(
            "Patient", "Add C&onsultation", None, 1))
        self.addconsPb.setToolTip(
            QApplication.translate(
                "Patient", "Add new consultation", None, 1))
        self.closePb.setText(
            QApplication.translate("Patient", "Close", None, 1))
        ## self.closePb.setShortcut(
        ##     QApplication.translate("Patient", "Esc", None, 1))
        self.pbalLb.setText(
            QApplication.translate("Patient", "Patient Balance:", None, 1))
        self.pbalanceLb.setText(
            QApplication.translate("Patient", "0.00", None, 1))
        self.cbalLb.setText(
            QApplication.translate("Patient", "Client Balance:", None, 1))
        self.cbalanceLb.setText(
            QApplication.translate("Patient", "0.00", None, 1))
        self.savecLb.setText(
            QApplication.translate("Patient", "Save Changes?", None, 1))
        self.lastLb.setText(
            QApplication.translate("Patient", "Last Seen:", None, 1))
        self.no_dbconn.setText(
            QApplication.translate("Patient", "No db connection...", None, 1))
        self.newconsLb.setText(QApplication.translate(
            "Patient", "Book new consultation?", None, 1))
        self.newcons_newPb.setText(QApplication.translate(
            "Products", "New", None, 1))
        self.newcons_selPb.setText(QApplication.translate(
            "Products", "Use &Selected", None, 1))
        self.newcons_selPb.setToolTip(QApplication.translate(
            "Products", "Add to &selected consultation", None, 1))
        self.newcons_ccPb.setText(QApplication.translate(
            "Products", "Cancel", None, 1))

if __name__ == '__main__':
    from PyQt4.QtGui import QMainWindow, QShortcut
    import gv_qrc
    a = QApplication([])
    b = Ui_Patient()
    w = QMainWindow()
    b.setupUi(w)
    b.breedLb.setText(
        QApplication.translate("Patient", "Breed", None, 1))
    b.sexLb.setText(
        QApplication.translate("Patient", "Sex", None, 1))
    b.ageLb.setText(
        QApplication.translate("Patient", "Age", None, 1))
    b.colourLb.setText(
        QApplication.translate("Patient", "Colour", None, 1))
    b.identLb.setText('040096100106864')
    b.petpassnoLb.setText('040-0101555')
    b.lLb.setText('patient_ui')
    QShortcut('Ctrl+W', w, quit)
    w.show()
    exit(a.exec_())
