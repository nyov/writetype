# Copyright 2010, 2011 Max Shinn

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
import logger

# This serves as a common interface to all of the text to speech
# backend drivers.
class Speaker:
    def __init__(self, text):
        self.setDriver()
        #self.text = text
        #threading.Thread.__init__(self)

    def say(self, text):
        """Speak the selected text"""
        text = unicode(text)
        #Sanitize input
        text.replace("<", "")
        text.replace(">", "")
        if self.driver == "festival":
            logger.log("Festival driver speaking")
            self.ttsdriver.stop()
            self.ttsdriver.speak(self.addSableMarkup(text))

        elif self.driver == "espeak":
            logger.log("Espeak driver speaking")
            self.ttsdriver.stop()
            self.ttsdriver.speak(self.addSsmlMarkup(text))

        elif self.driver == "pyttsx":
            logger.log("Pyttsx driver speaking")
            self.ttsdriver.setReadingSpeed(platformSettings.getSetting("readingspeed", 0))
            self.ttsdriver.speak(text)
        else:
            logger.log("No driver selected", logtype="Info")
            return True 
           
    def stop(self):
        """Try to stop speaking the text"""
        self.ttsdriver.stop()

    def setDriver(self, driver=None):
        """Init the selected driver, or the suggested driver for the platform"""
        if not driver:
            driver = platformSettings.getSetting("ttsengine", "")
            
        self.driver = driver
        availableEngines = platformSettings.getPlatformSetting("ttsEngines").split(",")
        availableEngines.append("null")
        #Defaults per platform
        if not self.driver:
            logger.log("No TTS driver selected.  Selecting default.", logtype="Info")
            self.driver = availableEngines[0]
            del availableEngines[0]
        #Import
        while True:
            try:
                self.installDriver(self.driver)
                break
            except ImportError:
                logger.log("Error importing ", self.driver, "!  Trying the next.", logtype="Error", tb=True)
                self.driver = availableEngines[0] #Not checking for errors, since the null driver is last in the list
                del availableEngines[0]
                
    def addSableMarkup(self, text):
        #Do some things to make text sound more realistic
        while text.find('"') != text.rfind('"'):
            text = text.replace('"', "<PITCH BASE='20%'>", 1)
            text = text.replace('"', "</PITCH>", 1)
        text = '<LANGUAGE ID="' + platformSettings.getSetting("spellchecklang", platformSettings.getPlatformSetting("language"))[0:2] + '">' + text + '</LANGUAGE>'
        text = text.replace("\n", '<BREAK LEVEL="large" />')
        text = re.sub(re.compile(re.escape("writetype"), re.I), '<PRON SUB="right type">writetype</PRON>', text, 0)
        #Set the speed to the user preference
        speed = platformSettings.getSetting("readingspeed", 0)
        text = '<RATE SPEED="' + str(speed) + '%">' + text + "</RATE>"
        return u"<SABLE>"+unicode(text)+u"</SABLE>"

    def addSsmlMarkup(self, text):
        #Do some things to make text sound more realistic
        while text.find('"') != text.rfind('"'):
            text = text.replace('"', '<prosody pitch="+20%">', 1)
            text = text.replace('"', "</prosody>", 1)
        text = text.replace("\n", '.<break strength="x-large" time="1s" />')
        text = re.sub(re.compile(re.escape("writetype"), re.I), 'write type', text, 0)
        #Set the speed to the user preference
        speed = platformSettings.getSetting("readingspeed", 0)
        text = unicode('<prosody rate="' + unicode(speed) + '%">' + text + "</prosody>")
        return "<speak xml:lang=\""+platformSettings.getSetting("spellchecklang", platformSettings.getPlatformSetting("language")).replace('_', '-')+"\">"+text+"</speak>"
    
    def installDriver(self, driver):
        logger.log("Trying TTS driver ", driver)
        if driver == "festival":
            from festivalInterface import FestivalInterface
            self.ttsdriver = FestivalInterface(platformSettings.getPlatformSetting("pathToFestival"))
        elif driver == "pyttsx":
            from pyttsxInterface import PyttsxInterface
            self.ttsdriver = PyttsxInterface() # This will make a bug, I'll fix it later
        elif driver == "espeak":
            from espeakInterface import EspeakInterface
            self.ttsdriver = EspeakInterface(platformSettings.getPlatformSetting("pathToEspeak"))
        elif driver == "null":
            from ttsInterface import TtsInterface
            self.ttsdriver = TtsInterface()
            logger.log("Invalid TTS Driver... Running without TTS support", logtype="Error", tb=True)
