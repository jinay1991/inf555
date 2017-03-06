'''
  Galif.cpp
  inf555

  - Converted to Python Source by Jinay Patel on 03/03/2017
  - Created by Camille MASSET on 24/11/2015.
  Copyright 2015 Basile Camille. All rights reserved.
'''
import cv2
import numpy as np
import math 

FEAT_SIZE = 256

class GALIF:
	w0 = 0
	sigx = 0
	sigy = 0
	k = 0
	n = 0
	filters = []

	def __init__(self, w0, w, k, n):
		assert (k > 0)
		assert (n > 0)

		self.w0 = w0
		self.k = k
		self.n = n
		self.sigx = 0.02 * w
		self.sigy = self.sigx / 0.3

		self.filters = np.array((k), dtype='uint8')
		
	def __del__(self):
		del self.filters

	def gaussian(self, i, u, v, cols, rows):
		assert (0 <= i & i < self.k)

		theta = i * math.pi / self.k

		u = 2 * math.pi * u / cols
		v = 2 * math.pi * v / rows

		ut = u * math.cos(theta) - v * math.sin(theta)
		vt = u * math.sin(theta) - v * math.cos(theta)

		expression = (-2 * math.pi * ((ut - self.w0) * (ut - self.w0) * self.sigx * self.sigx + vt * vt * self.sigy * self.sigy) )
		return float(math.exp(expression))
	
	def get_filter(self, i, rows, cols):
		assert(rows > 0 & cols > 0)
		
		fi = np.array((rows, cols), dtype=cv2.CV_32F)

		for l in range(cols):
			for j in range(rows):
				fi[i][j] = self.gaussian(i, l, j, cols, rows)
		
		return fi

	def compute_filters(self, I):
		rows = I.shape[0]
		cols = I.shape[1]

		for i in range(self.k):
			self.filters[i] = self.get_filter(i, rows, cols)

	def filter(self, i, I):
		assert(I.type() == cv2.CV_32FC1)

		planes = [ I.convertto(dtype=float), np.zeros(I.size(), dtype=cv2.CV_32F)]

		complexI = cv2.merge(planes, 2)
		complexI = cv2.dft(complexI)

		planesm = [ np.zeros(complexI.size(), dtype=cv2.CV_32F), np.zeros(complexI.size(), dtype=cv2.CV_32F)]
		planesm = cv2.split(complexI)

		for h in range(complexI.total()):
			planesm[0][h] = planesm[0][h] * self.filters[i][h]
			planesm[1][h] = planesm[1][h] * self.filters[i][h]

		complexI = cv2.merge(planesm, 2)

		fi = np.array(I.size(), dtype=cv2.CV_32FC2)
		fi = cv2.idft(complexI, fi)
		planes2 = [ np.zeros(I.size(), dtype=cv2.CV_32F), np.zeros(I.size(), dtype=cv2.CV_32F) ]
		planes2 = cv2.split(fi)

		dft_I = cv2.magnitude(planes2[0], planes2[1])
		dft_I += 1
		dft_I = cv2.log(dft_I)

		dft_I = cv2.normalize(dft_I, 0, 1, cv2.CV_MINMAX)

		return dft_I

	def features(self, I, p):
		pass

if __name__ == "__main__":
	print "self test"
	obj = GALIF(0.13, 5, 4, 8)