# **MODE OF USE**: Run in a folder
#
# WARNING!!! Will rename all files in the folder where this script is run.
#
# Enter prefix. Let's say you entered "newfilename". All the files will be renamed to `newfilename_1.txt`, `newfilename_2.mp3`, ... for all files in the folder, in the order of alphabet, I guess.
#
# EXCEPTED: `.exe`, `.dll`, `.py`, `.bat`, folders

import sys, os, re
import time, datetime, shutil
import getopt

prefix = input("filename prefix: ")

listFiles = os.listdir(".")
extsOut = [".py", ".bat", ".dll", ".exe", ".md"]
i = 1
for fname in listFiles:
	if os.path.isdir("./"+fname):
		continue
	noext, ext = os.path.splitext(fname)
	if ext in extsOut:
		continue
	destination = prefix + "_" + str(i) + ext
	print(fname, destination)
	os.rename(fname, destination)
	i += 1
