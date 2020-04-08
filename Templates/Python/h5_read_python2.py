#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import h5py
import sys


if __name__ == '__main__' :
	EXIT_FAILURE = 1
	EXIT_SUCCESS = 0
	
	# Check if we have a program argument, otherwise terminate
	if len(sys.argv) <= 1 :
		print "Usage: " + sys.argv[0] + " H5FILE\n"
		sys.exit(EXIT_FAILURE)
	filename = sys.argv[1]
	
	# Open HDF5 file
	
	h5in = h5py.File(filename, 'r')
	try :
		pass
		
	finally :
		h5in.close()
