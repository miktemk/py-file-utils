# **MODE OF USE**: Run in a folder
#
# Automatically generates a new folder that begins with a date stamp (`year_month_day`)

import sys, re, os
import time, datetime

postfix = input("folder name: ")

today = datetime.date.today()
month = str(today.month).zfill(2)
day = str(today.day).zfill(2)

dirname = str(today.year) + "_" + month + "_" + day + "_" + postfix
print ("creating directory:", dirname)

os.mkdir("./" + dirname)