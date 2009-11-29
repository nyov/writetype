# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Tue Nov 24 15:51:19 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,400,300).size()).expandedTo(Dialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Dialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")

        self.customWordlistTab = QtGui.QWidget()
        self.customWordlistTab.setObjectName("customWordlistTab")

        self.gridlayout = QtGui.QGridLayout(self.customWordlistTab)
        self.gridlayout.setObjectName("gridlayout")

        self.textEdit = QtGui.QTextEdit(self.customWordlistTab)
        self.textEdit.setObjectName("textEdit")
        self.gridlayout.addWidget(self.textEdit,1,0,1,1)

        self.label = QtGui.QLabel(self.customWordlistTab)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)
        self.tabWidget.addTab(self.customWordlistTab,"")

        self.settingsTab = QtGui.QWidget()
        self.settingsTab.setObjectName("settingsTab")

        self.gridlayout1 = QtGui.QGridLayout(self.settingsTab)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_2 = QtGui.QLabel(self.settingsTab)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2,0,0,1,1)

        self.fontComboBox = QtGui.QFontComboBox(self.settingsTab)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridlayout1.addWidget(self.fontComboBox,0,1,1,1)
        self.tabWidget.addTab(self.settingsTab,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.okayButton = QtGui.QPushButton(Dialog)
        self.okayButton.setObjectName("okayButton")
        self.hboxlayout.addWidget(self.okayButton)

        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.label.setBuddy(self.textEdit)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Please enter any custom words you would like to appear in the spell check, one per line.", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customWordlistTab), QtGui.QApplication.translate("Dialog", "Custom Words", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Default Font:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.okayButton.setText(QtGui.QApplication.translate("Dialog", "Okay", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

