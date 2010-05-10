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

import pyttsx
from threading import Thread, Event

class pyttsxInterface:
    def speak(self, text):
        self.stopEvent = Event()
        self.st = SpeakerThread(text, self.stopEvent)

    def stop(self):
        self.stopEvent.set()

class SpeakerThread(Thread):
    def __init__(self, text, stopEvent):
        self.stopEvent = stopEvent
        self.text = text
        threading.Thread.__init__(self)

    def run(self):
        def onWord(name, location, length):
            if self.stopEvent.isSet():
                speaker.stop()
        speaker = pyttsx.init()
        speaker.say(self.text)
        speaker.runAndWait()
                
if __name__ == "__main__":
    interface = pyttsxInterface()
    interface.speak("Hello, this should take some time to say.")
