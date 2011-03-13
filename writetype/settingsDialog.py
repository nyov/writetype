# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/settings.ui'
#
# Created: Sat Mar 12 19:31:53 2011
#      by: PyQt4 UI code generator 4.7.4
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
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
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
        self.phraseCompletionCheckbox = QtGui.QCheckBox(self.wordCompletionTab)
        self.phraseCompletionCheckbox.setChecked(True)
        self.phraseCompletionCheckbox.setObjectName("phraseCompletionCheckbox")
        self.verticalLayout_8.addWidget(self.phraseCompletionCheckbox)
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
        self.advancedSubstitutionsCheckbox.setText("")
        self.advancedSubstitutionsCheckbox.setObjectName("advancedSubstitutionsCheckbox")
        self.gridLayout_4.addWidget(self.advancedSubstitutionsCheckbox, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.misspellingSettings)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.misspellingSettings)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.tabWidget.addTab(self.wordCompletionTab, "")
        self.autocorrections = QtGui.QWidget()
        self.autocorrections.setObjectName("autocorrections")
        self.verticalLayout = QtGui.QVBoxLayout(self.autocorrections)
        self.verticalLayout.setObjectName("verticalLayout")
        self.autocorrectionCheckBox = QtGui.QCheckBox(self.autocorrections)
        self.autocorrectionCheckBox.setChecked(True)
        self.autocorrectionCheckBox.setObjectName("autocorrectionCheckBox")
        self.verticalLayout.addWidget(self.autocorrectionCheckBox)
        self.autocorrectionGroupBox = QtGui.QGroupBox(self.autocorrections)
        self.autocorrectionGroupBox.setObjectName("autocorrectionGroupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.autocorrectionGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.autocorrectionsTable = QtGui.QTableWidget(self.autocorrectionGroupBox)
        self.autocorrectionsTable.setRowCount(1)
        self.autocorrectionsTable.setColumnCount(2)
        self.autocorrectionsTable.setObjectName("autocorrectionsTable")
        self.autocorrectionsTable.setColumnCount(2)
        self.autocorrectionsTable.setRowCount(1)
        self.autocorrectionsTable.horizontalHeader().setDefaultSectionSize(150)
        self.autocorrectionsTable.horizontalHeader().setMinimumSectionSize(34)
        self.autocorrectionsTable.horizontalHeader().setStretchLastSection(True)
        self.autocorrectionsTable.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.autocorrectionsTable)
        self.contractionsCheckbox = QtGui.QCheckBox(self.autocorrectionGroupBox)
        self.contractionsCheckbox.setObjectName("contractionsCheckbox")
        self.verticalLayout_3.addWidget(self.contractionsCheckbox)
        self.verticalLayout.addWidget(self.autocorrectionGroupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget.addTab(self.autocorrections, "")
        self.settingsTab = QtGui.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.gridLayout_2 = QtGui.QGridLayout(self.settingsTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.defaultFont = QtGui.QFontComboBox(self.settingsTab)
        self.defaultFont.setObjectName("defaultFont")
        self.gridLayout_2.addWidget(self.defaultFont, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.settingsTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.settingsTab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 6, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.settingsTab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
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
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.settingsTab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.ttsEngineBox = QtGui.QComboBox(self.settingsTab)
        self.ttsEngineBox.setEditable(False)
        self.ttsEngineBox.setObjectName("ttsEngineBox")
        self.gridLayout_2.addWidget(self.ttsEngineBox, 3, 1, 1, 1)
        self.useDefaultFont = QtGui.QCheckBox(self.settingsTab)
        self.useDefaultFont.setObjectName("useDefaultFont")
        self.gridLayout_2.addWidget(self.useDefaultFont, 5, 1, 1, 1)
        self.grammarCheckbox = QtGui.QCheckBox(self.settingsTab)
        self.grammarCheckbox.setChecked(True)
        self.grammarCheckbox.setObjectName("grammarCheckbox")
        self.gridLayout_2.addWidget(self.grammarCheckbox, 1, 1, 1, 1)
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), settingsDialog.close)
        QtCore.QObject.connect(self.guessMisspellingsCheckbox, QtCore.SIGNAL("toggled(bool)"), self.misspellingSettings.setVisible)
        QtCore.QObject.connect(self.useDefaultFont, QtCore.SIGNAL("toggled(bool)"), self.defaultFont.setDisabled)
        QtCore.QObject.connect(self.autocorrectionCheckBox, QtCore.SIGNAL("toggled(bool)"), self.autocorrectionGroupBox.setVisible)
        QtCore.QObject.connect(self.speedSlider, QtCore.SIGNAL("valueChanged(int)"), self.spinBox.setValue)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL("valueChanged(int)"), self.speedSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QtGui.QApplication.translate("settingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("settingsDialog", "Please enter any custom words you would like to appear in the spell check, one per line.", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customWordlistTab), QtGui.QApplication.translate("settingsDialog", "Custom Words", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("settingsDialog", "Please select the size of the word completion database:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("settingsDialog", "Word lists", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("settingsDialog", "View settings for the custom word completion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("settingsDialog", "Minimum letters:", None, QtGui.QApplication.UnicodeUTF8))
        self.phraseCompletionCheckbox.setText(QtGui.QApplication.translate("settingsDialog", "Offer phrase completions", None, QtGui.QApplication.UnicodeUTF8))
        self.guessMisspellingsCheckbox.setText(QtGui.QApplication.translate("settingsDialog", "Try to guess misspellings", None, QtGui.QApplication.UnicodeUTF8))
        self.misspellingSettings.setTitle(QtGui.QApplication.translate("settingsDialog", "Misspelling Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.thresholdSpinbox.setToolTip(QtGui.QApplication.translate("settingsDialog", "How many entries need to be displayed, at the minimum, before WriteType will attempt to guess the spelling?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("settingsDialog", "Misspelling Threshold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("settingsDialog", "Advanced Substitutions?", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wordCompletionTab), QtGui.QApplication.translate("settingsDialog", "Word Completion", None, QtGui.QApplication.UnicodeUTF8))
        self.autocorrectionCheckBox.setText(QtGui.QApplication.translate("settingsDialog", "Use auto-correction", None, QtGui.QApplication.UnicodeUTF8))
        self.autocorrectionGroupBox.setTitle(QtGui.QApplication.translate("settingsDialog", "Auto-correction settings", None, QtGui.QApplication.UnicodeUTF8))
        self.contractionsCheckbox.setText(QtGui.QApplication.translate("settingsDialog", "Contractions", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.autocorrections), QtGui.QApplication.translate("settingsDialog", "Auto-corrections", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("settingsDialog", "Default Font:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("settingsDialog", "Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("settingsDialog", "Reading speed:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox.setSuffix(QtGui.QApplication.translate("settingsDialog", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("settingsDialog", "TTS Engine", None, QtGui.QApplication.UnicodeUTF8))
        self.useDefaultFont.setText(QtGui.QApplication.translate("settingsDialog", "System Default", None, QtGui.QApplication.UnicodeUTF8))
        self.grammarCheckbox.setText(QtGui.QApplication.translate("settingsDialog", "Check document for grammar mistakes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QtGui.QApplication.translate("settingsDialog", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.okayButton.setText(QtGui.QApplication.translate("settingsDialog", "Okay", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("settingsDialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("settingsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

