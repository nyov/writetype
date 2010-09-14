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
import re
from platform import system

#This will do more in the future... I guess...
class Speaker:
	def __init__(self, text):
		self.setDriver()
		#self.text = text
		#threading.Thread.__init__(self)

	def say(self, text):
		text = unicode(text)
		#Sanitize input
		text.replace("<", "")
		text.replace(">", "")
		print "selecting driver"
		if self.driver == "festival":
			print "festival"
			self.ttsdriver.stop()
			#Do some things to make text sound more realistic
			while text.find('"') != text.rfind('"'):
				text = text.replace('"', "<PITCH BASE='20%'>", 1)
				text = text.replace('"', "</PITCH>", 1)
				print text
			text = '<LANGUAGE ID="' + platformSettings.getPlatformSetting("language")[0:2] + '">' + text + '</LANGUAGE>'
			text = text.replace("\n", '<BREAK LEVEL="large" />')
			text = re.sub(re.compile(re.escape("writetype"), re.I), '<PRON SUB="right type">writetype</PRON>', text, 0)
			#Set the speed to the user preference
			speed = platformSettings.getSetting("readingspeed", 0)
			text = '<RATE SPEED="' + str(speed) + '%">' + text + "</RATE>"
			print text
			self.ttsdriver.speak(u"<SABLE>"+unicode(text)+u"</SABLE>")

		elif self.driver == "espeak":
			print "espeak"
			self.ttsdriver.stop()
			#Do some things to make text sound more realistic
			while text.find('"') != text.rfind('"'):
				text = text.replace('"', '<prosody pitch="+20%">', 1)
				text = text.replace('"', "</prosody>", 1)
				print text
			text = text.replace("\n", '.<break strength="x-large" time="1s" />')
			text = re.sub(re.compile(re.escape("writetype"), re.I), 'write type', text, 0)
			#Set the speed to the user preference
			speed = platformSettings.getSetting("readingspeed", 0)
			text = unicode('<prosody rate="' + unicode(speed) + '%">' + text + "</prosody>")
			print text
			self.ttsdriver.speak("<speak xml:lang=\""+platformSettings.getPlatformSetting("language").replace('_', '-')+"\">"+text+"</speak>")

		elif self.driver == "pyttsx":
			print "pyttsx"
			self.ttsdriver.setReadingSpeed(platformSettings.getSetting("readingspeed", 0))
			self.ttsdriver.speak(text)
		else:
			return True
			
	def stop(self):
   		self.ttsdriver.stop()

	def setDriver(self, driver=None):
		if not driver:
			driver = platformSettings.getSetting("ttsengine", "")

		self.driver = driver
		#Defaults per platform
		if not self.driver:
			print "Driver error!  Driver not found!  Selecting default."
			if system() == "Linux":
				self.driver = "festival"
			else:
				self.driver = "pyttsx"
		#Import
		try:
			if self.driver == "festival":
				from festivalInterface import FestivalInterface
				self.ttsdriver = FestivalInterface(platformSettings.getPlatformSetting("pathToFestival"))
			elif self.driver == "pyttsx":
				from pyttsxInterface import PyttsxInterface
				self.ttsdriver = PyttsxInterface() # This will make a bug, I'll fix it later
			elif self.driver == "espeak":
				from espeakInterface import EspeakInterface
				self.ttsdriver = EspeakInterface(platformSettings.getPlatformSetting("pathToEspeak"))
		except ImportError:
			from .ttsInterface import TtsInterface
			self.ttsdriver = TtsInterface()
			self.driver = "null"
			print "===========ERROR!===========\nInvalid TTS Driver\nRunning without TTS support"
			
