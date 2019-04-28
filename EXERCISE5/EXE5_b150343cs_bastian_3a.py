import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *


img=cv2.imread('cameraman.tif',0)
print("IMAGE")
print(img)
histogram=np.zeros((255,))
Transform=np.zeros(img.shape,dtype=float64)


"""for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		histogram[int(round(img[i][j]))]+=1
print("Histogram")
print(histogram)"""
plt.hist(img.ravel(),256,[0,256]);
plt.savefig("3a.jpg")
plt.show()


