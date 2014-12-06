"""Try to replace QCompleter with something more to my liking, that offers not 
only entries that start with txt, but also those that CONTAIN it."""

from PyQt4.QtCore import pyqtSignal, QEvent, QString
from PyQt4.QtGui import QFrame, QLabel, QScrollArea
from util import ch_conn

class Gcompcell(QLabel):
    """Single Completer Line."""
    clicked = pyqtSignal(QString)
    __index = -1
    _index = -1

    def __init__(self, parent=None, txt=''):
        self.__class__.__index += 1
        self._index = self.__class__.__index
        super(Gcompcell, self).__init__(parent)
        self.setAttribute(55) # Qt.WA_DeleteOnClose

    def index(self): # superfluous?  But nice :).
        return self._index

    def mousePressEvent(self, ev): # ev is QMouseEvent
        self.clicked.emit(self.text())
        
class Gcompleter(QScrollArea):
    selected = pyqtSignal(QString)
    maxshow = 7
    gccellss = """Gcompcell {{
background: white;
color: black;
border: 0px;
border-radius: 3px;
}}
"""
    
    def __init__(self, parent=None, l=None, widget=None):
        super(Gcompleter, self).__init__(parent)
        self.conns = {} # pyqt bug disconnect
        self.sigs = {} # dto
        self.setHorizontalScrollBarPolicy(1) # never
        self.setVerticalScrollBarPolicy(0)   # as needed
        self.setFrameShape(0)
        self.clist = l or []
        if not self.clist:  return
        self.resize(self.parent.size())
        self.maxy = self.maxshow * self.height()
        self.fr = None
        if widget:
            self.setwidget(widget, l)

    def delete(self):
        if self.fr:
            del(self.fr) # should delete all gcompcells as well            
        
    def listmatch(self, txt=''):
        # first delete all existing gcompcells
        if not txt:  return
        txt = str(txt).lower()
        mlist = [e for e in self.clist if e.lower().startswith(txt)]
        mlist.extend([e for e in self.clist if e.lower().count(txt)
                      and e not in mlist])
        ipos = 0
        self.fr = QFrame(self)
        self.fr.setFrameShape(0) # ?
        self.fr.resize(self.widget.size())
        for e in mlist:
            i = Gcompcell(self.fr, e)
            i.setGeometry(0, ipos, self.fr.width(), i.sizeHint().height()) # ?
            i.setStyle(gccell)
            ipos += i.sizeHint().height()
            i.clicked.connect(self.select)
        self.fr.resize(self.fr.width(), ipos)
        if self.fr.height() > self.maxy:
            self.resize(self.maxy)
        else:
            self.resize(self.fr.size())

    def select(self, txt):
        if self.wtype == 'le':
            self.widget.setText(txt)
        elif self.wtype == 'dd':
            self.widget.setCurrentIndex(self.widget.findText(txt))
        self.delete()

    def setwidget(self, new=None, l=None):
        ch_conn(self, 'widget')
        self.delete()
        self.clist = l or []
        self.widget = new
        if isinstance(new, QLineEdit):
            ch_conn(self, 'widget', new.textEdited.connect, self.listmatch)
            self.wtype = 'le'
        elif isinstance(new, QComboBox):
            ch_conn(self, 'widget',
                    new.lineEdit().textEdited.connect, self.listmatch)
            self.wtype = 'dd'
        
