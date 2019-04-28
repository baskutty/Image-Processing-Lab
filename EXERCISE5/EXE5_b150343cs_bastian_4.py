import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *


img=cv2.imread('cameraman.tif',0)
print("IMAGE")
print(img)

blur=np.zeros(img.shape,dtype=float64)

n=img.shape[0]

for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		temp = 0
		for k in range(3):
			for l in range(3):
				if i+k<n and i+k>=0 and j+l<n and j+l>=0:
					temp +=img[i+k][j+l]
		blur[i][j] = temp
blur=blur/9
print("BLUR")
print(blur)
cv2.imwrite("4b.jpg",blur)
gmask=img-blur
print("GMASK")
print(gmask)
cv2.imwrite("4c.jpg",gmask)
addmask=img+gmask
print("ADDED")
print(addmask)
cv2.imwrite("4d.jpg",addmask)
ans=np.hstack((img,blur,gmask,addmask))
cv2.imwrite("4.jpg",ans)






