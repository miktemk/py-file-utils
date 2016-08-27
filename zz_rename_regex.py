# **MODE OF USE**: Run in a folder
#
#  - tweak reSearch and reReplace before running this script
#  - use regex101.com to figure it out

import sys, os, re
import time, datetime, shutil
import getopt

reSearch = r'(.*)-(\d+-\d+-\d+)(.*)'
reReplace = r'\2-\1\3'

listFiles = os.listdir(".")
extsOut = [".py", ".bat", ".dll", ".exe", ".md"]
for fname in listFiles:
	if os.path.isdir("./"+fname):
		continue
	noext, ext = os.path.splitext(fname)
	if ext in extsOut:
		continue
	if re.search(reSearch, fname):
		destination = re.sub(reSearch, reReplace, fname)
		print(fname, destination)
		os.rename(fname, destination)
