import sys
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
import enchant
import enchant.checker
from enchant.tokenize import get_tokenizer
from wordsList import wordsList
import threading
from platformSettings import platformSettings
from settingsDialog import Ui_settingsDialog

class MainApplication(QtGui.QMainWindow):
	def __init__(self, parent=None):
		
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle("WriteType - Untitled Document")
		QtCore.QObject.connect(self.ui.actionOpen, QtCore.SIGNAL("triggered()"), self.openDialog)
		QtCore.QObject.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.saveFile)
		QtCore.QObject.connect(self.ui.actionSave_As, QtCore.SIGNAL("triggered()"), self.saveFileAs)
		QtCore.QObject.connect(self.ui.actionSpeak, QtCore.SIGNAL("triggered()"), self.readAloud)
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("wordEdited"), self.createButtons)
		QtCore.QObject.connect(self.ui.spellingSuggestionsList, QtCore.SIGNAL("itemPressed(QListWidgetItem*)"), self.ui.textArea.correctWordList)
		
		#Bold and garbage
		QtCore.QObject.connect(self.ui.actionBold, QtCore.SIGNAL("triggered()"), self.ui.textArea.boldSelectedText)
		QtCore.QObject.connect(self.ui.actionItalic, QtCore.SIGNAL("triggered()"), self.ui.textArea.italicSelectedText)
		QtCore.QObject.connect(self.ui.actionUnderline, QtCore.SIGNAL("triggered()"), self.ui.textArea.underlineSelectedText)
		#Font point size
		QtCore.QObject.connect(self.ui.spinBoxFontSize, QtCore.SIGNAL("valueChanged(int)"), self.ui.textArea.setFontPointSize)
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("cursorPositionChanged()"), self.updateFontSizeSpinBoxValue)
		#Font
		QtCore.QObject.connect(self.ui.fontComboBox, QtCore.SIGNAL("currentFontChanged(const QFont&)"), self.ui.textArea.setCurrentFont)
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("cursorPositionChanged()"), self.updateFontComboBoxValue)
		QtCore.QObject.connect(self.ui.fontComboBox, QtCore.SIGNAL("currentFontChanged(const QFont&)"), self.ui.textArea.setCurrentFont)



		#about boxes
		QtCore.QObject.connect(self.ui.actionAboutQt, QtCore.SIGNAL("triggered()"), self.showAboutQt)
		QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.showAbout)
		QtCore.QObject.connect(self.ui.actionDocumentation, QtCore.SIGNAL("triggered()"), self.openHelpPage)


		#Word list for autocompletion
		self.wl = wordsList()
		self.tokenizer = get_tokenizer("en_US")
		#printer
		self.printer = QtGui.QPrinter()
		QtCore.QObject.connect(self.ui.actionPrint, QtCore.SIGNAL("triggered()"), self.openPrintDialog)
		self.filename = ""
		self.filetitle = "Untitled Document"
		
		#modified
		QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("keyPressed"), self.updateTitle)


		#create the settings dialog box
		self.settings_box = settingsDialogBox(self)
		
		#Set up the settings box
		QtCore.QObject.connect(self.ui.actionSettings, QtCore.SIGNAL("triggered()"), self.settings_box.show)
		QtCore.QObject.connect(self.settings_box, QtCore.SIGNAL("dialogSaved"), self.wl.refreshWordsCustom)
		
		#Add some more widgets to the toolbar
		self.ui.editToolBar.addWidget(self.ui.sizeLabel)
		self.ui.editToolBar.addWidget(self.ui.spinBoxFontSize)
		self.ui.editToolBar.addWidget(self.ui.fontComboBox)


	
	def openDialog(self):
		self.filename = QtGui.QFileDialog.getOpenFileName(self, "Open file", platformSettings.defaultOpenDirectory, "Formatted Text (*.html *.htm);;Plain Text (*)")
		from os.path import isfile
		if isfile(self.filename):
			text = open(self.filename).read()
			self.ui.textArea.setText(text)
			self.filetitle = str(self.filename).split(platformSettings.ds).pop()
			self.updateTitle(False)
			
			#Add the words in the document to the custom words list
			for token in self.tokenizer(str(self.ui.textArea.toPlainText())):
				self.wl.addCustomWord(token[0].lower())
				print token[0].lower()

	def saveFile(self):
		from os.path import isfile
		if isfile(self.filename):
			file = open(self.filename, 'w')
			file.write(self.ui.textArea.toHtml())
			self.filetitle = str(self.filename).split(platformSettings.ds).pop()
			self.updateTitle(False)
			file.close()
	def saveFileAs(self):
		self.filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", platformSettings.defaultOpenDirectory, "Formatted Text (*.html)")
		if not str(self.filename).find('.html'):
			self.filename += '.html'
			self.updateTitle(False)
		file = open(self.filename, 'w+')
		file.write(self.ui.textArea.toHtml())
		file.close()
		self.filetitle = str(self.filename).split(platformSettings.ds).pop()
	def readAloud(self):
		if self.ui.textArea.textCursor().selectedText():
			text = self.ui.textArea.textCursor().selectedText()
		else:
			text = self.ui.textArea.toPlainText()
		speaker = speakerThread(text)
		speaker.start()
	def spellcheck(self):
		dictionary = enchant.Dict("en_US")
		tokenizer = get_tokenizer("en_US")
		for word in tokenizer(self.ui.textArea.toPlainText()):
			if dictionary.check(word) == False:
				pass
	def correctWordList(self, wordItem):
		word = wordItem.text()
		#Replace the selected word with another word the user selected
		cursor = self.ui.textArea.textCursor()
		cursor.select(QTextCursor.WordUnderCursor)
		cursor.removeSelectedText()
		cursor.insertText(word)
		cursor.endEditBlock()
		self.ui.textArea.setFocus()
	def createButtons(self, text):
		self.ui.spellingSuggestionsList.clear()
		#If the user typed a word + delimiter, add it to the custom word list and don't display any more suggestions after the delimiter
		if text[len(text)-1] in (" ", ".", ",", "!", "?"):
			self.wl.addCustomWord(text.lower()[0:len(text)-1])
			return
		
		#Search the custom words
		words = self.wl.search(text, True)
		print text
			#i = 0
		customWords = False
		for word in words:
			item = QtGui.QListWidgetItem(word, self.ui.spellingSuggestionsList)
			customWords = True
			#self.ui.spellingSuggestionsList.addItem(item)
			
			
		#Search the normal words
		words = self.wl.search(text, False)
		for word in words:
			
			#Gray them if there are any custom words
			item = QtGui.QListWidgetItem(word, self.ui.spellingSuggestionsList)
			if customWords:
				item.setForeground(QtGui.QBrush(QtCore.Qt.darkGray))
			
			
			
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
	def updateFontSizeSpinBoxValue(self):
		if not self.ui.textArea.textCursor().selectedText():
			self.ui.spinBoxFontSize.setValue(int(self.ui.textArea.fontPointSize()))
		if self.ui.spinBoxFontSize.value() == 0:
			self.ui.spinBoxFontSize.setValue(12)
	def updateFontComboBoxValue(self):
		if not self.ui.textArea.textCursor().selectedText():
			self.ui.fontComboBox.setCurrentFont(self.ui.textArea.currentFont())
		self.ui.textArea.setFocus()
	def showAboutQt(self):
		QtGui.QMessageBox.aboutQt(self)
	def showAbout(self):
		QtGui.QMessageBox.about(self, "About this program", """<h1>WriteType</h1><h2>Created by: Max Shinn </h2><a href="mailto:admin@bernsteinforpresident.com">admin@BernsteinForPresident.com</a> <br /><a href="http://bernsteinforpresident.com">http://BernsteinForPresident.com</a>""")
	def openHelpPage(self):
		QtGui.QDesktopServices.openUrl(QtCore.QUrl("http://Bernsteinforpresident.com"))
	def openPrintDialog(self):
		printer = QtGui.QPrinter()
		printer.setDocName("writetype_" + self.filename)
		printDialog = QtGui.QPrintDialog(printer)
		printDialog.setModal(True)
		printDialog.setWindowTitle("WriteType - Print")
		if printDialog.exec_():
			self.ui.textArea.document().print_(printer)
	def updateTitle(self, modified=True):
		print "here"
		titlestring = "WriteType - " + self.filetitle
		if modified:
			titlestring += " *"
			self.ui.actionSave.setDisabled(False)
		else:
			self.ui.actionSave.setDisabled(True)
		self.setWindowTitle(titlestring)
		print "here2"
	def closeEvent(self, event):
		print "Quitting"
		if self.ui.actionSave.isEnabled():
			response =  QtGui.QMessageBox.question(self, "Quit?", "You have unsaved work.  Do you want to save?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No, QtGui.QMessageBox.Cancel)
			if response == QtGui.QMessageBox.Yes:
				self.saveFileAs()
				return
			elif response == QtGui.QMessageBox.No:
				pass
			elif response == QtGui.QMessageBox.Cancel:
				event.ignore()
				return 
		QtGui.QMainWindow.closeEvent(self, event)
class speakerThread(threading.Thread):
	def __init__(self, text):
		self.text = text
		threading.Thread.__init__(self)
	def run(self):
		import pyttsx
		speaker = pyttsx.init()
		speaker.say(self.text)
		speaker.runAndWait()
class settingsDialogBox(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_settingsDialog()
		self.ui.setupUi(self)
		
		#Load words into textarea
		fileHandle = open(platformSettings.pathToCustomWords, 'r')
		self.ui.customWordsTextEdit.setPlainText(fileHandle.read())
		fileHandle.close()
		QtCore.QObject.connect(self.ui.okayButton, QtCore.SIGNAL("clicked()"), self.okayClicked)
		QtCore.QObject.connect(self.ui.applyButton, QtCore.SIGNAL("clicked()"), self.applyClicked)
	def applyClicked(self):
		fileHandle = open(platformSettings.pathToCustomWords, "w")
		fileHandle.write(self.ui.customWordsTextEdit.toPlainText())
		fileHandle.close()
		self.emit(QtCore.SIGNAL("dialogSaved"))
	def okayClicked(self):
		self.applyClicked()
		self.close()
		
		
application = QtGui.QApplication(sys.argv)
app = MainApplication()
app.show()
application.exec_()