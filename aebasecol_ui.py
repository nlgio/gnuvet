# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aebasecol.ui'
#
# Created: Mon Dec 22 21:53:13 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AeBasecol(object):
    def setupUi(self, AeBasecol):
        AeBasecol.resize(400, 469)
        AeBasecol.setMinimumSize(400, 469)
        AeBasecol.setMaximumSize(400, 469)
        self.centralwidget = QtGui.QWidget(AeBasecol)
        self.errFr = QtGui.QFrame(self.centralwidget)
        self.errFr.setGeometry(10, 10, 380, 340)
        self.errFr.setMinimumSize(0, 0)
        self.errFr.setAutoFillBackground(True)
        self.errFr.setFrameShape(QtGui.QFrame.StyledPanel)
        self.errFr.setFrameShadow(QtGui.QFrame.Raised)
        self.warningPix = QtGui.QLabel(self.errFr)
        self.warningPix.setGeometry(10, 81, 40, 39)
        self.warningPix.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/warning.png")))
        self.errMsgLb = QtGui.QLabel(self.errFr)
        self.errMsgLb.setGeometry(70, 20, 210, 175)
        self.errMsgLb.setWordWrap(True)
        self.errMsgLb.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.okPb = QtGui.QPushButton(self.centralwidget)
        self.okPb.setGeometry(70, 358, 80, 30)
        self.backPb = QtGui.QPushButton(self.centralwidget)
        self.backPb.setGeometry(160, 358, 80, 30)
        self.cancelPb = QtGui.QPushButton(self.centralwidget)
        self.cancelPb.setGeometry(250, 358, 80, 30)
        self.cancelPb.setAutoDefault(True)
        self.confFr = QtGui.QFrame(self.centralwidget)
        self.confFr.setGeometry(10, 10, 380, 340)
        self.confFr.setMinimumSize(0, 0)
        self.confFr.setAutoFillBackground(True)
        self.confFr.setFrameShape(QtGui.QFrame.StyledPanel)
        self.confFr.setFrameShadow(QtGui.QFrame.Raised)
        self.qPix = QtGui.QLabel(self.confFr)
        self.qPix.setGeometry(20, 148, 32, 32)
        self.qPix.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/question.png")))
        self.confMsgLb = QtGui.QLabel(self.confFr)
        self.confMsgLb.setGeometry(79, 24, 261, 281)
        self.addFr = QtGui.QFrame(self.centralwidget)
        self.addFr.setGeometry(10, 10, 380, 340)
        self.addFr.setMinimumSize(0, 0)
        self.addFr.setAutoFillBackground(True)
        self.addFr.setFrameShape(QtGui.QFrame.StyledPanel)
        self.addFr.setFrameShadow(QtGui.QFrame.Raised)
        self.bcName = QtGui.QLineEdit(self.addFr)
        self.bcName.setGeometry(30, 17, 231, 27)
        self.bcName.setMaxLength(25)
        self.bcnameLb = QtGui.QLabel(self.addFr)
        self.bcnameLb.setGeometry(30, 50, 116, 19)
        self.groupBox = QtGui.QGroupBox(self.addFr)
        self.groupBox.setGeometry(30, 90, 231, 111)
        self.oblRb = QtGui.QRadioButton(self.groupBox)
        self.oblRb.setGeometry(25, 50, 91, 23)
        self.noRb = QtGui.QRadioButton(self.groupBox)
        self.noRb.setGeometry(25, 77, 58, 23)
        self.possRb = QtGui.QRadioButton(self.groupBox)
        self.possRb.setGeometry(25, 23, 78, 23)
        self.possRb.setChecked(True)
        self.addMsgLb = QtGui.QLabel(self.addFr)
        self.addMsgLb.setGeometry(30, 8, 231, 37)
        self.addMsgLb.setWordWrap(True)
        self.togglePb = QtGui.QPushButton(self.addFr)
        self.togglePb.setGeometry(250, 200, 80, 30)
        self.sAllPb = QtGui.QPushButton(self.addFr)
        self.sAllPb.setGeometry(250, 160, 80, 30)
        AeBasecol.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AeBasecol)
        self.menubar.setGeometry(0, 0, 400, 28)
        AeBasecol.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(AeBasecol)
        self.statusbar.setSizeGripEnabled(False)
        AeBasecol.setStatusBar(self.statusbar)
        self.bcnameLb.setBuddy(self.bcName)

        self.retranslateUi(AeBasecol)
        QtCore.QMetaObject.connectSlotsByName(AeBasecol)
        AeBasecol.setTabOrder(self.bcName, self.possRb)
        AeBasecol.setTabOrder(self.possRb, self.oblRb)
        AeBasecol.setTabOrder(self.oblRb, self.noRb)
        AeBasecol.setTabOrder(self.noRb, self.togglePb)
        AeBasecol.setTabOrder(self.togglePb, self.okPb)
        AeBasecol.setTabOrder(self.okPb, self.backPb)
        AeBasecol.setTabOrder(self.backPb, self.cancelPb)

    def retranslateUi(self, AeBasecol):
        AeBasecol.setWindowTitle(_translate("AeBasecol", "GnuVet: Add Basecolour", None))
        self.okPb.setText(_translate("AeBasecol", "OK", None))
        self.backPb.setText(_translate("AeBasecol", "Bac&k", None))
        self.cancelPb.setText(_translate("AeBasecol", "Cancel", None))
        self.cancelPb.setShortcut(_translate("AeBasecol", "Esc", None))
        self.bcnameLb.setText(_translate("AeBasecol", "BaseC&olour Name", None))
        self.groupBox.setTitle(_translate("AeBasecol", "Combinations of this Basecolour", None))
        self.oblRb.setToolTip(_translate("AeBasecol", "This Basecolour has to be combined with another", None))
        self.oblRb.setStatusTip(_translate("AeBasecol", "Combination required", None))
        self.oblRb.setText(_translate("AeBasecol", "n&ecessary", None))
        self.noRb.setToolTip(_translate("AeBasecol", "This Basecolour can not be combined with others", None))
        self.noRb.setStatusTip(_translate("AeBasecol", "No combination possible", None))
        self.noRb.setText(_translate("AeBasecol", "&none", None))
        self.possRb.setToolTip(_translate("AeBasecol", "This Basecolour can be combined with others", None))
        self.possRb.setStatusTip(_translate("AeBasecol", "Combination possible", None))
        self.possRb.setText(_translate("AeBasecol", "&possible", None))
        self.togglePb.setText(_translate("AeBasecol", "Toggle &All", None))
        self.sAllPb.setText(_translate("AeBasecol", "&Select All", None))

import gv_qrc

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication, QMainWindow, QShortcut
    a = QApplication([])
    a.setStyle('plastique')
    b = Ui_AeBasecol()
    w = QMainWindow()
    b.setupUi(w)
    QShortcut('Ctrl+Q', w, quit)
    b.cancelPb.clicked.connect(quit)
    w.show()
    exit(a.exec_())
