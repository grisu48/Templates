#!/usr/bin/python3
# -*- coding: utf-8 -*-


from astropy.io import fits


with fits.open(sys.argv[1], "readonly") as hdul :
	hdul.info()
	
	# access via hdul[0] and hdul[0].data
