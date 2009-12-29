from PyQt4.QtCore import QSettings
#Some defines
class platformSettings:
	
	#default open directory
	defaultOpenDirectory = "/home/max/My Scripts/"
	pathToRes = "res"
	pathToWordlists = "wordlists"
	
	language = "en_US"
	
	@staticmethod
	def getSetting(key, default=None):
		settingsHandle = QSettings("BernsteinForPresident", "WriteType")
		return settingsHandle.value(key, default)
	@staticmethod
	def setSetting(key, value):
		settingsHandle = QSettings("BernsteinForPresident", "WriteType")
		settingsHandle.setValue(key, value)
		