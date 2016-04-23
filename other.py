#!/usr/bin/env python

import os
import glob


file = 0
dir =  0
other = 0

for item in glob.glob(os.path.join("/dev","*")):
	if os.path.isdir(item):
		dir += 1
	elif os.path.isfile(item):
		file += 1
	else:
		#print item
		other += 1

print "Directories:%d" % dir
print "Files:%d" % file
print "Other:%d" % other
	

