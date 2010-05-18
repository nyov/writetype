from distutils.core import setup
from os import listdir
import glob
import os.path
import sys

setup(
    name = 'WriteType',
    version = '0.1.53',
    description = 'A program to help people type more easily.',
    author = 'Max Shinn',
    author_email = 'trombonechamp@gmail.com',
    url = 'http://bernsteinforpresident.com/software/writetype',
    packages = ['writetype'],
    scripts = ['scripts/writetype'],
    data_files = [(os.path.join(sys.prefix, 'share', 'writetype', 'res'), glob.glob('res/*')),
                  (os.path.join(sys.prefix, 'share', 'writetype', 'wordlists'), glob.glob('wordlists/*')),
                  (os.path.join(sys.prefix, 'share', 'writetype'), ['platformSettings.ini']),
                  (os.path.join(sys.prefix, 'share', 'applications'), ['writetype.desktop'])],
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License',
        'Natural Language :: English',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Topic :: Education',
        ],
    requires = ['PyQt4', 'pyttsx', 'enchant']
    )

