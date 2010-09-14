translation:
	pylupdate4 writetype/*.py -ts translations/writetype.ts translations/qt_nl_NL.ts translations/qt_es_AR.ts translations/qt_eu_ES.ts
	lrelease-qt4 translations/qt_nl_NL.ts -qm translations/qt_nl_NL.qm
	lrelease-qt4 translations/qt_es_AR.ts -qm translations/qt_es_AR.qm
	lrelease-qt4 translations/qt_eu_ES.ts -qm translations/qt_eu_ES.qm
	#Other spanish locales too?
	cp translations/qt_es_AR.qm translations/qt_es_ES.qm
	cp translations/qt_es_AR.qm translations/qt_es_MX.qm

revno:
	printf "aboutrevno = `bzr revno`" > writetype/revno.py

changelog:
	bzr log > CHANGELOG

gui:
	pyuic4 ui/mainwindow.ui -o writetype/mainwindow.py
	pyuic4 ui/distractionfree.ui -o writetype/distractionFree.py
	pyuic4 ui/settings.ui -o writetype/settingsDialog.py
	pyuic4 ui/statistics.ui -o writetype/statistics.py

rc:
	pyrcc4 res/resources.qrc -o writetype/resources_rc.py

all: translation revno gui rc changelog
