"""GnuVet 'About' Dialog."""
from PyQt4.QtGui import QAction, QMainWindow
from PyQt4.QtCore import pyqtSignal
from about_ui import Ui_About
import gv_version
from keycheck import Keycheck

class About(QMainWindow):
    def __init__(self, parent=None, lang='en'):
        super(About, self).__init__(parent)
        self.w = Ui_About()
        self.w.setupUi(self)
        quitA = QAction(self.tr('&Quit'), self)
        quitA.setAutoRepeat(0)
        quitA.setShortcut(self.tr('Ctrl+Q'))
        self.addAction(quitA)
        quitA.triggered.connect(self.gv_quitconfirm)
        closeA = QAction(self)
        closeA.setAutoRepeat(0)
        closeA.setShortcut('Ctrl+W')
        closeA.triggered.connect(self.close)
        if parent:
            self.w.okPb.clicked.connect(self.hide)
        else:
            self.w.okPb.clicked.connect(self.close)
        self.w.okPb.setDefault(1)
        keycheck = Keycheck(self)
        self.installEventFilter(keycheck)
        keycheck.enter.connect(self.w.okPb.click)
        self.w.vLb.setText(gv_version.version)
        self.w.aboutLb.setText(gv_version.copyleft[lang])
        self.show()

    def closeEvent(self, ev):
        if self.parent():
            self.parent().xy_decr()
        
    def gv_quitconfirm(self):
        if self.parent():
            self.parent().gv_quitconfirm()
        else:
            exit()

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    from options import read_options
    options = read_options()
    a = QApplication([])
    b = About(None, options['lang'])
    b.show()
    exit(a.exec_())
