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
from os import unlink
from PyQt4.QtGui import QMessageBox
import codecs
from PyQt4.QtCore import QCoreApplication
import os

class EspeakInterface(TtsInterface):
    def __init__(self, executableName):
        self.executableName = executableName
        self.proc = None
        self.tmpPaths = []

    def __del__(self):
        print "destructor"
        for path in self.tmpPaths:
            print "removing " + str(path[1])
            unlink(path[1])

    def speak(self, text):
        tmpfile = mkstemp(suffix=".ssml", prefix="wt_")
        self.tmpPaths.append(tmpfile)
        print text
        tmpfileHandle = codecs.open(tmpfile[1], 'w', encoding="utf-8")
        tmpfileHandle.write(text)
        tmpfileHandle.close()
        call = [self.executableName, "-m", "-f", tmpfile[1]]
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
        try:
            self.proc = subprocess.Popen(call, startupinfo=startupinfo)
        except OSError:
            QMessageBox.warning(None, QCoreApplication.translate("EspeakInferface", "Feature unavailable"), QCoreApplication.translate("EspeakInterface", "eSpeak is not installed on this computer.  To use this feature, please install eSpeak or select a new TTS driver in the Settings box."))
        
    def stop(self):
        if self.proc:
            try:
                self.proc.terminate()
            except WindowsError:
                pass
