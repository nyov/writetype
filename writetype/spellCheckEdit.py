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


from PyQt4.Qt import QTextEdit, QMouseEvent, QTextCursor, QSyntaxHighlighter, QKeyEvent, QFont, QColor, QMenu
from PyQt4.Qt import Qt
from PyQt4.Qt import QEvent
from PyQt4.Qt import QAction
from PyQt4.Qt import QTextCharFormat
from PyQt4.QtCore import SIGNAL
from PyQt4 import QtCore
import re
import enchant
import enchant.checker
import platformSettings
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QTextBlockUserData
import sip
import sys

class spellCheckEdit(QTextEdit):
    #To support the highlighting feature
    highlighting = False

    #Hide your eyes!
    def __new__(cls, *args, **kwargs):
        if '-c' in sys.argv:
            import colemak
            self = sip.wrapper.__new__(colemak.ColemakEdit, *args, **kwargs)
        else:
            self = sip.wrapper.__new__(spellCheckEdit, *args, **kwargs)
        return self
    #Okay, you can look again

    def __init__(self, *args):
        QTextEdit.__init__(self, *args)
        try:
            self.dictionary = enchant.DictWithPWL(platformSettings.getPlatformSetting('language'), None)
        except enchant.Error:
            self.dictionary = enchant.DictWithPWL("en_US", None)
        self.highlighter = Highlighter(self.document())
        self.highlighter.setDict(self.dictionary)
        self.menu = QMenu(self)
        self.lastWord = ""
        
    def mousePressEvent(self, event):
        """Move the cursor to the appropriate position"""
        if event.button() == Qt.RightButton:
            event = QMouseEvent(QEvent.MouseButtonPress, event.pos(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)

##      #Highlight an image if it is clicked
##      cursor = self.textCursor()
##      cursor.select(QTextCursor.WordUnderCursor)
##      if str(cursor.selection().toHtml()).find("img") != False:
##          self.setTextCursor(cursor)

        QTextEdit.mousePressEvent(self, event)
    
    def mouseReleaseEvent(self, event):
        """Highlight the word under the cursor if necessary"""
        if self.highlighting:
            self.highlightAction()
        else:
            QTextEdit.mousePressEvent(self, event)

    def contextMenuEvent(self, event):
        """Display the context menu"""
        cursor = self.textCursor()
        position = cursor.position()
        menu = QMenu(self)
        menu.addAction(self.actionCut)
        menu.addAction(self.actionCopy)
        menu.addAction(self.actionPaste)

        ## print str(cursor.selection().toHtml())
        ## #Check to see if an image is under the cursor
        ## if str(cursor.selection().toHtml()).find("<img") != -1:
        ##  self.setTextCursor(cursor) #show the image highlighed
        ##  menu.addSeparator()
        ##  action = QAction("Align Left", menu)
        ##  self.connect(action, SIGNAL("triggered()"), self.alignImageLeft)
        ##  menu.addAction(action)
        ##  self.addAction(action)
        ##  action = QAction("Align Right", menu)
        ##  self.connect(action, SIGNAL("triggered()"), self.alignImageRight)
        ##  menu.addAction(action)

        #grammar check
        if self.highlighter.getDescriptionText(cursor.position(), self.toPlainText()):
            menu.addSeparator()
            for mistake in self.highlighter.getDescriptionText(cursor.position(), self.toPlainText()):
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
        
    def selectTextByPosition(self, begin, end):
        """Select text by specifying its beginning and ending index"""
        cursor = self.textCursor()
        cursor.setPosition(begin)
        cursor.setPosition(end, QTextCursor.KeepAnchor)
        self.setTextCursor(cursor)

    def replaceTextByPosition(self, word, begin, end):
        """Replace text by specifying its beginning and ending indices"""
        cursor = self.textCursor()
        cursor.setPosition(begin)
        cursor.setPosition(end, QTextCursor.KeepAnchor)
        cursor.beginEditBlock()
        cursor.removeSelectedText()
        cursor.insertText(word)
        cursor.endEditBlock()

    def addToDictionary(self, word):
        """Add a word to the spell check dictionary"""
        self.dictionary.add(word)
        
    def replaceSelectedWord(self, word):
        """Replace the most recently typed word with another"""
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
        #self.log.log(oldword + " -> " + str(word))

    def replaceLastWord(self, word):
        """Replace the last word typed with another.  Works by remembering the
        last word selected in the word suggestion box, and removing that many
        characters.  This is necessary for spell checking in the box to function."""
        #Dirtier than the above, but works better in the case of spellcheck
        cursor = self.textCursor()
        if cursor.hasSelection():
            return
        cursor.beginEditBlock()
        
        #Make sure the last word is selected
        if not self.lastWord:
            cursor2 = self.textCursor()
            cursor2.select(QTextCursor.WordUnderCursor)
            #cursor2.movePosition(cursor.PreviousCharacter, cursor.KeepAnchor)
            while not cursor2.selectedText():
                cursor2.deletePreviousChar()
                cursor2.select(QTextCursor.WordUnderCursor)
            self.lastWord = cursor2.selectedText()
        #Capitalization
        if re.match(u'[A-Z][a-z]*', unicode(self.lastWord)):
            word = unicode(word).capitalize()
        else:
            word = unicode(word).lower()
            
        #Remove the word
        for i in range(0, len(self.lastWord)):
            cursor.deletePreviousChar()
        cursor.insertText(word)
        cursor.endEditBlock()

        self.lastWord = word
        self.keyPressEvent(QKeyEvent(QEvent.KeyPress, 0, Qt.NoModifier))
        self.setFocus()     

    def keyPressEvent(self, event):
        """Emit tab events and events indicating the last word/char typed"""
        #Tabs should scroll through the words
        if event.key() == Qt.Key_Backtab or event.key() == Qt.Key_Up:
            self.emit(SIGNAL("tabBackEvent"))
            return
        if event.key() == Qt.Key_Tab or event.key() == Qt.Key_Down:
            self.emit(SIGNAL("tabEvent"))
            return
        if event.key() == Qt.Key_Backspace:
            QTextEdit.keyPressEvent(self, event)
            return #Speed things up a bit
        if event.text() != "":
            self.lastWord = ""
        #Don't do all this if someone just clicked something in the word list
        if event.key() == 0:
            return

        cursor = self.textCursor()
        #Check to make sure text is selected on the left, not the right
        cursor.movePosition(cursor.PreviousCharacter, cursor.KeepAnchor)
        if cursor.selectedText() != " ":
            cursor.select(QTextCursor.WordUnderCursor)
            if cursor.hasSelection():
                text = unicode(cursor.selectedText() + event.text())
            else:
                text = unicode(event.text())
            self.emit(SIGNAL("wordEdited"), text)
        else:
            self.emit(SIGNAL("wordEdited"), unicode(event.text()))
        self.emit(SIGNAL("keyPressed"))
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

    def setFont(self, font):
        """Ensure that only one font is being used in the document"""
        if not self.hasFocus():
            cursor = self.textCursor()
            cursor.setPosition(0)
            cursor.setPosition(len(self.toPlainText()), cursor.KeepAnchor)
            fontFormat = QTextCharFormat()
            fontFormat.setFontFamily(font.family())
            cursor.mergeCharFormat(fontFormat)

    def setFontSize(self, size):
        """Ensure that only one font size is being used in the paragraph"""
        if not self.hasFocus():
            cursor = self.textCursor()
            cursor.select(QTextCursor.BlockUnderCursor)

            fontFormat = QTextCharFormat()
            fontFormat.setFontPointSize(size)
            cursor.mergeCharFormat(fontFormat)

    def toggleHighlight(self, isSet):
        """Set the cursor to highlight the word underneath it and disable
        standard editing functions"""
        self.highlighting = isSet
        if isSet:
            self.setReadOnly(True)
        else:
            self.setReadOnly(False)

    def highlightAction(self):
        """Highlight the word underneath the cursor"""
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

    ## def insertImage(self):
    ##  imageurl = QFileDialog.getOpenFileName(self, "Insert image", platformSettings.getPlatformSetting('defaultOpenDirectory'), "Image file (*.jpg *.jpeg *.gif *.png)")
    ##  self.insertImageByUrl(imageurl)

    ## def insertImageByUrl(self, url):
    ##  #cursor = self.textCursor()
    ##  self.insertHtml('&nbsp;<img src="{0}" style="float:right" />&nbsp;'.format(url))
        
    ## def alignImageRight(self):
    ##  cursor = self.textCursor()
    ##  cursor.select(QTextCursor.WordUnderCursor)
    ##  selection = str(cursor.selection().toHtml())
    ##  selection = selection.replace("float: left", "float: right")
    ##  selection = selection.replace("float: none", "float: right")
    ##  cursor.removeSelectedText()
    ##  cursor.insertHtml(selection)
    ##  self.setHtml(self.toHtml()) #framework bugs are not cute
        
    ## def alignImageLeft(self):
    ##  cursor = self.textCursor()
    ##  cursor.select(QTextCursor.WordUnderCursor)
    ##  selection = cursor.selection().toHtml()
    ##  selection = selection.replace("float: right", "float: left")
    ##  selection = selection.replace("float: none", "float: left")
    ##  cursor.removeSelectedText()
    ##  cursor.insertHtml(selection)
    ##  self.setHtml(self.toHtml()) #see above for bad pun

class Highlighter(QSyntaxHighlighter):
    """Highlight misspellings and grammar/formatting issues"""

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
            "re": re.compile(u'([^[.?!"\'])[ ]{2,}([A-Za-z])'), #This accounts for the fact that many people (myself included) use two spaces after punctuation.  However, there is a bug here that makes two spaces after a quote acceptable.  Unless it gets reported, I don't care.
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
            "re": re.compile(u' ([a-z]+) \\1([ .!?,:;])', re.IGNORECASE),
            "fix": ' \\1\\2' }]
    
    
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
        """Perform the highlighting"""
        if not self.dict:
            return
    
        text = unicode(text)

        #Spellcheck
        words = re.finditer(self.WORDS, text)
        matches = [word_object for word_object in words if not self.dict.check(word_object.group(1))]
        for word_object in matches:
                self.setFormat(word_object.start(), (word_object.end() - len(word_object.group(2))) - word_object.start(), self.format_spelling)

        if not platformSettings.getSetting("grammarcheck", True):
            return
        #Grammar
        for rule in self.corrections:
            for word_object in re.finditer(rule["re"], text):
                    self.setFormat(word_object.start(), word_object.end() - word_object.start(), self.format_grammar)

    def getDescriptionText(self, pos, text):
        """Given a grammar mistake, figure out what the mistake was"""
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
