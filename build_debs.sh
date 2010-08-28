#!/bin/sh
rm -r deb_dist
python setup.py --command-packages=stdeb.command sdist_dsc --force-buildsystem=False
cd deb_dist/*
sed 's/${python:Depends}/python (>= 2.5), python-support (>= 0.7.1)/' debian/control > debian/control2
rm debian/control
mv debian/control2 debian/control
dpkg-buildpackage -rfakeroot 
dpkg-buildpackage -S
