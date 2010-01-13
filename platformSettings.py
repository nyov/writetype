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


from PyQt4.QtCore import QSettings
#Some defines
class platformSettings:
	
	#default open directory
	defaultOpenDirectory = "/home/max/My Scripts/"
	pathToRes = "res"
	pathToWordlists = "wordlists"
	statsUrl = "http://BernsteinForPresident.com/writetypelog.php"
	
	language = "en_US"
	
	@staticmethod
	def getSetting(key, default=None):
		settingsHandle = QSettings("BernsteinForPresident", "WriteType")
		return settingsHandle.value(key, default)
	@staticmethod
	def setSetting(key, value):
		settingsHandle = QSettings("BernsteinForPresident", "WriteType")
		settingsHandle.setValue(key, value)
		