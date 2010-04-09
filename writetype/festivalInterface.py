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

class FestivalInterface:
	def __init__(self, executableName, libPath=None):
		self.executableName = executableName
		self.libPath = libPath
	def speak(self, text):
		call = [self.executableName, "--tts", "-"]
		if self.libPath:
			call.append("--libpath")
			call.append(self.libPath)
		self.proc = subprocess.Popen(call, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
		stdout, stderr = self.proc.communicate(input=text)