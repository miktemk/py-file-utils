# **MODE OF USE**: Run in a folder OR drag and drop a folder into me
#
# Generates a txt file with all the contents of this folder (recursive)
#
#  - if run in a folder -> generates `zz_fileListingRecursive.txt`
#  - if drag and drop -> generates `folder name` + `.recursivelist.txt`

import sys, os, shutil
import getopt, codecs
import glob
from os import path

os.path.dirname(os.path.abspath(__file__)) # .... set . to CWD (good practice)

# NOTE: comment/uncomment whichever print lines you need to build your script

# print('#!/bin/sh') # for bash scripts

def gitFolderHere_doWork(folder):
	# print("Git folder!!!", folder)
	print("cd %s" % (folder))
	# print("cd %s" % (folder.replace('C:', '/c').replace('\\', '/'))) # for bash scripts
	# print("git status")
	# print("git stash list")
	print("git clean -fdx")
	# dirList = os.listdir(folder)
	# if "node_modules" in dirList:
	# 	print("rm -rf node_modules")
	# print('>>>>>>>> glob', folder + '\\*.sln')
	# slnFiles = glob.glob(folder + '\\*.sln')
	# if len(slnFiles) > 0:
	# 	print("CsProjNukeBinObj -v .")


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