#!/usr/bin/env python

import thread
import time

def worker():
	print "Thread is alive"


thread.start_new_thread(worker)
