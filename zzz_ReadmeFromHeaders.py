# **MODE OF USE**: Run in a folder
#
# Automatically generates `README.md` file from combined headers of all the scripts.
# If `README.md` already exists, it will back it up with a timestamp, this way you are
# spared that oops moment...

import sys, os, re, shutil
import time, datetime
import getopt

def ParseScript_getSummary(script):
	script = script.strip()
	lines = script.split('\n')
	if len(lines) == 0:
		return "README-Error: No script!"
	if lines[0].strip().startswith('"""'):
		mo = re.match('"""(.*?)"""', script, re.DOTALL)
		if mo == None:
			return "README-Error: quote comment has invalid syntax"
		return mo.group(1).strip()
	if lines[0].strip().startswith("#"):
		sb = ""
		for line in lines:
			line2 = line.strip()
			if not line2.startswith("#"):
				break
			line2 = line2[1:].strip()
			sb += line2 + "\n"
		return sb.strip()
	return "README-Error: No header comment! Consider adding one..."

# back up old one
if os.path.exists("README.md"):
	today = datetime.date.today()
	month = str(today.month).zfill(2)
	day = str(today.day).zfill(2)
	todayTime = datetime.datetime.now()
	hour = str(todayTime.hour).zfill(2)
	minute = str(todayTime.minute).zfill(2)
	second = str(todayTime.second).zfill(2)
	timestamp = str(today.year) + month + day + hour + minute + second
	shutil.move("README.md", "README.md.backup-" + timestamp)

allText = ""
dirList = os.listdir(".")
for fname in dirList:
	noext, ext = os.path.splitext(fname)
	if not ext.lower() in [".py"]:
		continue
	with open(fname, "r") as fin:
		script = fin.read()
	summary = ParseScript_getSummary(script)
	allText += "## " + fname.replace("_", "\\_") + "\n\n" + summary + "\n\n---\n\n"

with open("README.md", "w") as fout:
	fout.write(allText)
