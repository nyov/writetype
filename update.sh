#!/bin/bash

#Update ui files
pyuic4 ui/mainwindow.ui -o writetype/mainwindow.py
pyuic4 ui/distractionfree.ui -o writetype/distractionFree.py
pyuic4 ui/settings.ui -o writetype/settingsDialog.py

#Update qrc file
pyrcc4 res/resources.qrc -o writetype/resources_rc.py