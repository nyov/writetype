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
#from PyQt4 import QtCore
import sys
import resources_rc


#Debugging application
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)


#Constants
LINE_HEIGHT = 30
#Formatting constants
PADDING_RIGHT = 2
PADDING_LEFT = 2

class ListWidget(QtGui.QWidget):
	words = [("monkey", 3), ("ape", 0), ("gorilla", 9), ("orangutan", 0), ("chimpanzee", 0)]
	words_hash = None
	index = None
	arrow_image = QPixmap(":/res/arrow-right.png")
	speaker_image = QPixmap(":/res/speaker.png")

	def paintEvent(self, e):
		"""Overloaded paintEvent from QWidget"""
		self.sortElements()			
		painter = QPainter(self)
		for word in enumerate(self.words):
			painter.setPen(Qt.black)

			#coloring the backgrounds if necessary
			bgcolor = QtGui.QColor.fromHsv(250-word[1][1]*25, word[1][1]*10, 255)
			painter.setBrush(bgcolor) 
			upperleft = QPoint(0,word[0]*LINE_HEIGHT)
			lowerright = QPoint(self.width(), LINE_HEIGHT*(word[0]+1))
			painter.drawRect(QRect(upperleft, lowerright))

			textpos = QPoint(20, word[0]*LINE_HEIGHT+LINE_HEIGHT/1.5)
			painter.drawText(textpos, word[1][0])

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
			print "Implement this later... speak the word " + self.words[hoverindex][0]
		QtGui.QWidget.mouseReleaseEvent(self, e)

	def keyPressEvent(self, e):
		"""Overloaded keyPressEvent from QWidget"""
		#Tabbing to a word
		if e.key() == Qt.Key_Tab or e.key() == Qt.Key_Down:
			if self.index == None or self.index == len(self.words) - 1:
				self.index = 0
			else:
				self.index += 1
		elif e.key() == Qt.Key_Backtab or e.key() == Qt.Key_Up:
			if self.index == None or self.index == 0:
				self.index = len(self.words) - 1
			else:
				self.index -= 1
		#F-keys select words quickly
		fkeys = [Qt.Key_F1, Qt.Key_F2, Qt.Key_F3, Qt.Key_F4, Qt.Key_F5, Qt.Key_F6, Qt.Key_F7, Qt.Key_F8, Qt.Key_F9, Qt.Key_F10, Qt.Key_F11, Qt.Key_F12]
		if e.key() in fkeys:
			fkeyindex = fkeys.index(e.key())
			if fkeyindex <= len(self.words) - 1:
				self.index = fkeyindex
		QtGui.QWidget.keyPressEvent(self, e)
		self.repaint()

	def clearSelection(self):
		"""Resets the selected word index"""
		self.index = None
		self.repaint()

	def sortElements(self):
		self.words.sort(lambda x, y : cmp(y[1],x[1]))

#Finish debugging application
if __name__ == "__main__":
	widget = ListWidget()
	widget.show()
	app.exec_()
