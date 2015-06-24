# apprends _# to each file

import sys, os, re
import time, datetime, shutil
import getopt

prefix = input("Add filename prefix: ")

listFiles = os.listdir(".")
extsOut = [".py", ".bat", ".dll", ".exe", ".md"]
for fname in listFiles:
	if os.path.isdir("./"+fname):
		continue
	noext, ext = os.path.splitext(fname)
	if ext in extsOut:
		continue
	destination = prefix + "_" + fname
	print(fname, destination)
	os.rename(fname, destination)
