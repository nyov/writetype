#!/bin/sh
rm -r deb_dist
python setup.py --command-packages=stdeb.command sdist_dsc
cd deb_dist/writetype-0.0.3
dpkg-buildpackage -rfakeroot
dpkg-buildpackage -S
