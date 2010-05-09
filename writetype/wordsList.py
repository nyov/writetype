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
from sys import getrecursionlimit, setrecursionlimit
from os import path

class wordsList:
	def __init__(self):
		self.refreshWords()
		self.refreshWordsCustom()
		self.refreshReplacementTable()

	def refreshWords(self):
		self.words = self.loadWords(platformSettings.getPlatformSetting('pathToWordlists') + "/list" + str(platformSettings.getSetting("wordlist", 2)) + ".txt")

	def refreshWordsCustom(self):
		self.wordsCustom = str(platformSettings.getSetting("customwords", "")).split("\n")

	def refreshReplacementTable(self):
		self.replacementTable = {}
		if not platformSettings.getSetting('autocompletion'):
			return
		if platformSettings.getSetting('autocompletioncontractions'):
			for line in self.loadWords(path.join(platformSettings.getPlatformSetting('pathToWordlists'), "replacements.txt")):
				if not line or line == ",": continue
				self.replacementTable[line.split(",")[0]] = line.split(",")[1]
		for line in str(platformSettings.getSetting("customAutocompletions", "")).split("\n"):
			print line
			if not line or line == ",": continue
			self.replacementTable[line.split(",")[0]] = line.split(",")[1]

	def loadWords(self, filePath):
		fileHandle = open(filePath, 'r')
		return fileHandle.read().split("\n")

	def addCustomWord(self, word):
		word = word.lower()
		if not word in self.wordsCustom:
			self.wordsCustom = self.mergesort(self.wordsCustom, word)
		if word in self.words:
			self.words.pop(self.words.index(word))

	@staticmethod
	def quicksort(tosort):
		if len(tosort) == 0:
			return []
		if len(tosort) == 1:
			return tosort
		if len(tosort) == 2:
			if tosort[0] <= tosort[1]:
				return tosort
			else:
				return [tosort[1], tosort[0]]
		if(getrecursionlimit() < len(tosort)):
			setrecursionlimit(len(tosort))
		pivot = tosort.pop()
		list1 = []
		list2 = []
		while tosort != []:
			item = tosort.pop()
			if item <= pivot:
				list1.append(item)
			else:
				list2.append(item)
		return wordsList.quicksort(list1) + [pivot] + wordsList.quicksort(list2)
	
	@staticmethod
	def mergesort(baselist, mergelist):
		if not type(mergelist) == type([]):
			mergelist = [mergelist]
		#This assumes the base list is already sorted - no need to bother checking otherwise.
		for i in range(0, len(mergelist)):
			for j in range(0, len(baselist)):
				set = False
				if baselist[j] > mergelist[i]:
					baselist = baselist[:j] + [mergelist[i]] + baselist[j:]
					set = True
					break
			if not set:
				baselist += [mergelist[i]]
		return baselist
	
	def search(self, firstLetters, customWords=False, noSort=False):
		if customWords:
			wordsList = self.wordsCustom
		else:
			wordsList = self.words
		results = []
		results = filter(lambda x:x.startswith(firstLetters.lower()), wordsList)
		#for num in range(0, len(wordsList)):
			#if wordsList[num].find(firstLetters.lower()) == 0:
				#results.append(wordsList[num])
		if noSort:
			return results
		return self.quicksort(results)

	def correctWord(self, word):
		if word.strip().lower() in self.replacementTable:
			return self.replacementTable[word.strip().lower()]
		else:
			print "'" + word + "'"
			return False
		
