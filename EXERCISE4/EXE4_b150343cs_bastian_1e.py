import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *
import math



img=cv2.imread('q3.tif',0)
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

cov=E-(np.dot(XC,np.transpose(XC)))"""
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
recons=np.dot(np.dot(np.transpose(np.conjugate(T)),KLT),np.conjugate(T))
print("RECONSTRUCTION")
print(recons)
cv2.imwrite("1e_basis.jpg",np.abs(T*255))
cv2.imwrite("1e.jpg",np.abs(KLT))
cv2.imwrite("1e_reconstruction.jpg",np.abs(recons))

T=np.triu(T,0)
print("KL BASIS CR")
print(T)
KLT=np.dot(np.dot(T,img),np.transpose(T))
print("KL TRANSFORM CR")
print(KLT)
recons=np.dot(np.dot(np.transpose(np.conjugate(T)),KLT),np.conjugate(T))
print("RECONSTRUCTION CR")
print(recons)
cv2.imwrite("1e_basis_cr.jpg",np.abs(T*255))
cv2.imwrite("1e_cr.jpg",np.abs(KLT))
cv2.imwrite("1e_reconstruction_cr.jpg",np.abs(recons))












