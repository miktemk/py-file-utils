# **MODE OF USE**: Run in a folder (with wavs!)
#
# Generates a batch file that converts every single wav in this folder to mp3 using
# `Lame For Audacity`. Also makes the "convert" directory if it doesn't exist.
# Feel free to change the path to lame if you dare...

############ config ############
OUT_DIRNAME = "convert"
SRC_EXT = ".wav"
BITRATE = "128"
################################

import sys, os, shutil
import __main__



fff = open("zz_mp3_convert_batch.bat", "w")
fff.write("""
@ECHO OFF

rem echo "Please set the audio folder path"
rem pause
rem exit

cd \"""" + os.path.dirname(os.path.abspath(__file__)) + """\"

""")

if not os.path.exists(OUT_DIRNAME):
	os.mkdir(OUT_DIRNAME)
dirList = os.listdir(".")
for fname in dirList:
	fullPathS = "./" + fname
	if os.path.isdir(fullPathS):
		continue
	if not fname.lower().endswith(SRC_EXT):
		continue
	fname2 = fname.lower().replace(SRC_EXT, ".mp3")
	fname2 = OUT_DIRNAME + "/" + fname2
	fff.write('"C:\Program Files (x86)\Lame For Audacity\lame.exe"')
	if SRC_EXT == "mp3":
		fff.write(' --mp3input')
	fff.write(' -b ' + BITRATE + ' "' + fname + '" "' + fname2 + '" \n')

		
fff.write("""

PAUSE

""")
fff.close()
