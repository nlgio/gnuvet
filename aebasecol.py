"""Add or edit base-colours."""

# TODO:
# save all basecolours as col.lower()?

from psycopg2 import OperationalError
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import (QAction, QLabel, QMainWindow, QMenu)

from keycheck import Keycheck
from util import querydb
from aebasecol_ui import Ui_Aebasecol

class Aebasecol(QMainWindow):
    # signals
    addedbc = pyqtSignal(int, str, str)
    helpsig = pyqtSignal(str)
    savestate = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Aebasecol, self).__init__(parent)
        self.w = Ui_Aebasecol()
        self.w.setupUi(self)
        #    ACTIONS
        closeA = QAction(self.tr('Close &Window'), self)
        closeA.setAutoRepeat(False)
        closeA.setShortcut(self.tr('Ctrl+W'))
        closeA.setStatusTip(self.tr('Close this window'))
        self.dbA = QAction(self.tr('&Reconnect to database'), self)
        self.dbA.setAutoRepeat(False)
        self.dbA.setShortcut(self.tr('Ctrl+R'))
        self.dbA.setStatusTip(self.tr('Try to reconnect to database'))
        helpA = QAction(self.tr('&Help'), self)
        helpA.setAutoRepeat(False)
        helpA.setShortcut(self.tr('F1'))
        helpA.setStatusTip(self.tr('Context sensitive help'))
        aboutA = QAction(self.tr('About &GnuVet'), self)
        aboutA.setAutoRepeat(False)
        aboutA.setStatusTip(self.tr('GnuVet version info'))
        quitA = QAction(self.tr('&Quit GnuVet'), self)
        quitA.setAutoRepeat(False)
        quitA.setShortcut(self.tr('Ctrl+Q'))
        quitA.setStatusTip(self.tr('Close all windows and quit GnuVet'))
        #    MENUES hierwei
        taskM = QMenu
        helpM = QMenu
        self.w.menubar.addAction(taskM.menuAction())
        self.w.menubar.addAction(helpM.menuAction())
        ...
        
    def closeEvent(self, ev):
        pass

