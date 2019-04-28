import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *
imgr=cv2.imread('cameraman.tif',0)

img1=cv2.imread('2A.jpg',0)
img2=cv2.imread('2B.jpg',0)
img3=cv2.imread('2C.jpg',0)
img4=cv2.imread('2D.jpg',0)
img=np.zeros(img1.shape,dtype=float)

for i in range (img1.shape[0]):
	for j in range (img1.shape[1]):
		img[i][j]=float(float(img1[i][j])+float(img2[i][j])+float(img3[i][j])+float(img4[i][j])+float(imgr[i][j]))
print("Averaged")
print(img/5)
Transform=img/5
combine=np.hstack((imgr,Transform))
cv2.imwrite("2e.jpg",combine)
combine2=np.hstack((imgr,img1,img2,img3,img4,Transform))
cv2.imwrite("2.jpg",combine2)
