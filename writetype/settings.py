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
from platformSettings import *
from os.path import join

class SettingsDialogBox(QtGui.QDialog):
    """The settings dialog box"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_settingsDialog()
        self.ui.setupUi(self)
        
        #Load words into textarea
        self.ui.customWordsTextEdit.setPlainText(getSetting("customwords", ""))
        QtCore.QObject.connect(self.ui.okayButton, QtCore.SIGNAL("clicked()"), self.okayClicked)
        QtCore.QObject.connect(self.ui.applyButton, QtCore.SIGNAL("clicked()"), self.applyClicked)

        #Load word list from xml
        self.wordListButtonGroup = QtGui.QButtonGroup()
        filepath = join(getPlatformSetting("pathToWordlists"), "wordlists.xml")
        dom = minidom.parse(filepath)
        # TODO Don't forget to sort these by sortweight!
        for node in dom.getElementsByTagName("wordlist"):
            self.ui.noneAvailableLabel.setVisible(False) # Hide the text that says none are available
            button = QtGui.QRadioButton(node.getAttribute("name"), self.ui.tab)
            button.icon = node.getAttribute("lang") + ".png"
            button.setProperty("lang", node.getAttribute("lang"))
            self.ui.verticalLayout_4.addWidget(button)
            self.wordListButtonGroup.addButton(button, int(node.getAttribute("id")))
        self.hideOtherLanguageCheckboxes()
        QtCore.QObject.connect(self.ui.showAllLangsCheckBox, QtCore.SIGNAL("toggled(bool)"), self.languageCheckboxToggled)

        #Load the radio button settings
        self.wordListButtonGroup.setExclusive(True)
        #Now actually select the correct button
        try:
            self.wordListButtonGroup.buttons()[getSetting("wordlist", 4)-1].setChecked(True)
        except IndexError:
            #self.wordListButtonGroup.buttons()[0].setChecked(True)
            pass

        #Load the word completion settings
        self.ui.guessMisspellingsCheckbox.setChecked(getSetting("guessmisspellings", True))
        self.ui.thresholdSpinbox.setValue(getSetting("threshold", 3))
        self.ui.advancedSubstitutionsCheckbox.setChecked(getSetting("advancedsubstitutions", True))
        self.ui.minimumLetters.setValue(getSetting("minimumletters", 0))
        self.ui.phraseCompletionCheckbox.setChecked(getSetting("phrasecompletion", True))

        #Autocorrection
        self.ui.autocorrectionCheckBox.setChecked(getSetting("autocorrection", True))
        self.ui.contractionsCheckbox.setChecked(getSetting("autocorrectioncontractions", True))
        self.ui.autocorrectionsTable.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem(self.tr("Replace:")))
        self.ui.autocorrectionsTable.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem(self.tr("With:")))

        #Other
        self.ui.grammarCheckbox.setChecked(getSetting("grammarcheck", True))
        self.ui.spellingCheckbox.setChecked(getSetting("spellingcheck", True))
        self.ui.disableFancyInterfaceCheckbox.setChecked(getSetting("disablefancyinterface", False))
        self.ui.readAsTypedCheckbox.setChecked(getSetting("readastyped", False))

        i = 0
        for line in getSetting("customautocorrections", "").split("\n"):
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
        if getSetting("defaultfont", ""):
            self.ui.defaultFont.setCurrentFont(QtGui.QFont(getSetting("defaultfont")))
        else:
            self.ui.useDefaultFont.setChecked(True)
            self.ui.defaultFont.setDisabled(True)

        #TTS
        self.ui.speedSlider.setValue(getSetting("readingspeed", 0))
        engines = getPlatformSetting("ttsEngines").split(",")
        for engine in engines:
            self.ui.ttsEngineBox.addItem(engine)
        currentValue = getSetting("ttsengine", "")
        if currentValue in engines:
            index = engines.index(currentValue)
            self.ui.ttsEngineBox.setCurrentIndex(index)

    # This function saves the settings when the user closes the dialog box.
    def applyClicked(self):
        setSetting("customwords", self.ui.customWordsTextEdit.toPlainText())
        setSetting("wordlist", self.wordListButtonGroup.checkedId())
        setSetting("spellchecklang", self.wordListButtonGroup.checkedButton().property("lang").toString())
        setSetting("phrasecompletion", self.ui.phraseCompletionCheckbox.isChecked())
        setSetting("guessmisspellings", self.ui.guessMisspellingsCheckbox.isChecked())
        setSetting("threshold", self.ui.thresholdSpinbox.value())
        setSetting("advancedsubstitutions", self.ui.advancedSubstitutionsCheckbox.isChecked())
        setSetting("minimumletters", self.ui.minimumLetters.value())
        setSetting("autocorrection", self.ui.autocorrectionCheckBox.isChecked())
        setSetting("autocorrectioncontractions", self.ui.contractionsCheckbox.isChecked())
        setSetting("readingspeed", self.ui.speedSlider.value())
        setSetting("ttsengine", self.ui.ttsEngineBox.currentText())
        setSetting("grammarcheck", self.ui.grammarCheckbox.isChecked())
        setSetting("spellingcheck", self.ui.spellingCheckbox.isChecked())
        setSetting("disablefancyinterface", self.ui.disableFancyInterfaceCheckbox.isChecked())
        setSetting("readastyped", self.ui.readAsTypedCheckbox.isChecked())

        if self.ui.useDefaultFont.isChecked():
            setSetting("defaultfont", "")
        else:
            setSetting("defaultfont", self.ui.defaultFont.currentFont())

        autocorrectionsList = ""
        for i in range(0, self.ui.autocorrectionsTable.rowCount()):
            cell1 = self.ui.autocorrectionsTable.item(i, 0)
            cell2 = self.ui.autocorrectionsTable.item(i, 1)
            if cell1 and cell2:
                if cell1.text() and cell2.text():
                    autocorrectionsList += cell1.text() + "," + cell2.text() + "\n"
        print autocorrectionsList
        setSetting("customautocorrections", autocorrectionsList)
        
        
        self.emit(QtCore.SIGNAL("dialogSaved"))

    def okayClicked(self):
        self.applyClicked()
        self.close()
        
    # This function manages the signals received from
    # showAllLangsCheckBox, and calls either
    # hideOtherLanguageCheckboxes if it is now unchecked, or
    # showOtherLanguageCheckboxes if it is now checked.
    def languageCheckboxToggled(self, enabled):
        if enabled:
            self.showOtherLanguageCheckboxes()
        else:
            self.hideOtherLanguageCheckboxes()
    # Normally, users will only want to view the wordlists for their
    # language.  When the settings dialog box is opened, or when the
    # user unchecks the checkbox in the settings panel to display all
    # languages, this function is run.
    def hideOtherLanguageCheckboxes(self):
        for button in self.wordListButtonGroup.buttons():
            if not getPlatformSetting("language").startswith(button.property("lang").toString()):
                button.setVisible(False)

    # In some situations, such as at language schools, it may be
    # desirable to have word completion be in a different language
    # than the interface.  Checking the appropriate checkbox in the
    # word completion tab will show all languages instead by running
    # this function.
    def showOtherLanguageCheckboxes(self):
        for button in self.wordListButtonGroup.buttons():
            button.setVisible(True)
