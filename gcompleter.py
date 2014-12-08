# -*- coding: utf-8 -*-
"""Try to replace QCompleter with something more to my liking, that offers not 
only entries that start with txt, but also those that CONTAIN it."""

from PyQt4.QtCore import pyqtSignal, QEvent, QString
from PyQt4.QtGui import (QComboBox, QFrame, QMouseEvent, QLabel, QLineEdit,
                         QScrollArea)
from util import ch_conn

class Gcompcell(QLabel):
    """Single Completer Line."""
    clicked = pyqtSignal(QString)
    __index = -1
    _index = -1

    gccellss = """Gcompcell {{
background: {};
color: {};
border: 1px solid lightgray;
border-radius: 3px;
}}
"""

    normal = ('white', 'black')
    selection = ('darkblue', 'white')

    def __init__(self, parent=None, txt=''):
        super(Gcompcell, self).__init__(parent)
        self.setAttribute(55) # Qt.WA_DeleteOnClose
        self.setStyleSheet(self.gccellss.format(*self.normal))
        self.setMouseTracking(True)
        if txt:
            self.setText(txt)

    def enterEvent(self, ev): # Cave this seems to differ from Qt's way
        self.setStyleSheet(self.gccellss.format(*self.selection))
        
    def leaveEvent(self, ev):
        self.setStyleSheet(self.gccellss.format(*self.normal))
        
    def mousePressEvent(self, ev): # ev is QMouseEvent
        self.clicked.emit(self.text())
        
class Gcompleter(QScrollArea):
    selected = pyqtSignal(QString)
    maxshow = 7

    def __init__(self, parent=None, widget=None, l=None):
        super(Gcompleter, self).__init__(parent)
        self.conns = {} # pyqt bug disconnect
        self.sigs = {} # dto
        self.setHorizontalScrollBarPolicy(1) # never
        self.setVerticalScrollBarPolicy(0)   # as needed
        self.setFrameShape(0)
        self.clist = l or []
        if not self.clist:  return
        self.fr = None
        if widget:
            self.setwidget(widget, l)
            ## print('LineEdit size {}, sizeHint {}'.format(
            ##     widget.size(), widget.sizeHint()))
        self.hide()

    def delcompl(self):
        if hasattr(self, 'fr'):
            del(self.fr) # should delete all gcompcells as well
        self.hide()

    def keyPressEvent(self, ev):
        # how tell between Le and Dd???
        if ev.key() == Qt.Key_Down:
            pass
        elif ev.key() == Qt.Key_Up:
            pass
        elif ev.key() == Qt.Key_Right:
            pass
        
    def listmatch(self, txt=''):
        if not txt:
            self.delcompl()
            return
        txt = str(txt).lower()
        mlist = [e for e in self.clist if e.lower().startswith(txt)]
        mlist.extend([e for e in self.clist if e.lower().count(txt)
                      and e not in mlist])
        self.resize(self.widget.width(), self.widget.height()*self.maxshow)
        self.setFrameShape(1)
        ipos = 0
        self.fr = QFrame(self)
        self.fr.resize(self.widget.width(), self.widget.height()*len(mlist))
        for e in mlist:
            i = Gcompcell(self.fr, e)
            i.setGeometry(0, ipos, self.fr.width(), self.widget.height())
            ## i.setStyleSheet(self.gccellss.format(*self.normal))
            ipos += i.height()
            i.clicked.connect(self.select)
        self.setWidget(self.fr)
        hcorr = 2
        if self.fr.height()+hcorr < self.height():
            self.resize(self.width(), self.fr.height()+hcorr)
        self.show()

    def select(self, txt):
        if self.wtype == 'le':
            self.widget.setText(txt)
        elif self.wtype == 'dd':
            self.widget.setCurrentIndex(self.widget.findText(txt))
        self.delcompl()

    def setwidget(self, new=None, l=None):
        ch_conn(self, 'widget')
        self.delcompl()
        self.clist = l or []
        self.move(new.x(),
                  new.y()+new.height())
        if isinstance(new, QLineEdit):
            ch_conn(self, 'widget', new.textEdited, self.listmatch)
            self.wtype = 'le'
        elif isinstance(new, QComboBox):
            ch_conn(self, 'widget',
                    new.lineEdit().textEdited, self.listmatch)
            self.wtype = 'dd'
        self.widget = new
