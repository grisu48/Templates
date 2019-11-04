#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## 2019, Felix Niederwanger
## My matplotlib skeleton code for a simple plot


import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import re

class CSV :
	'''
	CSV container class
	'''
	def __init__(self):
		self._data = []

	def append(self, row) :
		if len(self._data) == 0 :
			self._data.append(row)
		else :
			ref = self._data[0]
			if len(ref) != len(row) : raise ValueError("Column count mismatch")
			self._data.append(np.array(row))
	def clear(self) : 
		self._data = []
	def __len__(self) :
		return len(self._data)
	def __getitem__(self, key) :
		return self._data[key]

	def rows(self) :
		return len(self._data)
	def columns(self) :
		if len(self._data) == 0 : return 0
		else : return len(self._data[0])

	def extract(self, col=0) :
		'''
		Extract a certain column from the dataset
		'''
		n = len(self._data)
		ret = np.zeros(n)
		for i in range(n) : ret[i] = self._data[i][col]
		return ret
	def x(self) : return self.extract(0)
	def y1(self) : return self.extract(1)
	def y2(self) : return self.extract(2)
	def y3(self) : return self.extract(3)
	def y4(self) : return self.extract(4)


def read_csv(filename) :
	ret = CSV()
	
	# Split by regex
	regex = re.compile(":|;|\t| |,")
	
	with open(filename, 'r') as f_in :
		iLine = 0
		for line in f_in.readlines() :
			iLine += 1
			line = line.strip()
			if len(line) == 0 or line[0] in "#$:;'\"@!" : continue		# Comments
			line = regex.split(line)
			if len(line) < 2 :
				sys.stderr.write("Line " + str(iLine) + " - Not enough columns\n")
				continue
			try :
				f_val = [float(x) for x in line]
				ret.append(f_val)
			except ValueError :
				sys.stderr.write("Line " + str(iLine) + " - " + str(e) + "\n")
				continue
	
	return ret

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
	
	## Read data from file
	csv = read_csv(sys.argv[1])
	
	## Create plot
	#ax.plot(x, y1, "c-", x, y2, "g-")
	ax.plot(csv.x(), csv.y1(), "c-")
	
	## Eventually, save to file
	#fig.savefig("file.png", dpi=100,papertype="A4",format=format)
	plt.show()
