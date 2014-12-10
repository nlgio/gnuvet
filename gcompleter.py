# -*- coding: utf-8 -*-
"""Try to replace QCompleter with something more to my liking, that offers not 
only entries that start with txt, but also those that CONTAIN it, and doesn't
cause as much unused overhead."""

# TODO:
# 

from PyQt4.QtCore import pyqtSignal, QString
from PyQt4.QtGui import (QComboBox, QFrame, QMouseEvent, QLabel, QLineEdit,
                         QScrollArea)
from util import ch_conn

class Gcompcell(QLabel):
    """Single Completer Line."""
    clicked = pyqtSignal(QString)

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
    selected = None # was pyqtSignal(QString)
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
            self.setwidget(new=widget, l=l)
        self.hide()

    def delcompl(self):
        self.selected = None
        if hasattr(self, 'fr'):
            del(self.fr) # should delete all gcompcells as well
            self.gclist = []
        self.hide()

    def eventFilter(self, ob, ev):
        # how tell between Le and Dd???  I start with Le. # hierwei
        if ev.type() != 6: # QEvent.KeyPress
            return False
        if ev.key() == 0x01000015: # Qt.Key_Down
            if self.widget.hasFocus():
                self.fr.setFocus()
                self.setselection(self.gclist[0])
                return True
            elif self.fr.hasFocus():
                new = (len(self.gclist) > self.gclist.index(self.selected) and
                       self.gclist[self.gclist.index(self.selected)+1] or
                       self.selected)
                self.setselection(new)
                return True
        elif ev.key() == 0x01000013: # Qt.Key_Up
            if not self.widget.hasFocus():
                new = (self.gclist.index(self.selected) > 0 and
                       self.gclist[self.gclist.index(self.selected)-1] or None)
                if new:
                    self.setselection(new)
                else:
                    self.widget.setFocus()
                return True
            return False # ?
        elif ev.key() == 0x01000014: # Qt.Key_Right
            if self.selected:
                if self.wtype == 'le':
                    self.widget.setText(self.selected.text())
                elif self.wtype == 'dd':
                    self.widget.setCurrentIndex(
                        self.widget.findText(self.selected.text())) # flags?
                self.delcompl()
                return True
        return False ## ???
        
    def listmatch(self, txt=''):
        # use install|removeEventFilter on (parent) widget?  (QCompleter.cpp)
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
            self.gclist.append(i)
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

    def setselection(self, gc):
        if self.selected:
            self.selected.leaveEvent(None)
        self.selected = gc
        gc.enterEvent(None)
        
    def setwidget(self, old=None, new=None, l=None):
        ch_conn(self, 'widget')
        if old:
            old.removeEventFilter(self)
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
        new.installEventFilter(self)
        self.widget = new
