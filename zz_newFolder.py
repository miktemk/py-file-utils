import sys, re, os
import time, datetime

today = datetime.date.today()
postfix = input("folder name: ")

month = str(today.month).zfill(2)
day = str(today.day).zfill(2)

dirname = str(today.year) + "_" + month + "_" + day + "_" + postfix
print ("creating directory:", dirname)

os.mkdir("./" + dirname)