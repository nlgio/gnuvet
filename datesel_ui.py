# -*- coding: utf-8 -*-

# Form implementation generated from scratch
# Created: Wed May 22 16:41:23
#      by: gnuvet

from PyQt4.QtGui import (QApplication,QDateEdit,QPushButton)

def tl(txt=''):
    return QApplication.translate("Datesel", txt, None, 1)

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
        Datesel.setWindowTitle(tl("GnuVet: Select date"))
        self.okPb.setText(tl("Select"))
        self.ccPb.setText(tl("Cancel"))

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
