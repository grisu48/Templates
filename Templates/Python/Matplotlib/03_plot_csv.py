#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## 2020, Felix Niederwanger
## My matplotlib skeleton code for creating a plot based on CSV

## This python script reads in a CSV file with an arbitrary number of columns
## and creates a matplotlib plot out of it
## In the CSV file, the following parameters can be set:
##
## :title = STRING                              Set plot title
## :xlabel = STRING                             Set label of x axis
## :ylabel = STRING                             Set label of y axis
## :xlim = MIN,MAX                              Set extent of x axis
## :ylim = MIN,MAX                              Set extent of y axis
## :figsize = WIDTH,HEIGHT                      Set resulting figure size
## :logx = [0,1]|[false,true]                   If x axis is logarithmic
## :logy = [0,1]|[false,true]                   If y axis is logarithmic
## :styles = STYLES,...                         Set styles of plots (matplotlib)
##           e.g. "k-, g-- "
## :legend = LOCATION                           Determine if legend is plottet
##           [upper right, center left, best, upper left, right, lower right]
##           [lower left, center right, upper center]
## :labels = PLOT1,PLOT2,...                    Set labels used by legend
## :modifier = MODIFIER                         Set modifier func for values
##             e.g. xy                          value = x*y
##                  x^3*y                       you should get it :-)
## :linewidth = 1                               Define line width (i.e. strength)


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
		self.title = ""				## Title
		self.labelx = ""
		self.labely = ""
		self.xlim = None
		self.ylim = None
		self.logx = False
		self.logy = False
		self.styles = ["k-"]		## Matplotlib plot line styles
		self.labels = []
		self.legend = None
		self.figsize= (12,6)
		self.modifier = None
		self.linewidth = 1

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
	
	def createplot(self) :
		'''
		Create figure and axis object
		'''
		fig = plt.figure(figsize=self.figsize)		# Figsize in inches
		ax = fig.add_subplot(111)
	
		## Set Log scaling, if needed
		if self.logx : ax.set_xscale("log")
		if self.logy : ax.set_yscale("log")
	
		## Mainipulate ticks
		#delta = float(extend[1] - extend[0]) / float(ticks)
		#x_ticks = [extend[0]+x*delta for x in range(ticks+1) ]
		#ax.get_xaxis().set_ticks(x_ticks)
	
		## Set axis limits
		if not self.xlim is None : ax.set_xlim(self.xlim[0], self.xlim[1])
		if not self.ylim is None : ax.set_ylim(self.ylim[0], self.ylim[1])

		## Set labels and titles
		if len(self.labelx) > 0 : ax.set_xlabel(self.labelx)
		if len(self.labely) > 0 : ax.set_ylabel(self.labely)
		if len(self.title) > 0 : ax.set_title(self.title)
		
		return (fig,ax)
		
	def plot(self) :
		'''
		Create plot instance. You still need to call plt.plot() or fig.savefig()
		Returns the created (fig, ax) instance
		'''
		if len(self._data) == 0 : raise ValueError("Empty data")
		fig,ax = self.createplot()
		
		nCol = len(self._data[0])-1
		for i in range(nCol) :
			style = self.styles[i % len(self.styles)]
			label = ""
			if i < len(self.labels) : label = self.labels[i]
			x = csv.x()
			y = csv.extract(i+1)
			if not self.modifier is None : y = self.modifier(x,y)
			ax.plot(x, y, style, label=label, linewidth=self.linewidth)
		
		## Legend
		if not self.legend is None : ax.legend(loc=self.legend)
		
		return fig,ax

def createModifierFunc(modifier) :
	'''
	Create modifier function (lambda x,y : value)
	'''
	if modifier is None : return lambda x,y : x
	modifier = str(modifier).strip().lower()
	if len(modifier) == 0 : return lambda x,y : x
	func = lambda x,y : x
	# TODO: Build parse tree
	
	# For now, we limit ourselves to some pretty simple cases (hardcoded)
	if modifier == "x" : return lambda x,y : x
	elif modifier == "y" : return lambda x,y : y
	elif modifier == "xy" or modifier == "yx" : return lambda x,y : x*y
	elif modifier == "x^2y" or modifier == "yx^2" : return lambda x,y : (x**2)*y
	elif modifier == "x^2.7y" or modifier == "yx^2.7" : return lambda x,y : (x**2.7)*y		# Commonly used in CR physics
	elif modifier == "x^3y" or modifier == "yx^3" : return lambda x,y : (x**3)*y
	
	else :
		raise ValueError("Unsupported modifier function (sorry!)")
	
	return func
			

def read_csv(filename) :
	ret = CSV()
	
	# Split by regex
	regex = re.compile(":|;|\t| |,")
	
	def strbool(text,default=False) :
		TRUEVALUES = ["1","true","on","yes"]
		FALSEVALUES = ["0","false","off","no"]
		if text in TRUEVALUES : return True
		elif text in FALSEVALUES : return False
		else : return default
	
	with open(filename, 'r') as f_in :
		iLine = 0
		for line in f_in.readlines() :
			iLine += 1
			line = line.strip()
			if len(line) == 0 or line[0] in "#;'\"@!" : continue	# Comments
			if line[0] == ":" :		# Special command
				split = line.split("=", 1)
				if len(split) < 2 : 
					sys.stderr.write("Line " + str(iLine) + " - Format error\n")
					continue
				else :
					# Strip, lowercase and remove : at begin
					name = split[0].strip().lower()[1:]
					value = split[1].strip()
					
					if name == "label" or name == "title" :
						ret.title = value
					elif name == "xlabel" or name == "labelx" :
						ret.labelx = value
					elif name == "ylabel" or name == "labely" :
						ret.labely = value
					elif name == "xlim" or name == "limx" :
						ret.xlim = [float(x.strip()) for x in value.split(",")]
					elif name == "ylim" or name == "limy" :
						ret.ylim = [float(x.strip()) for x in value.split(",")]
					elif name == "figuresize" or name == "figsize" :
						ret.figsize = [float(x.strip()) for x in value.split(",")]
					elif name == "logx" or name == "xlog" :
						ret.logx = strbool(value)
					elif name == "logy" or name == "ylog" :
						ret.logy = strbool(value)
					elif name == "legend" :
						ret.legend = value.lower()
					elif name == "styles" :
						ret.styles = [x.strip() for x in value.split(",")]
					elif name == "labels" :
						ret.labels = [x.strip() for x in value.split(",")]
					elif name == "modifier" :
						ret.modifier = createModifierFunc(value)
					elif name == "linewidth" :
						ret.linewidth = float(value)
					else :
						sys.stderr.write("Line " + str(iLine) + " - Unknown parameter '" + name + "'\n")
						continue	
						
			else :
				line = regex.split(line)
				if len(line) < 2 :
					sys.stderr.write("Line " + str(iLine) + " - Not enough columns\n")
					continue
				try :
					f_val = [float(x) for x in line]
					ret.append(f_val)
				except ValueError as e:
					sys.stderr.write("Line " + str(iLine) + " - " + str(e) + "\n")
					continue
	
	return ret

if __name__ == '__main__':
	def check_help(args) :
		for arg in args :
			if arg in ["-h", "--help"] : return True
		return False
	if len(sys.argv) < 2 or check_help(sys.argv[1:]) :
		print("Simple matplotlib CSV-plotting utility")
		print("Usage: " + sys.argv[0] + " CSV [EXPORTFILE]")
		print("  CSV is a csv file")
		print("  if EXPORTFILE is determined, I will write the plot to this file")
		sys.exit(0)
	## Read data from file
	csv = read_csv(sys.argv[1])
	fig,ax = csv.plot()
	
	## Eventually, save to file
	if len(sys.argv) > 2 :
		filename = sys.argv[2]
		fig.savefig(filename, dpi=100,papertype="A4")
		print("Written to " + filename)
	else :
		plt.show()
