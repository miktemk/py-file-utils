# **MODE OF USE**: command line style:
#
#  - `script.py -b file1.txt -t file2.txt`
#  - `script.py --base file1.txt --target file2.txt`
#
# lists all files in base that are missing in target. Search is performed only by the last part of the filename

import sys, os, re
import getopt
import codecs

os.path.dirname(os.path.abspath(__file__)) # .... set . to CWD (good practice)
#sys.argv = ["", "--base", "./2015_02_italia.recursivelist.txt", "--target", "./2015_02_italia.recursivelist2.txt"] # .... debug tests
#sys.argv = ["", "-b", "./suka.txt", "-t", "./suka2.txt"] # .... debug tests

def getFileLines(fname):
	infile = codecs.open(fname, "r", "utf-8")
	lines = infile.readlines()
	infile.close()
	return lines

def path_leaf(fff):
    return os.path.split(fff)[-1]

def MakeListOfPathLeaves(listFulls):
	list2 = []
	for targetFile in listFulls:
		targetFile = targetFile.strip()
		fnameLeaf = path_leaf(targetFile)
		list2 += [fnameLeaf]
	return list2

def filenameInList(fname, list2Levaes):
	fnameLeaf = path_leaf(fname)
	inHere = False
	for targetFileLeaf in list2Levaes:
		if fnameLeaf == targetFileLeaf:
			inHere = True
			break
	return inHere

try:
    opts, args = getopt.getopt(sys.argv[1:], "b:t:o:", ["base=", "target=", "output="])
except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(2)
filenameBase = None
filenameTarget = None
filenameOut = None
for o, a in opts:
    if o in ("-b", "--base"):
        filenameBase = a
    elif o in ("-t", "--target"):
        filenameTarget = a
    elif o in ("-o", "--output"):
        filenameOut = a
        print ("output file SET!!!!!!!!!!!!")
    else:
        assert False, "unhandled option"

outFile = sys.stdout
if filenameOut != None:
	outFile = codecs.open(filenameOut, "w", "utf-8")

listBase = getFileLines(filenameBase)
listTarget = getFileLines(filenameTarget)
fnamesOnlyTarget = MakeListOfPathLeaves(listTarget)

for baseFile in listBase:
	baseFile = baseFile.strip()
	if not filenameInList(baseFile, fnamesOnlyTarget):
		outFile.write(baseFile + "\n")
