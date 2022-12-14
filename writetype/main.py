#!/usr/bin/python

# Copyright 2010-2012 Max Shinn

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
from PyQt4.QtCore import QCoreApplication
import resources_rc
import enchant
from enchant.tokenize import get_tokenizer
from wordsList import WordsList
from platformSettings import *
from settings import SettingsDialogBox
from ui_distractionfree import Ui_distractionFree
import re
from os import path, sep
from speaker import Speaker
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import QTranslator, QLocale, qVersion
from ui_statistics import Ui_statisticsDialog
from os.path import isfile
import getopt
import sys
import revno
import logger
import codecs
from PyQt4.QtCore import QLibraryInfo

#Command line arguments
parsedoptions, options = getopt.gnu_getopt(sys.argv[1:], "l:t:c?", ["lang=", "tts-engine=", "help"])
for optionname, optionvalue in parsedoptions:
    if optionname == "-l" or optionname == "--lang":
        setPSettingTmp("language", optionvalue)
    elif optionname == "-t" or optionname == "--tts-engine":
        setSettingTmp("ttsengine", optionvalue)
    elif optionname == "-?" or optionname == "--help":
        print """Usage: writetype [OPTION] ... FILE
Open FILE when the application starts.

Mandatory arguments to long options are mandatory for short options too.
  -l,  --lang           Set the language for this session
  -t,  --tts-engine     Set the tts engine for this session.  Changes in the settings during this session will override this.
  -?,  --help           Display this help and exit

Report bugs to <admin@bernsteinforpresident.com>"""
        exit(0)

application = QtGui.QApplication(sys.argv)
from listWidget import *
from ui_mainwindow import Ui_MainWindow


class MainApplication(QtGui.QMainWindow):
    """The main application class"""

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #General Actions
        QtCore.QObject.connect(self.ui.actionOpen, QtCore.SIGNAL("triggered()"), self.openDialog)
        QtCore.QObject.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.saveFile)
        QtCore.QObject.connect(self.ui.actionSave_As, QtCore.SIGNAL("triggered()"), self.saveFileAs)
        QtCore.QObject.connect(self.ui.actionBold, QtCore.SIGNAL("triggered()"), self.ui.textArea.boldSelectedText)
        QtCore.QObject.connect(self.ui.actionItalic, QtCore.SIGNAL("triggered()"), self.ui.textArea.italicSelectedText)
        QtCore.QObject.connect(self.ui.actionUnderline, QtCore.SIGNAL("triggered()"), self.ui.textArea.underlineSelectedText)
        QtCore.QObject.connect(self.ui.actionHighlightMode, QtCore.SIGNAL("toggled(bool)"), self.ui.textArea.toggleHighlight)
        QtCore.QObject.connect(self.ui.actionHighlight, QtCore.SIGNAL("triggered()"), self.ui.textArea.highlightAction)
        QtCore.QObject.connect(self.ui.actionAlignLeft, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignLeft)
        QtCore.QObject.connect(self.ui.actionAlignCenter, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignCenter)
        QtCore.QObject.connect(self.ui.actionAlignRight, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignRight)
        # Removing this functionality for now.  Apparently this doesn't work in Qt 4.8?
        if True == False and '4.8.' in qVersion(): #only for the new unreleased QT, unfortunately
            QtCore.QObject.connect(self.ui.actionDoubleSpace, QtCore.SIGNAL("triggered()"), self.ui.textArea.doubleSpace)
            QtCore.QObject.connect(self.ui.actionSingleSpace, QtCore.SIGNAL("triggered()"), self.ui.textArea.singleSpace)
        else:
            self.ui.actionDoubleSpace.setVisible(False)
            self.ui.actionSingleSpace.setVisible(False)

        #Context menu for textarea
        self.ui.textArea.actionCut = self.ui.actionCut
        self.ui.textArea.actionCopy = self.ui.actionCopy
        self.ui.textArea.actionPaste = self.ui.actionPaste

        #The title
        self.setWindowTitle(self.tr("WriteType - ") + self.tr("Untitled Document"))
        QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("keyPressed"), self.updateTitle)

        #Set up the TTS
        self.speaker = Speaker("festival")
        QtCore.QObject.connect(self.ui.actionSpeak, QtCore.SIGNAL("triggered()"), self.readAloud)
        QtCore.QObject.connect(self.ui.actionStop, QtCore.SIGNAL("triggered()"), self.speaker.stop)
        QtCore.QObject.connect(self.ui.spellingSuggestionsList, QtCore.SIGNAL("speakWord"), self.sayText)

        #Fonts
        QtCore.QObject.connect(self.ui.spinBoxFontSize, QtCore.SIGNAL("valueChanged(int)"), self.ui.textArea.setFontSize)
        QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("cursorPositionChanged()"), self.updateFontSizeSpinBoxValue)
        QtCore.QObject.connect(self.ui.fontComboBox, QtCore.SIGNAL("currentFontChanged(const QFont&)"), self.ui.textArea.setFont)
        self.ui.textArea.setStyleSheet("/*background-image: url(:/res/background.png);*/ font: 12pt;")
        if not getSetting("disablefancyinterface", False):
            QtGui.QFontDatabase.addApplicationFont(":/res/ArchitectsDaughter.ttf")
            self.ui.menubar.setStyleSheet("font-family: \"Architects Daughter\"; font-size: 12pt;")
        else:
            self.setStyleSheet("")

        #about boxes
        QtCore.QObject.connect(self.ui.actionAboutQt, QtCore.SIGNAL("triggered()"), lambda : QtGui.QMessageBox.aboutQt(self))
        QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.showAbout)
        QtCore.QObject.connect(self.ui.actionDocumentation, QtCore.SIGNAL("triggered()"), self.openHelpPage)
        QtCore.QObject.connect(self.ui.actionCheck_for_Updates, QtCore.SIGNAL("triggered()"), self.checkForUpdates)
        QtCore.QObject.connect(self.ui.actionSaveDebugLog, QtCore.SIGNAL("triggered()"), self.saveLog)

        #Word list for word completion
        self.wl = WordsList()
        logger.init(self.wl)
        try:
            self.tokenizer = get_tokenizer(getPlatformSetting('language'))
        except enchant.tokenize.Error:
            self.tokenizer = get_tokenizer("en_US")
            logger.log("Language error, falling back to US English tokenizer", logtype="Error")
        self.wlIndex = None
        self.wordsN = []
        self.lastCursorPos = 0
        QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("tabEvent"), self.ui.spellingSuggestionsList.tabEvent)
        QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("tabBackEvent"), self.ui.spellingSuggestionsList.backtabEvent)
        QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("wordEdited"), self.populateWordList)
        QtCore.QObject.connect(self.ui.spellingSuggestionsList, QtCore.SIGNAL("wordPressed"), self.correctWordFromListItem)
        QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("cursorPositionChanged()"), self.clearWordList)

        #Autocorrect
        QtCore.QObject.connect(self.ui.textArea, QtCore.SIGNAL("wordEdited"), self.checkForAutocorrection)

        #printer
        QtCore.QObject.connect(self.ui.actionPrint, QtCore.SIGNAL("triggered()"), self.openPrintDialog)
        self.filename = ""
        self.filetitle = self.tr("Untitled Document")

        #settings dialog box
        self.settings_box = SettingsDialogBox(self)
        QtCore.QObject.connect(self.ui.actionSettings, QtCore.SIGNAL("triggered()"), self.settings_box.show)
        QtCore.QObject.connect(self.settings_box, QtCore.SIGNAL("dialogSaved"), self.refreshAfterSettingsDialogClosed)

        #Distraction free
        self.distractionFree_box = DistractionFreeWindow(self)
        self.ui.distractionButton.hide()
        QtCore.QObject.connect(self.ui.actionDistractionFree, QtCore.SIGNAL("triggered()"), self.openDistractionFreeMode)
        QtCore.QObject.connect(self.distractionFree_box, QtCore.SIGNAL("rejected()"), self.closeDistractionFreeMode)
        QtCore.QObject.connect(self.ui.distractionButton, QtCore.SIGNAL("clicked()"), self.closeDistractionFreeMode)

        #Statistics
        self.statisticsDialog = StatisticsWindow(self)
        QtCore.QObject.connect(self.ui.actionStatistics, QtCore.SIGNAL("triggered()"), self.showStatisticsDialog)

        #Diction check
        self.dictionCheckModeDisable()
        self.dictionReplacements = None
        self.index = 0
        self.lastDictionReplacementsIndex = -1
        QtCore.QObject.connect(self.ui.nextButton, QtCore.SIGNAL("clicked()"), self.nextDictionError)
        QtCore.QObject.connect(self.ui.actionDiction_Check, QtCore.SIGNAL("triggered()"), self.dictionCheckModeEnable)
        QtCore.QObject.connect(self.ui.dictionCloseButton, QtCore.SIGNAL("clicked()"), self.dictionCheckModeDisable)
        if getPlatformSetting("language") != "en_US":
            self.ui.actionDiction_Check.setVisible(False)

        ## #images
        ## QtCore.QObject.connect(self.ui.actionInsert_Image, QtCore.SIGNAL("triggered()"), self.ui.textArea.insertImage)
        ## QtCore.QObject.connect(self.ui.actionAlign_Image_Right, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignImageRight)
        ## QtCore.QObject.connect(self.ui.actionAlign_Image_Left, QtCore.SIGNAL("triggered()"), self.ui.textArea.alignImageLeft)
        ## #Lets disable image support for now.  Yeah... I think that would be a wise idea.  (And double spacing too,  since I can't get it to work.)
        ## self.ui.imageToolBar.setVisible(False)
        self.ui.actionEnableImageToolbar.setVisible(False)
        #self.ui.actionDoubleSpace.setVisible(False)
        #self.ui.actionSingleSpace.setVisible(False)

        #Apply some settings
        if getSetting("defaultfont", ""):
            self.ui.fontComboBox.setCurrentFont(QtGui.QFont(getSetting("defaultfont")))

        #Add some more widgets to the toolbar
        self.ui.editToolBar.addWidget(self.ui.sizeLabel)
        self.ui.editToolBar.addWidget(self.ui.spinBoxFontSize)
        self.ui.editToolBar.addWidget(self.ui.fontComboBox)

        #Check to see if there is unsaved work
        if getSetting("autosavepath", ""):
            response = QtGui.QMessageBox.question(self, self.tr("Crash recovery"), self.tr("WriteType found unsaved work from a crash.  Would you like to recover it?"), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if response == QtGui.QMessageBox.Yes:
                text = codecs.open(getSetting("autosavepath", ""), encoding='utf-8').read()
                self.ui.textArea.setText(text)
                self.filetitle = self.tr("Recovered file")
                self.updateTitle()
                #Add the words in the document to the custom words list
                for token in self.tokenizer(unicode(self.ui.textArea.toPlainText())):
                    self.wl.addCustomWord(token[0].lower())
        #Load the file if one was specified
        global options
        if len(options) >= 1:
            self.openFile(options[0])


    def __del__(self):
        print "destructor"
        QtGui.QMainWindow.__del__(self)


    #FILE OPENING/SAVING

    def openDialog(self):
        """Display a dialog to open a file"""
        filename = QtGui.QFileDialog.getOpenFileName(self, self.tr("Open file"), getSetting('lastdir', ''), QCoreApplication.translate("WriteTypeMain", "All Compatible Files (*.wtd *.htm *.html *.txt);;WriteType Document (*.wtd);;Formatted Text (*.html *.htm);;All Files (*.*)"))
        if filename:
            setSetting("lastdir", path.dirname(unicode(filename))+sep)
        self.openFile(filename)

    def openFile(self, filename):
        """Open a file and display it"""
        if isfile(filename):
            self.filename = filename
            text = codecs.open(self.filename, encoding='utf-8').read()
            self.ui.textArea.setText(text)
            self.filetitle = str(self.filename).split(sep).pop()
            self.updateTitle(False)

            #Add the words in the document to the custom words list
            for token in self.tokenizer(unicode(self.ui.textArea.toPlainText())):
                self.wl.addCustomWord(token[0].lower())

            #Set the correct font
            cursor = self.ui.textArea.textCursor()
            cursor.setPosition(2)
            self.ui.fontComboBox.setCurrentFont(cursor.charFormat().font())

    def saveFile(self):
        """Save the current document to a prespecified file"""
        if isfile(self.filename):
            self.writeFile()
            self.filetitle = unicode(self.filename).split(sep).pop()
            self.updateTitle(False)
            return True
        else:
            return self.saveFileAs()

    def saveFileAs(self):
        """Prompt the user on where to save the current document"""
        filename, filter_ = QtGui.QFileDialog.getSaveFileNameAndFilter(self, self.tr("Save file"), getSetting('lastdir', ''), QCoreApplication.translate("WriteTypeMain", "WriteType Document (*.wtd);;Formatted Text (*.html);;Plain Text (*.txt)"))
        if not filename:
            return

        setSetting("lastdir", path.dirname(unicode(filename))+sep)

        if '(*.wtd)' in filter_:
            ext = '.wtd'
        elif '(*.html)' in filter_:
            ext = '.html'
        elif '(*.txt)' in filter_:
            ext = '.txt'
        else:
            ext = ""
        if ((not str(filename).endswith(ext))):
            filename = filename + ext
        self.filename = filename

        self.writeFile()

        self.filetitle = unicode(self.filename).split(sep).pop()
        self.updateTitle(False)
        return True

    def writeFile(self):
        """Used by save functions to write the file to the disk"""
        extension = unicode(self.filename).split('.').pop()
        try:
            file = codecs.open(self.filename, 'w+', encoding='utf-8')
            if extension == "html" or extension == "wtd":
                content = self.ui.textArea.document().toHtml('UTF-8')
                #Sort of hacky way to fix the black spots where there used to be highlighted sections
                content = content.replace("background-color:#000000", "")
                file.write(unicode(content))
            else:
                file.write(unicode(self.ui.textArea.toPlainText()))
            file.close()
        except:
            logger.log("Error saving work", logtype="Error", tb=True)
            QMessageBox.warning(self, self.tr("Save error"), self.tr("WriteType was unable to save your work.  Please check the file extension, ensure that the selected file is writable, and try again."))

    def autoSave(self):
        """Autosave the current document whenever called"""
        #This function should be called whenever an autosave is desired
        path = getSetting("autosavepath", "")
        if not path:
            from tempfile import mkstemp
            path = mkstemp()[1]
            setSetting("autosavepath", path)
        handle = codecs.open(path, 'w', encoding='utf-8')
        handle.write(unicode(self.ui.textArea.toHtml()))
        handle.close()

    #TTS

    def readAloud(self):
        """Speak the document or the selected text out loud"""
        if self.ui.textArea.textCursor().selectedText():
            text = self.ui.textArea.textCursor().selectedText()
        else:
            text = self.ui.textArea.toPlainText()
        self.sayText(text)

    def sayText(self, text, showalert=True):
        """Speak the specified text out loud, and disable read-back buttons on failure"""
        if self.speaker.say(text) == True:
            self.ui.actionSpeak.setDisabled(True)
            self.ui.actionStop.setDisabled(True)
            #On failure, should we show an alert?
            if showalert:
                QMessageBox.warning(None, self.tr("Feature unavailable"), self.tr("The current TTS driver is invalid.  Read-back is unavailable for this session."))

    def disableSpeakButton(self):
        self.ui.actionSpeak.disable()

    #AUTOCORRECTIONS

    def checkForAutocorrection(self, word):
        """Check to see if the last word typed needed to be automatically corrected.
        Unless I structure this better, it also looks to see if the last word was
        misspelled and offers suggestions in the word completion box."""
        if word[-1:] in [".", "!", "?"]:
            logger.log("Autosaving")
            self.autoSave()
        if word[-1:] in ["", "\b", " ", "\t", ".", "?", ":", "!", ",", ";", ")"]:
            if self.wl.correctWord(word[:-1]) != False:
                self.ui.textArea.replaceSelectedWord(self.wl.correctWord(word[:-1]))
                word = self.wl.correctWord(word[:-1])
            self.ui.spellingSuggestionsList.clear()
            self.wordsN = []

            #This is HORRIBLE of me.  Why is all this garbage down here that has nothing to do with autocorrections?

            wordraw = word
            word = re.sub('[ \t!"#$%&()*+,./:;<=>?@\[\\]^_`{|}~]', '', word)
            #word.translate(None, ' \t!"#$%&()*+,./:;<=>?@[\\]^_`{|}~')

            #Read back the word just typed
            if getSetting("readastyped", False):
                if word:
                    self.sayText(word, showalert=False)

            #Display spell check suggestions in the misspelling box after a space is pressed
            if not word:
                if wordraw:
                    self.wl.pattern.clearLastCheckedWord()
            elif self.ui.textArea.spellCheckEnabled == True and getSetting("spellingcheck", True) and self.ui.textArea.dictionary.check(word) == False:
                logger.log("Checking words was false: ", word)
                self.wordsN = []
                words = self.ui.textArea.dictionary.suggest(word)
                for word in words:
                    self.wordsN.append((word, 0))
                for word in self.wordsN:
                    item = ListWidgetItem(word[0], mode=MODE_REPLACE, colorfg=Qt.red)
                    self.ui.spellingSuggestionsList.addItem(item)
            elif getSetting("phrasecompletion", True):
                #This is still HORRIBLE of me.  Still nothing to do with autocorrections.
                links = self.wl.pattern.getLinks(word)
                if links:
                    self.ui.spellingSuggestionsList.clear()
                    for link in links:
                        item = ListWidgetItem(link[0], weight=link[1], mode=MODE_INSERT)
                        self.ui.spellingSuggestionsList.addItem(item)
                    for word in self.wordsN:
                        #Colors!
                        count = link[1]
                        if count > 10: count = 10
                        bgcolor = QtGui.QColor.fromHsv(250-count*25, count*10, 255, int(bool(count))*255)
                        item = ListWidgetItem(word[0], bgcolor=bgcolor)
                        self.ui.spellingSuggestionsList.addItem(item)


        self.ui.spellingSuggestionsList.repaint()

    #SPELLING SUGGESTIONS/WORD LISTS

    def tabEvent(self):
        """Tab through the words in the spelling completion box"""
        if not self.wordsN:
            return
        if self.wlIndex == None:
            self.wlIndex = 0
        elif self.wlIndex >= len(self.wordsN)-1:
            self.wlIndex = 0
        else:
            self.wlIndex += 1
        if self.wordsN[self.wlIndex][2] == "i": #i for insert
            self.ui.textArea.insertPlainText(self.wordsN[self.wlIndex][0])
        else: #r for replace
            self.ui.textArea.replaceLastWord(self.wordsN[self.wlIndex][0])
        self.ui.spellingSuggestionsList.setCurrentRow(self.wlIndex)

    def tabBackEvent(self):
        """Tab backwards through words in the spelling completion box"""
        if not self.wordsN:
            return
        if self.wlIndex == None:
            self.wlIndex = 0
        elif self.wlIndex == 0:
            self.wlIndex = len(self.wordsN)-1
        else:
            self.wlIndex -= 1
        self.ui.textArea.replaceLastWord(self.wordsN[self.wlIndex][0])
        self.ui.spellingSuggestionsList.setCurrentRow(self.wlIndex)

    def clearWordList(self):
        """Clear the spelling completion box"""
        curpos = self.ui.textArea.textCursor().position()
        if abs(curpos - self.lastCursorPos) > 1:
            if self.ui.textArea.lastWord == None:
                self.ui.spellingSuggestionsList.clear()
        self.lastCursorPos = curpos

    def correctWordFromListItem(self, word, mode):
        """Replace the last word typed with the currently selected row in the
        spelling completion box"""
        if mode == MODE_INSERT: #insert #TODO fix this
            if not self.ui.textArea.lastWord:
                self.ui.textArea.insertPlainText(word)
                self.ui.textArea.lastWord = word
                return
        #MODE_REPLACE
        self.ui.textArea.replaceLastWord(word)

    def populateWordList(self, text):
        """Serach for completions and fill the word completion box with words"""
        text = unicode(text)

        #If the user typed a word + delimiter, add it to the custom word list and don't display any more suggestions after the delimiter
        if text[0:-1] and text[-1:] in (" ", ".", ",", "!", "?", "\t"):
            if self.ui.textArea.spellCheckEnabled == False or getSetting("spellingcheck", True) == False or self.ui.textArea.dictionary.check(text[0:-1]):
                self.wl.addCustomWord(text.lower()[0:-1])
            #return

        #This way, the word list won't keep changing if the user tabs to select a new word
        if self.ui.spellingSuggestionsList.index != None:
            return

        self.ui.spellingSuggestionsList.clear()

        if len(text) <= getSetting("minimumletters", 0):
            return

        if not text:
            return

        if self.ui.textArea.textCursor().hasSelection():
            self.ui.spellingSuggestionsList.clear()
            return

        words = self.wl.search(text)
        for w,s in words:
            self.ui.spellingSuggestionsList.addNewItem(w, weight=s)

        if getSetting("guessmisspellings", True) and len(self.ui.spellingSuggestionsList.words) <= getSetting("threshold", 0):
            replacements = [
                ["a", "e"],
                ["a", "o"],
                ["d", "dd"],
                ["d", "t"],
                ["d", "tt"],
                ["e", "a"],
                ["e", "ea"],
                ["e", "i"],
                ["e", "ie"],
                ["ea", "ee"],
                ["ee", "i"],
                ["ei", "i"],
                ["i", "ee"],
                ["k", "c"],
                ["k", "ck"],
                ["k", "ch"],
                ["l", "le"],
                ["l", "ll"],
                ["n", "kn"],
                ["o", "a"],
                ["o", "ou"],
                ["s", "c"],
                ["s", "ss"],
                ["sh", "c"],
                ["t", "d"],
                ["t", "tt"],
                ["u", "o"],
                ["u", "oo"],
                ["u", "ou"],
                ["xs", "x"]
            ]

            possibilities = []
            text = text.lower()
            for replacement in replacements:
                if replacement[0] in text:
                    possibilities.append(text.replace(replacement[0], replacement[1]))
            words = self.wl.search(tuple(possibilities))
            for w,s in words:
                self.ui.spellingSuggestionsList.addNewItem(w, weight=s)
        self.ui.spellingSuggestionsList.repaint()

    def keyPressEvent(self, e):
        """Overloaded keyPressEvent from QWidget to catch F-keys"""
        #F-keys select words quickly
        fkeys = [Qt.Key_F1, Qt.Key_F2, Qt.Key_F3, Qt.Key_F4, Qt.Key_F5, Qt.Key_F6, Qt.Key_F7, Qt.Key_F8, Qt.Key_F9, Qt.Key_F10, Qt.Key_F11, Qt.Key_F12]
        if e.key() in fkeys:
            fkeyindex = fkeys.index(e.key())
            self.ui.spellingSuggestionsList.activate(fkeyindex)
        QtGui.QMainWindow.keyPressEvent(self, e)
        self.repaint()

    # DICTION CHECKING

    def dictionCheckModeEnable(self):
        """Open the diction check toolbar"""
        #Load these into memory only if we need to
        if self.dictionReplacements == None:
            logger.log("Loading resources for diction check")
            filepath = path.join(getPlatformSetting('pathToWordlists'),  "diction.txt")
            fileHandle = open(filepath, 'r')
            lines = fileHandle.read().split("\n")
            self.dictionReplacements = []
            for line in lines:
                self.dictionReplacements.append(line.partition("\t"))
        self.ui.dictionErrorFrame.setVisible(True)
        self.ui.nextButton.setDisabled(False)
        #self.ui.prevButton.setDisabled(False)
        self.dictionCheck()

    def dictionCheckModeDisable(self):
        """Close the diction check toolbar"""
        self.ui.dictionErrorFrame.setVisible(False)
        self.dictionReplacementsIndex = 0
        self.lastDictionReplacementsIndex = -1

    def dictionCheck(self):
        """Check the document for diction mistakes"""
        text = str(self.ui.textArea.toPlainText()).lower()
        while True:
            index = text.find(self.dictionReplacements[self.dictionReplacementsIndex][0], self.lastDictionReplacementsIndex+2)
            #Make sure it is a separate word.  This is easier than regex
            if index != -1 and not text[index + len(self.dictionReplacements[self.dictionReplacementsIndex][0])] in [" " , ".", "!", ",", ":", ";"]:
                self.lastDictionReplacementsIndex = index
                continue
            #If a word was found
            if index != -1:
                self.ui.textArea.selectTextByPosition(index, index + len(self.dictionReplacements[self.dictionReplacementsIndex][0]))
                suggestiontext = str(self.dictionReplacements[self.dictionReplacementsIndex][2])
                if suggestiontext and suggestiontext[0] == "=":
                    suggestiontext = [z for x,y,z in self.dictionReplacements if x == suggestiontext[1:]][0]
                if not suggestiontext:
                    suggestiontext = self.tr("<i>No suggestion available.</i>")
                self.ui.dictionErrorLabel.setText(suggestiontext)
                self.lastDictionReplacementsIndex = index
                break
            else:
                self.lastDictionReplacementsIndex = -1
                self.dictionReplacementsIndex += 1
                if self.dictionReplacementsIndex >= len(self.dictionReplacements):
                    self.dictionReplacementsIndex = 0
                    self.ui.dictionErrorLabel.setText(self.tr("<i>Diction check completed.</i>"))
                    self.ui.nextButton.setDisabled(True)
                    #self.ui.prevButton.setDisabled(True)
                    self.ui.textArea.selectTextByPosition(0, 0)
                    break

    def nextDictionError(self):
        """Go to the next diction error"""
        logger.log("going to diction check")
        self.dictionCheck()

    def updateFontSizeSpinBoxValue(self):
        """Update the font size spinbox when the cursor moves"""
        if not self.ui.textArea.textCursor().selectedText():
            if int(self.ui.textArea.fontPointSize()) > .1:
                self.ui.spinBoxFontSize.setValue(int(self.ui.textArea.fontPointSize()))

    def updateFontComboBoxValue(self):
        """Update the font family combobox when the cursor moves"""
        if not self.ui.textArea.textCursor().selectedText():
            self.ui.fontComboBox.setCurrentFont(self.ui.textArea.currentFont())
        self.ui.textArea.setFocus()

    #DIALOGS

    def showAbout(self):
        """Open the about box"""
        QtGui.QMessageBox.about(self, self.tr("About this program"), self.tr("""
        <h1>WriteType <span style="font-size: large">Revision r%1</span></h1>
        <h3>Copyright 2010-2012 Max Shinn</h3><br />
        <a href="mailto:admin@bernsteinforpresident.com">admin@BernsteinForPresident.com</a> <br />
        <a href="http://bernsteinforpresident.com">http://BernsteinForPresident.com</a> <br />
        This software is made available under the GNU General Public
        License v3 or later. For more information about your rights,
        see: <a href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a><br />
        <h3>Additional Contributions</h3>
        <table border="1" width="100%">
        <tr><td>Emilio Lopez</td><td>Spanish Translations</td></tr>
        <tr><td>Gorka Azkarate</td><td>Basque Translations</td></tr>
        <tr><td>Harm Bathoorn</td><td>Dutch Translations</td></tr>
        <tr><td><a href="mailto:sbasalaev@gmail.com">Sergey Basalaev</a></td><td>Russian Translations</td></tr>
        <tr><td><a href="mailto:topgunbg@gmail.com">Galin Petrov</a></td><td>Bulgarian Translations</td></tr>
        <tr><td>Agnese Dal Borgo</td><td>Italian Translations</td></tr>
        <tr><td>Riccardo Murri</td><td>Italian Translations</td></tr>
        <tr><td>Clm</td><td>French Translations</td></tr>
        <tr><td>Thomas  Weber</td><td>German Translations</td></tr>
        </table>""").arg(revno.aboutrevno))

    def checkForUpdates(self):
        """Check for updates"""
        from urllib2 import urlopen
        try:
            version = urlopen(getPlatformSetting("updateServer")).read()
            if int(version) > int(revno.aboutrevno):
                message = self.tr("""<html>A new version of WriteType is available!  You are using WriteType version r%2.  Find more information about WriteType version r%3 at: <a href="%1">%1</a></html>""").arg(getPlatformSetting("updateUrl")).arg(revno.aboutrevno).arg(version)
            else:
                message = self.tr("Your version of WriteType is up to date.  You are using WriteType version r%1.").arg(revno.aboutrevno)
        except:
            message = self.tr("There was an unexpected error in establishing a connection.  Please try again later.", tb=True)
        QtGui.QMessageBox.information(self, self.tr("Updates"), message)

    def openHelpPage(self):
        """Open the Bernsteinforpresident.com documentation"""
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(getPlatformSetting("documentationUrl")))

    def saveLog(self):
        """Save the log to a file, or display it if there is an error."""
        filename = QtGui.QFileDialog.getSaveFileName(self, self.tr("Save file"), "", "Log file (*.log)")
        if not filename:
            return
        try:
            file = codecs.open(filename, 'w+', encoding='utf-8')
            file.write(logger.formatLog())
            file.close()
        except:
            logger.log("Ironically, the log couldn't be saved.", logtype="Error", tb=True)
            messagebox = QMessageBox(self)
            messagebox.setDetailedText(logger.formatLog())
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.setWindowTitle(self.tr("Save error"))
            messagebox.setText(self.tr("WriteType was unable to save the log file.  Please check the file extension, ensure that the selected file is writable, and try again."))
            messagebox.open()


    def openPrintDialog(self):
        """Print a document"""
        printer = QtGui.QPrinter()
        printer.setDocName("writetype_" + self.filename)
        printDialog = QtGui.QPrintDialog(printer)
        printDialog.setModal(True)
        printDialog.setWindowTitle(self.tr("WriteType - ") + self.tr("Print"))
        if printDialog.exec_():
            currentGrammarColor = self.ui.textArea.highlighter.format_grammar.underlineColor()
            self.ui.textArea.highlighter.format_grammar.setUnderlineColor(Qt.transparent)
            currentSpellingColor = self.ui.textArea.highlighter.format_spelling.underlineColor()
            self.ui.textArea.highlighter.format_spelling.setUnderlineColor(Qt.transparent)
            self.ui.textArea.highlighter.rehighlight()

            self.ui.textArea.document().print_(printer)
            self.ui.textArea.highlighter.format_grammar.setUnderlineColor(currentGrammarColor)
            self.ui.textArea.highlighter.format_grammar.setUnderlineColor(currentSpellingColor)
            self.ui.textArea.highlighter.rehighlight()

    def showStatisticsDialog(self):
        """Show document statistics"""
        #Update the statistics
        self.statisticsDialog.ui.filenameLabel.setText(self.filename)
        #Only alpha-numerics
        chars = 0
        for char in unicode(self.ui.textArea.toPlainText()):
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
                chars += 1
        self.statisticsDialog.ui.charactersLabel.setText(str(chars))
        #Stupid tokenizer, doesn't work with len()
        words = 0
        for x in self.tokenizer(unicode(self.ui.textArea.toPlainText())):
            words += 1
        self.statisticsDialog.ui.wordsLabel.setText(unicode(words))
        sentences = len(re.findall('[A-Z][^A-Z]*[.!?]', unicode(self.ui.textArea.toPlainText())))
        self.statisticsDialog.ui.sentencesLabel.setText(unicode(sentences))
        paragraphs = self.ui.textArea.document().blockCount()
        self.statisticsDialog.ui.paragraphsLabel.setText(unicode(paragraphs))
        #Automated Readability Index - this is the easiest to implement :)
        try:
            readability = 4.71*(float(chars)/words) + .5*(float(words)/sentences) - 21.43
            self.statisticsDialog.ui.readabilityLabel.setText(unicode(round(readability, 1)))
        except ZeroDivisionError:
            self.statisticsDialog.ui.readabilityLabel.setText(QCoreApplication.translate("WriteTypeMain", "Invalid, no sentences found."))

        self.statisticsDialog.show()

    def openDistractionFreeMode(self):
        """Display only the text entry box and the word completion list in fullscreen
        mode.  Buggy on older operating systems, but who uses those anyway? :)"""
        self.distractionFree_box.ui.verticalLayout_2.addWidget(self.ui.centralwidget)
        #Gnome compatible version of showFullScreen()
        self.distractionFree_box.setWindowFlags(self.distractionFree_box.windowFlags() | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.distractionFree_box.setFixedSize(application.desktop().size())
        self.distractionFree_box.setGeometry(0, 0, self.distractionFree_box.width(), self.distractionFree_box.height())

        self.distractionFree_box.show()
        self.ui.distractionButton.show()

    def closeDistractionFreeMode(self):
        """Display the normal application again"""
        self.distractionFree_box.hide()
        self.ui.centralwidget.setParent(self)
        self.setCentralWidget(self.ui.centralwidget)
        self.ui.distractionButton.hide()

    def refreshAfterSettingsDialogClosed(self):
        """Reload the settings that were changed in the settings dialog"""
        self.ui.actionSpeak.setDisabled(False)
        self.ui.actionStop.setDisabled(False)

        self.ui.textArea.setUpDictionary()
        self.wl.loadWords()
        self.wl.refreshReplacementTable()
        self.speaker.setDriver()

    #MISC

    def updateTitle(self, modified=True):
        """Change the window title to either remove the 'unsaved asterisk'
        or change the document title."""
        titlestring = self.tr("WriteType - ") + self.filetitle
        if modified:
            titlestring += " *"
            self.ui.actionSave.setDisabled(False)
        else:
            self.ui.actionSave.setDisabled(True)
        self.setWindowTitle(titlestring)

    def closeEvent(self, event):
        """Clean up!"""
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
        #Purge the autosaves
        path = getSetting("autosavepath", "")
        if path:
            from os import unlink
            setSetting("autosavepath", "")
            try:
                unlink(path)
            except Exception:
                pass
        QtGui.QMainWindow.closeEvent(self, event)

class DistractionFreeWindow(QtGui.QDialog):
    """Fullscreen window onto which the word suggestion list
    and the text editing widget are reparented"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_distractionFree()
        self.ui.setupUi(self)

class StatisticsWindow(QtGui.QDialog):
    """Statistics dialog box"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_statisticsDialog()
        self.ui.setupUi(self)

# Translations.
trans = QTranslator()
transqt = QTranslator()
# We only use the first two chararcters of the language (by saying
# [0:2]) because we don't have multiple translations from the same
# language.
logger.log("Language is ", getPlatformSetting("language")[0:2], logtype="Info")
transqt.load("qt_" + getPlatformSetting("language")[0:2], QLibraryInfo.location(QLibraryInfo.TranslationsPath))
application.installTranslator(transqt)
trans.load("qt_" + getPlatformSetting("language")[0:2], path.join(getPlatformSetting("basePath"), "translations"))
application.installTranslator(trans)

app = MainApplication()
app.show()
application.exec_()
