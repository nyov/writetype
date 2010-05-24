#!/usr/bin/python
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

from ttsInterface import TtsInterface
import subprocess
from tempfile import mkstemp
from os import unlink, uname
from PyQt4.QtGui import QMessageBox

class EspeakInterface(TtsInterface):
	def __init__(self, executableName):
		self.executableName = executableName
		self.proc = None

	def speak(self, text):
		tmpfile = mkstemp(suffix=".ssml", prefix="wt_")
		print tmpfile
		tmpfileHandle = open(tmpfile[1], 'w')
		tmpfileHandle.write(text)
		tmpfileHandle.close()
		call = [self.executableName, "-m", "-f", tmpfile[1]]
		try:
			self.proc = subprocess.Popen(call)
		except OSError:
			QMessageBox.warning(None, self.tr("Feature unavailable", "eSpeak is not installed on this computer.  To use this feature, please install eSpeak or select a new TTS driver in the Settings box."))
		
	def stop(self):
		if self.proc:
			self.proc.terminate()



