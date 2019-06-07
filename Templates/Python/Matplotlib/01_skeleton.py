#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## 2017, Felix Niederwanger
## My matplotlib skeleton code for a simple plot


import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
	
	fig = plt.figure(figsize=(12,6))		# Figsize in inches
	ax = fig.add_subplot(111)
	
	## Set Log scaling, if needed
	#ax.set_xscale("log")
	ax.set_yscale("log")
	
	
	## Mainipulate ticks
	#delta = float(extend[1] - extend[0]) / float(ticks)
	#x_ticks = [extend[0]+x*delta for x in range(ticks+1) ]
	#ax.get_xaxis().set_ticks(x_ticks)
	
	## Set axis limits
	#ax.set_ylim(1e-1, 1e3) # <--
	#ax.set_xlim(1, 10)

	## Set labels and titles
	#ax.set_xlabel("Length [cm s$^{-1}$]")		# Between $ is LaTeX
	#ax.set_ylabel("Ticks [1]")
	#ax.set_title("Title")
	
	x = np.arange(1.0, 10.0, 1.0)
	y1 = x * 2
	y2 = x*x
	
	## Create plot
	ax.plot(x, y1, "c-", x, y2, "g-")
	
	## Eventually, save to file
	#fig.savefig("file.png", dpi=100,papertype="A4",format=format)
	plt.show()
