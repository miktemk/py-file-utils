# Apprends a timestamp, e.g. `... 20150809_125758` to the file dragged in, based on the current time
#
# **MODE OF USE**: Drag and drop.
#
# 1. Drag a file (e.g. `abc.txt`) into it
# 2. Will generate `abc_20150809_125758.txt`, depending on the time and day, of course
# 3. NOTE: Change the DELIMETER constant as needed

import sys, os
import shutil
from datetime import datetime

DELIMETER = '_'

#DEBUG: sample command line argument for debugging with Sublime+REPL
#sys.argv = [sys.argv[0], "README.md"]

# command line options: note the first line parameter and the if statements below
if len(sys.argv) <= 1:
	print("Usage: drag the file in and enter a nummar!")
	exit(1)

argFname = sys.argv[1]
noext, ext = os.path.splitext(argFname)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

shutil.move(argFname, noext + DELIMETER + timestamp + ext)

