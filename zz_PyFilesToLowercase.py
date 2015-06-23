# Renames all files to lowercase. Works only on one level of the folder

import sys, os, shutil

SRC_ROOT = "./"

def processFolder(pathS):
	dirList = os.listdir(pathS)
	for fname in dirList:
		fullPathS = pathS + "/" + fname
		if not os.path.isdir(fullPathS):
			fnameFinal = fullPathS.lower()
			print fnameFinal
			os.rename(fullPathS, fnameFinal)

processFolder(SRC_ROOT)
