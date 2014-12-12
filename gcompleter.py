# -*- coding: utf-8 -*-
"""Try to replace QCompleter with something more to my liking, that offers not 
only entries that start with txt, but also those that CONTAIN it, and doesn't
cause as much unused overhead."""

# TODO:
# oops, there's still problems with le:
# on only one completion: eventFilter->select_cell->enterEvent->
# RuntimeError: wrapped C/C++ object of type Gcompcell has been deleted
#  -> change eventFilter from le|dd to fr on moving via keys and vice versa!
# and:
##   File "/usr/local/enno/src/py/gnuvet/gcompleter.py", line 77, in eventFilter
##     self.fr.setFocus()
## AttributeError: 'Gcompleter' object has no attribute 'fr'
## and:
## on completion (Key_Right) in dd focus jumps to le

#
# ck gcompleter w/ dd

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

    def enterEvent(self, ev=None): # Cave this seems to differ from Qt's way
        self.setStyleSheet(self.gccellss.format(*self.selection))
        
    def leaveEvent(self, ev=None):
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
        if hasattr(self, 'ewidget'):
            self.ewidget.removeEventFilter(self)
        if hasattr(self, 'fr'):
            del(self.fr) # should delete all gcompcells as well
            self.gclist = []
        self.hide()

    def eventFilter(self, ob, ev):
        # how tell between Le and Dd???  I start with Le. # hierwei
        if ev.type() != 6: # QEvent.KeyPress
            return False
        if ev.key() == 0x01000015: # Qt.Key_Down
            if self.ewidget.hasFocus():
                self.fr.setFocus()
                self.select_cell(self.gclist[0])
                return True
            elif self.fr.hasFocus():
                new = (len(self.gclist) > self.gclist.index(self.selected) and
                       self.gclist[self.gclist.index(self.selected)+1] or
                       self.selected)
                self.select_cell(new)
                return True
        elif ev.key() == 0x01000013: # Qt.Key_Up
            if not self.ewidget.hasFocus():
                new = (self.gclist.index(self.selected) > 0 and
                       self.gclist[self.gclist.index(self.selected)-1] or None)
                if new:
                    self.select_cell(new)
                else:
                    self.ewidget.setFocus()
                return True
            return False # ?
        elif ev.key() in (0x01000004, 0x01000005, 0x01000014): # Ret Enter Right
            if self.selected:
                if self.wtype == 'le':
                    self.ewidget.setText(self.selected.text())
                elif self.wtype == 'dd':
                    self.ewidget.setCurrentIndex(
                        self.ewidget.findText(self.selected.text())) # flags?
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
        if len(mlist) == 1:
            if self.wtype == 'le':
                self.ewidget.setText(mlist[0])
                # hierwei mark text s. saepat?
            elif self.wtype == 'dd': # hierwei completiontext
                self.ewidget.setCurrentIndex(self.ewidget.findText(mlist[0]))
                if len(self.ewidget.currentText()) > len(txt):
                    self.ewidget.lineEdit().setSelection(len(txt), 80)
            self.delcompl()
            # hierwei removeEventFilter?
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
        hcorr = 2
        if self.fr.height()+hcorr < self.height():
            self.resize(self.width(), self.fr.height()+hcorr)
        self.show()

    def select(self, txt):
        if self.wtype == 'le':
            self.ewidget.setText(txt)
        elif self.wtype == 'dd':
            self.ewidget.setCurrentIndex(self.ewidget.findText(txt))
        self.delcompl()

    def select_cell(self, gc):
        if self.selected:
            self.selected.leaveEvent()
        self.selected = gc
        gc.enterEvent()
        
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
        self.ewidget = new
