import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *

img=cv2.imread('q1.jpg',0)
print(img)
HB=np.zeros(img.shape,dtype=int)

n=img.shape[0]
HB[0][0]=1
i = 1
while i < n:
    for j in range(i):
        for k in range(i):
            HB[j+i][k]    = HB[j][k]
            HB[j][k+i]    = HB[j][k]
            HB[j+i][k+i] = -(HB[j][k])
    i += i
print(HB)

hadamard=np.dot(np.dot(HB,img),HB)
print(hadamard)
recons=np.dot(np.dot(HB,hadamard),HB)/(n*n)
print(recons)

cv2.imwrite("1b_basis.jpg",HB*255)
cv2.imwrite("1b.jpg",hadamard)
cv2.imwrite("1b_reconstruction.jpg",recons)
