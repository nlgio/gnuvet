"""Try to replace QCompleter with something more to my liking, that offers not 
only entries that start with txt, but also those that CONTAIN it."""

from PyQt4.QtCore import pyqtSignal, QEvent, QString
from PyQt4.QtGui import QFrame, QLabel, QScrollArea

class Gcompcell(QLabel):
    """Single Completer Line."""
    clicked = pyqtSignal(QString)

    def __init__(self, parent=None, txt=''):
        super(Gcompcell, self).__init__(parent)
        self.setAttribute(55) # Qt.WA_DeleteOnClose

    def mousePressEvent(self, ev): # ev is QMouseEvent
        self.clicked.emit(self.text())
        
class Gcompleter(QScrollArea):
    selected = pyqtSignal(QString)
    maxshow = 7
    gccellss = """Gcompcell {{
background: {};
color: {};
border: 0px;
border-radius: 3px;
}}
"""
    normal = ('white', 'black')
    selection = ('darkblue', 'white')
    prevss = ''
    
    def __init__(self, parent=None, l=None):
        super(Gcompleter, self).__init__(parent)
        self.setHorizontalScrollBarPolicy(1) # never
        self.setVerticalScrollBarPolicy(0) # as needed
        self.setFrameShape(0)
        self.fr = QFrame(self)
        
        ## self.resize(...)
