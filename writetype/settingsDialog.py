# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/settings.ui'
#
# Created: Fri May 21 14:39:15 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(471, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(settingsDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(settingsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.customWordlistTab = QtGui.QWidget()
        self.customWordlistTab.setObjectName("customWordlistTab")
        self.gridLayout = QtGui.QGridLayout(self.customWordlistTab)
        self.gridLayout.setObjectName("gridLayout")
        self.customWordsTextEdit = QtGui.QTextEdit(self.customWordlistTab)
        self.customWordsTextEdit.setUndoRedoEnabled(False)
        self.customWordsTextEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.customWordsTextEdit.setAcceptRichText(False)
        self.customWordsTextEdit.setObjectName("customWordsTextEdit")
        self.gridLayout.addWidget(self.customWordsTextEdit, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.customWordlistTab)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.customWordlistTab, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.wordListSize1 = QtGui.QRadioButton(self.tab)
        self.wordListSize1.setObjectName("wordListSize1")
        self.verticalLayout_7.addWidget(self.wordListSize1)
        self.wordListSize2 = QtGui.QRadioButton(self.tab)
        self.wordListSize2.setObjectName("wordListSize2")
        self.verticalLayout_7.addWidget(self.wordListSize2)
        self.wordListSize3 = QtGui.QRadioButton(self.tab)
        self.wordListSize3.setChecked(True)
        self.wordListSize3.setObjectName("wordListSize3")
        self.verticalLayout_7.addWidget(self.wordListSize3)
        self.wordListSize4 = QtGui.QRadioButton(self.tab)
        self.wordListSize4.setObjectName("wordListSize4")
        self.verticalLayout_7.addWidget(self.wordListSize4)
        self.wordListSize5 = QtGui.QRadioButton(self.tab)
        self.wordListSize5.setChecked(False)
        self.wordListSize5.setObjectName("wordListSize5")
        self.verticalLayout_7.addWidget(self.wordListSize5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.wordCompletionTab = QtGui.QWidget()
        self.wordCompletionTab.setObjectName("wordCompletionTab")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.wordCompletionTab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtGui.QLabel(self.wordCompletionTab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtGui.QLabel(self.wordCompletionTab)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.minimumLetters = QtGui.QSpinBox(self.wordCompletionTab)
        self.minimumLetters.setObjectName("minimumLetters")
        self.horizontalLayout_2.addWidget(self.minimumLetters)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.guessMisspellingsCheckbox = QtGui.QCheckBox(self.wordCompletionTab)
        self.guessMisspellingsCheckbox.setChecked(True)
        self.guessMisspellingsCheckbox.setObjectName("guessMisspellingsCheckbox")
        self.verticalLayout_8.addWidget(self.guessMisspellingsCheckbox)
        self.misspellingSettings = QtGui.QGroupBox(self.wordCompletionTab)
        self.misspellingSettings.setEnabled(True)
        self.misspellingSettings.setFlat(False)
        self.misspellingSettings.setObjectName("misspellingSettings")
        self.gridLayout_4 = QtGui.QGridLayout(self.misspellingSettings)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.thresholdSpinbox = QtGui.QSpinBox(self.misspellingSettings)
        self.thresholdSpinbox.setMaximum(25)
        self.thresholdSpinbox.setProperty("value", 2)
        self.thresholdSpinbox.setObjectName("thresholdSpinbox")
        self.gridLayout_4.addWidget(self.thresholdSpinbox, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.misspellingSettings)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.advancedSubstitutionsCheckbox = QtGui.QCheckBox(self.misspellingSettings)
        self.advancedSubstitutionsCheckbox.setObjectName("advancedSubstitutionsCheckbox")
        self.gridLayout_4.addWidget(self.advancedSubstitutionsCheckbox, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.misspellingSettings)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.misspellingSettings)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.tabWidget.addTab(self.wordCompletionTab, "")
        self.autocompletions = QtGui.QWidget()
        self.autocompletions.setObjectName("autocompletions")
        self.verticalLayout = QtGui.QVBoxLayout(self.autocompletions)
        self.verticalLayout.setObjectName("verticalLayout")
        self.autocompletionCheckBox = QtGui.QCheckBox(self.autocompletions)
        self.autocompletionCheckBox.setChecked(True)
        self.autocompletionCheckBox.setObjectName("autocompletionCheckBox")
        self.verticalLayout.addWidget(self.autocompletionCheckBox)
        self.autocorrectionGroupBox = QtGui.QGroupBox(self.autocompletions)
        self.autocorrectionGroupBox.setObjectName("autocorrectionGroupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.autocorrectionGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.autocompletionsTable = QtGui.QTableWidget(self.autocorrectionGroupBox)
        self.autocompletionsTable.setRowCount(1)
        self.autocompletionsTable.setColumnCount(2)
        self.autocompletionsTable.setObjectName("autocompletionsTable")
        self.autocompletionsTable.setColumnCount(2)
        self.autocompletionsTable.setRowCount(1)
        self.autocompletionsTable.horizontalHeader().setDefaultSectionSize(150)
        self.autocompletionsTable.horizontalHeader().setMinimumSectionSize(34)
        self.autocompletionsTable.horizontalHeader().setStretchLastSection(True)
        self.autocompletionsTable.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.autocompletionsTable)
        self.contractionsCheckbox = QtGui.QCheckBox(self.autocorrectionGroupBox)
        self.contractionsCheckbox.setObjectName("contractionsCheckbox")
        self.verticalLayout_3.addWidget(self.contractionsCheckbox)
        self.verticalLayout.addWidget(self.autocorrectionGroupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget.addTab(self.autocompletions, "")
        self.settingsTab = QtGui.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.gridLayout_2 = QtGui.QGridLayout(self.settingsTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.usageStatisticsCheckbox = QtGui.QCheckBox(self.settingsTab)
        self.usageStatisticsCheckbox.setObjectName("usageStatisticsCheckbox")
        self.gridLayout_2.addWidget(self.usageStatisticsCheckbox, 2, 1, 1, 1)
        self.defaultFont = QtGui.QFontComboBox(self.settingsTab)
        self.defaultFont.setObjectName("defaultFont")
        self.gridLayout_2.addWidget(self.defaultFont, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.settingsTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.settingsTab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 6, 1, 1, 1)
        self.useDefaultFont = QtGui.QCheckBox(self.settingsTab)
        self.useDefaultFont.setObjectName("useDefaultFont")
        self.gridLayout_2.addWidget(self.useDefaultFont, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.settingsTab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.speedSlider = QtGui.QSlider(self.settingsTab)
        self.speedSlider.setMinimum(-90)
        self.speedSlider.setMaximum(90)
        self.speedSlider.setSingleStep(10)
        self.speedSlider.setProperty("value", 0)
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setObjectName("speedSlider")
        self.horizontalLayout.addWidget(self.speedSlider)
        self.spinBox = QtGui.QSpinBox(self.settingsTab)
        self.spinBox.setMinimum(-90)
        self.spinBox.setMaximum(90)
        self.spinBox.setSingleStep(10)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.settingsTab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.ttsEngineBox = QtGui.QComboBox(self.settingsTab)
        self.ttsEngineBox.setEditable(False)
        self.ttsEngineBox.setObjectName("ttsEngineBox")
        self.gridLayout_2.addWidget(self.ttsEngineBox, 4, 1, 1, 1)
        self.tabWidget.addTab(self.settingsTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.okayButton = QtGui.QPushButton(settingsDialog)
        self.okayButton.setObjectName("okayButton")
        self.horizontalLayout_3.addWidget(self.okayButton)
        self.applyButton = QtGui.QPushButton(settingsDialog)
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout_3.addWidget(self.applyButton)
        self.cancelButton = QtGui.QPushButton(settingsDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label.setBuddy(self.customWordsTextEdit)
        self.label_5.setBuddy(self.thresholdSpinbox)
        self.label_6.setBuddy(self.advancedSubstitutionsCheckbox)

        self.retranslateUi(settingsDialog)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), settingsDialog.close)
        QtCore.QObject.connect(self.guessMisspellingsCheckbox, QtCore.SIGNAL("toggled(bool)"), self.misspellingSettings.setVisible)
        QtCore.QObject.connect(self.useDefaultFont, QtCore.SIGNAL("toggled(bool)"), self.defaultFont.setDisabled)
        QtCore.QObject.connect(self.autocompletionCheckBox, QtCore.SIGNAL("toggled(bool)"), self.autocorrectionGroupBox.setVisible)
        QtCore.QObject.connect(self.speedSlider, QtCore.SIGNAL("valueChanged(int)"), self.spinBox.setValue)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL("valueChanged(int)"), self.speedSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QtGui.QApplication.translate("settingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("settingsDialog", "Please enter any custom words you would like to appear in the spell check, one per line.", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customWordlistTab), QtGui.QApplication.translate("settingsDialog", "Custom Words", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("settingsDialog", "Please select the size of the word completion database:", None, QtGui.QApplication.UnicodeUTF8))
        self.wordListSize1.setText(QtGui.QApplication.translate("settingsDialog", "Big", None, QtGui.QApplication.UnicodeUTF8))
        self.wordListSize2.setText(QtGui.QApplication.translate("settingsDialog", "Really Big", None, QtGui.QApplication.UnicodeUTF8))
        self.wordListSize3.setText(QtGui.QApplication.translate("settingsDialog", "Huge", None, QtGui.QApplication.UnicodeUTF8))
        self.wordListSize4.setText(QtGui.QApplication.translate("settingsDialog", "Super Huge", None, QtGui.QApplication.UnicodeUTF8))
        self.wordListSize5.setText(QtGui.QApplication.translate("settingsDialog", "Ginormous", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("settingsDialog", "Word lists", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("settingsDialog", "View settings for the custom word completion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("settingsDialog", "Minimum letters:", None, QtGui.QApplication.UnicodeUTF8))
        self.guessMisspellingsCheckbox.setText(QtGui.QApplication.translate("settingsDialog", "Try to guess misspellings", None, QtGui.QApplication.UnicodeUTF8))
        self.misspellingSettings.setTitle(QtGui.QApplication.translate("settingsDialog", "Misspelling Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.thresholdSpinbox.setToolTip(QtGui.QApplication.translate("settingsDialog", "How many entries need to be displayed, at the minimum, before WriteType will attempt to guess the spelling?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("settingsDialog", "Misspelling Threshold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("settingsDialog", "Advanced Substitutions?", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wordCompletionTab), QtGui.QApplication.translate("settingsDialog", "Word Completion", None, QtGui.QApplication.UnicodeUTF8))
        self.autocompletionCheckBox.setText(QtGui.QApplication.translate("settingsDialog", "Use auto-completion", None, QtGui.QApplication.UnicodeUTF8))
        self.autocorrectionGroupBox.setTitle(QtGui.QApplication.translate("settingsDialog", "Auto-correction settings", None, QtGui.QApplication.UnicodeUTF8))
        self.contractionsCheckbox.setText(QtGui.QApplication.translate("settingsDialog", "Contractions", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.autocompletions), QtGui.QApplication.translate("settingsDialog", "Auto-completions", None, QtGui.QApplication.UnicodeUTF8))
        self.usageStatisticsCheckbox.setText(QtGui.QApplication.translate("settingsDialog", "Send usage statistics to help improve the program", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("settingsDialog", "Default Font:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("settingsDialog", "Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.useDefaultFont.setText(QtGui.QApplication.translate("settingsDialog", "System Default", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("settingsDialog", "Reading speed:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox.setSuffix(QtGui.QApplication.translate("settingsDialog", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("settingsDialog", "TTS Engine", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QtGui.QApplication.translate("settingsDialog", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.okayButton.setText(QtGui.QApplication.translate("settingsDialog", "Okay", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("settingsDialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("settingsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

