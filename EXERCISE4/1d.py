import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *

img=cv2.imread('q1.jpg',0)
print("IMAGE")
print(img)
CB=np.zeros(img.shape,dtype=float64)

n=img.shape[0]
for u in range(n):
	for x in range(n):
		if u==0:
			CB[u][x]=np.sqrt(1/n)*(np.cos((2*x+1)*np.pi*u/(2*n)))
		else:
			CB[u][x]=np.sqrt(2/n)*(np.cos((2*x+1)*np.pi*u/(2*n)))
print("COSINE BASIS")
print (CB)

DCT=np.dot(np.dot(CB,img),np.transpose(CB))
print("COSINE TRANSFORM")
print(DCT)
recons=np.dot(np.dot(np.transpose(CB),DCT),CB)
print("RECONSTRUCTION")
print(recons)
cv2.imwrite("1d_basis.jpg",CB*255)
cv2.imwrite("1d.jpg",DCT)
cv2.imwrite("1d_reconstruction.jpg",recons)
