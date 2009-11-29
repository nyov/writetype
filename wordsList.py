from platformSettings import platformSettings

class wordsList:
	def __init__(self):
		self.filename = platformSettings.pathToStandardWords
		self.refreshWords()
		self.refreshWordsCustom()
		#self.words = self.bubbleSort(self.words)
	def refreshWords(self):
		self.words = self.loadWords(platformSettings.pathToStandardWords)
	def refreshWordsCustom(self):
		self.wordsCustom = self.loadWords(platformSettings.pathToCustomWords)
		print "refreshing"
	def loadWords(self, filePath):
		fileHandle = open(filePath, 'r')
		return fileHandle.read().split("\n")
		
	def bubbleSort(self, tosort):
		print "Sorting words in list"
		i = 1
		while i > 0:
			i = 0
			for num in range(1, len(tosort)-1):
				if cmp(tosort[num], tosort[num-1]) < 0:
					tmp = tosort[num]
					tosort[num] = tosort[num-1]
					tosort[num-1] = tmp
					i += 1
		print "Done sorting list.  Continuing."
		return tosort
	def search(self, firstLetters, customWords=False):
		if customWords:
			wordsList = self.wordsCustom
		else:
			wordsList = self.words
		results = []
		print firstLetters.lower()
		for num in range(0, len(wordsList)):
			if wordsList[num].find(firstLetters.lower()) == 0:
				results.append(wordsList[num])
				print firstLetters.lower()+'*'+' '+ wordsList[num]

		return results