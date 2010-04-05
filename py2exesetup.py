
from distutils.core import setup
import py2exe
import enchant

setup(
	windows=['main.py'],
	data_files = enchant.utils.win32_data_files(),
	options = {"py2exe": {
		"includes":["sip"], 
		"packages":["pyttsx"], 
		"bundle_files":1,
		"typelibs" : [('{C866CA3A-32F7-11D2-9602-00C04F8EE628}', 0, 5, 0)]
	}}
)
