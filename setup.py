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
                    "includes":["sip"], 
                    "bundle_files":1,
                    "typelibs" : [('{C866CA3A-32F7-11D2-9602-00C04F8EE628}', 0, 5, 0)]
    }
    windows_value += ['scripts/writetype']

#Setup!
setup(
    name = 'WriteType',
    version = '1.0.98',
    description = 'A program to help young students type more easily.',
    long_description = 'WriteType is a simple word processor designed to help young students type more easily and accurately.  It offers spelling suggestions as students type, making the process easier and less frustrating.  It also provides the ability to read back text through either an eSpeak or a Festival backend.  In addition, there are special tools for teachers, and the entire application is easily translatable.',
    author = 'Max Shinn',
    author_email = 'max@bernsteinforpresident.com',
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
    requires = ['PyQt4', 'enchant']
    )
