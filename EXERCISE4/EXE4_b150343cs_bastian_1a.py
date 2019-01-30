import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *



def make_array(num,bits):
	
	arr=np.zeros((bits,),dtype=int)
	i=bits-1
	while i>=0:
		arr[i]=num%2
		num=num/2
		i=i-1
	return arr
			

def count_overlap(a,b,bits):
	count=0
	for i in range(bits):
		if a[i]==b[i] and a[i]==1:
			count=count+1
	return count

img=cv2.imread('q1.tif',0)
print("IMAGE")
print(img)

WB=np.zeros(img.shape,dtype=float64)

n=img.shape[0]
bits=int (math.log(n,2))

for x in range(n):
	x_t=np.flipud(make_array(x,bits))
	for y in range(n):
		if count_overlap(make_array(y,bits),x_t,bits)%2==0:
			WB[x][y]=1
		else:
			WB[x][y]=-1
print("WALSH BASIS")
print(WB)

WT=np.dot(np.dot(WB,img),WB)
print("WALSH TRANSFORM")
print(WT)
recons=np.dot(np.dot(WB,WT),WB)/(n*n)
print("RECONSTRUCTION")
print(recons)

cv2.imwrite("1a_basis.jpg",WB*255)
cv2.imwrite("1a.jpg",WT)
cv2.imwrite("1a_reconstruction.jpg",recons)

WB=np.triu(WB,0)

print("WALSH BASIS CR")
print(WB)

WT=np.dot(np.dot(WB,img),np.transpose(WB))
print("WALSH TRANSFORM CR")
print(WT)
recons=np.dot(np.dot(np.transpose(WB),WT),WB)/(n*n)
print("RECONSTRUCTION CR")
print(recons)

cv2.imwrite("1a_basis_cr.jpg",WB*255)
cv2.imwrite("1a_cr.jpg",WT)
cv2.imwrite("1a_reconstruction_cr.jpg",recons)
		
