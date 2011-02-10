#!/usr/bin/python

# Copyright 2010 Max Shinn

# This file is part of WriteType.

# WriteType is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# WriteType is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with WriteType.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui
from PyQt4.QtGui import QPainter, QPixmap, QColor
from PyQt4.QtCore import QPoint, QRect, Qt
from PyQt4.QtCore import SIGNAL
#from PyQt4 import QtCore
import sys
import resources_rc


#Debugging application
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

#Defines
MODE_REPLACE = 1
MODE_INSERT = 2
#Constants
LINE_HEIGHT = 30
#Formatting constants
PADDING_RIGHT = 2
PADDING_LEFT = 2

class ListWidgetItem:
    def __init__(self, word, weight=0, mode=MODE_REPLACE, colorfg=None, colorbg=None):
        self.word = word
        self.mode = mode
        self.weight = weight
        self.colorfg = colorfg
        self.colorbg = colorbg
        
class ListWidget(QtGui.QWidget):
    words = [ListWidgetItem("monkey", 3), ListWidgetItem("ape", 0), ListWidgetItem("gorilla", 9), ListWidgetItem("orangutan", 0), ListWidgetItem("chimpanzee", 0)]
    words_hash = None
    index = None
    arrow_image = QPixmap(":/res/arrow-right.png")
    speaker_image = QPixmap(":/res/speaker.png")

    def paintEvent(self, e):
        """Overloaded paintEvent from QWidget"""
        self.sortElements()         
        painter = QPainter(self)
        for word in enumerate(self.words):
            if (word[0]+1)*LINE_HEIGHT > self.height():
                break
            painter.setPen(Qt.black)

            #coloring the backgrounds if necessary
            bgcolor = QtGui.QColor.fromHsv(250-word[1].weight*25, word[1].weight*10, 255)
            painter.setBrush(bgcolor) 
            upperleft = QPoint(0,word[0]*LINE_HEIGHT)
            lowerright = QPoint(self.width()-2, LINE_HEIGHT*(word[0]+1))
            painter.drawRect(QRect(upperleft, lowerright))

            textpos = QPoint(20, word[0]*LINE_HEIGHT+LINE_HEIGHT/1.5)
            painter.drawText(textpos, word[1].word)

            if word[0] == self.index:
                arrowpos = QPoint(PADDING_LEFT, word[0]*LINE_HEIGHT+LINE_HEIGHT/2-self.arrow_image.height()/2)
                painter.drawPixmap(arrowpos, self.arrow_image)

            speakerpos = QPoint(self.width()-self.speaker_image.width()-PADDING_RIGHT, word[0]*LINE_HEIGHT+LINE_HEIGHT/2-self.arrow_image.height()/2)
            painter.drawPixmap(speakerpos, self.speaker_image)

            #Draw F-key shortcut hints
            if word[0] + 1 <= 12:
                painter.setPen(Qt.gray)
                fpos = QPoint(self.width()-PADDING_RIGHT-self.speaker_image.width()-30, word[0]*LINE_HEIGHT+LINE_HEIGHT/1.5)
                painter.drawText(fpos, "(F" + str(word[0]+1) + ")")
            
        QtGui.QWidget.paintEvent(self, e)

    def mouseReleaseEvent(self, e):
        """Overloaded mouseReleaseEvent from QWidget"""
        #Over which word is it hovering?
        hoverindex = int(e.y()/LINE_HEIGHT)

        #Speak the word?
        if e.x() < self.width()-PADDING_RIGHT and e.x() > self.width()-self.speaker_image.width()-PADDING_RIGHT:
            self.emit(SIGNAL("speakWord"), self.words[hoverindex].word)
        else:
            self.activate(hoverindex)
        QtGui.QWidget.mouseReleaseEvent(self, e)

    def _countLines(self):
        lines = int(self.height()/LINE_HEIGHT)
        if len(self.words) < lines:
            lines = len(self.words)
        return lines

    def tabEvent(self):
        if self.index == None or self.index == self._countLines() - 1:
            self.index = 0
        else:
            self.index += 1
        self.activate(self.index)

    def backtabEvent(self):
        if self.index == None or self.index == 0:
            self.index = self._countLines() - 1
        else:
            self.index -= 1
        self.activate(self.index)

    def clearSelection(self):
        """Resets the selected word index"""
        self.index = None
        self.repaint()

    def clear(self):
        self.words = []
        self.clearSelection()
        self.repaint()

    def sortElements(self):
        self.words.sort(lambda x, y : cmp(y.weight,x.weight))

    def setWords(self, words):
        self.words = words

    def addItem(self, item):
        self.words.append(item)
        #self.repaint()

    def addNewItem(self, word, **kwargs):
        item = ListWidgetItem(word, **kwargs)
        self.addItem(item)

    def activate(self, index):
        """Set a particular list item as active"""
        self.index = index
        self.emit(SIGNAL("wordPressed"), unicode(self.words[index].word), self.words[index].mode)
        self.repaint()

#Finish debugging application
if __name__ == "__main__":
    widget = ListWidget()
    widget.show()
    app.exec_()
