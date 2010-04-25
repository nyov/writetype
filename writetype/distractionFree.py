# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/distractionfree.ui'
#
# Created: Sat Apr 24 13:39:41 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_distractionFree(object):
    def setupUi(self, distractionFree):
        distractionFree.setObjectName("distractionFree")
        distractionFree.resize(377, 315)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(distractionFree.sizePolicy().hasHeightForWidth())
        distractionFree.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtGui.QVBoxLayout(distractionFree)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.retranslateUi(distractionFree)
        QtCore.QMetaObject.connectSlotsByName(distractionFree)

    def retranslateUi(self, distractionFree):
        distractionFree.setWindowTitle(QtGui.QApplication.translate("distractionFree", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

