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
import pyttsx
from threading import Thread, Event
from PyQt4.QtGui import QMessageBox


class PyttsxInterface(TtsInterface):
    def __init__(self, rate=0):
        self.rate = rate
        self.stopEvent = Event()
    def speak(self, text):
        self.st = SpeakerThread(text, self.stopEvent, self.rate)
        self.st.start()

    def stop(self):
        self.stopEvent.set()

    def setReadingSpeed(self, rate):
        self.rate = rate

class SpeakerThread(Thread):
    def __init__(self, text, stopEvent, rate=0):
        self.rate = 200 + rate
        self.stopEvent = stopEvent
        self.text = text
        Thread.__init__(self)

    def run(self):
        def onWord(name, location, length):
            print "in subroutine"
            if self.stopEvent.isSet():
                speaker.stop()
        speaker = pyttsx.init()
        speaker.connect('started-word', onWord)
        speaker.setProperty('rate', self.rate)
        speaker.say(self.text)
        speaker.runAndWait()
