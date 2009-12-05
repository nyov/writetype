from PyQt4.Qt import QTextEdit, QMouseEvent, QTextCursor, QSyntaxHighlighter, QKeyEvent, QFont
from PyQt4.Qt import Qt
from PyQt4.Qt import QEvent
from PyQt4.Qt import QAction
from PyQt4.Qt import QTextCharFormat
from PyQt4.QtCore import SIGNAL
from PyQt4 import QtCore
import re
import enchant
import enchant.checker
from enchant.tokenize import get_tokenizer
from platformSettings import platformSettings

class spellCheckEdit(QTextEdit):
	def __init__(self, *args):
		QTextEdit.__init__(self, *args)
		self.dictionary = enchant.DictWithPWL('en_us')
		self.highlighter = Highlighter(self.document())
		self.setFontPointSize(12)
		self.highlighter.setDict(self.dictionary)
		#Set the stuff up to ask for a save on exit
		
		
	def mousePressEvent(self, event):
		if event.button() == Qt.RightButton:
			#This will move the cursor to the appropriate position
			event = QMouseEvent(QEvent.MouseButtonPress, event.pos(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
		QTextEdit.mousePressEvent(self, event)
	
	def contextMenuEvent(self, event):
		menu = self.createStandardContextMenu()
		#Select the word under the cursor
		cursor = self.textCursor()
		cursor.select(QTextCursor.WordUnderCursor)
		#self.setTextCursor(cursor)
		
		#If there is a word highlighted
		if cursor.hasSelection():
			text = unicode(cursor.selectedText())
			#If that word isn't in the dictionary
			if not self.dictionary.check(text):
				menu.addSeparator()
				spellingMenuItem = menu.addAction("Spelling:")
				spellingMenuItem.setEnabled(False)
				for word in self.dictionary.suggest(text):
					action = QAction(word, menu)
					self.connect(action, SIGNAL("triggered()"), lambda targ=word: self.correctWord(targ, cursor))
					menu.addAction(action)
				if len(self.dictionary.suggest(text)) == 0:
					noneMenuItem = menu.addAction("None")
					noneMenuItem.setEnabled(False)
				addToDictionary = QAction("Add to dictionary", menu)
				self.connect(addToDictionary, SIGNAL("triggered()"), lambda targ=text: self.addToDictionary(targ))
				menu.addAction(addToDictionary)
		
		menu.exec_(event.globalPos())
		
	def correctWord(self, word, cursor=0):
		#Replace the selected word with another word
		if cursor == 0:
			cursor = self.textCursor()
		cursor.beginEditBlock()
		cursor.removeSelectedText()
		cursor.insertText(word)
		cursor.endEditBlock()
	def addToDictionary(self, word):
		self.dictionary.add(word)
		
	def correctWordList(self, wordItem):
		word = wordItem.text()
		#Replace the selected word with another word
		cursor = self.textCursor()
		cursor.select(QTextCursor.WordUnderCursor)
		#Make sure the last word is selected
		while not cursor.selectedText():
			cursor.deletePreviousChar()
			cursor.select(QTextCursor.WordUnderCursor)
		if re.match(u'[A-Z][a-z]*', unicode(cursor.selectedText())):
			word = unicode(word).capitalize()
		cursor.beginEditBlock()
		cursor.removeSelectedText()
		cursor.insertText(word)
		cursor.endEditBlock()
		self.keyPressEvent(QKeyEvent(QEvent.KeyPress, 0, Qt.NoModifier))
		self.setFocus()
		
	def keyPressEvent(self, event):
		cursor = self.textCursor()
		cursor.select(QTextCursor.WordUnderCursor)
		if cursor.hasSelection():
			text = unicode(cursor.selectedText() + event.text())
		else:
			text = unicode(event.text())
		self.emit(SIGNAL("wordEdited"), text)
		self.emit(SIGNAL("keyPressed"))
		QTextEdit.keyPressEvent(self, event)
		
	#def italicSelectedText(self):
		#if self.fontItalic():
			#self.setFontItalic(0)
		#else:
			#self.setFontItalic(1)
		#self.setFocus()
	#def underlineSelectedText(self):
		#if self.fontUnderline():
			#self.setFontUnderline(0)
		#else:
			#self.setFontUnderline(1)
		#self.setFocus()
	#def titleSelectedText(self):
		#if self.fontPointSize() == 10:
			#self.setFontPointSize(24)
		#else:
			#self.setFontPointSize()
		#self.setFocus()
	def boldSelectedText(self):
		print "here"
		if self.fontWeight() == QFont.Bold:
			newweight = QFont.Normal
		else:
			newweight = QFont.Bold
		self.setFontWeight(newweight)
		self.setFocus()
		
	def italicSelectedText(self):
		print "here"
		self.setFontItalic(not self.fontItalic())
		self.setFocus()
	def underlineSelectedText(self):
		print "here"
		self.setFontUnderline(not self.fontUnderline())
		self.setFocus()



class Highlighter(QSyntaxHighlighter):

	WORDS = u'((?iu)[\w\']+)([\s\n .?!])'
	SENTENCE_ENDS = u'[.?!][\s]*[a-z]'
	SENTENCE_STARTS = u'^[a-z]'
	#A vs An?
	
	
	def __init__(self, *args):
		QSyntaxHighlighter.__init__(self, *args)
	
		self.dict = None
	
	def setDict(self, dict):
		self.dict = dict
	
	def highlightBlock(self, text):
		if not self.dict:
			return
	
		text = unicode(text)
	
		format_spelling = QTextCharFormat()
		format_spelling.setUnderlineColor(Qt.red)
		format_spelling.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
		format_spelling.setToolTip("Spelling error")
		
		format_capital = QTextCharFormat()
		format_capital.setUnderlineColor(Qt.blue)
		format_capital.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
		format_capital.setToolTip("Capitalize the first letter in the sentence.")
		
		for word_object in re.finditer(self.WORDS, text):
			#word_object = re.search(self.WORDS, word_object_extra.group())
			
			if not self.dict.check(word_object.group(1)):
				self.setFormat(word_object.start(), (word_object.end() - len(word_object.group(2))) - word_object.start(), format_spelling)
		for word_object in re.finditer(self.SENTENCE_ENDS, text):
				self.setFormat(word_object.start(), word_object.end() - word_object.start(), format_capital)
		for word_object in re.finditer(self.SENTENCE_STARTS, text):
				self.setFormat(word_object.start(), word_object.end() - word_object.start(), format_capital)