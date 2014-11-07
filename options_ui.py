# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created: Fri Apr 23 00:02:26 2010
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui  import (QDialogButtonBox, QCheckBox, QApplication)

class Ui_Options(object):
    def setupUi(self, Options):
        Options.resize(245,175)
        Options.setMinimumSize(245,175)
        self.buttonBox = QDialogButtonBox(Options)
        self.buttonBox.setGeometry(10,120,221,32)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.autoConsCb = QCheckBox(Options)
        self.autoConsCb.setGeometry(60,20,107,23)
        self.autoHistCb = QCheckBox(Options)
        self.autoHistCb.setGeometry(60,50,104,23)
        self.lSympCb = QCheckBox(Options)
        self.lSympCb.setGeometry(60,80,122,23)
        self.retranslateUi(Options)

    def retranslateUi(self, Options):
        Options.setWindowTitle(QApplication.translate(
            "Options", "GnuVet: Set Options", None, 1))
        self.autoConsCb.setToolTip(QApplication.translate(
            "Options", "To automatically book consultation", None, 1))
        self.autoConsCb.setText(QApplication.translate(
            "Options", "Auto-Consult", None, 1))
        self.autoHistCb.setToolTip(QApplication.translate(
            "Options", "To automatically open History Window.", None, 1))
        self.autoHistCb.setText(QApplication.translate(
            "Options", "Auto-History", None, 1))
        self.lSympCb.setToolTip(QApplication.translate(
            "Options", "To use the Lead Symptom feature.", None, 1))
        self.lSympCb.setText(QApplication.translate(
            "Options", "Lead Symptom", None, 1))

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication, QMainWindow, QShortcut
    a = QApplication([])
    b = Ui_Options()
    w = QMainWindow()
    b.setupUi(w)
    QShortcut('Ctrl+W', w, quit)
    w.show()
    exit(a.exec_())
