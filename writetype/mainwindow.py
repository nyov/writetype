# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Tue Apr 12 08:47:09 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/key120x120.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(222, 240, 248, 255), stop:1 rgba(183, 229, 248, 255));\n"
"}\n"
"#MainWindow #centralwidget {\n"
"    background: transparent;\n"
"}\n"
"#MainWindow .QToolBar {\n"
"    background: transparent;\n"
"}\n"
"QFontComboBox, QSpinBox {\n"
"    background: rgb(247, 251, 254);\n"
"}\n"
"#textArea { \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 246, 209, 255), stop:1 rgba(255, 252, 240, 255));\n"
"}\n"
"#MainWindow QMenu {\n"
"    background-color: rgb(217, 245, 255);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"#MainWindow QMenu::item:selected {\n"
"    background-color: rgb(191, 216, 224);\n"
"}\n"
"#fileToolBar QToolButton, #editToolBar QToolButton, #speakToolBar QToolButton { \n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.514, fx:0.5, fy:0.5, stop:0.382514 rgba(54, 68, 156, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"#fileToolBar QToolButton:hover, #editToolBar QToolButton:hover, #speakToolBar QToolButton:hover {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.514, fx:0.5, fy:0.5, stop:0.382514 rgba(89, 112, 255, 255), stop:1 rgba(255, 255, 255, 0));\n"
"    border-radius: 8px;\n"
"}\n"
"#fileToolBar QToolButton:pressed, #editToolBar QToolButton:pressed, #speakToolBar QToolButton:pressed{\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.436, fx:0.5, fy:0.5, stop:0 rgba(42, 66, 220, 255), stop:1 rgba(255, 255, 255, 0))\n"
"}\n"
"#editToolBar QToolButton:checked {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.514, fx:0.5, fy:0.5, stop:0.382514 rgba(156, 54, 54, 255), stop:1 rgba(255, 255, 255, 0));\n"
"    border: transparent;\n"
"}")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("None")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBoxFontSize = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxFontSize.setProperty("value", 12)
        self.spinBoxFontSize.setObjectName("spinBoxFontSize")
        self.gridLayout.addWidget(self.spinBoxFontSize, 0, 1, 1, 1)
        self.fontComboBox = QtGui.QFontComboBox(self.centralwidget)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout.addWidget(self.fontComboBox, 0, 2, 1, 1)
        self.sizeLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(22)
        sizePolicy.setHeightForWidth(self.sizeLabel.sizePolicy().hasHeightForWidth())
        self.sizeLabel.setSizePolicy(sizePolicy)
        self.sizeLabel.setMaximumSize(QtCore.QSize(22, 22))
        self.sizeLabel.setText("")
        self.sizeLabel.setPixmap(QtGui.QPixmap(":/res/text.png"))
        self.sizeLabel.setScaledContents(True)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.textArea = spellCheckEdit(self.splitter)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.textArea.setFont(font)
        self.textArea.setObjectName("textArea")
        self.spellingSuggestionsList = ListWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spellingSuggestionsList.sizePolicy().hasHeightForWidth())
        self.spellingSuggestionsList.setSizePolicy(sizePolicy)
        self.spellingSuggestionsList.setMaximumSize(QtCore.QSize(300, 16777215))
        self.spellingSuggestionsList.setObjectName("spellingSuggestionsList")
        self.verticalLayout.addWidget(self.splitter)
        self.dictionErrorFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dictionErrorFrame.sizePolicy().hasHeightForWidth())
        self.dictionErrorFrame.setSizePolicy(sizePolicy)
        self.dictionErrorFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.dictionErrorFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.dictionErrorFrame.setObjectName("dictionErrorFrame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.dictionErrorFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dictionCloseButton = QtGui.QToolButton(self.dictionErrorFrame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/fileclose.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dictionCloseButton.setIcon(icon1)
        self.dictionCloseButton.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.dictionCloseButton.setAutoRaise(True)
        self.dictionCloseButton.setObjectName("dictionCloseButton")
        self.horizontalLayout.addWidget(self.dictionCloseButton)
        self.dictionErrorLabel = QtGui.QLabel(self.dictionErrorFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dictionErrorLabel.sizePolicy().hasHeightForWidth())
        self.dictionErrorLabel.setSizePolicy(sizePolicy)
        self.dictionErrorLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.dictionErrorLabel.setText("")
        self.dictionErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dictionErrorLabel.setWordWrap(True)
        self.dictionErrorLabel.setObjectName("dictionErrorLabel")
        self.horizontalLayout.addWidget(self.dictionErrorLabel)
        self.nextButton = QtGui.QPushButton(self.dictionErrorFrame)
        self.nextButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon2)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout.addWidget(self.dictionErrorFrame)
        self.distractionButton = QtGui.QPushButton(self.centralwidget)
        self.distractionButton.setObjectName("distractionButton")
        self.verticalLayout.addWidget(self.distractionButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuToolbars = QtGui.QMenu(self.menuView)
        self.menuToolbars.setObjectName("menuToolbars")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileToolBar = QtGui.QToolBar(MainWindow)
        self.fileToolBar.setMovable(False)
        self.fileToolBar.setIconSize(QtCore.QSize(26, 26))
        self.fileToolBar.setObjectName("fileToolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.fileToolBar)
        self.editToolBar = QtGui.QToolBar(MainWindow)
        self.editToolBar.setEnabled(True)
        self.editToolBar.setMovable(False)
        self.editToolBar.setIconSize(QtCore.QSize(26, 26))
        self.editToolBar.setObjectName("editToolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.editToolBar)
        self.speakToolBar = QtGui.QToolBar(MainWindow)
        self.speakToolBar.setMovable(False)
        self.speakToolBar.setIconSize(QtCore.QSize(26, 26))
        self.speakToolBar.setObjectName("speakToolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.speakToolBar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/res/filesave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/res/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon4)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/res/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon5)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/res/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon6)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSettings = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/res/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon7)
        self.actionSettings.setObjectName("actionSettings")
        self.actionBold = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/res/text_bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon8)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/res/text_italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon9)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/res/text_under.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon10)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionSpeak = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/res/voicecall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpeak.setIcon(icon11)
        self.actionSpeak.setObjectName("actionSpeak")
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/res/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon12)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/res/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon13)
        self.actionRedo.setObjectName("actionRedo")
        self.actionEnableFileToolbar = QtGui.QAction(MainWindow)
        self.actionEnableFileToolbar.setCheckable(True)
        self.actionEnableFileToolbar.setChecked(True)
        self.actionEnableFileToolbar.setObjectName("actionEnableFileToolbar")
        self.actionEnableEditToolbar = QtGui.QAction(MainWindow)
        self.actionEnableEditToolbar.setCheckable(True)
        self.actionEnableEditToolbar.setChecked(True)
        self.actionEnableEditToolbar.setObjectName("actionEnableEditToolbar")
        self.actionEnableSpeakerToolbar = QtGui.QAction(MainWindow)
        self.actionEnableSpeakerToolbar.setCheckable(True)
        self.actionEnableSpeakerToolbar.setChecked(True)
        self.actionEnableSpeakerToolbar.setObjectName("actionEnableSpeakerToolbar")
        self.actionDocumentation = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/res/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDocumentation.setIcon(icon14)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/res/idea.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon15)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAboutQt = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/res/qtcreator_logo_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAboutQt.setIcon(icon16)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionPrint = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/res/fileprint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon17)
        self.actionPrint.setObjectName("actionPrint")
        self.actionHighlightMode = QtGui.QAction(MainWindow)
        self.actionHighlightMode.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/res/highlight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHighlightMode.setIcon(icon18)
        self.actionHighlightMode.setObjectName("actionHighlightMode")
        self.actionHighlight = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/res/highlight_single.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHighlight.setIcon(icon19)
        self.actionHighlight.setObjectName("actionHighlight")
        self.actionDistractionFree = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/res/page-simple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDistractionFree.setIcon(icon20)
        self.actionDistractionFree.setObjectName("actionDistractionFree")
        self.actionInsert_Image = QtGui.QAction(MainWindow)
        self.actionInsert_Image.setIcon(icon)
        self.actionInsert_Image.setObjectName("actionInsert_Image")
        self.actionAlign_Image_Left = QtGui.QAction(MainWindow)
        self.actionAlign_Image_Left.setIcon(icon)
        self.actionAlign_Image_Left.setObjectName("actionAlign_Image_Left")
        self.actionAlign_Image_Right = QtGui.QAction(MainWindow)
        self.actionAlign_Image_Right.setIcon(icon)
        self.actionAlign_Image_Right.setObjectName("actionAlign_Image_Right")
        self.actionEnableImageToolbar = QtGui.QAction(MainWindow)
        self.actionEnableImageToolbar.setCheckable(True)
        self.actionEnableImageToolbar.setChecked(True)
        self.actionEnableImageToolbar.setObjectName("actionEnableImageToolbar")
        self.actionStop = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/res/player_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon21)
        self.actionStop.setObjectName("actionStop")
        self.actionAlignLeft = QtGui.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/res/format-justify-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignLeft.setIcon(icon22)
        self.actionAlignLeft.setObjectName("actionAlignLeft")
        self.actionAlignCenter = QtGui.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/res/format-justify-center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignCenter.setIcon(icon23)
        self.actionAlignCenter.setObjectName("actionAlignCenter")
        self.actionAlignRight = QtGui.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/res/format-justify-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignRight.setIcon(icon24)
        self.actionAlignRight.setVisible(False)
        self.actionAlignRight.setObjectName("actionAlignRight")
        self.actionDoubleSpace = QtGui.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/res/format-line-spacing-double.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDoubleSpace.setIcon(icon25)
        self.actionDoubleSpace.setObjectName("actionDoubleSpace")
        self.actionSingleSpace = QtGui.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/res/format-line-spacing-normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSingleSpace.setIcon(icon26)
        self.actionSingleSpace.setObjectName("actionSingleSpace")
        self.actionStatistics = QtGui.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/res/view-statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStatistics.setIcon(icon27)
        self.actionStatistics.setObjectName("actionStatistics")
        self.actionDiction_Check = QtGui.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/res/diction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDiction_Check.setIcon(icon28)
        self.actionDiction_Check.setObjectName("actionDiction_Check")
        self.actionCut = QtGui.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/res/editcut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon29)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(MainWindow)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/res/editcopy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon30)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(MainWindow)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/res/editpaste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon31)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCheck_for_Updates = QtGui.QAction(MainWindow)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/res/system-software-update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCheck_for_Updates.setIcon(icon32)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.actionSaveDebugLog = QtGui.QAction(MainWindow)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/res/debug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveDebugLog.setIcon(icon33)
        self.actionSaveDebugLog.setObjectName("actionSaveDebugLog")
        self.menuToolbars.addAction(self.actionEnableFileToolbar)
        self.menuToolbars.addAction(self.actionEnableEditToolbar)
        self.menuToolbars.addAction(self.actionEnableSpeakerToolbar)
        self.menuToolbars.addAction(self.actionEnableImageToolbar)
        self.menuView.addAction(self.menuToolbars.menuAction())
        self.menuView.addAction(self.actionDistractionFree)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionClose)
        self.menuTools.addAction(self.actionSpeak)
        self.menuTools.addAction(self.actionStatistics)
        self.menuTools.addAction(self.actionDiction_Check)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCheck_for_Updates)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuHelp.addAction(self.actionSaveDebugLog)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionBold)
        self.menuEdit.addAction(self.actionItalic)
        self.menuEdit.addAction(self.actionUnderline)
        self.menuEdit.addAction(self.actionDoubleSpace)
        self.menuEdit.addAction(self.actionSingleSpace)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.fileToolBar.addAction(self.actionOpen)
        self.fileToolBar.addAction(self.actionSave)
        self.fileToolBar.addAction(self.actionSave_As)
        self.fileToolBar.addAction(self.actionPrint)
        self.editToolBar.addAction(self.actionBold)
        self.editToolBar.addAction(self.actionItalic)
        self.editToolBar.addAction(self.actionUnderline)
        self.editToolBar.addAction(self.actionAlignLeft)
        self.editToolBar.addAction(self.actionAlignCenter)
        self.editToolBar.addAction(self.actionAlignRight)
        self.editToolBar.addAction(self.actionHighlight)
        self.editToolBar.addAction(self.actionHighlightMode)
        self.editToolBar.addSeparator()
        self.speakToolBar.addAction(self.actionSpeak)
        self.speakToolBar.addAction(self.actionStop)
        self.speakToolBar.addSeparator()
        self.sizeLabel.setBuddy(self.spinBoxFontSize)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.actionEnableEditToolbar, QtCore.SIGNAL("toggled(bool)"), self.editToolBar.setVisible)
        QtCore.QObject.connect(self.actionEnableFileToolbar, QtCore.SIGNAL("toggled(bool)"), self.fileToolBar.setVisible)
        QtCore.QObject.connect(self.actionEnableSpeakerToolbar, QtCore.SIGNAL("toggled(bool)"), self.speakToolBar.setVisible)
        QtCore.QObject.connect(self.actionUndo, QtCore.SIGNAL("triggered()"), self.textArea.undo)
        QtCore.QObject.connect(self.actionRedo, QtCore.SIGNAL("triggered()"), self.textArea.redo)
        QtCore.QObject.connect(self.textArea, QtCore.SIGNAL("undoAvailable(bool)"), self.actionUndo.setEnabled)
        QtCore.QObject.connect(self.textArea, QtCore.SIGNAL("redoAvailable(bool)"), self.actionRedo.setEnabled)
        QtCore.QObject.connect(self.actionCopy, QtCore.SIGNAL("triggered()"), self.textArea.copy)
        QtCore.QObject.connect(self.actionCut, QtCore.SIGNAL("triggered()"), self.textArea.cut)
        QtCore.QObject.connect(self.actionPaste, QtCore.SIGNAL("triggered()"), self.textArea.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.spinBoxFontSize, self.fontComboBox)
        MainWindow.setTabOrder(self.fontComboBox, self.textArea)
        MainWindow.setTabOrder(self.textArea, self.spellingSuggestionsList)
        MainWindow.setTabOrder(self.spellingSuggestionsList, self.distractionButton)
        MainWindow.setTabOrder(self.distractionButton, self.nextButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.dictionCloseButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.distractionButton.setText(QtGui.QApplication.translate("MainWindow", "Go Back ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuToolbars.setTitle(QtGui.QApplication.translate("MainWindow", "Toolbars", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.fileToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.editToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.speakToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Speak text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("MainWindow", "Save As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBold.setText(QtGui.QApplication.translate("MainWindow", "Bold", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBold.setToolTip(QtGui.QApplication.translate("MainWindow", "Bold", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBold.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionItalic.setText(QtGui.QApplication.translate("MainWindow", "Italic", None, QtGui.QApplication.UnicodeUTF8))
        self.actionItalic.setToolTip(QtGui.QApplication.translate("MainWindow", "Italic", None, QtGui.QApplication.UnicodeUTF8))
        self.actionItalic.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnderline.setText(QtGui.QApplication.translate("MainWindow", "Underline", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnderline.setToolTip(QtGui.QApplication.translate("MainWindow", "Underline", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnderline.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSpeak.setText(QtGui.QApplication.translate("MainWindow", "Speak", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSpeak.setToolTip(QtGui.QApplication.translate("MainWindow", "Speak Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setToolTip(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setToolTip(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnableFileToolbar.setText(QtGui.QApplication.translate("MainWindow", "File Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnableFileToolbar.setToolTip(QtGui.QApplication.translate("MainWindow", "Enable File Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnableEditToolbar.setText(QtGui.QApplication.translate("MainWindow", "Edit Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnableEditToolbar.setToolTip(QtGui.QApplication.translate("MainWindow", "Enable Edit Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnableSpeakerToolbar.setText(QtGui.QApplication.translate("MainWindow", "Speaker Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnableSpeakerToolbar.setToolTip(QtGui.QApplication.translate("MainWindow", "Enable Speaker Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setText(QtGui.QApplication.translate("MainWindow", "Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About WriteType", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setToolTip(QtGui.QApplication.translate("MainWindow", "About WriteType", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setToolTip(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHighlightMode.setText(QtGui.QApplication.translate("MainWindow", "Highlight Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHighlightMode.setToolTip(QtGui.QApplication.translate("MainWindow", "Highlight Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHighlight.setText(QtGui.QApplication.translate("MainWindow", "Highlight", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHighlight.setToolTip(QtGui.QApplication.translate("MainWindow", "Highlight", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDistractionFree.setText(QtGui.QApplication.translate("MainWindow", "Distraction Free", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDistractionFree.setToolTip(QtGui.QApplication.translate("MainWindow", "Distraction Free Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_Image.setText(QtGui.QApplication.translate("MainWindow", "Insert Image", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlign_Image_Left.setText(QtGui.QApplication.translate("MainWindow", "Align Image Left", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlign_Image_Right.setText(QtGui.QApplication.translate("MainWindow", "Align Image Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnableImageToolbar.setText(QtGui.QApplication.translate("MainWindow", "Image Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignLeft.setText(QtGui.QApplication.translate("MainWindow", "Align Left", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignCenter.setText(QtGui.QApplication.translate("MainWindow", "Align Center", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignRight.setText(QtGui.QApplication.translate("MainWindow", "Align Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDoubleSpace.setText(QtGui.QApplication.translate("MainWindow", "Double Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSingleSpace.setText(QtGui.QApplication.translate("MainWindow", "Single Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStatistics.setText(QtGui.QApplication.translate("MainWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDiction_Check.setText(QtGui.QApplication.translate("MainWindow", "Diction Check", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_for_Updates.setText(QtGui.QApplication.translate("MainWindow", "Check for Updates", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveDebugLog.setText(QtGui.QApplication.translate("MainWindow", "Save Debug Log", None, QtGui.QApplication.UnicodeUTF8))

from spellCheckEdit import spellCheckEdit
from listWidget import ListWidget
import resources_rc
