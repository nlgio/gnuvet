# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created: Mon Apr 19 13:36:59 2010
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import (QApplication, QFont, QFrame, QLabel, QLineEdit,
                         QMenu, QMenuBar, QPixmap, QPushButton,
                         QShortcut, QStatusBar, QWidget,)
from PyQt4.QtCore import Qt # for alignment

class Ui_Mainform(object):
    def setupUi(self, Mainform):
        Mainform.resize(390,280)
        Mainform.setMinimumSize(390,280)
        # one pixel, otherwise at least enlightenment hides titlebar
        Mainform.setMaximumSize(391,280)
        self.centralwidget = QWidget(Mainform)
        self.gnuLb = QLabel(self.centralwidget)
        self.gnuLb.setGeometry(90,30,214,155)
        self.gnuLb.setPixmap(QPixmap(":/images/gnu.png"))
        # quit Frame
        self.qFr = QFrame(self.centralwidget)
        self.qFr.setGeometry(10,0,361,231)
        self.qFr.setFrameStyle(0)
        self.closeLb = QLabel(self.qFr)
        self.closeLb.setGeometry(108,18,198,19)
        font = QFont()
        font.setBold(True)
        self.closeLb.setFont(font)
        self.qLb = QLabel(self.qFr)
        self.qLb.setGeometry(50,13,32,32)
        self.qLb.setPixmap(QPixmap(":/images/question.png"))
        self.noPb = QPushButton(self.qFr)
        self.noPb.setGeometry(190,190,84,30)
        self.noPb.setAutoDefault(False)
        self.noPb.setDefault(True)
        self.yesPb = QPushButton(self.qFr)
        self.yesPb.setGeometry(90,190,84,30)
        self.gnubgLb = QLabel(self.qFr)
        self.gnubgLb.setGeometry(83,30,214,155)
        self.gnubgLb.setPixmap(QPixmap(":/images/gnu-bg.png"))
        self.qFr.hide()
        # login Frame
        self.lFr = QWidget(self.centralwidget)
        self.lFr.setGeometry(10, 0, 390, 280)
        self.lgnuLb = QLabel(self.lFr)
        self.lgnuLb.setGeometry(83,30,214,155)
        self.lgnuLb.setPixmap(QPixmap(":/images/gnu-bg.png"))
        self.lognameLb = QLabel(self.lFr)
        self.lognameLe = QLineEdit(self.lFr)
        self.logpassLb = QLabel(self.lFr)
        self.logpassLe   = QLineEdit(self.lFr)
        self.logokPb   = QPushButton(self.lFr)
        self.lognameLb.setGeometry(20, 73, 102, 19)
        self.lognameLe.setGeometry(160, 72, 151, 21)
        self.logpassLb.setGeometry(20, 114, 94, 19)
        self.logpassLe.setGeometry(160, 113, 151, 21)
        self.logokPb.setGeometry(145, 160, 84, 30)
        self.lognameLe.setMaxLength(25)
        self.logpassLe.setMaxLength(25)
        self.logpassLe.setEchoMode(1) # QLineEdit.NoEcho
        self.lognameLb.setBuddy(self.lognameLe)
        self.logpassLb.setBuddy(self.logpassLe)
        #devel:
        self.lFr.hide()
        # Mainform further
        Mainform.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Mainform)
        self.taskM = QMenu(self.menubar)
        self.maintM = QMenu(self.menubar)
        self.helpM = QMenu(self.menubar)
        Mainform.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Mainform)
        self.statusbar.setSizeGripEnabled(False)
        Mainform.setStatusBar(self.statusbar)
        #    NODBCONN
        self.no_dbconn = QLabel(self.statusbar)
        self.no_dbconn.setGeometry(100, 240, 198, 19)
        self.no_dbconn.setFont(font)
        self.statusbar.addPermanentWidget(self.no_dbconn)
        self.menubar.addAction(self.taskM.menuAction())
        self.menubar.addAction(self.maintM.menuAction())
        self.menubar.addAction(self.helpM.menuAction())
        self.lLb = QLabel(Mainform)
        self.lLb.setGeometry(Mainform.width()-90, 1, 85, 19)
        self.lLb.setAlignment(Qt.AlignRight|Qt.AlignBottom)
        self.retranslateUi(Mainform)

    def retranslateUi(self, Mainform):
        Mainform.setWindowTitle(
            QApplication.translate("Mainform", "GnuVet", None, 1))
        self.closeLb.setText(
            QApplication.translate("Mainform", "You want to close GnuVet?",
                                   None, 1))
        self.noPb.setText(
            QApplication.translate("Mainform", "&No", None, 1))
        self.noPb.setShortcut(
            QApplication.translate("Mainform", "N", None, 1))
        self.yesPb.setText(
            QApplication.translate("Mainform", "&Yes", None, 1))
        self.yesPb.setShortcut(
            QApplication.translate("Mainform", "Y", None, 1))
        self.maintM.setTitle(
            QApplication.translate("Mainform", "&Maintenance", None, 1))
        self.taskM.setTitle(
            QApplication.translate("Mainform", "&Task", None, 1))
        self.helpM.setTitle(
            QApplication.translate("Mainform", "&Help", None, 1))
        self.lognameLb.setText(
            QApplication.translate("Mainform", "&Username:", None, 1))
        self.logpassLb.setText(
            QApplication.translate("Mainform", "&Password:", None, 1))
        self.logokPb.setText(
            QApplication.translate("Mainform", "&Login", None, 1))
        self.lLb.setText(
            QApplication.translate("Mainform", "no login", None, 1))
        self.no_dbconn.setText(
            QApplication.translate("Mainform", 'No db connection...', None, 1))

if __name__ == '__main__':
    import gv_qrc
    a = QApplication([])
    from PyQt4.QtGui import QMainWindow
    Mainform = QMainWindow()
    b = Ui_Mainform()
    b.setupUi(Mainform)
    QShortcut('Ctrl+Q', Mainform, quit)
    Mainform.show()
    exit(a.exec_())
