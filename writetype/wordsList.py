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


from platformSettings import getSetting, getPlatformSetting
from os import path
from xml.dom import minidom
import codecs
import logger
from PyQt4.QtCore import QCoreApplication

class WordsList:
    """Interface to the dirty work of searching for word
    suggestions and autocorrections"""

    NOSORT = 1
    SORT = 2
    NORMAL_WORDS = 1
    CUSTOM_WORDS = 2
    

    def __init__(self):
        #List of all words
        self.words = []
        #List of words added during runtime
        self.wordsCustom = []
        #A dictionary, indexed by word, of each word's weight
        self.weights = {}
        #Given the letter of the index, the first word in self.words
        #that starts with this letter
        self.wordsIndex = {}
        self.loadWords()
        self.refreshReplacementTable()
        self.pattern = WordPattern()

    def loadWords(self):
        """Loads the words from the list files, as well as the custom
        words, into the self.words list.  This is a massive list in
        the form of (word, weight), where weight is the sorting
        weight.  A higher weight means it is sorted higher in the
        list."""
        #If refreshing after saving the settings dialog, keep the weights through the dump
        dump = self.dump()
        self.words = []
        #Find the path to the wordlist file.  If it isn't available, find the closest size
        filename = "blank.txt"
        dom = minidom.parse(path.join(getPlatformSetting('basePath'), 'wordlists', 'wordlists.xml'))
        for node in dom.getElementsByTagName("wordlist"):
            if getPlatformSetting("language").startswith(node.getAttribute("lang")):
                filename = node.getAttribute('file')
                if node.getAttribute("id") == getSetting("wordlist", "3"):
                    break
                    
        wordspath = path.join(getPlatformSetting('basePath'), 'wordlists', filename)
        #Load the wordlist from that file
        logger.log("Loading words from " + wordspath)
        try:
            fileHandle = codecs.open(wordspath, 'r', encoding='utf-8')
            wordslist = fileHandle.read().split("\n")
            fileHandle.close()
        except IOError:
            logger.log("Could not load word list.  Language not available.  Using a blank.", logtype="Error", tb=True)
            wordslist = ""
        for word in wordslist:
            if word != u"":
                self.words.append(unicode(word))
                self.weights[unicode(word)] = 0
        #Now load the words from the settings dialog
        settingswords = getSetting("customwords", "").lower().split("\n")
        for word in settingswords:
            if word != "" and not word in self.words:
                self.words.append(word)
                self.weights[word] = int(getPlatformSetting("defaultWordWeight"))
        self.words.sort()

        #Build a dictionary of word positions, by first letter, to
        #make searching faster.  So a=1, b=34 if the first word
        #starting with a b occurs at position 34 in the list
        i = 0
        lastletter = ""
        while i < len(self.words):
            lastletter = self.words[i][0]
            self.wordsIndex[lastletter] = i
            while lastletter == self.words[i][0]:
                i += 1
                if i >= len(self.words)-1:
                    break

        self.loadDump(dump)

    def _nextLetter(self, char):
        """Return the next letter in the alphabet.  Returns "{" after "z"."""
        return chr(ord(char.lower())+1)

    def addCustomWord(self, word, weight=1):
        """Add a new word to the list of words, or increment the weight by weight"""
        word = unicode(word).lower()
        if word in self.words + self.wordsCustom:
            self.weights[word] = self.weights[word] + weight
        else:
            self.wordsCustom.append(word)
            self.weights[word] = weight
            self.wordsCustom.sort()
            

    #WORD COMPLETION FUNCTIONS

    def search(self, firstLetters):
        """Search through self.words for a word that starts with
        firstLetters.  firstLetters can also be a tuple."""
        results = []
        if type(firstLetters) in [str, unicode]:
            firstLetters = firstLetters.lower()
            #This will speed things up in most cases, but I don't want
            #to take up the memory to index all the unicode
            #characters, so when it doesn't work, it will fail
            #silenty.
            try:
                searchlist = self.words[self.wordsIndex[firstLetters[0]]:self.wordsIndex[self._nextLetter(firstLetters[0])]]
            except (KeyError, IndexError):
                searchlist = self.words
        else:
            #It's a tuple
            flset = set()
            for word in firstLetters:
                flset.add(word[0])
            #This will also fail for some letters.  Let's not bother
            #with those, because the performance difference should be
            #negligible. 
            try:
                searchlist = []
                for fl in flset:
                    searchlist += self.words[self.wordsIndex[fl]:self.wordsIndex[self._nextLetter(fl)]]
            except (KeyError, IndexError):
                searchlist = self.words

        results = filter(lambda x:x.startswith(firstLetters), searchlist)
        results += filter(lambda x:x.startswith(firstLetters), self.wordsCustom)
        #results = [w for w in self.words if w.startswith(fllower)]
        #results = += [w for w in self.wordsCustom if w.startswith(fllower)]
        tuples = []
        results.sort()
        for result in results:
            tuples.append((result, self.weights[result]))
        return tuples
   


    def dump(self):
        """Dump all of the words with some weight into a csv"""
        dump = ""
        for word in self.words + self.wordsCustom:
            if self.weights[word] > 0:
                dump += ''.join([word, ',', unicode(self.weights[word]), "\n"])
        return dump

    def loadDump(self, dump):
        """Take a csv dump file and merge it into the current words list"""
        dumplist = dump.split("\n")
        for word in dumplist:
            if word:
                splitword = word.split(',')
                self.addCustomWord(splitword[0], int(splitword[1]))


    #AUTOCORRECTION

    def refreshReplacementTable(self):
        """Reload the list of autoreplacements from the settings box"""
        self.replacementTable = {}
        if not getSetting('autocorrection'):
            return
        if getSetting('autocorrectioncontractions', True):
            fileHandle = open(path.join(getPlatformSetting('pathToWordlists'), "replacements.txt"), 'r')
            autocorrections = fileHandle.read().split("\n")
            for line in autocorrections:
                if not line or line == ",": continue
                self.replacementTable[line.split(",")[0]] = line.split(",")[1]
        for line in str(getSetting("customautocorrections", "")).split("\n"):
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
    #TODO - Clean this class up... how does this even run it's so ugly?
    def __init__(self):
        #Words are the index to a sub-dictionary, with the word indexed to frequency
        self.words = []
        self.lastcheckedword = ""

    def _cleanString(self, s):
        #s = s.lower()
        s = s.strip(".,!?;: \t\n")
        return s

    def insertLink(self, first, second):
        """Insert the word order link into the data structure"""
        first = self._cleanString(first)
        second = self._cleanString(second)
        secondNode = [n for n in self.words if n.word == second]
        firstNode = [n for n in self.words if n.word == first]
        if not secondNode:
            secondNode = LinkNode(second)
            self.words.append(secondNode)
        else:
            secondNode = secondNode[0]
        if not firstNode:
            firstNode = LinkNode(first)
            self.words.append(firstNode)
        else:
            firstNode = firstNode[0]
        firstNode.addLink(secondNode)
        logger.log("Added link from ", first, " to ", second)


    def getLinks(self, word):
        """Return a list of tuples (word, frequency) of words that come
        after the requested word"""
        word = self._cleanString(word)
        if self.lastcheckedword and word:
            self.insertLink(self.lastcheckedword, word)
        self.lastcheckedword = word
        
        #if not word in self.words:
        #    return []

        node = [n for n in self.words if n.word == word]
        if not node:
            return []
        return node[0].getLinks()

    def clearLastCheckedWord(self):
        self.lastcheckedword = None

    def dump(self):
        dump = u""
        for word in self.words:
            dump += word.dumpToCsvLine()
        return dump

    def loadDump(self, csv):
        lines = csv.split("\n")
        for line in lines:
            vals = line.split(',')
            vals.reverse()
            first = vals.pop()
            while vals:
                second = vals.pop()
                w = int(vals.pop())
                for i in range(0,w-1):
                    self.insertLink(first, second)
        
class LinkNode:
    #TODO - Clean this class up also

    WORDS_THRESHOLD = 1 #How many links before it suggests a phrase completion

    def __init__(self, word):
        self.word = word
        self.links = []

    def addLink(self, node, weight=1):
        result = [(n,w) for n,w in self.links if n.word == node.word]
        if not result:
            self.links.append((node, weight))
        else:
            index = self.links.index(result[0])
            self.links[index] = (node, result[0][1]+weight)

    def getLinks(self, preappend="", i=0):
        finallist = []
        finallist.extend([(preappend+n.word, w) for n,w in self.links if w>self.WORDS_THRESHOLD])
        for link in [(n,w) for (n,w) in self.links if w-i>self.WORDS_THRESHOLD]:
            finallist.extend(link[0].getLinks(preappend+link[0].word+" ", i+1))
        return finallist

    def dumpToCsvLine(self):
        """Converts the object into a CSV line, in the format of:
        word, link1, link1-weight, link2, link2-weight, etc."""
        links = []
        for link in self.links:
            links += [',', link[0].word, ',', str(link[1])]
        return u''.join([self.word] + links + ["\n"])
