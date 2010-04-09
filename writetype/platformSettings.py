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


from PyQt4.QtCore import QSettings, QVariant
from ConfigParser import SafeConfigParser
import os
import sys

prefix = os.path.join(sys.prefix, 'share', 'writetype')
if not os.path.exists(prefix):
	prefix = ".."
	print "setting prefix"
print "passed path"

#Some defines
try:
	parser = SafeConfigParser()
	
	parser.read(os.path.join(prefix, 'platformSettings.ini'))
	cache = {} #A dictionary
	settingsHandle = QSettings("BernsteinForPresident", "WriteType")
	settingsError = False
except:
	print "Error loading settings file!"
	settingsError = True
def getPlatformSetting(key):
	global prefix
	if key == "pathToWordlists":
		return os.path.join(prefix, 'wordlists')
	elif key == "pathToRes":
		return os.path.join(prefix, 'res')

	return parser.get('General', key)

def getSetting(key, default=None):
	
	if key in cache: #Check to see if it is in the cache
		return QVariant(cache[key]) #Why doesn't it store as a QVariant in the first place?
	else:
		if settingsError == False:
			val = settingsHandle.value(key, default)
			cache[key] = val
			return val
		else:
			return QVariant(default)

def setSetting(key, value):
	if settingsError == False:
		settingsHandle.setValue(key, value)
		cache[key] = value
