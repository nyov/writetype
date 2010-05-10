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

from festivalInterface import FestivalInterface
import platformSettings
import re
from platform import system

#This will do more in the future... I guess...
class Speaker:
	def __init__(self, text):
		self.setDriver()
		#self.text = text
		#threading.Thread.__init__(self)

	def say(self, text):
		print "selecting driver"
		if self.driver == "festival":
			print "festival"
			text = str(text)
			self.ttsdriver.stop()
			#Do some things to make text sound more realistic
			while text.find('"') != text.rfind('"'):
				text = text.replace('"', "<PITCH BASE='20%'>", 1)
				text = text.replace('"', "</PITCH>", 1)
				print text
			text = text.replace("\n", '<BREAK LEVEL="large" />')
			text = re.sub(re.compile(re.escape("writetype"), re.I), '<PRON SUB="right type">writetype</PRON>', text, 0)
			#Set the speed to the user preference
			speed = platformSettings.getSetting("readingspeed", 0)
			text = '<RATE SPEED="' + str(speed) + '%">' + text + "</RATE>"
			self.ttsdriver.speak("<SABLE>"+text+"</SABLE>")

		elif self.driver == "pyttsx":
			print "pyttsx"
			text = str(text)
			self.ttsdriver.setReadingSpeed(platformSettings.getSetting("readingspeed", 0))
			self.ttsdriver.speak(text)
			
	def stop(self):
   		self.ttsdriver.stop()

	def setDriver(self, driver=None):
		if not driver:
			driver = platformSettings.getSetting("ttsengine", "")

		self.driver = driver
		#Defaults per platform
		if not self.driver in platformSettings.getPlatformSetting("ttsEngines"):
			print "Driver error!  Driver not found!  Selecting default."
			if system() == "Linux":
				self.driver = "festival"
			else:
				self.driver = "pyttsx"
		#Import
		if self.driver == "festival":
			from festivalInterface import FestivalInterface
			self.ttsdriver = FestivalInterface(platformSettings.getPlatformSetting("pathToFestival"))
		elif self.driver == "pyttsx":
			from pyttsxInterface import PyttsxInterface
			self.ttsdriver = PyttsxInterface() # This will make a bug, I'll fix it later
