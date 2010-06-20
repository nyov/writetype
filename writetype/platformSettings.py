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


from PyQt4.QtCore import QSettings, QVariant, QLocale
from ConfigParser import SafeConfigParser
import os
import sys

prefix = os.path.join(sys.prefix, 'share', 'writetype')
if not os.path.exists(prefix):
	prefix = os.path.join(os.path.dirname(__file__), "..")
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
	elif key == "basePath":
		return prefix
	elif key == "language":
		language = str(QLocale.system().name())
		return language



	return parser.get('General', key)

def getSetting(key, default=None):
	if key in cache: #Check to see if it is in the cache
		return correctType(cache[key], default)
	else:
		if settingsError == False:
			val = settingsHandle.value(key, QVariant(default))
#			val = val.toPyObject()
			#Dynamic type casting to the default's type
			cache[key] = val
			return correctType(val, default)
		else:
			return default

def correctType(val, default):
	if isinstance(default, bool):
		val = val.toBool()
	elif isinstance(default, int):
		val = val.toInt()[0]
	elif isinstance(default, str):
		val = str(val.toString())
	elif isinstance(default, float):
		val = val.toFloat()
	else:
		val = val.toPyObject()
	return val

def setSetting(key, value):
	if settingsError == False:
		settingsHandle.setValue(key, value)
		cache[key] = QVariant(value)
	else:
		print "Settings error!  Setting not saved!"
