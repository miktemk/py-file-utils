# Apprends _# to each file
#
# **MODE OF USE**: Drag and drop.
#
# 1. Drag a file (e.g. `abc.txt`) into it
# 2. Enter start index X
# 3. Enter end index Y
# 4. Will generate files named `abc_X.txt`, ... `abc_5.txt`, `abc_6.txt`, ... and `abc_Y.txt`, all copies of `abc.txt`. Notice how the the range [X..Y] is X,Y-inclusive

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

indexStart = input("start index: ")
indexEnd = input("end index: ")
indexStart = int(indexStart)
indexEnd = int(indexEnd)
filename, fileExtension = os.path.splitext(argFname)






print(indexStart, indexEnd)

for i in range(indexStart, indexEnd+1):
	destination = filename + "_" + str(i) + fileExtension
	print(argFname, destination)
	shutil.copyfile(argFname, destination)
