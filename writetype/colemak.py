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

from spellCheckEdit import spellCheckEdit
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QKeyEvent
from PyQt4.QtCore import QEvent

class ColemakEdit(spellCheckEdit):
	newmap = {
		Qt.Key_E: Qt.Key_F,
		Qt.Key_R: Qt.Key_P,
		Qt.Key_T: Qt.Key_G,
		Qt.Key_Y: Qt.Key_J,
		Qt.Key_U: Qt.Key_L,
		Qt.Key_I: Qt.Key_U,
		Qt.Key_O: Qt.Key_Y,
		Qt.Key_P: Qt.Key_Semicolon,
		Qt.Key_P & Qt.Key_Shift: Qt.Key_Colon,
		Qt.Key_S: Qt.Key_R,
		Qt.Key_D: Qt.Key_S,
		Qt.Key_F: Qt.Key_T,
		Qt.Key_G: Qt.Key_D,
		Qt.Key_J: Qt.Key_N,
		Qt.Key_K: Qt.Key_E,
		Qt.Key_L: Qt.Key_I,
		Qt.Key_Semicolon: Qt.Key_O,
		Qt.Key_Colon: Qt.Key_O,
		Qt.Key_N: Qt.Key_K,
		Qt.Key_CapsLock: Qt.Key_Backspace,
		}
	newtext = {
		"E": "F",
		"R": "P",
		"T": "G",
		"Y": "J",
		"U": "L",
		"I": "U",
		"O": "Y",
		"P": ":",
		"S": "R",
		"D": "S",
		"F": "T",
		"G": "D",
		"J": "N",
		"K": "E",
		"L": "I",
		":": "O",
		"N": "K",
		"e": "f",
		"r": "p",
		"t": "g",
		"y": "j",
		"u": "l",
		"i": "u",
		"o": "y",
		"p": ";",
		"s": "r",
		"d": "s",
		"f": "t",
		"g": "d",
		"j": "n",
		"k": "e",
		"l": "i",
		";": "o",
		"n": "k",
		"": ""
		}
	def keyPressEvent(self, event):
		if event.key() in self.newmap:
			event = QKeyEvent(QEvent.KeyPress, self.newmap[event.key()], event.modifiers(), self.newtext[str(event.text())], event.isAutoRepeat(), event.count())
		spellCheckEdit.keyPressEvent(self, event)
