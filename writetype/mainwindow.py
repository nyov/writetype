# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Mon May  3 14:57:37 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/key22x22.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
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
        self.spellingSuggestionsList = QtGui.QListWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spellingSuggestionsList.sizePolicy().hasHeightForWidth())
        self.spellingSuggestionsList.setSizePolicy(sizePolicy)
        self.spellingSuggestionsList.setMaximumSize(QtCore.QSize(300, 16777215))
        self.spellingSuggestionsList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.spellingSuggestionsList.setObjectName("spellingSuggestionsList")
        self.verticalLayout.addWidget(self.splitter)
        self.distractionButton = QtGui.QPushButton(self.centralwidget)
        self.distractionButton.setObjectName("distractionButton")
        self.verticalLayout.addWidget(self.distractionButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuToolbars = QtGui.QMenu(self.menuView)
        self.menuToolbars.setObjectName("menuToolbars")
        self.menuHelo = QtGui.QMenu(self.menubar)
        self.menuHelo.setObjectName("menuHelo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileToolBar = QtGui.QToolBar(MainWindow)
        self.fileToolBar.setObjectName("fileToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.fileToolBar)
        self.editToolBar = QtGui.QToolBar(MainWindow)
        self.editToolBar.setObjectName("editToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.editToolBar)
        self.speakToolBar = QtGui.QToolBar(MainWindow)
        self.speakToolBar.setObjectName("speakToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.speakToolBar)
        self.imageToolBar = QtGui.QToolBar(MainWindow)
        self.imageToolBar.setObjectName("imageToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.imageToolBar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/filesave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon2)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/res/fileclose.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/res/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon4)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSettings = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/res/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon5)
        self.actionSettings.setObjectName("actionSettings")
        self.actionBold = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/res/text_bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon6)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/res/text_italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon7)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/res/text_under.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon8)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionSpeak = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/res/voicecall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpeak.setIcon(icon9)
        self.actionSpeak.setObjectName("actionSpeak")
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/res/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon10)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/res/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon11)
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
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAboutQt = QtGui.QAction(MainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionPrint = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/res/fileprint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon12)
        self.actionPrint.setObjectName("actionPrint")
        self.actionHighlightMode = QtGui.QAction(MainWindow)
        self.actionHighlightMode.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/res/highlight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHighlightMode.setIcon(icon13)
        self.actionHighlightMode.setObjectName("actionHighlightMode")
        self.actionHighlight = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/res/highlight_single.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHighlight.setIcon(icon14)
        self.actionHighlight.setObjectName("actionHighlight")
        self.actionDistractionFree = QtGui.QAction(MainWindow)
        self.actionDistractionFree.setObjectName("actionDistractionFree")
        self.actionInsert_Image = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/res/key120x120.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsert_Image.setIcon(icon15)
        self.actionInsert_Image.setObjectName("actionInsert_Image")
        self.actionAlign_Image_Left = QtGui.QAction(MainWindow)
        self.actionAlign_Image_Left.setIcon(icon15)
        self.actionAlign_Image_Left.setObjectName("actionAlign_Image_Left")
        self.actionAlign_Image_Right = QtGui.QAction(MainWindow)
        self.actionAlign_Image_Right.setIcon(icon15)
        self.actionAlign_Image_Right.setObjectName("actionAlign_Image_Right")
        self.actionEnableImageToolbar = QtGui.QAction(MainWindow)
        self.actionEnableImageToolbar.setCheckable(True)
        self.actionEnableImageToolbar.setChecked(True)
        self.actionEnableImageToolbar.setObjectName("actionEnableImageToolbar")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionBold)
        self.menuEdit.addAction(self.actionItalic)
        self.menuEdit.addAction(self.actionUnderline)
        self.menuEdit.addAction(self.actionSpeak)
        self.menuToolbars.addAction(self.actionEnableFileToolbar)
        self.menuToolbars.addAction(self.actionEnableEditToolbar)
        self.menuToolbars.addAction(self.actionEnableSpeakerToolbar)
        self.menuToolbars.addAction(self.actionEnableImageToolbar)
        self.menuView.addAction(self.menuToolbars.menuAction())
        self.menuView.addAction(self.actionDistractionFree)
        self.menuHelo.addAction(self.actionDocumentation)
        self.menuHelo.addAction(self.actionAbout)
        self.menuHelo.addAction(self.actionAboutQt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelo.menuAction())
        self.fileToolBar.addAction(self.actionOpen)
        self.fileToolBar.addAction(self.actionSave)
        self.fileToolBar.addAction(self.actionSave_As)
        self.fileToolBar.addAction(self.actionPrint)
        self.editToolBar.addAction(self.actionBold)
        self.editToolBar.addAction(self.actionItalic)
        self.editToolBar.addAction(self.actionUnderline)
        self.editToolBar.addAction(self.actionHighlight)
        self.editToolBar.addAction(self.actionHighlightMode)
        self.speakToolBar.addAction(self.actionSpeak)
        self.imageToolBar.addAction(self.actionInsert_Image)
        self.imageToolBar.addAction(self.actionAlign_Image_Left)
        self.imageToolBar.addAction(self.actionAlign_Image_Right)
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
        QtCore.QObject.connect(self.actionEnableImageToolbar, QtCore.SIGNAL("toggled(bool)"), self.imageToolBar.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeLabel.setText(QtGui.QApplication.translate("MainWindow", "Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.distractionButton.setText(QtGui.QApplication.translate("MainWindow", "Go Back ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuToolbars.setTitle(QtGui.QApplication.translate("MainWindow", "Toolbars", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelo.setTitle(QtGui.QApplication.translate("MainWindow", "Helo", None, QtGui.QApplication.UnicodeUTF8))
        self.fileToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.editToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.speakToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.imageToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
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

from spellCheckEdit import spellCheckEdit
import resources_rc