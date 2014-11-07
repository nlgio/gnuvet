# -*- coding: utf-8 -*-

# Form implementation generated from scratch
# Created: Wed May 22 16:41:23
#      by: gnuvet

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QApplication,QDateEdit,QPushButton)

class Ui_Datesel(object):
    def setupUi(self, Datesel):
        Datesel.resize(320, 100)
        Datesel.setMinimumSize(320, 100)
        Datesel.setMaximumSize(320, 101)
        self.dE = QDateEdit(Datesel)
        self.dE.setGeometry(110, 20, 120, 24)
        self.dE.setCalendarPopup(True)
        self.okPb = QPushButton(Datesel)
        self.okPb.setGeometry(70, 60, 80, 24)
        self.okPb.setDefault(True)
        self.okPb.setAutoDefault(True)
        self.ccPb = QPushButton(Datesel)
        self.ccPb.setGeometry(170, 60, 80, 24)
        self.retranslateUi(Datesel)

    def retranslateUi(self, Datesel):
        Datesel.setWindowTitle(QApplication.translate(
            "Datesel", "GnuVet: Select date", None, 1))
        self.okPb.setText(QApplication.translate(
            "Datesel", "Select", None, 1))
        self.ccPb.setText(QApplication.translate(
            "Datesel", "Cancel", None, 1))

if __name__ == '__main__':
    from PyQt4.QtGui import QMainWindow, QShortcut
    a = QApplication([])
    a.setStyle('plastique')
    b = Ui_Datesel()
    w = QMainWindow()
    b.setupUi(w)
    QShortcut('Ctrl+W', w, quit)
    w.show()
    exit(a.exec_())
