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

#This will do more in the future... I guess...
class Speaker:
	def __init__(self, text):
		self.festival = FestivalInterface(platformSettings.getPlatformSetting("pathToFestival"))
		#self.text = text
		#threading.Thread.__init__(self)

	def say(self, text):
		text = str(text)
		self.festival.stop()
		#Do some things to make text sound more realistic
		while text.find('"') != text.rfind('"'):
			text = text.replace('"', "<PITCH BASE='20%'>", 1)
			text = text.replace('"', "</PITCH>", 1)
			print text
		text = text.replace("\n", '<BREAK LEVEL="large" />')
		text = re.sub(re.compile(re.escape("writetype"), re.I), '<PRON SUB="right type">writetype</PRON>', text, 0)
		#Set the speed to the user preference
		speed = platformSettings.getSetting("readingspeed", 100)
		text = '<RATE SPEED="' + str(speed) + '%">' + text + "</RATE>"
		self.festival.speak("<SABLE>"+text+"</SABLE>")

	def stop(self):
		self.festival.stop()
