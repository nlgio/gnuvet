# -*- coding: utf-8 -*-
"""Replace QCompleter with something more to my liking, that offers not only 
entries that start with txt, but also those that CONTAIN it, and doesn't 
cause as much unused overhead."""

from PyQt4.QtCore import pyqtSignal, QString
from PyQt4.QtGui import (QComboBox, QFrame, QMouseEvent, QLabel,
                         QLineEdit, QScrollArea)
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
        self.parent = parent.parent()
        self.setAttribute(55) # Qt.WA_DeleteOnClose
        self.setStyleSheet(self.gccellss.format(*self.normal))
        self.setMouseTracking(True)
        if txt:
            self.setText(txt)

    def enterEvent(self, ev=None): # Cave this seems to differ from Qt's way
        """Select self when mouse hovers over self."""
        if self.parent.selected:
            self.parent.selected.unselect()
        self.parent.selected = self
        self.setStyleSheet(self.gccellss.format(*self.selection))

    def mousePressEvent(self, ev): # ev is QMouseEvent
        self.clicked.emit(self.text())
        
    def unselect(self):
        """Was leaveEvent, unusable under these circumstances."""
        self.setStyleSheet(self.gccellss.format(*self.normal))
        
class Gcompleter(QScrollArea):
    maxshow = 7
    selected = None

    def __init__(self, parent=None, widget=None, l=None):
        super(Gcompleter, self).__init__(parent)
        self.conns = {} # pyqt bug disconnect
        self.sigs = {} # dto
        self.gclist = [] # new 1412181748
        self.setHorizontalScrollBarPolicy(1) # never
        self.setVerticalScrollBarPolicy(0)   # as needed
        self.setFrameShape(0)
        self.clist = l or []
        if not self.clist:  return
        if widget:
            self.setwidget(new=widget, l=l)
        self.hide()

    def delcompl(self):
        """Kill the completer (fr w/ labels)."""
        self.selected = None
        if hasattr(self, 'ewidget'):
            self.ewidget.removeEventFilter(self)
            wid = self.ewidget
        if hasattr(self, 'fr'):
            del(self.fr)
            self.gclist = []
        self.hide()
        wid.setFocus()
        
    def eventFilter(self, ob, ev):
        if ev.type() != 6: # QEvent.KeyPress
            return False
        if ev.key() == 0x01000015: # Qt.Key_Down
            if hasattr(self, 'fr'):
                if self.ewidget.hasFocus():
                    self.ewidget.removeEventFilter(self)
                    self.fr.setFocus()
                    self.fr.installEventFilter(self)
                    self.select_cell(self.gclist[0])
                elif self.fr.hasFocus():
                    new = (len(self.gclist)>self.gclist.index(self.selected) and
                           self.gclist[self.gclist.index(self.selected)+1] or
                           self.selected)
                    self.select_cell(new)
                return True
        elif ev.key() == 0x01000013: # Qt.Key_Up
            if hasattr(self, 'fr') and self.fr.hasFocus():
                new = (self.gclist.index(self.selected) > 0 and
                       self.gclist[self.gclist.index(self.selected)-1] or None)
                if new:
                    self.select_cell(new)
                else:
                    self.fr.removeEventFilter(self)
                    self.ewidget.setFocus()
                    self.ewidget.installEventFilter(self)
                    if self.selected:
                        self.selected.unselect()
                        self.selected = None
                return True
            return True
        elif ev.key() in (0x01000004, 0x01000005, 0x01000014): # Ret Enter Right
            if self.selected:
                self.select(self.selected.text())
                self.delcompl()
                return True
        return False
        
    def listmatch(self, txt=''):
        """Set up the proper completer."""
        self.delcompl()
        if not txt:
            self.otxt = ''
            return
        txt = str(txt).lower()
        if len(self.otxt) < len(txt):
            self.otxt = txt
        mlist = self.mklist(txt)
        if len(mlist) == 1:
            if self.wtype == 'le':
                wid = self.ewidget
                wid.setText(mlist[0])
            elif self.wtype == 'dd':
                wid = self.ewidget.lineEdit()
                self.ewidget.setCurrentIndex(self.ewidget.findText(mlist[0]))
            self.otxt = mlist[0].lower()
            if self.otxt.startswith(txt) and self.otxt != txt: # backspace etc.
                while len(mlist) == 1:
                    txt = txt[:-1]
                    mlist = self.mklist(txt)
                markstart = len(txt)
                wid.setSelection(markstart, 80)
            return
        self.resize(self.ewidget.width(), self.ewidget.height()*self.maxshow)
        self.setFrameShape(1)
        ipos = 0
        self.fr = QFrame(self)
        self.fr.resize(self.ewidget.width(), self.ewidget.height()*len(mlist))
        for e in mlist:
            i = Gcompcell(self.fr, e)
            i.setGeometry(0, ipos, self.fr.width(), self.ewidget.height())
            self.gclist.append(i)
            ipos += i.height()
            i.clicked.connect(self.select)
        self.setWidget(self.fr)
        self.ewidget.installEventFilter(self)
        hcorr = 2
        if self.fr.height()+hcorr < self.height():
            self.resize(self.width(), self.fr.height()+hcorr)
        self.show()

    def mklist(self, txt=''):
        mlist = [e for e in self.clist if e.lower().startswith(txt)]
        mlist.extend([e for e in self.clist if e.lower().count(txt)
                      and e not in mlist])
        return mlist
    
    def select(self, txt):
        """Put selected text into active widget and delete completer."""
        if self.wtype == 'le':
            self.ewidget.setText(txt)
        elif self.wtype == 'dd':
            self.ewidget.setCurrentIndex(self.ewidget.findText(txt))
        self.delcompl()

    def select_cell(self, gc):
        if self.selected:
            self.selected.unselect()
        self.selected = gc
        gc.enterEvent()
        
    def setwidget(self, old=None, new=None, l=None):
        """Bind Gcompleter to a (new) widget with a completion list."""
        if old == new:  return
        if old:
            old.removeEventFilter(self)
        self.clist = l or []
        self.move(new.x(),
                  new.y()+new.height())
        if isinstance(new, QLineEdit):
            wid = new
            self.wtype = 'le'
        elif isinstance(new, QComboBox):
            wid = new.lineEdit()
            self.wtype = 'dd'
        ch_conn(self, 'widget', wid.textEdited, self.listmatch)
        self.otxt = str(wid.text().toLatin1()).lower()
        self.ewidget = new
        self.delcompl()
