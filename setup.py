from distutils.core import setup
from os import listdir
import glob
import os.path
import sys
from platform import system

#Settings for all platforms
data_files_value = [(os.path.join(sys.prefix, 'share', 'writetype', 'res'), glob.glob('res/*')),
                    (os.path.join(sys.prefix, 'share', 'writetype', 'wordlists'), glob.glob('wordlists/*')),
                    (os.path.join(sys.prefix, 'share', 'writetype', 'translations'), glob.glob('translations/*')),
                    (os.path.join(sys.prefix, 'share', 'writetype'), ['platformSettings.ini']),
                    (os.path.join(sys.prefix, 'share', 'applications'), ['writetype.desktop'])]
options_value = {}
windows_value = []

#Settings for Windows only
if system() == "Windows":
    import py2exe
    import enchant
    data_files_value += enchant.utils.win32_data_files()
    options_value["py2exe"] = {
                    "includes":["sip", "pyttsx.drivers.sapi5"], 
                    "bundle_files":1,
                    "optimize":2,
                    "typelibs" : [('{C866CA3A-32F7-11D2-9602-00C04F8EE628}', 0, 5, 0)]
    }
    windows_value += [{"script": 'writetype/main.py',
                       "icon_resources": [(1, 'res/writetype.ico')]}]

#Setup!
setup(
    name = 'WriteType',
    version = '1.3.163',
    description = 'A program to help young students type more easily.',
    long_description = 'WriteType is a simple word processor designed to help young students type more easily and accurately.  It offers spelling suggestions as students type, making the process easier and less frustrating.  It also provides the ability to read back text through either an eSpeak or a Festival backend.',
    author = 'Max Shinn',
    author_email = 'max@bernsteinforpresident.com',
    url = 'http://writetype.bernsteinforpresident.com',
    packages = ['writetype'],
    scripts = ['scripts/writetype'],
    data_files = data_files_value,
    windows = windows_value,
    options = options_value,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License',
        'Natural Language :: English',
        'Natural Language :: Dutch',
        'Natural Language :: Spanish',
        'Natural Language :: Russian',
        'Natural Language :: Bulgarian',
        'Natural Language :: Italian',
        'Natural Language :: Basque',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Topic :: Education',
        ],
    requires = ['PyQt4', 'enchant', 'pyttsx']
    )
