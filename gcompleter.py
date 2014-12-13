# -*- coding: utf-8 -*-
"""Try to replace QCompleter with something more to my liking, that offers not 
only entries that start with txt, but also those that CONTAIN it, and doesn't
cause as much unused overhead."""

# TODO:
# OOPS, ein quirx zwischen mouseHover und Selektion per Tasten!
# oops, there's still problems with le:
# on only one completion: eventFilter->select_cell->enterEvent->
# RuntimeError: wrapped C/C++ object of type Gcompcell has been deleted
#  -> change eventFilter from le|dd to fr on moving via keys and vice versa!
# fixed?
# and:
##   File "/usr/local/enno/src/py/gnuvet/gcompleter.py", line 77, in eventFilter
##     self.fr.setFocus()
## AttributeError: 'Gcompleter' object has no attribute 'fr'
## and:
## backspace problem in le: use selection?
## and:
## on completion (Key_Right) in dd focus jumps to le
# ck focusChanged in parent: use list of widgets2complete!
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
        self.parent = parent.parent()
        self.setAttribute(55) # Qt.WA_DeleteOnClose
        self.setStyleSheet(self.gccellss.format(*self.normal))
        self.setMouseTracking(True)
        if txt:
            self.setText(txt)

    def enterEvent(self, ev=None): # Cave this seems to differ from Qt's way
        if self.parent.selected:
            self.parent.selected.deselect()
        self.parent.selected = self
        self.setStyleSheet(self.gccellss.format(*self.selection))
        
    def deselect(self):
        self.setStyleSheet(self.gccellss.format(*self.normal))
        
    def mousePressEvent(self, ev): # ev is QMouseEvent
        self.clicked.emit(self.text())
        
class Gcompleter(QScrollArea):
    selected = None
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
        print('delcompl')
        self.selected = None
        if hasattr(self, 'ewidget'):
            self.ewidget.removeEventFilter(self)
        if hasattr(self, 'fr'):
            del(self.fr) # should delete all gcompcells as well
            self.gclist = []
        self.hide()

    def eventFilter(self, ob, ev):
        if ev.type() != 6: # QEvent.KeyPress
            return False
        if ev.key() == 0x01000015: # Qt.Key_Down
            print('evF Down'),
            if self.ewidget.hasFocus():
                print('ewidget')
                self.ewidget.removeEventFilter(self)
                self.fr.setFocus()
                self.fr.installEventFilter(self)
                self.select_cell(self.gclist[0])
                return True
            elif self.fr.hasFocus():
                print('fr')
                new = (len(self.gclist) > self.gclist.index(self.selected) and
                       self.gclist[self.gclist.index(self.selected)+1] or
                       self.selected)
                self.select_cell(new)
                return True
        elif ev.key() == 0x01000013: # Qt.Key_Up
            print('evF Up'),
            if self.fr.hasFocus():
                print('fr'),
                new = (self.gclist.index(self.selected) > 0 and
                       self.gclist[self.gclist.index(self.selected)-1] or None)
                if new:
                    print('lower')
                    self.select_cell(new)
                else:
                    print('upmost')
                    self.fr.removeEventFilter(self)
                    self.ewidget.setFocus()
                    self.ewidget.installEventFilter(self)
                    self.selected.deselect()
                    self.selected = None
                return True
        elif ev.key() in (0x01000004, 0x01000005, 0x01000014): # Ret Enter Right
            print('evF confirm')
            if self.selected:
                self.select(self.selected.text())
                return True
            return False
        return False ## ???
        
    def listmatch(self, txt=''):
        self.delcompl()
        if not txt:
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

    def select(self, txt):
        if self.wtype == 'le':
            self.ewidget.setText(txt)
        elif self.wtype == 'dd':
            self.ewidget.setCurrentIndex(self.ewidget.findText(txt))
        self.delcompl()

    def select_cell(self, gc):
        if self.selected:
            self.selected.deselect()
        self.selected = gc
        gc.enterEvent()
        
    def setwidget(self, old=None, new=None, l=None):
        ch_conn(self, 'widget')
        if old: ## and old in self.wlist:
            old.removeEventFilter(self)
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
        self.ewidget = new
