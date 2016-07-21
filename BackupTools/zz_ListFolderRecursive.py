# **MODE OF USE**: Run in a folder OR drag and drop a folder into me
#
# Generates a txt file with all the contents of this folder (recursive)
#
#  - if run in a folder -> generates `zz_fileListingRecursive.txt`
#  - if drag and drop -> generates `folder name` + `.recursivelist.txt`

import sys, os, shutil
import getopt, codecs
from os import path

os.path.dirname(os.path.abspath(__file__)) # .... set . to CWD (good practice)
#sys.argv = ["exe", "C:\\Users\\Mikhail\\Documents\\GitHub\\py\\py-file-utils\\BackupTools\\test"] # .... debug tests

def ListFolder(folder, fOut):
	dirList = os.listdir(folder)
	for fname in dirList:
		fullName = path.join(folder, fname)
		if path.isdir(fullName):
			ListFolder(fullName, fOut)
		else:
			#print (fullName.encode('utf-8'))
			fOut.write(fullName + "\n")

targetDir = "."
outFilename = path.join(targetDir, "zz_fileListingRecursive.txt") # .... run in a folder

# .... drag and drop
optlist, args = getopt.getopt(sys.argv[1:], "")
if len(args) > 0:
	targetDir = args[0]
	outFilename = targetDir + ".recursivelist.txt"

#targetDir = "C:\\Users\\Mikhail\\Pictures\\2015_02_italia" # .... debug tests

fOut = codecs.open(outFilename, "w", "utf-8")
ListFolder(targetDir, fOut)
fOut.close()
