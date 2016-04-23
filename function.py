#!/usr/bin/python


import sys


def PrintStimes(line_to_print):

	for count in range(0,5):
		print line_to_print


PrintStimes(sys.argv[2])

