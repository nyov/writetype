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


from PyQt4.Qt import QTextEdit, QMouseEvent, QTextCursor, QSyntaxHighlighter, QKeyEvent, QFont, QColor
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
import platformSettings
#For logger
import urllib
import urllib2
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QTextBlockUserData

class spellCheckEdit(QTextEdit):
	#To support the highlighting feature
	highlighting = False
	
	def __init__(self, *args):
		QTextEdit.__init__(self, *args)
		self.dictionary = enchant.DictWithPWL('en_us')
		self.highlighter = Highlighter(self.document())
		self.setFontPointSize(12)
		self.highlighter.setDict(self.dictionary)
			##Logging... for me :)
		self.log = logger()
		
	def mousePressEvent(self, event):
		#This will move the cursor to the appropriate position
		if event.button() == Qt.RightButton:
			event = QMouseEvent(QEvent.MouseButtonPress, event.pos(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)

## 		#Highlight an image if it is clicked
## 		cursor = self.textCursor()
## 		cursor.select(QTextCursor.WordUnderCursor)
## 		if str(cursor.selection().toHtml()).find("img") != False:
## 			self.setTextCursor(cursor)

		QTextEdit.mousePressEvent(self, event)
	
	def mouseReleaseEvent(self, event):
		#Highlight on click?
		if self.highlighting:
			self.highlightAction()
		else:
			QTextEdit.mousePressEvent(self, event)

	
	def contextMenuEvent(self, event):
		menu = self.createStandardContextMenu()
		#Select the word under the cursor
		cursor = self.textCursor()
		position = cursor.position()


		## print str(cursor.selection().toHtml())
		## #Check to see if an image is under the cursor
		## if str(cursor.selection().toHtml()).find("<img") != -1:
		## 	self.setTextCursor(cursor) #show the image highlighed
		## 	menu.addSeparator()
		## 	action = QAction("Align Left", menu)
		## 	self.connect(action, SIGNAL("triggered()"), self.alignImageLeft)
		## 	menu.addAction(action)
		## 	self.addAction(action)
		## 	action = QAction("Align Right", menu)
		## 	self.connect(action, SIGNAL("triggered()"), self.alignImageRight)
		## 	menu.addAction(action)

		#grammar check
		if self.highlighter.getDescriptionText(cursor.position(), self.toPlainText()):
			menu.addSeparator()
			for mistake in self.highlighter.getDescriptionText(cursor.position(), self.toPlainText()):
				print mistake
				action = QAction(mistake["description"], menu)
				self.connect(action, SIGNAL("triggered()"), lambda targ=mistake["new"], l=mistake["left"], r=mistake["right"]: self.replaceTextByPosition(targ, l, r))
				menu.addAction(action)

	
		cursor.select(QTextCursor.WordUnderCursor)
		#If there is a word highlighted fix the spelling
		if cursor.hasSelection():
			text = unicode(cursor.selectedText())
			#If that word isn't in the dictionary
			if not self.dictionary.check(text):
				menu.addSeparator()
				spellingMenuItem = menu.addAction("Spelling:")
				spellingMenuItem.setEnabled(False)
				for word in self.dictionary.suggest(text):
					action = QAction(word, menu)
					self.connect(action, SIGNAL("triggered()"), lambda targ=word, l=cursor.selectionStart(), r=cursor.selectionEnd(): self.replaceTextByPosition(targ, l, r))
					menu.addAction(action)
				if len(self.dictionary.suggest(text)) == 0:
					noneMenuItem = menu.addAction("None")
					noneMenuItem.setEnabled(False)
				addToDictionary = QAction("Add to dictionary", menu)
				self.connect(addToDictionary, SIGNAL("triggered()"), lambda targ=text: self.addToDictionary(targ))
				menu.addAction(addToDictionary)
		
		menu.exec_(event.globalPos())
		
	def replaceTextByPosition(self, word, begin, end):
		#Replace from begin to end with word
		cursor = self.textCursor()
		cursor.setPosition(begin)
		cursor.setPosition(end, QTextCursor.KeepAnchor)
		cursor.beginEditBlock()
		cursor.removeSelectedText()
		cursor.insertText(word)
		cursor.endEditBlock()

	def addToDictionary(self, word):
		self.dictionary.add(word)
		
	def correctWordFromListItem(self, wordItem):
		word = wordItem.text()
		self.replaceSelectedWord(word)

	def replaceSelectedWord(self, word):
		#Replace the selected word with another word
		cursor = self.textCursor()
		cursor.select(QTextCursor.WordUnderCursor)
		oldword = cursor.selectedText()
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
		#Log it
		self.log.log(oldword + " -> " + str(word))
		
	def keyPressEvent(self, event):
		#Auto-repeats shouldn't be needed
		if event.isAutoRepeat():
			return

		#Tabs should scroll through the words
		if event.key() == Qt.Key_Tab or event.key() == Qt.Key_Down:
			self.emit(SIGNAL("tabEvent"))
			return
		if (event.key() == Qt.Key_Tab | Qt.Key_Shift) or event.key() == Qt.Key_Up:
			self.emit(SIGNAL("tabBackEvent"))
			return
		#Don't do all this if someone just clicked something in the word list
		if event.key() == 0:
			return

		cursor = self.textCursor()
		cursor.select(QTextCursor.WordUnderCursor)
		if cursor.hasSelection():
			text = unicode(cursor.selectedText() + event.text())
		else:
			text = unicode(event.text())
		self.emit(SIGNAL("wordEdited"), text)
		self.emit(SIGNAL("keyPressed"))
		#else:
			#self.emit(SIGNAL("whiteSpacePressed"))
		#Autocompletions
		QTextEdit.keyPressEvent(self, event)

	def boldSelectedText(self):
		if self.fontWeight() == QFont.Bold:
			newweight = QFont.Normal
		else:
			newweight = QFont.Bold
		self.setFontWeight(newweight)
		self.setFocus()
		
	def italicSelectedText(self):
		self.setFontItalic(not self.fontItalic())
		self.setFocus()

	def underlineSelectedText(self):
		self.setFontUnderline(not self.fontUnderline())
		self.setFocus()

	def alignLeft(self):
		self.setAlignment(Qt.AlignLeft)
		
	def alignCenter(self):
		self.setAlignment(Qt.AlignCenter)

	def alignRight(self):
		self.setAlignment(Qt.AlignRight)

	def doubleSpace(self):
		#self.document().setDefaultStyleSheet("line-height: 2em;")
		pass

	def singleSpace(self):
		pass

	#Don't allow multiple fonts in one document
	def setFont(self, font):
		cursor = self.textCursor()
		cursor.setPosition(0)
		cursor.setPosition(len(self.toPlainText()), cursor.KeepAnchor)
		fontFormat = QTextCharFormat()
		fontFormat.setFont(font)
		cursor.setCharFormat(fontFormat)

	def toggleHighlight(self, isSet):
		self.highlighting = isSet
		if isSet:
			self.setReadOnly(True)
		else:
			self.setReadOnly(False)

	def highlightAction(self):
		cursor = self.textCursor()
		if cursor.charFormat().background().color() == QColor.fromRgb(255, 255, 0):
			format_highlight = QTextCharFormat()
			format_highlight.setBackground(Qt.transparent)
			#cursor.mergeCharFormat(format_highlight)
			#Wow this is ugly.  Why isn't there some "select by text format" method?  It recurses backwards to find if the characters are highlighted, and then forwards.  Eeeww...
			pos = cursor.position()
			i = 0
			while cursor.charFormat().background().color() == QColor.fromRgb(255, 255, 0) and pos + i > 0:
				i -= 1
				cursor.setPosition(pos + i)
			start = i + pos
			i = 0
			cursor.setPosition(pos)
			while cursor.charFormat().background().color() == QColor.fromRgb(255, 255, 0) and pos + i < len(self.toPlainText()):
				i += 1
				cursor.setPosition(pos + i)
				if i + pos == len(self.toPlainText()):
					break
			end = i + pos
			cursor.setPosition(start)
			cursor.setPosition(end, QTextCursor.KeepAnchor)
			cursor.mergeCharFormat(format_highlight)
		else:
			if not cursor.hasSelection():
				cursor.select(QTextCursor.WordUnderCursor)
			else:
				#Don't visually represent highlighted text on the screen
				cursorToApply = self.textCursor()
				#cursorToApply.movePosition(QTextCursor.NextCharacter)
				cursorToApply.clearSelection()
				self.setTextCursor(cursorToApply)
				
			format_highlight = QTextCharFormat()
			format_highlight.setBackground(QColor.fromRgb(255, 255, 0))
			cursor.mergeCharFormat(format_highlight)

	def insertImage(self):
		imageurl = QFileDialog.getOpenFileName(self, "Insert image", platformSettings.getPlatformSetting('defaultOpenDirectory'), "Image file (*.jpg *.jpeg *.gif *.png)")
		self.insertImageByUrl(imageurl)

	def insertImageByUrl(self, url):
		#cursor = self.textCursor()
		self.insertHtml('&nbsp;<img src="{0}" style="float:right" />&nbsp;'.format(url))
		
	def alignImageRight(self):
		cursor = self.textCursor()
		cursor.select(QTextCursor.WordUnderCursor)
		selection = str(cursor.selection().toHtml())
		selection = selection.replace("float: left", "float: right")
		selection = selection.replace("float: none", "float: right")
		cursor.removeSelectedText()
		cursor.insertHtml(selection)
		self.setHtml(self.toHtml()) #framework bugs are not cute
		
	def alignImageLeft(self):
		cursor = self.textCursor()
		cursor.select(QTextCursor.WordUnderCursor)
		selection = cursor.selection().toHtml()
		print "'", selection, "'"
		selection = selection.replace("float: right", "float: left")
		selection = selection.replace("float: none", "float: left")
		cursor.removeSelectedText()
		cursor.insertHtml(selection)
		self.setHtml(self.toHtml()) #see above for bad pun

class Highlighter(QSyntaxHighlighter):

	WORDS = re.compile(u'((?iu)[\w\']+)([\s\n .?!])')

	corrections = [
		{
			"description": "Sentence starts without a capital letter",
			"re": re.compile(u'([.?!])([\s]*)([a-z])'),
			"fix": lambda m: m.group(1) + m.group(2) + m.group(3).capitalize() },
		{
			"description": "Sentence starts without a capital letter",
			"re": re.compile(u'^[a-z]'),
			"fix": lambda m: m.group(0).capitalize() },
		{
			"description": "No space after punctuation",
			"re": re.compile(u'([.?!,])([A-Za-z])'),
			"fix": u'\\1 \\2' },
		{
			"description": "Too many spaces", 
			"re": re.compile(u'([^[.?!])[ ]{2,}([A-Za-z])'), #This accounts for the fact that mny people (myself included) use two spaces after punctuation.
			"fix": u'\\1 \\2' },
		{
			"description": "Spaces before punctuation",
			"re": re.compile(u'[ ]+([.?!])'),
			"fix": u'\\1' },
		{
			"description": "Use 'an' instead of 'a'",
			"re": re.compile(u' ([Aa]) ([AEIOUaeiou])'),
			"fix": ' \\1n \\2' },
		{
			"description": "Use 'an' instead of 'a'",
			"re": re.compile(u'^([Aa]) ([AEIOUaeiou])'),
			"fix": '\\1n \\2' },
		{
			"description": "Use 'a' instead of 'an'",
			"re": re.compile(u' ([Aa])n ([BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])'),
			"fix": ' \\1 \\2' },
		{
			"description": "Use 'a' instead of 'an'",
			"re": re.compile(u'^([Aa])n ([BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])'),
			"fix": '\\1 \\2' },
		{
			"description": "Word repeated",
			"re": re.compile(u'([a-z]+) \\1', re.IGNORECASE),
			"fix": '\\1' }]
	
	
	def __init__(self, *args):
		QSyntaxHighlighter.__init__(self, *args)
	
		self.format_spelling = QTextCharFormat()
		self.format_spelling.setUnderlineColor(Qt.red)
		self.format_spelling.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)

		self.format_grammar = QTextCharFormat()
		self.format_grammar.setUnderlineColor(Qt.blue)
		self.format_grammar.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
		self.dict = None
	
	def setDict(self, dict):
		self.dict = dict
	
	def highlightBlock(self, text):
		if not self.dict:
			return
	
		text = unicode(text)

		#Spellcheck
		for word_object in re.finditer(self.WORDS, text):
			#word_object = re.search(self.WORDS, word_object_extra.group())
			
			if not self.dict.check(word_object.group(1)):
				self.setFormat(word_object.start(), (word_object.end() - len(word_object.group(2))) - word_object.start(), self.format_spelling)

		if not platformSettings.getSetting("grammarcheck", True):
			return
		#Grammar
		for rule in self.corrections:
			for word_object in re.finditer(rule["re"], text):
					self.setFormat(word_object.start(), word_object.end() - word_object.start(), self.format_grammar)
			
		## for word_object in re.finditer(self.SENTENCE_ENDS, text):
		## 		self.setFormat(word_object.start(), word_object.end() - word_object.start(), self.format_grammar)
		## for word_object in re.finditer(self.SENTENCE_STARTS, text):
		## 		self.setFormat(word_object.start(), word_object.end() - word_object.start(), self.format_grammar)
		## for word_object in re.finditer(self.SPACE_AFTER_PUNCTUATION, text):
		## 		self.setFormat(word_object.start(), word_object.end() - word_object.start(), self.format_grammar)
		## for word_object in re.finditer(self.MULTIPLE_SPACES_PUNCTUATION, text):
		## 		self.setFormat(word_object.start(), word_object.end() - word_object.start(), self.format_grammar)
		## for word_object in re.finditer(self.MULTIPLE_SPACES, text):
		## 		self.setFormat(word_object.start(), word_object.end() - word_object.start(), self.format_grammar)
		## for word_object in re.finditer(self.SPACE_BEFORE_PUNCTUATION, text):
		## 		self.setFormat(word_object.start(), word_object.end() - word_object.start(), self.format_grammar)

	def getDescriptionText(self, pos, text):
		text = unicode(text)
		results = []
		for rule in self.corrections:
			for word_object in re.finditer(rule["re"], text):
				if int(word_object.start()) <= pos and pos <= int(word_object.end()):
					results.append({
						"description": rule["description"],
						"left": word_object.start(),
						"right": word_object.end(),
						"text": word_object.group(0),
						"new": re.sub(rule["re"], rule["fix"], word_object.group(0)) })
		return results
					
class logger:
	logText = ""
	def log(self, text):
		self.logText += text
		self.logText += "<br />\n"
	def send(self):
		if not self.logText:
			return
		if platformSettings.getSetting("sendusagestatistics", True) == True:
			data = urllib.urlencode({"log": self.logText, "id": platformSettings.getPlatformSetting("statsId")})
			request = urllib2.Request(platformSettings.getPlatformSetting('statsUrl'), data)
			urllib2.urlopen(request)
		
	
