# Place this script into "convert" directory of zz_mp3_convert_makeBatFile.py
# and run it for audiobooks. Note: files must end with _0001.mp3, _0002.mp3, etc

import sys, os, re, shutil
import getopt
import time, datetime

# .... match TTS Utility's filename format (for long audiobooks). group(1)
# .... example: fname = casanova-ru_0001.mp3 => group(1) = casanova-ru
regexBookName = "(.*?)(_|-)(\d+.*)\.mp3$"

listOfAllBookNames = []

# .... list directory contents
cwd = "."
for fname in os.listdir(cwd):
	# .... skip this python script
	if fname == os.path.basename(__file__):
		continue
	fullPath = os.path.join(cwd, fname)
	if os.path.isdir(fullPath):
		continue
	moBookName = re.match(regexBookName, fname)
	if moBookName == None:
		continue
	bookName = moBookName.group(1)
	if bookName not in listOfAllBookNames:
		listOfAllBookNames += [bookName]

for bFolder in listOfAllBookNames:
	folder2B = os.path.join(".", bFolder)
	if not os.path.exists(folder2B):
		print ("making folder", folder2B)
		os.makedirs(folder2B)
	# .... move files to this folder
	for fname in os.listdir(cwd):
		fullPath = os.path.join(cwd, fname)
		if os.path.isdir(fullPath):
			continue
		moBookName = re.match(regexBookName, fname)
		if moBookName == None:
			continue
		fullPath2 = os.path.join(folder2B, fname)
		if fname.startswith(bFolder):
			print (fullPath, " -> ", fullPath2)
			os.rename(fullPath, fullPath2)
