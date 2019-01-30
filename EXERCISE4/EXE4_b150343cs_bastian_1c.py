import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *
import math

img=cv2.imread('q1.tif',0)
print("IMAGE")
print(img)
HAB=np.zeros(img.shape,dtype=float64)

N=img.shape[0]
n=int (math.log(N,2))

Z=np.zeros(N,dtype=float64)

for i in range (N):
	Z[i]=i/N


K=np.zeros((N,2),dtype=float64)
K[0][0]=0
K[0][1]=0
K[1][0]=0
K[1][1]=1

for i in range (1,n):
	for j in range (1,(2**i)+1):
		k=(2**i)+j-1
		K[k][0]=i
		K[k][1]=j

for i in range (N):
	for j in range (N):
		if i==0:
			HAB[i][j]=1
		else:
			p=(K[i][1]-1)/(2**K[i][0])
			q=(K[i][1]-(1/2))/(2**K[i][0])
			r=(K[i][1])/(2**K[i][0])
			if p<=Z[j]<q:
				HAB[i][j]=2**(K[i][0]/2)
			elif q<=Z[j]<r:
				HAB[i][j]=-2**(K[i][0]/2)
			else:		
				HAB[i][j]=0

		

HAB=HAB/(N**(1/2))			
print("HAAR BASIS")	
print (HAB)

HAT=np.dot(np.dot(HAB,img),np.transpose(HAB))
print("HAAR TRANSFORM")
print(HAT)
recons=np.dot(np.dot(np.transpose(HAB),HAT),HAB)
print("RECONSTRUCTION")
print(recons)
cv2.imwrite("1c_basis.jpg",HAB*255)
cv2.imwrite("1c.jpg",HAT)
cv2.imwrite("1c_reconstruction.jpg",recons)

HAB=np.triu(HAB,0)
print("HAAR BASIS CR")	
print (HAB)

HAT=np.dot(np.dot(HAB,img),np.transpose(HAB))
print("HAAR TRANSFORM CR")
print(HAT)
recons=np.dot(np.dot(np.transpose(HAB),HAT),HAB)
print("RECONSTRUCTION CR")
print(recons)
cv2.imwrite("1c_basis_cr.jpg",HAB*255)
cv2.imwrite("1c_cr.jpg",HAT)
cv2.imwrite("1c_reconstruction_cr.jpg",recons)


