# **MODE OF USE**: Run in a folder
#
# Generates `zz_fileListing.txt` with all the contents of this folder (1 level)

import sys, os, shutil

curDir = os.path.dirname(os.path.abspath(__file__))

fff = open("zz_fileListing.txt", "w")
fff.write("""
---------------- prefix ---------------------
""")
dirList = os.listdir(".")
for fname in dirList:
	fff.write(fname + "\n")
fff.write("""
---------------- postfix ---------------------
""")
fff.close()
