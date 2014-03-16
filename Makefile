DATADIR = $(DESTDIR)/usr/share/writetype
BINDIR = $(DESTDIR)/usr/bin
ICONDIR = $(DESTDIR)/usr/share/applications

all: ui res translations revno changelog

translations: $(foreach tsfile, $(wildcard translations/qt_*.ts), $(basename $(tsfile)).qm)
	pylupdate4 writetype/*.py -ts translations/writetype.ts  
	lconvert -of po -o translations/new_qt_eu_ES.po translations/new_qt_eu_ES.ts

translations/%.qm:
	cp $(basename $@).ts translations/new_$(notdir $(basename $@)).ts
	pylupdate4 writetype/*.py -ts translations/new_$(notdir $(basename $@)).ts
	lrelease-qt4 $(basename $@).ts -qm $@ 

revno:
	printf "aboutrevno = `bzr revno`" > writetype/revno.py

changelog:
	bzr log > CHANGELOG

ui: $(foreach uifile, $(wildcard ui/*.ui), writetype/ui_$(basename $(notdir $(uifile))).py)

writetype/ui_%.py:
	pyuic4 ui/$(basename $(notdir $(subst ui_, , $@))).ui -o $@

res:
	pyrcc4 res/resources.qrc -o writetype/resources_rc.py

clean:
	rm -f writetype/*.py[co]
	rm -f translations/new_qt_*.ts
	rm -f translations/qt_*.qm
	rm -f writetype/ui_*.py
	rm -f writetype/resources_rc.py
	rm -f CHANGELOG

install:
	mkdir -p $(DATADIR)
	mkdir -p $(BINDIR)
	cp -r writetype $(DATADIR)/
	cp -r wordlists $(DATADIR)/
	cp -r res $(DATADIR)/
	mkdir -p $(DATADIR)/translations
	cp -r translations/*.qm $(DATADIR)/translations/
	cp platformSettings.ini $(DATADIR)/
	cp scripts/writetype $(BINDIR)/writetype
	cp writetype.desktop $(ICONDIR)/writetype.desktop

uninstall:
	rm -rf $(DATADIR)
	rm -rf $(BINDIR)/writetype
	rm -rf $(ICONDIR)/writetype.desktop

.PHONY: translations revno ui res changelog
