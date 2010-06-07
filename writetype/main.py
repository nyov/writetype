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


import sys
from PyQt4 import QtCore, QtGui, Qt
import resources_rc
from mainwindow import Ui_MainWindow
import enchant
import enchant.checker
from enchant.tokenize import get_tokenizer
from wordsList import wordsList
import threading
import platformSettings
from settingsDialog import Ui_settingsDialog
from distractionFree import Ui_distractionFree
import re
from os import path, sep
from speaker import Speaker
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import QTranslator, QLocale
from xml.dom import minidom
from statistics import Ui_statisticsDialog

class MainApplication(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle(self.tr("WriteType - ") + self.tr("Untitled Document"))
		QtCore.QObject.connect(self.ui.actionOpen, QtCore.SIGNAL("triggered()"), self.openDialog)
		QtCore.QObject.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.saveFile)
		QtCore.QObject.connect(self.ui.actionSave_As, QtCore.SIGNAL("triggered()"), self.saveFileAs)
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("wordEdited"), self.populateWordList)
		QtCore.QObject.connect(self.ui.spellingSuggestionsList, QtCore.SIGNAL("itemPressed(QListWidgetItem*)"), self.correctWordFromListItem)
		#QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("cursorPositionChanged()"), self.resetWlPointer)

		#Statistics
		self.statisticsDialog = StatisticsWindow(self)
		QtCore.QObject.connect(self.ui.actionStatistics, QtCore.SIGNAL("triggered()"), self.showStatisticsDialog)

		#Set up the TTS
		self.speaker = Speaker("festival")
		QtCore.QObject.connect(self.ui.actionSpeak, QtCore.SIGNAL("triggered()"), self.readAloud)
		QtCore.QObject.connect(self.ui.actionStop, QtCore.SIGNAL("triggered()"), self.speaker.stop)

		#Bold and garbage
		QtCore.QObject.connect(self.ui.actionBold, QtCore.SIGNAL("triggered()"), self.ui.textArea.boldSelectedText)
		QtCore.QObject.connect(self.ui.actionItalic, QtCore.SIGNAL("triggered()"), self.ui.textArea.italicSelectedText)
		QtCore.QObject.connect(self.ui.actionUnderline, QtCore.SIGNAL("triggered()"), self.ui.textArea.underlineSelectedText)
		QtCore.QObject.connect(self.ui.actionHighlightMode, QtCore.SIGNAL("toggled(bool)"), self.ui.textArea.toggleHighlight)
		QtCore.QObject.connect(self.ui.actionHighlight, QtCore.SIGNAL("triggered()"), self.ui.textArea.highlightAction)
		#Alignment
		QtCore.QObject.connect(self.ui.actionAlignLeft, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignLeft)
		QtCore.QObject.connect(self.ui.actionAlignCenter, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignCenter)
		QtCore.QObject.connect(self.ui.actionAlignRight, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignRight)
		#Spacing
		QtCore.QObject.connect(self.ui.actionDoubleSpace, QtCore.SIGNAL("triggered()"), self.ui.textArea.doubleSpace)
		QtCore.QObject.connect(self.ui.actionSingleSpace, QtCore.SIGNAL("triggered()"), self.ui.textArea.singleSpace)
		
		#Font point size
		QtCore.QObject.connect(self.ui.spinBoxFontSize, QtCore.SIGNAL("valueChanged(int)"), self.ui.textArea.setFontSize)
		#QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("cursorPositionChanged()"), self.updateFontSizeSpinBoxValue)
		#Font
		QtCore.QObject.connect(self.ui.fontComboBox, QtCore.SIGNAL("currentFontChanged(const QFont&)"), self.ui.textArea.setFont)
		#QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("cursorPositionChanged()"), self.updateFontComboBoxValue)
		QtCore.QObject.connect(self.ui.fontComboBox, QtCore.SIGNAL("currentFontChanged(const QFont&)"), self.ui.textArea.setFont)
		#Clear the word list if a space is pressed
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("whiteSpacePressed"), self.ui.spellingSuggestionsList.clear)

		#about boxes
		QtCore.QObject.connect(self.ui.actionAboutQt, QtCore.SIGNAL("triggered()"), lambda : QtGui.QMessageBox.aboutQt(self))
		QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.showAbout)
		QtCore.QObject.connect(self.ui.actionDocumentation, QtCore.SIGNAL("triggered()"), self.openHelpPage)

		#Word list for autocompletion
		self.wl = wordsList()
		self.tokenizer = get_tokenizer(platformSettings.getPlatformSetting('language'))
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("tabEvent"), self.tabEvent)
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("tabBackEvent"), self.tabBackEvent)
		self.wlPointer = None

		#Connections for autocorrect
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("wordEdited"), self.checkForAutoreplacement)
		#Keyboard shortcuts
		#self.shortcut = Qt.QShortcut(Qt.Qt.Key_Tab, self.ui.textArea, self.tabEvent)
		
		#printer
		QtCore.QObject.connect(self.ui.actionPrint, QtCore.SIGNAL("triggered()"), self.openPrintDialog)
		self.filename = ""
		self.filetitle = self.tr("Untitled Document")
		
		#modified
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("keyPressed"), self.updateTitle)

		#create the settings dialog box
		self.settings_box = SettingsDialogBox(self)
		self.distractionFree_box = DistractionFreeWindow(self)
		
		#Set up the settings box
		QtCore.QObject.connect(self.ui.actionSettings, QtCore.SIGNAL("triggered()"), self.settings_box.show)
		QtCore.QObject.connect(self.settings_box, QtCore.SIGNAL("dialogSaved"),	self.refreshAfterSettingsDialogClosed)

		#Distraction free
		QtCore.QObject.connect(self.ui.actionDistractionFree, QtCore.SIGNAL("triggered()"), self.openDistractionFreeMode)
		QtCore.QObject.connect(self.distractionFree_box, QtCore.SIGNAL("rejected()"), self.closeDistractionFreeMode)
		QtCore.QObject.connect(self.ui.distractionButton, QtCore.SIGNAL("clicked()"), self.closeDistractionFreeMode)
		self.ui.distractionButton.hide()

		#images
		QtCore.QObject.connect(self.ui.actionInsert_Image, QtCore.SIGNAL("triggered()"), self.ui.textArea.insertImage)
		QtCore.QObject.connect(self.ui.actionAlign_Image_Right, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignImageRight)
		QtCore.QObject.connect(self.ui.actionAlign_Image_Left, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignImageLeft)
		#Lets disable image support for now.  Yeah... I think that would be a wise idea.
		self.ui.imageToolBar.setVisible(False)
		self.ui.actionEnableImageToolbar.setVisible(False)
		
		#Apply some settings
		if platformSettings.getSetting("defaultfont", ""):
			self.ui.fontComboBox.setCurrentFont(QtGui.QFont(platformSettings.getSetting("defaultfont")))
		
		#Add some more widgets to the toolbar
		self.ui.editToolBar.addWidget(self.ui.sizeLabel)
		self.ui.editToolBar.addWidget(self.ui.spinBoxFontSize)
		self.ui.editToolBar.addWidget(self.ui.fontComboBox)

		self.wordsC = []
		self.wordsN = []

		#Check to see if there is unsaved work
		if platformSettings.getSetting("autosavepath", ""):
			response = QtGui.QMessageBox.question(self, self.tr("Crash recovery"), self.tr("WriteType found unsaved work from a crash.  Would you like to recover it?"), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
			if response == QtGui.QMessageBox.Yes:
				text = open(platformSettings.getSetting("autosavepath", "")).read()
				self.ui.textArea.setText(text)
				self.filetitle = self.tr("Recovered file")
				self.updateTitle()
				#Add the words in the document to the custom words list
				for token in self.tokenizer(str(self.ui.textArea.toPlainText())):
					self.wl.addCustomWord(token[0].lower())

	
	def openDialog(self):
		self.filename = QtGui.QFileDialog.getOpenFileName(self, self.tr("Open file"), platformSettings.getPlatformSetting('defaultOpenDirectory'), "Formatted Text (*.html *.htm);;Plain Text (*)")
		from os.path import isfile
		if isfile(self.filename):
			text = open(self.filename).read()
			self.ui.textArea.setText(text)
			self.filetitle = str(self.filename).split(sep).pop()
			self.updateTitle(False)
			
			#Add the words in the document to the custom words list
			for token in self.tokenizer(str(self.ui.textArea.toPlainText())):
				self.wl.addCustomWord(token[0].lower())

	def saveFile(self):
		from os.path import isfile
		if isfile(self.filename):
			file = open(self.filename, 'w')
			file.write(self.ui.textArea.toHtml())
			self.filetitle = str(self.filename).split(sep).pop()
			self.updateTitle(False)
			file.close()
			return True
		else:
			return self.saveFileAs()

	def saveFileAs(self):
		self.filename = QtGui.QFileDialog.getSaveFileName(self, self.tr("Save file"), platformSettings.getPlatformSetting('defaultOpenDirectory'), "Formatted Text (*.html)")
		if not str(self.filename).find('.html'):
			self.filename += '.html'
			self.updateTitle(False)
		file = open(self.filename, 'w+')
		file.write(self.ui.textArea.toHtml())
		file.close()
		self.filetitle = str(self.filename).split(sep).pop()
		self.updateTitle(False)
		file.close()
		return True
	
	def autoSave(self):
		#This function should be called whenever an autosave is desired
		path = platformSettings.getSetting("autosavepath", "")
		if not path:
			from tempfile import mkstemp
			path = mkstemp()[1]
			platformSettings.setSetting("autosavepath", path)
		handle = open(path, 'w')
		handle.write(self.ui.textArea.toHtml())
		handle.close()

	def readAloud(self):
		if self.ui.textArea.textCursor().selectedText():
			text = self.ui.textArea.textCursor().selectedText()
		else:
			text = self.ui.textArea.toPlainText()
		#Disable the buttons if there was a failure
		if self.speaker.say(text) == True:
			self.ui.actionSpeak.setDisabled(True)
			self.ui.actionStop.setDisabled(True)
			QMessageBox.warning(None, self.tr("Feature unavailable"), self.tr("The current TTS driver is invalid.  Read-back is unavailable for this session."))
		
	def refreshAfterSettingsDialogClosed(self):
		self.ui.actionSpeak.setDisabled(False)
		self.ui.actionStop.setDisabled(False)

		self.wl.refreshWordsCustom()
		self.wl.refreshWords()
		self.wl.refreshReplacementTable()
		self.speaker.setDriver()

	def spellcheck(self):
		dictionary = enchant.Dict(platformSettings.getPlatformSetting('language'))
		tokenizer = get_tokenizer(platformSettings.getPlatformSetting('language'))
		for word in tokenizer(self.ui.textArea.toPlainText()):
			if dictionary.check(word) == False:
				pass

	def checkForAutoreplacement(self, word):
		#print "To autoreplace: '", word, "'"
		if word[-1:] in ["", "\b", " ", "\t", ".", "?", ":", "!", ",", ";", ")"]:
			if self.wl.correctWord(word[:-1]) != False:
				print "Correcting", word[:-1]
				self.ui.textArea.replaceSelectedWord(self.wl.correctWord(word[:-1]))
			self.wlPointer = None
			self.ui.spellingSuggestionsList.setCurrentRow(-1)
			self.ui.spellingSuggestionsList.clear()
		if word[-1:] in [".", "!", "?"]:
			print "Autosaving"
			self.autoSave()

	def populateWordList(self, text):
		text = str(text)

		#This way, the word list won't keep changing if the user tabs to select a new word
		if self.wlPointer != None:
			return
		
		#If the user typed a word + delimiter, add it to the custom word list and don't display any more suggestions after the delimiter
		if text[-1:] in (" ", ".", ",", "!", "?", "\t"):
			print "adding custom word"
			self.wl.addCustomWord(text.lower()[0:len(text)-1])
			return
		
		#Don't bother continuing if there are no words remaining
		#if len(self.wordsC) == 0 and len(self.wordsN) == 0 and len(text) > platformSettings.getSetting("minimumletters", 0) + 1:
			#return
		#YES bother because it could have been a typo
		
		self.ui.spellingSuggestionsList.clear()
		
		if len(text) <= platformSettings.getSetting("minimumletters", 0):
			return

		if not text:
			return

		#Create the font for the list
   	   	font = QtGui.QFont()
   		font.setPointSize(12)
			
		#Search the custom words
		## self.wordsC = self.wl.search(text, False) # I CHANGED THIS!
		## for word in self.wordsC:
		## 	item = QtGui.QListWidgetItem(word[0] + str(word[1]), self.ui.spellingSuggestionsList)
		## 	item.setFont(font)
			
		#Search the normal words
		self.wordsN = self.wl.search(str(text), False)
		for word in self.wordsN:
			item = QtGui.QListWidgetItem(word[0], self.ui.spellingSuggestionsList)
			item.setFont(font)

			## item.setForeground(QtGui.QColor.fromRgb(50-num, 50-num, 50-num))
			
			#action = QtGui.QAction(self)
			#action.setObjectName("action"+word)
			#action.setText(word)
			#self.ui.menuFile.addAction(action)
			#if len(word) > 4:
				#if self.widgets[i]:
					#self.ui.hboxlayout.removeWidget(self.widgets[i])
					#del self.widgets[i]
				#self.widgets[i]
				#self.widgets[i] = QtGui.QPushButton(self)
				#self.widgets[i].setText(word)
				#self.widgets[i].setObjectName("button"+word)
				#self.connect(self.widgets[i], QtCore.SIGNAL("pressed()"), lambda warg=word: self.ui.textArea.correctWordButton(warg))
				#self.ui.hboxlayout.addWidget(self.widgets[i])
				#self.widgets.append(self.widgets[i])
				#if i >= 3:
					#break
				#else:
					#i += 1
		if platformSettings.getSetting("guessmisspellings", True) and len(self.wordsC) + len(self.wordsN) <= platformSettings.getSetting("threshold", 0):
			#This is where things get trickier.  It MUST be a mispeling.  Fun fun fun!
			possibilities = []
			## ##Replace double letters with a single letter and look
			## #for cluster in re.findall(u'[a-z]\1', text):
			## 	#possibilities += self.wl.search(text.replace(cluster, cluster[0]))
			## #Replace "l" with "ll" and "s" with "ss", etc.
			## possibilities += self.wl.search(text.replace("l", "ll"), False, True)
			## possibilities += self.wl.search(text.replace("s", "ss"), False, True)
			## possibilities += self.wl.search(text.replace("t", "tt"), False, True)
			## possibilities += self.wl.search(text.replace("d", "dd"), False, True)
			## #Some more confusions
			## possibilities += self.wl.search(text.replace("t", "d"), False, True)
			## possibilities += self.wl.search(text.replace("d", "tt"), False, True)
			## possibilities += self.wl.search(text.replace("k", "ck"), False, True)
			## possibilities += self.wl.search(text.replace("k", "c"), False, True)
			## possibilities += self.wl.search(text.replace("s", "c"), False, True)
			## possibilities += self.wl.search(text.replace("l", "le"), False, True)

			## #Vowel confusions
			## possibilities += self.wl.search(text.replace("i", "ee"), False, True)
			## possibilities += self.wl.search(text.replace("ea", "ee"), False, True)
			## possibilities += self.wl.search(text.replace("ee", "i"), False, True)
			## possibilities += self.wl.search(text.replace("e", "i"), False, True)
			## possibilities += self.wl.search(text.replace("e", "ie"), False, True)
			## possibilities += self.wl.search(text.replace("a", "e"), False, True)
			## possibilities += self.wl.search(text.replace("u", "o"), False, True)

			## #Based on data analysis
			## possibilities += self.wl.search(text.replace("o", "a"), False, True) # becouse 
			## possibilities += self.wl.search(text.replace("a", "o"), False, True) # peaple 
			## possibilities += self.wl.search(text.replace("xs", "x"), False, True) # exsperience, exsplosion
			## possibilities += self.wl.search(text.replace("ei", "i"), False, True) # writeing, exciteing

			

			## if platformSettings.getSetting("advancedsubstitutions", False):
			## 	possibilities += self.wl.search(text.replace("u", "oo"), False, True)
			## 	possibilities += self.wl.search(text.replace("u", "ou"), False, True)
			## 	possibilities += self.wl.search(text.replace("e", "a"), False, True)
				

			## #possibilities = self.wl.quicksort(possibilities)
			## #Remove duplicates
			## #if wordsN:
			## 	#for i in range(len(possibilities)):
			## 		#if possibilities[0] in wordsN:
			## 			#del possibilities[0]

			## for word in filter(lambda x : x not in self.wordsN, possibilities):
			## 	item = QtGui.QListWidgetItem(word, self.ui.spellingSuggestionsList)
			## 	item.setForeground(QtGui.QColor.fromRgb(80, 80, 80))
			## 	item.setFont(font)
			
	def updateFontSizeSpinBoxValue(self):
		if not self.ui.textArea.textCursor().selectedText():
			self.ui.spinBoxFontSize.setValue(int(self.ui.textArea.fontPointSize()))
		if self.ui.spinBoxFontSize.value() == 0:
			self.ui.spinBoxFontSize.setValue(12)

	def updateFontComboBoxValue(self):
		if not self.ui.textArea.textCursor().selectedText():
			self.ui.fontComboBox.setCurrentFont(self.ui.textArea.currentFont())
		self.ui.textArea.setFocus()
		
	def showAbout(self):
		QtGui.QMessageBox.about(self, self.tr("About this program"), self.tr("""<h1>WriteType</h1><h2>Copyright 2010 Max Shinn</h2><a href="mailto:admin@bernsteinforpresident.com">admin@BernsteinForPresident.com</a> <br /><a href="http://bernsteinforpresident.com">http://BernsteinForPresident.com</a> <br />This software is made available under the GNU General Public License v3 or later. For more information about your rights, see: <a href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>"""))
		
	def openHelpPage(self):
		QtGui.QDesktopServices.openUrl(QtCore.QUrl("http://Bernsteinforpresident.com/software/writetype/documentation"))
		
	def openPrintDialog(self):
		printer = QtGui.QPrinter()
		printer.setDocName("writetype_" + self.filename)
		printDialog = QtGui.QPrintDialog(printer)
		printDialog.setModal(True)
		printDialog.setWindowTitle(self.tr("WriteType - ") + self.tr("Print"))
		if printDialog.exec_():
			currentGrammarColor = self.ui.textArea.highlighter.format_grammar.underlineColor()
			self.ui.textArea.highlighter.format_grammar.setUnderlineColor(Qt.Qt.transparent)
			currentSpellingColor = self.ui.textArea.highlighter.format_spelling.underlineColor()
			self.ui.textArea.highlighter.format_spelling.setUnderlineColor(Qt.Qt.transparent)
			self.ui.textArea.highlighter.rehighlight()

			self.ui.textArea.document().print_(printer)
			self.ui.textArea.highlighter.format_grammar.setUnderlineColor(currentGrammarColor)
			self.ui.textArea.highlighter.format_grammar.setUnderlineColor(currentSpellingColor)
			self.ui.textArea.highlighter.rehighlight()			

	def openDistractionFreeMode(self):
		self.distractionFree_box.ui.verticalLayout_2.addWidget(self.ui.centralwidget)
		self.distractionFree_box.show()
		self.ui.distractionButton.show()
		self.distractionFree_box.showFullScreen()
#		self.ui.splitter.setParent(None)
#		self.ui.splitter.showFullScreen()

	def closeDistractionFreeMode(self):
		self.distractionFree_box.hide()
		self.ui.centralwidget.setParent(self)
		self.setCentralWidget(self.ui.centralwidget)
		self.ui.distractionButton.hide()
			
	def disableSpeakButton(self):
		self.ui.actionSpeak.disable()

	def updateTitle(self, modified=True):
		titlestring = self.tr("WriteType - ") + self.filetitle
		if modified:
			titlestring += " *"
			self.ui.actionSave.setDisabled(False)
		else:
			self.ui.actionSave.setDisabled(True)
		self.setWindowTitle(titlestring)


	def tabEvent(self):
		if not self.wordsN:
			return
		if self.wlPointer == None:
			self.wlPointer = 0
		elif self.wlPointer >= len(self.wordsN)-1:
			self.wlPointer = 0
		else:
			self.wlPointer += 1
       		self.ui.textArea.replaceSelectedWord(self.wordsN[self.wlPointer][0])
		self.ui.spellingSuggestionsList.setCurrentRow(self.wlPointer)

	def tabBackEvent(self):
		if not self.wordsN:
			return
		if self.wlPointer == None: 
			self.wlPointer = 0
		elif self.wlPointer == 0:
			self.wlPointer = len(self.wordsN)-1
		else:
			self.wlPointer -= 1
		self.ui.textArea.replaceSelectedWord(self.wordsN[self.wlPointer][0])
		self.ui.spellingSuggestionsList.setCurrentRow(self.wlPointer)

	def correctWordFromListItem(self, wordItem):
		word = wordItem.text()
		self.wlPointer = self.ui.spellingSuggestionsList.row(wordItem)
		self.ui.textArea.replaceSelectedWord(word)

	def showStatisticsDialog(self):
		#Update the statistics
		self.statisticsDialog.ui.filenameLabel.setText(self.filename)
		#Only alpha-numerics
		chars = 0
		for char in str(self.ui.textArea.toPlainText()):
			if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
				chars += 1
		self.statisticsDialog.ui.charactersLabel.setText(str(chars))
		#Stupid tokenizer, doesn't work with len()
		words = 0
		for x in self.tokenizer(str(self.ui.textArea.toPlainText())):
			words += 1
		self.statisticsDialog.ui.wordsLabel.setText(str(words))
		sentences = len(re.findall('[A-Z][^A-Z]*[.!?]', self.ui.textArea.toPlainText()))
		self.statisticsDialog.ui.sentencesLabel.setText(str(sentences))
		paragraphs = self.ui.textArea.document().blockCount()
		self.statisticsDialog.ui.paragraphsLabel.setText(str(paragraphs))
		#Automated Readability Index - this is the easiest to implement :)
		try:
			readability = 4.71*(float(chars)/words) + .5*(float(words)/sentences) - 21.43
			self.statisticsDialog.ui.readabilityLabel.setText(str(round(readability, 3)))
		except ZeroDivisionError:
			self.statisticsDialog.ui.readabilityLabel.setText("Invalid, no sentences found.")

		self.statisticsDialog.show()

		
		

	def closeEvent(self, event):
		#Set the stuff up to ask for a save on exit
		if self.ui.actionSave.isEnabled():
			response =  QtGui.QMessageBox.question(self, self.tr("Quit?"), self.tr("You have unsaved work.  Do you want to save?"), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No, QtGui.QMessageBox.Cancel)
			if response == QtGui.QMessageBox.Yes:
				if not self.saveFile():
					event.ignore()
				return
			elif response == QtGui.QMessageBox.No:
				pass
			elif response == QtGui.QMessageBox.Cancel:
				event.ignore()
				return
		#Send the log
		self.ui.textArea.log.send()
		#Purge the autosaves
		path = platformSettings.getSetting("autosavepath", "")
		if path:
			from os import unlink
			platformSettings.setSetting("autosavepath", "")
			unlink(path)
		QtGui.QMainWindow.closeEvent(self, event)

class SettingsDialogBox(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_settingsDialog()
		self.ui.setupUi(self)
		
		#Load words into textarea
		self.ui.customWordsTextEdit.setPlainText(platformSettings.getSetting("customwords", ""))
		QtCore.QObject.connect(self.ui.okayButton, QtCore.SIGNAL("clicked()"), self.okayClicked)
		QtCore.QObject.connect(self.ui.applyButton, QtCore.SIGNAL("clicked()"), self.applyClicked)

		
		#NOTE TO SELF: Maybe I can load the word lists from an XML file one day if I have nothing better to do
		self.wordListButtonGroup = QtGui.QButtonGroup()
		filepath = path.join(platformSettings.getPlatformSetting("pathToWordlists"), "wordlists.xml")
		dom = minidom.parse(filepath)
		#Don't forget to sort these by sortweight!
		for node in dom.getElementsByTagName("wordlist"):
			button = QtGui.QRadioButton(node.getAttribute("name"), self.ui.tab)
			self.ui.verticalLayout_4.addWidget(button)
			self.wordListButtonGroup.addButton(button, int(node.getAttribute("id")))
		
		#Load the radio button settings
## 		self.wordListButtonGroup = QtGui.QButtonGroup()
## 		self.wordListButtonGroup.addButton(self.ui.wordListSize1, 1)
## 		self.wordListButtonGroup.addButton(self.ui.wordListSize2, 2)
## 		self.wordListButtonGroup.addButton(self.ui.wordListSize3, 3)
## 		self.wordListButtonGroup.addButton(self.ui.wordListSize4, 4)
## 		self.wordListButtonGroup.addButton(self.ui.wordListSize5, 5)
		self.wordListButtonGroup.setExclusive(True)
		#Now actually select the correct button
		self.wordListButtonGroup.buttons()[int(platformSettings.getSetting("wordlist", 2))-1].setChecked(True)
		
		#Load the word completion settings
		self.ui.guessMisspellingsCheckbox.setChecked(platformSettings.getSetting("guessmisspellings", True))
		self.ui.thresholdSpinbox.setValue(platformSettings.getSetting("threshold", 3))
		self.ui.advancedSubstitutionsCheckbox.setChecked(platformSettings.getSetting("advancedsubstitutions", True))
		self.ui.minimumLetters.setValue(platformSettings.getSetting("minimumletters", 0))

		#Autocompletion
		self.ui.autocompletionCheckBox.setChecked(platformSettings.getSetting("autocompletion", True))
		self.ui.contractionsCheckbox.setChecked(platformSettings.getSetting("autocompletioncontractions", True))
		self.ui.autocompletionsTable.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem(self.tr("Replace:")))
		self.ui.autocompletionsTable.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem(self.tr("With:")))

		#Other
		self.ui.grammarCheckbox.setChecked(platformSettings.getSetting("grammarcheck", True))
		
		i = 0
		for line in platformSettings.getSetting("customAutocompletions", "").split("\n"):
			if not line: break
			self.ui.autocompletionsTable.insertRow(i+1)
			item1 = QtGui.QTableWidgetItem(line.split(',')[0])
			item2 = QtGui.QTableWidgetItem(line.split(',')[1])
			self.ui.autocompletionsTable.setItem(i, 0, item1)
			self.ui.autocompletionsTable.setItem(i, 1, item2)
			i += 1
		def autoAddRows(row, col):
			if row + 1 == self.ui.autocompletionsTable.rowCount():
				self.ui.autocompletionsTable.insertRow(row + 1)
		QtCore.QObject.connect(self.ui.autocompletionsTable, QtCore.SIGNAL("cellDoubleClicked(int,int)"), autoAddRows)

		#Usage statistics
		self.ui.usageStatisticsCheckbox.setChecked(platformSettings.getSetting("sendusagestatistics", True))
		
		#Set the correct default font
		if platformSettings.getSetting("defaultfont", ""):
			self.ui.defaultFont.setCurrentFont(QtGui.QFont(platformSettings.getSetting("defaultfont")))
		else:
			self.ui.useDefaultFont.setChecked(True)
			self.ui.defaultFont.setDisabled(True)

		#TTS
		self.ui.speedSlider.setValue(platformSettings.getSetting("readingspeed", 0))
		engines = platformSettings.getPlatformSetting("ttsEngines").split(",")
		for engine in engines:
			self.ui.ttsEngineBox.addItem(engine)
		currentValue = platformSettings.getSetting("ttsengine", "")
		if currentValue in engines:
			index = engines.index(currentValue)
			self.ui.ttsEngineBox.setCurrentIndex(index)
		
		
	def applyClicked(self):
		platformSettings.setSetting("customwords", self.ui.customWordsTextEdit.toPlainText())
		platformSettings.setSetting("wordlist", self.wordListButtonGroup.checkedId())
		platformSettings.setSetting("guessmisspellings", self.ui.guessMisspellingsCheckbox.isChecked())
		platformSettings.setSetting("threshold", self.ui.thresholdSpinbox.value())
		platformSettings.setSetting("advancedsubstitutions", self.ui.advancedSubstitutionsCheckbox.isChecked())
		platformSettings.setSetting("sendusagestatistics", self.ui.usageStatisticsCheckbox.isChecked())
		platformSettings.setSetting("minimumletters", self.ui.minimumLetters.value())
		platformSettings.setSetting("autocompletion", self.ui.autocompletionCheckBox.isChecked())
		platformSettings.setSetting("autocompletioncontractions", self.ui.contractionsCheckbox.isChecked())
		platformSettings.setSetting("readingspeed", self.ui.speedSlider.value())
		platformSettings.setSetting("ttsengine", self.ui.ttsEngineBox.currentText())
		platformSettings.setSetting("grammarcheck", self.ui.grammarCheckbox.isChecked())

		if self.ui.useDefaultFont.isChecked():
			platformSettings.setSetting("defaultfont", "")
		else:
			platformSettings.setSetting("defaultfont", self.ui.defaultFont.currentFont())

		autocorrectionsList = ""
		for i in range(0, self.ui.autocompletionsTable.rowCount()):
			cell1 = self.ui.autocompletionsTable.item(i, 0)
			cell2 = self.ui.autocompletionsTable.item(i, 1)
			if cell1 and cell2:
				if cell1.text() and cell2.text():
					autocorrectionsList += cell1.text() + "," + cell2.text() + "\n"
		print autocorrectionsList
		platformSettings.setSetting("customAutocompletions", autocorrectionsList)
		
		
		self.emit(QtCore.SIGNAL("dialogSaved"))

	def okayClicked(self):
		self.applyClicked()
		self.close()


class DistractionFreeWindow(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_distractionFree()
		self.ui.setupUi(self)

class StatisticsWindow(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_statisticsDialog()
		self.ui.setupUi(self)

application = QtGui.QApplication(sys.argv)
#translation
trans = QTranslator()
trans.load("qt_" + QLocale.system().name())
application.installTranslator(trans)
app = MainApplication()
app.show()
application.exec_()
