# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../4qt/gnuvet/about.ui'
#
# Created: Sun May 16 01:07:33 2010
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

## from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QLabel, QFont, QPushButton

class Ui_About(object):
    def setupUi(self, About):
        ## About.setWindowModality(Qt.NonModal)
        About.resize(361,275)
        ## sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
        ##                                QtGui.QSizePolicy.Fixed)
        ## About.setSizePolicy(sizePolicy)
        About.setSizePolicy(0, 0)
        self.vLb = QLabel(About)
        self.vLb.setGeometry(93,20,165,19)
        font = QFont()
        font.setBold(True)
        self.vLb.setFont(font)
        ## self.vLb.setAlignment(Qt.AlignCenter)
        self.aboutLb = QLabel(About)
        self.aboutLb.setGeometry(25,50,298,160)
        self.aboutLb.setWordWrap(True)
        self.okPb = QPushButton(About)
        self.okPb.setGeometry(137,223,84,30)
        self.retranslateUi(About)

    def retranslateUi(self, About):
        About.setWindowTitle(
            QApplication.translate("About", "About GnuVet", None, 1))
        self.okPb.setText(QApplication.translate("About", "OK", None, 1))
