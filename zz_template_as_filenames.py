# **MODE OF USE**: Drag and drop.
#
# 1. create a subfolder in the directory with your files
# 2. put __template.png in the subfolder + this python script
# 3. run this python script from the subfolder

import sys, os, re
import time, datetime, shutil
import getopt

# --------- config ---------
DIR_SRC = ".."
DIR_DEST = "."
TEMPLATE = "__template.png"


dirname = DIR_SRC
dirList = os.listdir(dirname)
for fname in dirList:
	if fname == os.path.basename(__file__):
		continue
	if fname == "ZZZrun.bat":
		continue
	fullPath = dirname + "\\" + fname
	if not os.path.isdir(fullPath):
		print (fname);
		shutil.copyfile(DIR_DEST + "/" + TEMPLATE, DIR_DEST + "/" + fname)
