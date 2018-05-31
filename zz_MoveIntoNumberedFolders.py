# **MODE OF USE**: Run in a folder
#
# Creates numbered folders and moves all files there. Use when dealing with large number of files.

import sys, os, shutil

cwd = "."
folderName_Prefix = 'items'
folderName_CapacityThresh = 1000

index = 0
curFolderName = None
for fname in os.listdir(cwd):
	# .... skip this python script
	if fname == os.path.basename(__file__):
		continue
	fullPath = os.path.join(cwd, fname)
	if os.path.isdir(fullPath):
		continue
	if index % folderName_CapacityThresh == 0 or curFolderName == None:
		itemCountMin = folderName_CapacityThresh * int(index / folderName_CapacityThresh)
		itemCountMax = itemCountMin + folderName_CapacityThresh - 1
		curFolderName = os.path.join(cwd, "{0}_{1}_{2}".format(folderName_Prefix, itemCountMin, itemCountMax))
		if not os.path.exists(curFolderName):
			print ("making folder", curFolderName)
			os.makedirs(curFolderName)
	fullPath2 = os.path.join(curFolderName, fname)
	print (fullPath, " -> ", fullPath2)
	os.rename(fullPath, fullPath2)
	index += 1
