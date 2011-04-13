# Copyright 2011 Max Shinn

# This file is part of WriteType.

# WriteType is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# WriteType is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with WriteType.  If not, see <http://www.gnu.org/licenses/>.

import inspect
import os
import traceback, sys

_logs = []
_tracebacks = []
_wordslist = None
DEBUGGING_MODE = False


def init(wl = None):
    global _wordslist
    _wordslist = wl

def log(*args, **kargs):
    """Log whatever we find in the arguments (for performance) to the log file"""
    global _tracebacks
    if "logtype" in kargs:
        logtype = kargs['logtype']
    else:
        logtype = "Default"
    if "tb" in kargs:
        if kargs["tb"] == True:
            _tracebacks.append(traceback.format_exc())
            if DEBUGGING_MODE == True:
                print traceback.format_exc()
    description = ''.join(args)
    function = inspect.stack()[1][3]
    line = str(inspect.stack()[1][2])
    filename = inspect.stack()[1][1].split(os.sep).pop()
    _logs.append((logtype, function, line, filename, description))

    if DEBUGGING_MODE == True:
        print logtype + ": from " + function + " line " + line + " in " + filename + " - " + description

def formatLog(printlogtype=None):
    """Format the log to be saved or printed"""
    formattedlog = u""
    formattedlog += "===DEBUGGING LOG===\n"
    for logtype, function, line, filename, description in _logs:
        if logtype == logtype or printlogtype == None:
            formattedlog += ''.join([logtype, ": from ", function, " line ", line, " in ", filename, " - ", description, "\n"])
    global _wordslist
    if _wordslist != None:
        formattedlog += "\n\n===WORDS DUMP===\n"
        formattedlog += _wordslist.dump()
        formattedlog += "\n\n===WORD PATTERN DUMP===\n"
        formattedlog += _wordslist.pattern.dump()
    if _tracebacks:
        formattedlog += "\n\n===TRACEBACKS===\n"
        for tb in _tracebacks:
            formattedlog += tb
            
    return formattedlog
