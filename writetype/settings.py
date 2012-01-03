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

from ui_settings import Ui_settingsDialog
from xml.dom import minidom
from PyQt4 import QtCore, QtGui, Qt
import platformSettings
from os.path import join

class SettingsDialogBox(QtGui.QDialog):
    """The settings dialog box"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_settingsDialog()
        self.ui.setupUi(self)
        
        #Load words into textarea
        self.ui.customWordsTextEdit.setPlainText(platformSettings.getSetting("customwords", ""))
        QtCore.QObject.connect(self.ui.okayButton, QtCore.SIGNAL("clicked()"), self.okayClicked)
        QtCore.QObject.connect(self.ui.applyButton, QtCore.SIGNAL("clicked()"), self.applyClicked)

        #Load word list from xml
        self.wordListButtonGroup = QtGui.QButtonGroup()
        filepath = join(platformSettings.getPlatformSetting("pathToWordlists"), "wordlists.xml")
        dom = minidom.parse(filepath)
        #Don't forget to sort these by sortweight!
        for node in dom.getElementsByTagName("wordlist"):
            if node.getAttribute("lang") == platformSettings.getPlatformSetting("language"):
                self.ui.noneAvailableLabel.setVisible(False)
                button = QtGui.QRadioButton(node.getAttribute("name"), self.ui.tab)
                self.ui.verticalLayout_4.addWidget(button)
                self.wordListButtonGroup.addButton(button, int(node.getAttribute("id")))

        #Load the radio button settings
        self.wordListButtonGroup.setExclusive(True)
        #Now actually select the correct button
        try:
            self.wordListButtonGroup.buttons()[platformSettings.getSetting("wordlist", 4)-1].setChecked(True)
        except IndexError:
            #self.wordListButtonGroup.buttons()[0].setChecked(True)
            pass

        #Load the word completion settings
        self.ui.guessMisspellingsCheckbox.setChecked(platformSettings.getSetting("guessmisspellings", True))
        self.ui.thresholdSpinbox.setValue(platformSettings.getSetting("threshold", 3))
        self.ui.advancedSubstitutionsCheckbox.setChecked(platformSettings.getSetting("advancedsubstitutions", True))
        self.ui.minimumLetters.setValue(platformSettings.getSetting("minimumletters", 0))
        self.ui.phraseCompletionCheckbox.setChecked(platformSettings.getSetting("phrasecompletion", True))

        #Autocorrection
        self.ui.autocorrectionCheckBox.setChecked(platformSettings.getSetting("autocorrection", True))
        self.ui.contractionsCheckbox.setChecked(platformSettings.getSetting("autocorrectioncontractions", True))
        self.ui.autocorrectionsTable.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem(self.tr("Replace:")))
        self.ui.autocorrectionsTable.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem(self.tr("With:")))

        #Other
        self.ui.grammarCheckbox.setChecked(platformSettings.getSetting("grammarcheck", True))
        self.ui.spellingCheckbox.setChecked(platformSettings.getSetting("spellingcheck", True))
        self.ui.disableFancyInterfaceCheckbox.setChecked(platformSettings.getSetting("disablefancyinterface", False))
        self.ui.readAsTypedCheckbox.setChecked(platformSettings.getSetting("readastyped", False))

        i = 0
        for line in platformSettings.getSetting("customAutocorrections", "").split("\n"):
            if not line: break
            self.ui.autocorrectionsTable.insertRow(i+1)
            item1 = QtGui.QTableWidgetItem(line.split(',')[0])
            item2 = QtGui.QTableWidgetItem(line.split(',')[1])
            self.ui.autocorrectionsTable.setItem(i, 0, item1)
            self.ui.autocorrectionsTable.setItem(i, 1, item2)
            i += 1
        def autoAddRows(row, col):
            if row + 1 == self.ui.autocorrectionsTable.rowCount():
                self.ui.autocorrectionsTable.insertRow(row + 1)
        QtCore.QObject.connect(self.ui.autocorrectionsTable, QtCore.SIGNAL("cellDoubleClicked(int,int)"), autoAddRows)

        #Set the correct default font
        if platformSettings.getSetting("defaultfont", ""):
            self.ui.defaultFont.setCurrentFont(QtGui.QFont(platformSettings.getSetting("defaultfont")))
        else:
            self.ui.useDefaultFont.setChecked(True)
            self.ui.defaultFont.setDisabled(True)

        #TTS
        self.ui.speedSlider.setValue(platformSettings.getSetting("readingspeed", 0))
        engines = platformSettings.getPlatformSetting("ttsEngines").split(",")
        for engine in engines:
            self.ui.ttsEngineBox.addItem(engine)
        currentValue = platformSettings.getSetting("ttsengine", "")
        if currentValue in engines:
            index = engines.index(currentValue)
            self.ui.ttsEngineBox.setCurrentIndex(index)
        
        
    def applyClicked(self):
        platformSettings.setSetting("customwords", self.ui.customWordsTextEdit.toPlainText())
        platformSettings.setSetting("wordlist", self.wordListButtonGroup.checkedId())
        platformSettings.setSetting("phrasecompletion", self.ui.phraseCompletionCheckbox.isChecked())
        platformSettings.setSetting("guessmisspellings", self.ui.guessMisspellingsCheckbox.isChecked())
        platformSettings.setSetting("threshold", self.ui.thresholdSpinbox.value())
        platformSettings.setSetting("advancedsubstitutions", self.ui.advancedSubstitutionsCheckbox.isChecked())
        platformSettings.setSetting("minimumletters", self.ui.minimumLetters.value())
        platformSettings.setSetting("autocorrection", self.ui.autocorrectionCheckBox.isChecked())
        platformSettings.setSetting("autocorrectioncontractions", self.ui.contractionsCheckbox.isChecked())
        platformSettings.setSetting("readingspeed", self.ui.speedSlider.value())
        platformSettings.setSetting("ttsengine", self.ui.ttsEngineBox.currentText())
        platformSettings.setSetting("grammarcheck", self.ui.grammarCheckbox.isChecked())
        platformSettings.setSetting("spellingcheck", self.ui.spellingCheckbox.isChecked())
        platformSettings.setSetting("disablefancyinterface", self.ui.disableFancyInterfaceCheckbox.isChecked())
        platformSettings.setSetting("readastyped", self.ui.readAsTypedCheckbox.isChecked())

        if self.ui.useDefaultFont.isChecked():
            platformSettings.setSetting("defaultfont", "")
        else:
            platformSettings.setSetting("defaultfont", self.ui.defaultFont.currentFont())

        autocorrectionsList = ""
        for i in range(0, self.ui.autocorrectionsTable.rowCount()):
            cell1 = self.ui.autocorrectionsTable.item(i, 0)
            cell2 = self.ui.autocorrectionsTable.item(i, 1)
            if cell1 and cell2:
                if cell1.text() and cell2.text():
                    autocorrectionsList += cell1.text() + "," + cell2.text() + "\n"
        print autocorrectionsList
        platformSettings.setSetting("customAutocorrections", autocorrectionsList)
        
        
        self.emit(QtCore.SIGNAL("dialogSaved"))

    def okayClicked(self):
        self.applyClicked()
        self.close()
