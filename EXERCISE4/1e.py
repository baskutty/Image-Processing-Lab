import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *
import math


#img=np.array([[1,2,1,0],[2,-1,1,2]],dtype=float64)
img=cv2.imread('q1.tif',0)
print("IMAGE")
print(img)

"""E=np.zeros((img.shape[0],img.shape[0]),dtype=float64)


for i in range (img.shape[1]):
	E+=np.dot(np.transpose([img[:,i]]),[img[:,i]])
E=E/(img.shape[1])

print(E)

XC=np.zeros((img.shape[0],1),dtype=float64)
for i in range (img.shape[1]):
	XC+=np.transpose([img[:,i]])

XC=XC/(img.shape[1])

print(XC)

cov=E-(np.dot(XC,np.transpose(XC)))
print(cov)

I=np.identity(img.shape[0])
print(I)"""

cov=np.cov(img)
print("COVARIANCE")
print(cov)

eigen=np.linalg.eig(cov)
print("EIGEN VECTORS")
T=(eigen[1])
print("KL BASIS")
print(T)
KLT=np.dot(np.dot(T,img),np.transpose(T))
print("KL TRANSFORM")
print(KLT)
recons=np.dot(np.dot(np.transpose(T),KLT),T)
print("RECONSTRUCTION")
print(recons)
cv2.imwrite("1e_basis.jpg",T*255*255)
cv2.imwrite("1e.jpg",KLT)
cv2.imwrite("1e_reconstruction.jpg",recons)











