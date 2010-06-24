# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/statistics.ui'
#
# Created: Thu Jun 24 09:08:17 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_statisticsDialog(object):
    def setupUi(self, statisticsDialog):
        statisticsDialog.setObjectName("statisticsDialog")
        statisticsDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(statisticsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(statisticsDialog)
        self.label_2.setMargin(20)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(statisticsDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.filenameLabel = QtGui.QLabel(statisticsDialog)
        self.filenameLabel.setText("")
        self.filenameLabel.setObjectName("filenameLabel")
        self.gridLayout.addWidget(self.filenameLabel, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(statisticsDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(statisticsDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(statisticsDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(statisticsDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.charactersLabel = QtGui.QLabel(statisticsDialog)
        self.charactersLabel.setText("")
        self.charactersLabel.setObjectName("charactersLabel")
        self.gridLayout.addWidget(self.charactersLabel, 2, 1, 1, 1)
        self.sentencesLabel = QtGui.QLabel(statisticsDialog)
        self.sentencesLabel.setText("")
        self.sentencesLabel.setObjectName("sentencesLabel")
        self.gridLayout.addWidget(self.sentencesLabel, 4, 1, 1, 1)
        self.paragraphsLabel = QtGui.QLabel(statisticsDialog)
        self.paragraphsLabel.setText("")
        self.paragraphsLabel.setObjectName("paragraphsLabel")
        self.gridLayout.addWidget(self.paragraphsLabel, 5, 1, 1, 1)
        self.readabilityLabel = QtGui.QLabel(statisticsDialog)
        self.readabilityLabel.setText("")
        self.readabilityLabel.setObjectName("readabilityLabel")
        self.gridLayout.addWidget(self.readabilityLabel, 6, 1, 1, 1)
        self.label_6 = QtGui.QLabel(statisticsDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.wordsLabel = QtGui.QLabel(statisticsDialog)
        self.wordsLabel.setText("")
        self.wordsLabel.setObjectName("wordsLabel")
        self.gridLayout.addWidget(self.wordsLabel, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(statisticsDialog)
        QtCore.QMetaObject.connectSlotsByName(statisticsDialog)

    def retranslateUi(self, statisticsDialog):
        statisticsDialog.setWindowTitle(QtGui.QApplication.translate("statisticsDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("statisticsDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Document Statistics</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("statisticsDialog", "Filename: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("statisticsDialog", "Characters: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("statisticsDialog", "Sentences: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("statisticsDialog", "Paragraphs: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("statisticsDialog", "Readability", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("statisticsDialog", "Words: ", None, QtGui.QApplication.UnicodeUTF8))

