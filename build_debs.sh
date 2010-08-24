#!/bin/sh
rm -r deb_dist
python setup.py --command-packages=stdeb.command sdist_dsc
cd deb_dist/*
dpkg-buildpackage -rfakeroot
dpkg-buildpackage -S
