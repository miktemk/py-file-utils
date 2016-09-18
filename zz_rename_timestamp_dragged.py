# Apprends a timestamp, e.g. `_20150809_125758` to the file dragged in, based on the current time
#
# **MODE OF USE**: Drag and drop.
#
# 1. Drag a file (e.g. `abc.txt`) into it
# 2. Will generate `abc_20150809_125758.txt`, depending on the time and day, of course

import sys, os, re
import time, datetime, shutil
import getopt

#DEBUG: sample command line argument for debugging with Sublime+REPL
#sys.argv = [sys.argv[0], "README.md"]

# command line options: note the first line parameter and the if statements below
if len(sys.argv) <= 1:
	print("Usage: drag the file in and enter a nummar!")
	exit(1)

argFname = sys.argv[1]

today = datetime.date.today()
month = str(today.month).zfill(2)
day = str(today.day).zfill(2)
todayTime = datetime.datetime.now()
hour = str(todayTime.hour).zfill(2)
minute = str(todayTime.minute).zfill(2)
second = str(todayTime.second).zfill(2)
timestamp = str(today.year) + month + day + "_" + hour + minute + second

noext, ext = os.path.splitext(argFname)

shutil.move(argFname, noext + "_" + timestamp + ext)
