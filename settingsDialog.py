# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sat Nov 28 16:10:50 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(400, 300)
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
        self.settingsTab = QtGui.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.gridLayout_2 = QtGui.QGridLayout(self.settingsTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.settingsTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.fontComboBox = QtGui.QFontComboBox(self.settingsTab)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_2.addWidget(self.fontComboBox, 0, 1, 1, 1)
        self.tabWidget.addTab(self.settingsTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
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

        self.retranslateUi(settingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), settingsDialog.close)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QtGui.QApplication.translate("settingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("settingsDialog", "Please enter any custom words you would like to appear in the spell check, one per line.", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customWordlistTab), QtGui.QApplication.translate("settingsDialog", "Custom Words", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("settingsDialog", "Default Font:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QtGui.QApplication.translate("settingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.okayButton.setText(QtGui.QApplication.translate("settingsDialog", "Okay", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("settingsDialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("settingsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

