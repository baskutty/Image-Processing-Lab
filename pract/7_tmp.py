import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *
def correlation (A,B,m):
	midi = int(m/2) 
	midj = int(m/2)
	mid = int((m*m)/2)	
	n=A.shape[0]	
	C2=np.zeros(A.shape,dtype=float64)
	for i in range(n):
		for j in range(img.shape[1]):
			temp = 0
			for k in range(m):
				for l in range(m):
					if i+k-midi<n and i+k-midi>=0 and j+l-midj<img.shape[1] and j+l-midj>=0:
						temp += B[k][l]*A[i+k-midi][j+l-midj]
			C2[i][j] = temp	
	return C2
def lap(img):
	lap=np.zeros(img.shape,dtype=float64)
	
        
	for i in range(1,img.shape[0]-1):
		for j in range(1,img.shape[1]-1):
			lap[i][j]=lap[i][j]+img[i-1][j]+img[i+1][j]+img[i][j+1]+img[i][j-1]-(4*img[i][j])
	print("LAPLACE")
	return lap
img = cv2.imread("in.jpg",0)
def maxfil(img):
	maxf=np.zeros(img.shape,dtype=float64)

	
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			maxn=0
			for k in range(3):
				for l in range(3):
					if i+k<(img.shape[0]) and i+k>=0 and j+l<(img.shape[1]) and j+l>=0:
						if maxn<img[i+k][j+l]:
							maxn=img[i+k][j+l]
			maxf[i][j]=maxn
	return maxf

image=img

blur=np.zeros(img.shape,dtype=float64)

n=img.shape[0]

"""for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		temp = 0
		for k in range(3):
			for l in range(3):
				if i+k<n and i+k>=0 and j+l<img.shape[1] and j+l>=0:
					temp +=img[i+k][j+l]
		blur[i][j] = temp
blur=blur/9

img=blur"""


img=img+lap(image)

S1=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
S2=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
temp1=correlation(image,S1,3)
temp2=correlation(image,S2,3)
ans=np.sqrt(np.square(temp1)+np.square(temp2))

img=img+ans
img=img+maxfil(image)

cv2.imwrite("tmp.jpg",img)


