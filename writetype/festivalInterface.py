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

import subprocess
from tempfile import mkstemp
from os import unlink

class FestivalInterface:
	def __init__(self, executableName, libPath=None):
		self.executableName = executableName
		self.libPath = libPath
## 	def speak(self, text):
## 		call = [self.executableName, "--tts", "-"]
## 		if self.libPath:
## 			call.append("--libpath")
## 			call.append(self.libPath)
## 		self.proc = subprocess.Popen(call, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
## 		stdout, stderr = self.proc.communicate(input=text)

	#Doing it this way will give more flexibility in incorporating SABLE
	def speak(self, text):
		tmpfile = mkstemp(suffix=".sable", prefix="wt_")
		print tmpfile
		tmpfileHandle = open(tmpfile[1], 'w')
		tmpfileHandle.write("<SABLE>"+text+"</SABLE>")
#		tmpfileHandle.close()
		call = [self.executableName, "--tts", tmpfile[1]]
 		self.proc = subprocess.Popen(call)
		
#		unlink(tmpfile[1])


fi = FestivalInterface("festival")
fi.speak("hello <BREAK />world")