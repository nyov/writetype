DATADIR = $(DESTDIR)/usr/share/writetype
BINDIR = $(DESTDIR)/usr/bin
ICONDIR = $(DESTDIR)/usr/share/applications

translation:
	pylupdate4 writetype/*.py -ts translations/writetype.ts translations/qt_nl_NL.ts translations/qt_es.ts translations/qt_eu_ES.ts translations/qt_ru.ts
	lrelease-qt4 translations/qt_nl_NL.ts -qm translations/qt_nl_NL.qm
	lrelease-qt4 translations/qt_es.ts -qm translations/qt_es.qm
	lrelease-qt4 translations/qt_eu_ES.ts -qm translations/qt_eu_ES.qm
	lrelease-qt4 translations/qt_ru.ts -qm translations/qt_ru.qm

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

clean:
	rm -f writetype/*.py[co]

install:
	mkdir -p $(DATADIR)
	mkdir -p $(BINDIR)
	cp -r writetype $(DATADIR)/
	cp -r wordlists $(DATADIR)/
	cp -r res $(DATADIR)/
	cp -r translations $(DATADIR)/
	cp platformSettings.ini $(DATADIR)/
	cp scripts/writetype $(BINDIR)/writetype
	cp writetype.desktop $(ICONDIR)/writetype.desktop

uninstall:
	rm -rf $(DATADIR)
	rm -rf $(BINDIR)/writetype
	rm -rf $(ICONDIR)/writetype.desktop
