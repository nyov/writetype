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
import traceback

_logs = []
DEBUGGING_MODE = False

def log(description, logtype="Default"):
    function = inspect.stack()[1][3]
    line = str(inspect.stack()[1][2])
    filename = inspect.stack()[1][1].split(os.sep).pop()
    _logs.append((logtype, function, line, filename, description))

    if DEBUGGING_MODE == True:
        print logtype + ": from " + function + " line " + line + " in " + filename + " - " + description

def formatLog(printlogtype=None):
    formattedlog = ""
    formattedlog += "===DEBUGGING LOG===\n"
    for logtype, function, line, filename, description in _logs:
        if logtype == logtype or printlogtype == None:
            formattedlog += logtype + ": from " + function + " line " + line + " in " + filename + " - " + description + "\n"
    return formattedlog
