# -*- coding: utf-8 -*-
"""Try to replace QCompleter with something more to my liking, that offers not 
only entries that start with txt, but also those that CONTAIN it, and doesn't
cause as much unused overhead."""

from PyQt4.QtCore import pyqtSignal, QEvent, QString
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
            self.setwidget(widget, l)
            ## print('LineEdit size {}, sizeHint {}'.format(
            ##     widget.size(), widget.sizeHint()))
        self.hide()

    def delcompl(self):
        if hasattr(self, 'fr'):
            del(self.fr) # should delete all gcompcells as well
            self.gclist = []
        self.hide()

    def keyPressEvent(self, ev):
        # how tell between Le and Dd???  I start with Le. # hierwei
        if ev.key() == Qt.Key_Down:
            if self.widget.hasFocus():
                self.fr.setFocus() # ?
                self.setselection(self.gclist[0])
            elif self.fr.hasFocus():
                self.selected.setStyleSheet(self.gccellss.format(*self.normal))
                new = (len(self.gclist) > self.gclist.index(e) and
                       self.gclist[self.gclist.index(e)+1] or e)
                new.setStyleSheet(self.gccellss.format(*self.selection))
        elif ev.key() == Qt.Key_Up:
            if not self.widget.hasFocus():
                new = (self.gclist.index(self.selected) > 0 and
                       self.gclist[self.gclist.index(self.selected)-1] or None)
                if self.selected:
                    self.selected.setStyleSheet(
                        self.gccellss.format(*self.normal))
                if new:
                    new.setStyleSheet(
                        self.gccellss.format(*self.selection))
                else:
                    self.widget.setFocus()
        elif ev.key() == Qt.Key_Right:
            if self.selected:
                if self.wtype == 'le':
                    self.widget.setText(self.selected.text())
                elif self.wtype == 'dd':
                    self.widget.setCurrentIndex(
                        self.widget.findData(self.selected.text()))
        
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
            self.selected.setStyleSheet(self.gccellss.format(*self.normal))
        self.selected = gc
        gc.setStyleSheet(self.gccellss.format(*self.selection))
        
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
