# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/distractionfree.ui'
#
# Created: Mon Jan  2 15:48:17 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_distractionFree(object):
    def setupUi(self, distractionFree):
        distractionFree.setObjectName(_fromUtf8("distractionFree"))
        distractionFree.resize(377, 315)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(distractionFree.sizePolicy().hasHeightForWidth())
        distractionFree.setSizePolicy(sizePolicy)
        distractionFree.setStyleSheet(_fromUtf8("#distractionFree {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(222, 240, 248, 255), stop:1 rgba(183, 229, 248, 255));\n"
"}\n"
""))
        self.verticalLayout_2 = QtGui.QVBoxLayout(distractionFree)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.retranslateUi(distractionFree)
        QtCore.QMetaObject.connectSlotsByName(distractionFree)

    def retranslateUi(self, distractionFree):
        distractionFree.setWindowTitle(QtGui.QApplication.translate("distractionFree", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

