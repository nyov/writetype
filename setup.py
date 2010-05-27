from distutils.core import setup
from os import listdir
import glob
import os.path
import sys
from platform import system

#Settings for all platforms
data_files_value = [(os.path.join(sys.prefix, 'share', 'writetype', 'res'), glob.glob('res/*')),
                    (os.path.join(sys.prefix, 'share', 'writetype', 'wordlists'), glob.glob('wordlists/*')),
                    (os.path.join(sys.prefix, 'share', 'writetype'), ['platformSettings.ini']),
                    (os.path.join(sys.prefix, 'share', 'applications'), ['writetype.desktop'])]
options_value = {}
windows_value = []

#Settings for Windows only
if system() == "Windows":
    import py2exe
    import enchant
    data_files_value += enchant.utils.win32_data_files()
    options_value += {"py2exe": {
                    "includes":["sip"], 
                    "packages":["pyttsx"], 
                    "bundle_files":1,
                    "typelibs" : [('{C866CA3A-32F7-11D2-9602-00C04F8EE628}', 0, 5, 0)]
    }}
    windows_value += ['main.py']
setup(
    name = 'WriteType',
    version = '0.1.53',
    description = 'A program to help people type more easily.',
    author = 'Max Shinn',
    author_email = 'trombonechamp@gmail.com',
    url = 'http://bernsteinforpresident.com/software/writetype',
    packages = ['writetype'],
    scripts = ['scripts/writetype'],
    data_files = data_files_value,
    windows = windows_value,
    options = options_value,
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

