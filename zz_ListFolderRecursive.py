# **MODE OF USE**: Run in a folder OR drag and drop a folder into me
#
# Generates a txt file with all the contents of this folder (recursive)
#
#  - if run in a folder -> generates `zz_fileListingRecursive.txt`
#  - if drag and drop -> generates `folder name` + `.recursivelist.txt`

import sys, os, shutil
import getopt, codecs
from os import path

ignoreList = [\
	"zz_ListFolderRecursive.py", \
	"zz_fileListingRecursive.txt",\
	".git",\
	".svn-base$",\
	".class$",\
	".sfk$",\
	".vf.bak$",\
	".metadata.plugins",\
	"$RECYCLE.BIN", "System Volume Information"]

os.path.dirname(os.path.abspath(__file__)) # .... set . to CWD (good practice)
#sys.argv = ["exe", "C:\\Users\\miktemk\\Music\\Abook\\Frai_Bolshaya_telega_[tfile.ru]"] # .... debug tests

def isInIgnoreLit(fullName):
	global ignoreList
	for pattern in ignoreList:
		if pattern.endswith("$"):
			if fullName.endswith(pattern[:-1]):
				return True
		else:
			if pattern in fullName:
				return True
	return False

def ListFolder(folder, fOut):
	dirList = sorted(os.listdir(folder))
	for fname in dirList:
		fullName = path.join(folder, fname)
		if path.isdir(fullName):
			try:
				ListFolder(fullName, fOut)
			except PermissionError:
				print("could not read dir", fullName)
		else:
			#print (fullName.encode('utf-8'))
			if isInIgnoreLit(fullName):
				continue
			fOut.write(fullName + "\n")

targetDir = "."
outFilename = path.join(targetDir, "zz_fileListingRecursive.txt") # .... run in a folder

# .... drag and drop
optlist, args = getopt.getopt(sys.argv[1:], "o:", ["output="])
if len(args) > 0:
	targetDir = args[0]
	outFilename = targetDir + ".recursivelist.txt"
for o, a in optlist:
    if o in ("-o", "--output"):
        outFilename = a

#targetDir = "C:\\Users\\Mikhail\\Pictures\\2015_02_italia" # .... debug tests

fOut = codecs.open(outFilename, "w", "utf-8")
ListFolder(targetDir, fOut)
fOut.close()
