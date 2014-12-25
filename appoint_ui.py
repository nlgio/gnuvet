# -*- coding: utf-8 -*-

# Form implementation generated from scratch
# Created: Sat May 18 21:28:50 2013
#      by: gnuvet

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QApplication,QComboBox,QFont,QFrame,QLabel,QPixmap,
                         QPushButton,QRadioButton)
from gtable import Gtable
import gv_qrc

class Ui_Appointer(object):
    def setupUi(self, Appointer):
        Appointer.resize(958, 645)
        Appointer.setMinimumSize(958, 645)
        Appointer.setMaximumSize(958, 646)
        # self.centralwidget = QWidget(Appointer)
        self.menubar = Appointer.menuBar()
        self.statusbar = Appointer.statusBar()
        self.statusbar.setSizeGripEnabled(False)
        self.no_dbconn = QLabel(self.statusbar)
        font = QFont()
        font.setBold(True)
        self.no_dbconn.setFont(font)
        self.statusbar.addPermanentWidget(self.no_dbconn, 0)
        self.no_dbconn.hide()
        self.lLb = QLabel(Appointer)
        self.lLb.setGeometry(Appointer.width()-90, 1, 85, 19)
        self.lLb.setAlignment(Qt.AlignRight|Qt.AlignBottom) # tryin 2 elim Qt
        ## self.lLb.setAlignment(0x0002|0x0040) # dont work
        ## self.lLb.setAlignment(0x0042) # dont work
        ## self.lLb.setStyleSheet( # dont work either
        ##     """QLabel { text-align: right; vertical-align: bottom; }""")
        self.monthRb = QRadioButton(Appointer)
        self.monthRb.setGeometry(10, 35, 50, 22)
        self.weekRb = QRadioButton(Appointer)
        self.weekRb.setGeometry(60, 35, 50, 22)
        self.dayRb = QRadioButton(Appointer)
        self.dayRb.setGeometry(110, 35, 50, 22)
        self.yearbackPb = QPushButton(Appointer)
        self.yearbackPb.setGeometry(170, 33, 70, 24)
        self.monthbackPb = QPushButton(Appointer)
        self.monthbackPb.setGeometry(245, 33, 70, 24)
        self.weekbackPb = QPushButton(Appointer)
        self.weekbackPb.setGeometry(320, 33, 70, 24)
        self.daybackPb = QPushButton(Appointer)
        self.daybackPb.setGeometry(395, 33, 70, 24)
        self.dayforePb = QPushButton(Appointer)
        self.dayforePb.setGeometry(470, 33, 70, 24)
        self.weekforePb = QPushButton(Appointer)
        self.weekforePb.setGeometry(545, 33, 70, 24)
        self.monthforePb = QPushButton(Appointer)
        self.monthforePb.setGeometry(620, 33, 70, 24)
        self.yearforePb = QPushButton(Appointer)
        self.yearforePb.setGeometry(695, 33, 70, 24)
        self.staffLb = QLabel(Appointer)
        self.staffLb.setGeometry(780, 34, 40, 22)
        self.staffDd = QComboBox(Appointer)
        self.staffDd.setGeometry(823, 33, 118, 24)
        self.calendar = Gtable(Appointer, scrollh=0)
        self.calendar.jump = True
        self.calendar.setGeometry(12, 69, 930, 514)
        self.calendar.rowmode = 0 # single cell
        
        self.confirm = QFrame(Appointer)
        # hierwei
        self.confirm.setAutoFillBackground(True)
        self.confirm.setFrameShape(QFrame.StyledPanel)
        self.confirm.setFrameShadow(QFrame.Raised)
        self.confirm.setGeometry(300, 200, 350, 200)
        self.confirm.warnPix = QLabel(self.confirm)
        self.confirm.warnPix.setGeometry(15, 60, 40, 39)
        self.confirm.warnPix.setPixmap(QPixmap(":/images/warning.png"))
        self.confirm.msgLb = QLabel(self.confirm)
        ## self.confirm.msgLb.setFrameShape(QFrame.StyledPanel)
        ## self.confirm.msgLb.setGeometry(65, 10, 270, 140)
        self.confirm.msgLb.setWordWrap(True)
        self.confirm.msgLb.setText('Oops, there\'s summin wrong!')
        self.confirmokPb = QPushButton(self.confirm)
        self.confirmokPb.setGeometry(15, 160, 98, 24)
        self.confirmeditPb = QPushButton(self.confirm)
        self.confirmeditPb.setGeometry(125, 160, 98, 24)
        self.confirmccPb = QPushButton(self.confirm)
        self.confirmccPb.setGeometry(235, 160, 98, 24)
        self.confirmeditPb.setDefault(True)
        self.confirmeditPb.setAutoDefault(True)
        self.confirm.hide()
        self.closePb = QPushButton(Appointer)
        self.closePb.setGeometry(439, 595, 80, 24)
        self.staffLb.setBuddy(self.staffDd)
        self.retranslateUi(Appointer)

    def retranslateUi(self, Appointer):
        Appointer.setWindowTitle(QApplication.translate(
            "Appointer", "GnuVet: Appointments", None, 1))
        self.monthRb.setText(QApplication.translate(
            "Appointer", "&M", None, 1))
        self.monthRb.setToolTip(QApplication.translate(
            "Appointer", "Display month", None, 1))
        self.weekRb.setText(QApplication.translate(
            "Appointer", "&W", None, 1))
        self.weekRb.setToolTip(QApplication.translate(
            "Appointer", "Display week", None, 1))
        self.dayRb.setText(QApplication.translate(
            "Appointer", "&D", None, 1))
        self.dayRb.setToolTip(QApplication.translate(
            "Appointer", "Display day", None, 1))
        self.yearbackPb.setText(QApplication.translate(
            "Appointer", "&< year", None, 1))
        self.yearbackPb.setToolTip(QApplication.translate(
            "Appointer", "Select this day one year earlier", None, 1))
        self.monthbackPb.setText(QApplication.translate(
            "Appointer", "< m&onth", None, 1))
        self.monthbackPb.setToolTip(QApplication.translate(
            "Appointer", "Select this day one month earlier", None, 1))
        self.weekbackPb.setText(QApplication.translate(
            "Appointer", "< w&eek", None, 1))
        self.weekbackPb.setToolTip(QApplication.translate(
            "Appointer", "Select this day one week earlier", None, 1))
        self.daybackPb.setText(QApplication.translate(
            "Appointer", "< d&ay", None, 1))
        self.daybackPb.setToolTip(QApplication.translate(
            "Appointer", "Select one day earlier", None, 1))
        self.dayforePb.setText(QApplication.translate(
            "Appointer", "da&y >", None, 1))
        self.dayforePb.setToolTip(QApplication.translate(
            "Appointer", "Select one day later", None, 1))
        self.weekforePb.setText(QApplication.translate(
            "Appointer", "wee&k >", None, 1))
        self.weekforePb.setToolTip(QApplication.translate(
            "Appointer", "Select this day one week later", None, 1))
        self.monthforePb.setText(QApplication.translate(
            "Appointer", "month& >", None, 1))
        self.monthforePb.setToolTip(QApplication.translate(
            "Appointer", "Select this day one month later", None, 1))
        self.yearforePb.setText(QApplication.translate(
            "Appointer", "year &>", None, 1))
        self.yearforePb.setToolTip(QApplication.translate(
            "Appointer", "Select this day one year later", None, 1))
        self.staffLb.setText(QApplication.translate(
            "Appointer", "&Staff:", None, 1))
        self.confirmokPb.setText(QApplication.translate(
            "Appointer.confirm", "Save &anyway", None, 1))
        self.confirmeditPb.setText(QApplication.translate(
            "Appointer.confirm", "&Edit entry", None, 1))
        self.confirmccPb.setText(QApplication.translate(
            "Appointer.confirm", "&Cancel"))
        self.closePb.setText(QApplication.translate(
            "Appointer", "Close", None, 1))

if __name__ == '__main__':
    from PyQt4.QtGui import QMainWindow, QShortcut
    a = QApplication([])
    a.setStyle('plastique')
    b = Ui_Appointer()
    w = QMainWindow()
    b.setupUi(w)
    b.lLb.setText('appoint_ui')
    QShortcut('Ctrl+W', w, quit)
    b.closePb.clicked.connect(quit)
    w.show()
    exit(a.exec_())
    
