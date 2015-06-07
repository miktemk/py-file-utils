# apprends _# to each file

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
