#!/usr/bin/env python

import thread
import time

def worker_thread(id):
	
	print "\nThread ID %d now alive!" %id

	count = 1
	while True:
		print "\nThe thread with ID %d has counter value %d" %(id,count)
		time.sleep(2)
		count += 1

for i in range(2):
	print "i=%d:"%i
	thread.start_new_thread(worker_thread, (i,))

print "\nMain thread going for a infinite wait loop"

while True:
	time.sleep(1)

