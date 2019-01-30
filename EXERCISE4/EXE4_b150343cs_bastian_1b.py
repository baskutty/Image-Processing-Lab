import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *

img=cv2.imread('q1.tif',0)
print("IMAGE")
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
print("HADAMARD BASIS")
print(HB)

hadamard=np.dot(np.dot(HB,img),HB)
print("HADAMARD TRANSFORM")
print(hadamard)
recons=np.dot(np.dot(HB,hadamard),HB)/(n*n)
print("RECONSTRUCTION")
print(recons)

cv2.imwrite("1b_basis.jpg",HB*255)
cv2.imwrite("1b.jpg",hadamard)
cv2.imwrite("1b_reconstruction.jpg",recons)

HB=np.triu(HB,0)

print("HADAMARD BASIS CR")
print(HB)

hadamard=np.dot(np.dot(HB,img),np.transpose(HB))
print("HADAMARD TRANSFORM CR")
print(hadamard)
recons=np.dot(np.dot(np.transpose(HB),hadamard),HB)/(n*n)
print("RECONSTRUCTION CR")
print(recons)

cv2.imwrite("1b_basis_cr.jpg",HB*255)
cv2.imwrite("1b_cr.jpg",hadamard)
cv2.imwrite("1b_reconstruction_cr.jpg",recons)



