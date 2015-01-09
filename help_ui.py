# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../4qt/gnuvet/help.ui'
#
# Created: Sat May 15 18:16:39 2010
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import (QWidget, QToolButton, QIcon, QPixmap, QTextBrowser,
                         QApplication)

def tl(txt=''):
    return QApplication.translate("Help", txt, None, 1)

class Ui_Help(object):
    def setupUi(self, Help):
        Help.resize(550,390)
        Help.setMinimumSize(550,390)
        Help.setMaximumSize(900,600)
        self.centralwidget = QWidget(Help)
        self.centralwidget.setMinimumSize(550,400)
        self.backTb = QToolButton(self.centralwidget)
        self.backTb.setGeometry(5,5,22,21)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/images/arrowleft.png"))
        self.backTb.setIcon(icon)
        self.forwardTb = QToolButton(self.centralwidget)
        self.forwardTb.setGeometry(28,5,22,21)
        icon.addPixmap(QPixmap(":/images/arrowright.png"))
        self.forwardTb.setIcon(icon)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(0,30,550,311)
        self.textBrowser.setMinimumSize(550,311)
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setHorizontalScrollBarPolicy(1) # Qt.ScrollBarAlwaysOff
        Help.setCentralWidget(self.centralwidget)
        self.menubar = Help.menuBar()
        self.statusbar = Help.statusBar()
        self.statusbar.setSizeGripEnabled(False)
        self.retranslateUi(Help)

    def retranslateUi(self, Help):
        Help.setWindowTitle(tl("GnuVet Help"))
        self.backTb.setToolTip(tl("go back"))
        self.backTb.setStatusTip(tl("Go backwards in History"))
        self.forwardTb.setToolTip(tl("go forward"))
        self.forwardTb.setStatusTip(tl("Go forward in history"))
