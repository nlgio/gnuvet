# -*- coding: utf-8 -*-
"""Replacement for QCompleter with something more to my liking, that offers
not only entries that start with txt, but also those that CONTAIN it, and
doesn't cause as much unused overhead.

USE
Create a completer object, taking care to use the parent of the widget(s)
for correct placement of completer.  Prepare a list -- or method to produce
a list -- for the widget.  Then add
    self.gc = Gcompleter(self.widgetparent, self.widget, self.list)
to your __init__ or whatever sets the completer.

If more than one widget shall use the completer, create a list of the widgets
to use the completer, prepare a list -- or method to produce a list -- for
each widget.  I recommend to
    setattr(widget, 'list', wlist)
for each widget involved.

Then add
    self.gc = Gcompleter(self.widgetparent)
    QApplication.instance().focusChanged.connect(self.focuschange)
to your __init__ or whatever sets the completer.

focuschange can of course be any name you like if appropriate.
And add the function:
    wef focuschange(self, old, new):
        if new in self.widgetlist:
            self.gc.setwidget(old=old, new=new, l=new.list)
    
That should suffice.
"""

# TODO:
# Key_Up on top Gcompcell kills completer:  Why?  This is Nonsense!
# check if completer fits into parent, else place above widget?
#  no rather ck height and reduce self.height accordingly... done, test
# text completion highlighting in Le suboptimal, irritating, inconsistent
# delete completer on click somewhere else in parent, but how?
# change wef for def in docstring above!  That was nec to trick emacs!

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
    markadd = 0
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
        if ev.key() == 0x01000000: # Qt.Key_Escape
            self.delcompl()
            print('gcompleter esc')
            return True
        if ev.key() == 0x01000015: # Qt.Key_Down
            if hasattr(self, 'fr'):
                if self.ewidget.hasFocus():
                    self.ewidget.removeEventFilter(self)
                    self.fr.setFocus()
                    self.fr.installEventFilter(self)
                    self.select_cell(self.gclist[0])
                elif self.fr.hasFocus():
                    new = (len(self.gclist)-1>self.gclist.index(self.selected)
                           and self.gclist[self.gclist.index(self.selected)+1]
                           or self.selected)
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
            return True # yes, this stops dd from walking through its entries
        elif ev.key() == 0x01000010: # Key_Home
            if hasattr(self, 'fr') and self.fr.hasFocus():
                self.select_cell(self.gclist[0])
                return True
            return False
        elif ev.key() == 0x01000011: # Key_End
            if hasattr(self, 'fr') and self.fr.hasFocus():
                self.select_cell(self.gclist[-1])
                return True
            return False
        elif ev.key() == 0x01000016: # Key_PageUp
            if hasattr(self, 'fr') and self.fr.hasFocus():
                self.select_cell(self.gclist[
                    self.gclist.index(self.selected)-6 > 0 and
                    self.gclist.index(self.selected)-6 or 0])
                self.fr.move(0, self.fr.y()) # (py?)qt bug
                return True
            return False
        elif ev.key() == 0x01000017: # Key_PageDown
            if hasattr(self, 'fr') and self.fr.hasFocus():
                self.select_cell(self.gclist[
                    self.gclist.index(self.selected)+6 < len(self.gclist) and
                    self.gclist.index(self.selected)+6 or -1])
                self.fr.move(0, self.fr.y())
                return True
            return False
        elif ev.key() in (0x01000004, 0x01000005, 0x01000014): # Ret Enter Right
            if self.selected:
                self.select(self.selected.text())
                self.delcompl()
                return True
        ## elif ev.key() in (0x01000003, 0x01000007): # Backspace, Delete
        ##     self.markadd += 1
        ##     return True # ?
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
            if self.otxt.startswith(txt) and self.otxt != txt:
                print('startswith "{}"'.format(txt))
                markstart = len(txt)
                while len(mlist) == 1:
                    txt = txt[:-1]
                    mlist = self.mklist(txt)
                wid.setSelection(markstart, 80)
            return
        self.resize(self.ewidget.width(), self.ewidget.height()*self.maxshow)
        self.setFrameShape(1)
        ipos = 0
        hcorr = 2
        self.fr = QFrame(self)
        self.fr.resize(self.width(), self.ewidget.height()*len(mlist))
        for e in mlist:
            i = Gcompcell(self.fr, e)
            i.setGeometry(0, ipos, self.fr.width(), self.ewidget.height())
            self.gclist.append(i)
            ipos += i.height()
            i.clicked.connect(self.select)
        self.setWidget(self.fr)
        self.ewidget.installEventFilter(self)
        if self.fr.height()+hcorr < self.height():
            self.resize(self.width(), self.fr.height()+hcorr)
        y = self.ewidget.y() + self.ewidget.height()
        if (y + self.height() > self.parent().height()):
            self.resize(self.width(), self.parent().height()-y)
        self.fr.resize(
            self.width()-(self.verticalScrollBar().sizeHint().width()+hcorr),
            self.fr.height())
        self.move(self.ewidget.x(), y)
        self.show()

    def mklist(self, txt='', within=True):
        mlist = [e for e in self.clist if e.lower().startswith(txt)]
        if within:
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
        self.ensureWidgetVisible(gc, 0, 0)
        gc.enterEvent()
        
    def setwidget(self, old=None, new=None, l=None):
        """Bind Gcompleter to a (new) widget with a completion list."""
        if old == new:  return
        if old:
            old.removeEventFilter(self)
        self.clist = l or []
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
