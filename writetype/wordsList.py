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


import platformSettings
from os import path
from xml.dom import minidom
import codecs

class WordsList:
    """Interface to the dirty work of searching for word
    suggestions and autocorrections"""

    NOSORT = 1
    SORT = 2
    NORMAL_WORDS = 1
    CUSTOM_WORDS = 2

    def __init__(self):
        self.refreshWords()
        self.refreshWordsCustom()
        self.refreshReplacementTable()
        self.pattern = WordPattern()

    #WORD COMPLETION FUNCTIONS

    def refreshWords(self):
        """Reload the list of words from which suggestions are found"""
        dom = minidom.parse(path.join(platformSettings.getPlatformSetting('basePath'), 'wordlists', 'wordlists.xml'))
        self.words = []
        #It will be empty if it wasn't found, just like we want
        for node in dom.getElementsByTagName("wordlist"):
            if node.getAttribute("lang") == platformSettings.getPlatformSetting("language") and node.getAttribute("id") == platformSettings.getSetting("wordlist", "4"):
                self.words = self.loadWords(path.join(platformSettings.getPlatformSetting('basePath'), 'wordlists', node.getAttribute('file')))
                break

    def refreshWordsCustom(self):
        """Reload the words specified in the settings box, and give them a default weight of 5"""
        customwords = platformSettings.getSetting("customwords", "").lower().split("\n")
        wordsfinal = []
        for word in customwords:
            wordsfinal.append((word, 5)) 
        self.words += wordsfinal

    def loadWords(self, filePath):
        """Used by loading functions to load all of the words from the wordlist into memory"""
        print "Loading words"
        fileHandle = codecs.open(filePath, 'r', encoding='utf-8')
        words = fileHandle.read().split("\n")
        finalwords = []
        for word in words:
            finalwords.append((word, 0))
        return finalwords

    def addCustomWord(self, word):
        """Add a new word to the list of words, or increment the weight by 1"""
        word = unicode(word).lower()
        match = [(w,s) for w,s in self.words if w == word]
        if match:
            w,s = match[0]
            pos = self.words.index((w,s))
            self.words[pos] = (w,s+1)
        else:
            self.words.append((word, 1))
            self.words.sort(lambda x,y : cmp(x[0], y[0]))
   
    def search(self, firstLetters, customWords=NORMAL_WORDS, sort=NOSORT):
        """Search for a word in the list of words"""
        if customWords == self.CUSTOM_WORDS:
            wordsList = self.wordsCustom
        else:
            wordsList = self.words
        results = []
        #results = filter(lambda x:x[0].startswith(firstLetters.lower()), wordsList)
        fllower = firstLetters.lower();
        results = [(w,s) for w,s in wordsList if w.startswith(fllower)]
        if sort == self.SORT:
            return results
        results.sort(lambda x,y : cmp(x[0], y[0]))
        return results

    #AUTOCORRECTION

    def refreshReplacementTable(self):
        """Reload the list of autoreplacements from the settings box"""
        self.replacementTable = {}
        if not platformSettings.getSetting('autocorrection'):
            return
        if platformSettings.getSetting('autocorrectioncontractions', True):
            fileHandle = open(path.join(platformSettings.getPlatformSetting('pathToWordlists'), "replacements.txt"), 'r')
            autocorrections = fileHandle.read().split("\n")
            for line in autocorrections:
                if not line or line == ",": continue
                self.replacementTable[line.split(",")[0]] = line.split(",")[1]
        for line in str(platformSettings.getSetting("customAutocorrections", "")).split("\n"):
            print line
            if not line or line == ",": continue
            self.replacementTable[line.split(",")[0]] = line.split(",")[1]

    def correctWord(self, word):
        """Return the autocorrected form of a word"""
        if word.strip().lower() in self.replacementTable:
            return self.replacementTable[word.strip().lower()]
        else:
            return False
        

class WordPattern:
    """Keeps track of which words are generally typed after
    other words.  For instance, I generally type 'Shinn'
    after I type 'Max' and 'software' after I type 'free'."""
    def __init__(self):
        #Words are the index to a sub-dictionary, with the word indexed to frequency
        self.words = {}
        self.lastcheckedword = ""

    def _cleanString(self, s):
        s = s.lower()
        s = s.strip(".,!?;: \t\n")
        return s

    def insertLink(self, first, second):
        """Insert the word order link into the data structure"""
        first = self._cleanString(first)
        second = self._cleanString(second)
        if not first in self.words:
            self.words[first] = {}
        if second in self.words[first]:
            freq = self.words[first][second]
            self.words[first][second] = freq + 1
        else:
            self.words[first][second] = 1

    def getLinks(self, word):
        """Return a list of tuples (word, frequency) of words that come
        after the requested word"""
        word = self._cleanString(word)
        if self.lastcheckedword and word:
            self.insertLink(self.lastcheckedword, word)
        self.lastcheckedword = word
        
        if not word in self.words:
            return []
        returnlist = []
        print self.words
        for key, value in self.words[word].iteritems():
            returnlist.append((key, value))
            for k, v in self.words[key].iteritems():
                if v > 3:
                    returnlist.append((key + " " + k, v-3))
        return returnlist
