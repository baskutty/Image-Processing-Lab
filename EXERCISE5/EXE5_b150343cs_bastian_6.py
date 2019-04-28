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
		for j in range(n):
			temp = 0
			for k in range(m):
				for l in range(m):
					if i+k-midi<n and i+k-midi>=0 and j+l-midj<n and j+l-midj>=0:
						temp += B[k][l]*A[i+k-midi][j+l-midj]
			C2[i][j] = temp	
	return C2

img=cv2.imread('cameraman.tif',0)

print("MENU")
print("Enter 1 for SOBEL filter")
print("Enter 2 for PREWIT filter")
print("Enter 3 for LAPLACIAN filter")


choice=int(input("Choice:"))




if (choice==1):
	S1=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
	S2=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
	temp1=correlation(img,S1,3)
	temp2=correlation(img,S2,3)
	ans=np.sqrt(np.square(temp1)+np.square(temp2))
	print("SOBEL")
	print(ans)
	cv2.imwrite("6a.jpg",ans)
if (choice==2):
	S1=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
	S2=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
	temp1=correlation(img,S1,3)
	temp2=correlation(img,S2,3)
	ans=np.sqrt(np.square(temp1)+np.square(temp2))
	print("PREWIT")
	print(ans)
	cv2.imwrite("6b.jpg",ans)

if (choice==3):
	lap=np.zeros(img.shape,dtype=float64)
	midi=int(img.shape[0]/2)
	midj=int(img.shape[1]/2)
        
	for i in range(1,img.shape[0]-1):
		for j in range(1,img.shape[1]-1):
			lap[i][j]=lap[i][j]+img[i-1][j]+img[i+1][j]+img[i][j+1]+img[i][j-1]-(4*img[i][j])
	print("LAPLACE")
	print(lap)
	cv2.imwrite("6c.jpg",lap)	


