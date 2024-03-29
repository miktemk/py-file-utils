# Prepends a timestamp, e.g. `20150809_125758_...` to the file dragged in, based on the current time + prompts for custom suffix
# NOTE: original filename will be completely gone
#
# **MODE OF USE**: Drag and drop.
#
# 1. Drag a file (e.g. `abc.txt`) into it
# 2. Will generate `20150809_125758 this is me doodling.txt`, depending on the time and day, of course
# 3. NOTE: Change the DELIMETER constant as needed

import sys, os, re
import shutil
from datetime import datetime

DELIMETER = ' - '

#DEBUG: sample command line argument for debugging with Sublime+REPL
#sys.argv = [sys.argv[0], "README.md"]

# command line options: note the first line parameter and the if statements below
if len(sys.argv) <= 1:
	print("Usage: drag the file in and enter a nummar!")
	exit(1)

description = input("WAZDIZ: ")
description = re.sub('[\\\/:*?"<>|]', '', description) # A filename cannot contain any of the following characters: \ / : * ? " < > | https://regex101.com/r/AA4mot/1

argFname = sys.argv[1]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
(noext, ext) = os.path.splitext(os.path.basename(argFname))
targetFname = os.path.join(os.path.dirname(argFname), timestamp + DELIMETER + description + ext)

shutil.move(argFname, targetFname)
