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

#Stupid Windows.
if hasattr(sys, "frozen"):
	path = os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding( )))
else:
	path = os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))
	
prefix = os.path.join(path, "..")
if not os.path.isfile(os.path.join(prefix, "platformSettings.ini")):
	prefix = os.path.join(sys.prefix, 'share', 'writetype')
	if not os.path.isfile(os.path.join(prefix, "platformSettings.ini")):
		raise IOError("PlatformSettings not found!")
	print "setting intallation prefix"

#Some defines
parser = SafeConfigParser()
parser.read(os.path.join(prefix, 'platformSettings.ini'))
cache = {} #A dictionary for normal settings cache
pCache = {} #Platform settings cache
settingsHandle = QSettings("BernsteinForPresident", "WriteType")

#Global Overrides
for key,value in parser.items("GlobalOverride"):
	cache[str(key)] = QVariant(value)

def getPlatformSetting(key):
	"""Get a core setting, either hard-coded, dynamically created,
	or specified in platformsettings.ini"""
	if key in pCache:
		return pCache[key]
	global prefix
	if key == "pathToWordlists":
		return os.path.join(prefix, 'wordlists')
	elif key == "pathToRes":
		return os.path.join(prefix, 'res')
	elif key == "basePath":
		return prefix
	elif key == "pathToEspeak":
		path = parser.get('General', key)
		path = path.replace("[wt]", prefix)
		print path
		return path
	elif key == "language":
		language = str(QLocale.system().name())
		return language

	return parser.get('General', key)

def getSetting(key, default=None):
	"""Get a setting specified in the settings dialog box"""
	if key in cache: #Check to see if it is in the cache
		return correctType(cache[key], default)
	else:
		val = settingsHandle.value(key, QVariant(default))
		#val = val.toPyObject()
		#Dynamic type casting to the default's type
		cache[key] = val
		return correctType(val, default)


def correctType(val, default):
	"""Make sure the QVariant is cast to the right type"""
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
	"""Set a setting, probably from the settings box"""
	settingsHandle.setValue(key, QVariant(value))
	cache[key] = QVariant(value)

def setPSettingTmp(key, value):
	"""Set a temporary value for a platform setting"""
	pCache[key] = value

def setSettingTmp(key, value):
	"""Set a temporary value for a normal setting"""
	cache[key] = QVariant(value)
