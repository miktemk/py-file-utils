import sys, os, re, shutil

dirname, thisScript = os.path.split(__file__)
print (dirname)
dirList = os.listdir(dirname)
for dname in dirList:
	if dname == os.path.basename(__file__):
		continue
	fullPathDir = dirname + "\\" + dname
	if not os.path.isdir(fullPathDir):
		continue
	print("collapsing", dname)
	dirList2 = os.listdir(fullPathDir)
	hasConflicts = False
	for fname2 in dirList2:
		fullPathDirSrc = fullPathDir + "\\" + fname2
		fullPathDirDest = ".\\" + fname2
		print("  moving out", fname2)
		if os.path.exists(fullPathDirDest):
			print("!!!CONFLICT: will not move", fullPathDirSrc)
			hasConflicts = True
		else:
			shutil.move(fullPathDirSrc, fullPathDirDest)
	if not hasConflicts:
		shutil.rmtree(fullPathDir)
