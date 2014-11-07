"""The help module."""
from os import uname, path
from PyQt4.QtCore import QUrl, pyqtSignal
from PyQt4.QtGui import QMainWindow, QAction, QMenu
from help_ui import Ui_Help
import gv_qrc

class Help(QMainWindow):
    def __init__(self, parent=None, hdoc='toc.html'):
        super(Help, self).__init__(parent)
        self.w = Ui_Help()
        self.w.setupUi(self)
        self.w.textBrowser.setSearchPaths(self.help_dir())
        #    ACTIONS
        self.backA = QAction(self.tr('Bac&k'), self)
        self.backA.setAutoRepeat(0)
        self.backA.setShortcut(self.tr('Alt+Left'))
        self.backA.setStatusTip(self.tr('Go to previous page'))
        self.forwardA = QAction(self.tr('&Forward'), self)
        self.forwardA.setAutoRepeat(0)
        self.forwardA.setShortcut(self.tr('Alt+Right'))
        self.forwardA.setStatusTip(self.tr('Go to next page'))
        closeA = QAction(self.tr('&Close'), self)
        closeA.setAutoRepeat(0)
        closeA.setShortcut(self.tr('Ctrl+W'))
        closeA.setStatusTip(self.tr('Close Help Window'))
        contentsA = QAction(self.tr('Co&ntents'), self)
        contentsA.setAutoRepeat(0)
        contentsA.setStatusTip(self.tr('Go to Table of Contents'))
        indexA = QAction(self.tr('Help &Index'), self)
        indexA.setAutoRepeat(0)
        indexA.setShortcut(self.tr('Ctrl+I'))
        indexA.setStatusTip(self.tr('Go to Help Index'))
        quitA = QAction(self.tr('&Quit GnuVet'), self)
        quitA.setAutoRepeat(0)
        quitA.setShortcut(self.tr('Ctrl+Q'))
        quitA.setStatusTip(self.tr('Quit GnuVet'))
        helpA = QAction(self.tr('&Help'), self)
        helpA.setAutoRepeat(0)
        helpA.setShortcut('F1')
        helpA.setStatusTip(self.tr('How to use the Help System'))
        #    MENUES
        goM = QMenu(self.w.menubar)
        goM.setTitle(self.tr('&Go'))
        helpM = QMenu(self.w.menubar)
        helpM.setTitle(self.tr('&Help'))
        self.w.menubar.addAction(goM.menuAction())
        self.w.menubar.addAction(helpM.menuAction())
        goM.addAction(self.backA)
        goM.addAction(self.forwardA)
        goM.addSeparator()
        goM.addAction(contentsA)
        goM.addAction(indexA)
        goM.addSeparator()
        goM.addAction(closeA)
        goM.addAction(quitA)
        helpM.addAction(helpA)
        self.backA.setEnabled(0)
        self.forwardA.setEnabled(0)
        self.w.backTb.setEnabled(0)
        self.w.forwardTb.setEnabled(0)
        #    CONNECTIONS
        quitA.triggered.connect(self.gv_quitconfirm)
        helpA.triggered.connect(self.help_help)
        indexA.triggered.connect(self.help_index)
        closeA.triggered.connect(self.close)
        self.w.textBrowser.backwardAvailable.connect(self.toggle_back)
        self.w.textBrowser.forwardAvailable.connect(self.toggle_forw)
        self.w.backTb.clicked.connect(self.w.textBrowser.backward)
        self.backA.triggered.connect(self.w.textBrowser.backward)
        self.w.forwardTb.clicked.connect(self.w.textBrowser.forward)
        self.forwardA.triggered.connect(self.w.textBrowser.forward)
        contentsA.triggered.connect(self.contents_help)
        self.show()
        self.show_help(hdoc)

    def contents_help(self):
        self.help_file('toc.html')

    def gv_quitconfirm(self):
        if self.parent():
            self.parent().gv_quitconfirm()
        else:
            exit()
            
    def help_dir(self):
        """Return list of paths to help docs for setSearchPaths()."""
        if not 'os_name' in locals():
            from os import name as os_name
        if os_name == 'posix':
            return ['/usr/share/gnuvet/help/']
        elif os_name == 'nt':
            return ['/Program Files/gnuvet/help/']
        else:
            print('Xorry, OSs other than "posix" and "nt" not yet implemented.')
            return []

    def help_file(self, hfile):
        self.w.textBrowser.setSource(QUrl(hfile))

    def help_help(self):
        self.help_file('help.html')

    def help_index(self):
        self.help_file('index.html')

    def resizeEvent(self, ev):
        self.w.textBrowser.resize(ev.size().width(), ev.size().height()-89)

    def show_help(self, hdoc='toc.html'):
        self.help_file(hdoc)

    def toggle_back(self, avail=False):
        if avail:
            self.w.backTb.setEnabled(1)
            self.backA.setEnabled(1)
        else:
            self.w.backTb.setEnabled(0)
            self.backA.setEnabled(0)

    def toggle_forw(self, avail=False):
        if avail:
            self.w.forwardTb.setEnabled(1)
            self.forwardA.setEnabled(1)
        else:
            self.w.forwardTb.setEnabled(0)
            self.forwardA.setEnabled(0)

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    a = QApplication([])
    c = Help(None)
    exit(a.exec_())
