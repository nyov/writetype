from platformSettings import platformSettings
from sys import getrecursionlimit, setrecursionlimit

class wordsList:
	def __init__(self):
		self.refreshWords()
		self.refreshWordsCustom()

	def refreshWords(self):
		self.words = self.loadWords(platformSettings.pathToWordlists + "/list" + str(platformSettings.getSetting("wordlist", 2).toString()) + ".txt")
	def refreshWordsCustom(self):
		self.wordsCustom = str(platformSettings.getSetting("customwords", "").toString()).split("\n")
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
