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

def gitFolderHere_doWork(folder):
	# print("Git folder!!!", folder)
	print("cd %s" % (folder))
	print("git status")

def isGitRoot(folder):
	dirList = os.listdir(folder)
	if ".git" in dirList:
		return True
	return False

def ListFolder(folder):
	if isGitRoot(folder):
		gitFolderHere_doWork(folder)
		return
	dirList = os.listdir(folder)
	for fname in dirList:
		fullName = path.join(folder, fname)
		if path.isdir(fullName):
			try:
				ListFolder(fullName)
			except PermissionError:
				print("ERROR: could not read dir", fullName)

#ListFolder(".")
ListFolder("C:\\_mik\\gh")