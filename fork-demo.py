#!/usr/bin/env python

import os

def child_process():
	print "I'm the child process and my PID is: %d" % os.getpid()
	
	print "The child is existing"

def parent_process():
	
	print "I'm the parent process with PID: %d" % os.getpid()

	childpid = os.fork()
	#print "chilpid = %d" % childpid
	if childpid == 0:
		# We are inside the child

		child_process()
	else:
		#We are inside the parent process

		print "We are inside the parent process"
		print "Our child has the PID: %d" %childpid


parent_process()	
