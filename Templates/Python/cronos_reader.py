#!/usr/bin/python

import h5py    # HDF5 support
import numpy
import sys, os

class CRONOSHDF5 :
	def __init__(self, filename):
		self._filename = filename
		self._f = h5py.File(filename, "r")
		self._rho = self._f['/Data/rho']
		self._data = self._f['/Data']
		self._attrs = self._data.attrs
		
	def close(self):
		self._f.close()
	
	def getDimensions(self):
		return len(self._rho.shape)
	
	def getShape(self):
		return (self.getSizeX(), self.getSizeY(), self.getSizeZ())
	def getDimensions(self): return self.getShape()
	
	def getSizeX(self): return self._rho.shape[0]
	def getSizeY(self): return self._rho.shape[1]
	def getSizeZ(self): return self._rho.shape[2]

	def getField(self, field): return self._f['/Data/' + str(field)]
	
	def getRho(self): return self.getField('rho')
	def getEtherm(self): return self.getField('Etherm')
	def getVx(self): return self.getField('v_x')
	def getVy(self): return self.getField('v_y')
	def getVz(self): return self.getField('v_z')
	def getV(self, pos):
		(x,y,z) = pos
		return (self.getVx()[x,y,z], self.getVy()[x,y,z], self.getVz()[x,y,z])
	
	def getAttribute(self, key, default=None): return self._attrs.get(key, default)
	
	def getDx(self): return self.getAttribute('dx')
	def getBounds(self): return self.getAttribute('xmin')

## USER SECTION. Modify this function to your needs
def main(h5file):
	## USER SECTION
	pass

if __name__ == '__main__':
	if len(sys.argv) < 2 : 
		print "Usage:",os.path.basename(__file__), "FILE"
		sys.exit(1)
	filename = sys.argv[1]

	print "Reading file ",filename,"..."
	h5file = CRONOSHDF5(filename)

	try :
		main(h5file)
	finally:
		h5file.close()
	print "Done"



