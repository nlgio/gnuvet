"""GnuVet 'About' Dialog."""
from PyQt4.QtGui import QAction, QMainWindow
from about_ui import Ui_About
import gv_version
from keycheck import Keycheck

class About(QMainWindow):
    gaia = None
    
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
        self.w.okPb.clicked.connect(self.close)
        self.w.okPb.setDefault(1)
        # GAIA
        if hasattr(parent, 'gaia'):
            if parent.gaia == 'gaia':
                self.gaia = parent
            else:
                self.gaia = parent.gaia
        keycheck = Keycheck(self)
        self.installEventFilter(keycheck)
        keycheck.enter.connect(self.w.okPb.click)
        ## self.w.vLb.setFrameShape(1)
        self.w.vLb.setStyleSheet(
            """QLabel { text-align: center; }""")
        self.w.vLb.setText(gv_version.version)
        ## self.w.aboutLb.setFrameShape(1)
        self.w.aboutLb.setText(gv_version.copyleft[lang])
        self.show()

    def closeEvent(self, ev):
        if self.gaia:
            self.gaia.xy_decr()
        
    def gv_quitconfirm(self):
        if self.gaia:
            self.gaia.gv_quitconfirm()
        else:
            exit()

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    from options import defaults as options
    a = QApplication([])
    b = About(parent=None, lang=options['lang'])
    b.show()
    exit(a.exec_())
