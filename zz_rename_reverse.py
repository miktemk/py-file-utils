# **MODE OF USE**: Drag and drop.
#
# Quick
#
# - drag up to N files into me.
# - 2 files: `[1,2]` => `[2,1]` (swap)
# - 3 files: `[1,2,3]` => `[3,2,1]`
# - 4 files: `[1,2,3,4]` => `[4,3,2,1]`
#
# Lengthy
#
#  - When you drag 2 files `a.txt` and `b.txt` the files are renamed, their names swapped.
#  - When you drag `a.txt`, `b.txt`, `c.txt`, `a` is renamed to `c` and `c` to `a`. `b.txt` stays.
#  - When 4 files are dragged in: a, b, c, d... a is renamed d, b is renamed c...
#  - 5 files... you get the idea!

import sys, os, re
import time, datetime, shutil
import getopt

TMP_FILENAME = 'fdsaie324wfw_3232___fdkjoosl32432fjoiewjfdslkfja__fdjsklfj324sadfwe_dfkljskdl34234jasf'

curDir = os.path.dirname(os.path.abspath(__file__))
TMP_FILENAME = curDir + '/' + TMP_FILENAME

# command line options: note the first line parameter and the if statements below
optlist, args = getopt.getopt(sys.argv[1:], "")
if len(args) <= 1:
	print "Usage: drag the file in and enter a nummar!"
	exit(1)
	
def swapFnames(fname1, fname2):
	shutil.copyfile(fname1, TMP_FILENAME)
	shutil.copyfile(fname2, fname1)
	shutil.copyfile(TMP_FILENAME, fname2)

for i in range(len(args)/2):
	lasti = len(args)-i-1
	print 'swapping', i, lasti
	swapFnames(args[i], args[lasti])

if os.path.exists(TMP_FILENAME):
	os.remove(TMP_FILENAME)
