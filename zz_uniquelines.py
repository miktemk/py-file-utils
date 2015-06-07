# This is usually ran on dictionaries to eliminate duplicate lines
# For every `file.txt` dragged in, this script creates `file.txt.unique` which has only the unique lines

import sys, os, re
import time, datetime
import getopt

optlist, args = getopt.getopt(sys.argv[1:], "")
if len(args) == 0:
	print "Must specify args!"
	exit(1);

filenames = args

for fname in filenames:
		
	infile = open(fname)
	lines = infile.readlines()
	unique = [];
	count = 0
	for line in lines:
		word = line.strip()
		if word not in unique:
			unique += [word];
	infile.close()
	
	fff = open(fname + ".unique", "w")	
	for word in unique:
		fff.write(word + '\n')
	fff.close()
