# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'path/to/client.ui'
#
# Created: Fri Feb 18 13:30:31 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

# TODO:
# why's menubar smaller than in other windows?

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QApplication, QFont, QWidget, QLabel, QPixmap,
                         QPushButton)
from gtable import Gtable

class Ui_Client(object):
    def setupUi(self, Client):
        Client.resize(957, 660)
        Client.setMinimumSize(957, 661)
        self.centralwidget = QWidget(Client)
        self.menubar = Client.menuBar()
        self.statusbar = Client.statusBar()
        self.statusbar.setSizeGripEnabled(False)
        self.no_dbconn = QLabel(self.statusbar)
        font = QFont()
        font.setBold(True)
        self.no_dbconn.setFont(font)
        self.statusbar.addPermanentWidget(self.no_dbconn, 0)
        self.no_dbconn.hide()
        self.lLb = QLabel(Client)
        self.lLb.setGeometry(Client.width()-90, 1, 85, 19)
        self.lLb.setAlignment(Qt.AlignRight|Qt.AlignBottom)
        self.nameLb = QLabel(self.centralwidget)
        self.nameLb.setGeometry(10, 10, 281, 19)
        self.nameLb.setMinimumSize(0, 19)
        self.nameLb.setMaximumSize(291, 19)
        self.addr1Lb = QLabel(self.centralwidget)
        self.addr1Lb.setGeometry(10, 30, 241, 19)
        self.addr1Lb.setTextInteractionFlags(
            Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        self.addr2Lb = QLabel(self.centralwidget)
        self.addr2Lb.setGeometry(10, 50, 241, 19)
        self.addr2Lb.setTextInteractionFlags(
            Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        self.addr3Lb = QLabel(self.centralwidget)
        self.addr3Lb.setGeometry(10, 70, 241, 19)
        self.addr3Lb.setTextInteractionFlags(
            Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        self.telhomeLb = QLabel(self.centralwidget)
        self.telhomeLb.setGeometry(10, 90, 150, 19)
        self.telhomeLb.setTextInteractionFlags(
            Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        self.telworkLb = QLabel(self.centralwidget)
        self.telworkLb.setGeometry(10, 110, 150, 19)
        self.telworkLb.setTextInteractionFlags(
            Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        self.mobile1Lb = QLabel(self.centralwidget)
        self.mobile1Lb.setGeometry(175, 90, 150, 19)
        self.mobile1Lb.setTextInteractionFlags(
            Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        self.mobile2Lb = QLabel(self.centralwidget)
        self.mobile2Lb.setGeometry(175, 110, 150, 19)
        self.mobile2Lb.setTextInteractionFlags(
            Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        self.bdPix = QLabel(self.centralwidget)
        self.bdPix.setGeometry(300, 10, 17, 20)
        self.bdPix.setPixmap(QPixmap(":/images/redflag.png"))
        self.emailLb = QLabel(self.centralwidget)
        self.emailLb.setGeometry(370, 10, 184, 18)
        self.emailLb.setMaximumSize(290, 18)
        self.lastLb = QLabel(self.centralwidget)
        self.lastLb.setGeometry(370, 50, 68, 18)
        self.ldateLb = QLabel(self.centralwidget)
        self.ldateLb.setGeometry(450, 50, 75, 18)
        self.regLb = QLabel(self.centralwidget)
        self.regLb.setGeometry(370, 70, 75, 18)
        self.regdateLb = QLabel(self.centralwidget)
        self.regdateLb.setGeometry(450, 70, 75, 18)
        self.annoLb = QLabel(self.centralwidget)
        self.annoLb.setGeometry(680, 10, 81, 19)
        self.annoLb.setTextInteractionFlags(
            Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        self.annotxtLb = QLabel(self.centralwidget)
        self.annotxtLb.setGeometry(680, 30, 251, 131)
        self.annotxtLb.setWordWrap(1)
        self.annotxtLb.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.nameLb.setFont(font)
        self.patientsLb = QLabel(self.centralwidget)
        self.patientsLb.setGeometry(10, 156, 66, 18)
        self.patientsLb.setFont(font)
        self.patientsLb.setTextFormat(Qt.PlainText)
        self.newPb = QPushButton(self.centralwidget)
        self.newPb.setGeometry(330, 130, 140, 24)
        self.ripPb = QPushButton(self.centralwidget)
        self.ripPb.setGeometry(490, 130, 140, 24)
        self.plist = Gtable(self.centralwidget, resizecols=True, scrollh=0)
        self.plist.setGeometry(10, 180, 921, 371)
        self.plist.setMinimumSize(621, 371)
        self.balLb = QLabel(self.centralwidget)
        self.balLb.setGeometry(10, 570, 107, 18)
        self.balanceLb = QLabel(self.centralwidget)
        self.balanceLb.setGeometry(130, 570, 72, 18)
        self.balanceLb.setAlignment(
            Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mainPb = QPushButton(self.centralwidget)
        self.mainPb.setGeometry(340, 570, 140, 24)
        self.cancelPb = QPushButton(self.centralwidget)
        self.cancelPb.setGeometry(500, 570, 140, 24)
        Client.setCentralWidget(self.centralwidget)
        self.retranslateUi(Client)

    def retranslateUi(self, Client):
        Client.setWindowTitle(QApplication.translate(
            "Client", "GnuVet: Client", None, 1))
        # devel:
        self.nameLb.setText(QApplication.translate(
            "Client", "Mr Client N", None, 1))
        self.addr1Lb.setText(QApplication.translate(
            "Client", "House Street", None, 1))
        self.addr2Lb.setText(QApplication.translate(
            "Client", "Village, City", None, 1))
        self.addr3Lb.setText(QApplication.translate(
            "Client", "B76 0BA", None, 1))
        self.telhomeLb.setText(QApplication.translate(
            "Client", "Home: 01675 478 133", None, 1))
        self.telworkLb.setText(QApplication.translate(
            "Client", "Work: 01675 478 133", None, 1))
        self.mobile1Lb.setText(QApplication.translate(
            "Client", "Mobile: 07725 899 122", None, 1))
        self.mobile2Lb.setText(QApplication.translate(
            "Client", "Mobile: 07725 899 122", None, 1))
        self.balanceLb.setText(QApplication.translate(
            "Client", "0.00", None, 1))
        self.ldateLb.setText(QApplication.translate(
            "Client", "30.04.2009", None, 1))
        self.regdateLb.setText(QApplication.translate(
            "Client", "18.12.2008", None, 1))
        # end devel
        self.annoLb.setText(QApplication.translate(
            "Client", "Annotations:", None, 1))
        self.bdPix.setToolTip(QApplication.translate(
            "Client", "Bad Debtor", None, 1))
        self.emailLb.setText(QApplication.translate(
            "Client", "client.surname@provider.net", None, 1))
        self.lastLb.setText(QApplication.translate(
            "Client", "Last Seen:", None, 1))
        self.regLb.setText(QApplication.translate(
            "Client", "Registered:", None, 1))
        self.patientsLb.setText(QApplication.translate(
            "Client", "Patients:", None, 1))
        self.newPb.setText(QApplication.translate(
            "Client", "New Patient", None, 1))
        self.ripPb.setText(QApplication.translate(
            "Client", "&Mark as deceased", None, 1))
        self.balLb.setText(QApplication.translate(
            "Client", "Current Balance:", None, 1))
        self.mainPb.setText(QApplication.translate(
            "Client", "Select &Patient", None, 1))
        self.cancelPb.setText(QApplication.translate(
            "Client", "Cancel", None, 1))
        self.cancelPb.setShortcut(QApplication.translate(
            "Client", "Esc", None, 1))
        self.no_dbconn.setText(QApplication.translate(
            "Client", "No db connection...", None, 1))

if __name__ == '__main__':
    from PyQt4.QtGui import QMainWindow, QShortcut
    import gv_qrc
    a = QApplication([])
    b = Ui_Client()
    w = QMainWindow()
    b.setupUi(w)
    b.lLb.setText('client_ui')
    QShortcut('Ctrl+W', w, quit)
    b.no_dbconn.show()
    w.show()
    exit(a.exec_())
