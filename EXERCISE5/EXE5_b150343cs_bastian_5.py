import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *


img=cv2.imread('cameraman.tif',0)

print("MENU")
print("Enter 1 for MEDIAN filter")
print("Enter 2 for MAX filter")
print("Enter 3 for MIN filter")
print("Enter 4 for MEAN filter")

choice=int(input("Choice:"))

n=int(input("Odd No:"))

if (choice==1):
	med=img
	midi=0
	midj=0
	to=int(n/2)
	for i in range(to,img.shape[0]-to):
		for j in range(to,img.shape[1]-to):
			temp = np.zeros((n*n,),float64)
			count=0
			for k in range(n):
				for l in range(n):
					if i+k-midi<(img.shape[0]) and i+k-midi>=0 and j+l-midj<(img.shape[1]) and j+l-midj>=0:
						temp[count]=img[i+k-midi][j+l-midj]
						count=count+1
			
			med[i][j]=np.median(temp)
	print("MEDIAN")
	print(med)
	cv2.imwrite("5a.jpg",med)

if (choice==2):
	maxf=np.zeros(img.shape,dtype=float64)

	
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			maxn=0
			for k in range(n):
				for l in range(n):
					if i+k<(img.shape[0]) and i+k>=0 and j+l<(img.shape[1]) and j+l>=0:
						if maxn<img[i+k][j+l]:
							maxn=img[i+k][j+l]
			maxf[i][j]=maxn
	print("MAX")
	print(maxf)
	cv2.imwrite("5b.jpg",maxf)	


if (choice==3):
	minf=np.zeros(img.shape,dtype=float64)

	
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			minn=255
			for k in range(n):
				for l in range(n):
					if i+k<(img.shape[0]) and i+k>=0 and j+l<(img.shape[1]) and j+l>=0:
						if minn>img[i+k][j+l]:
							minn=img[i+k][j+l]
			minf[i][j]=minn
	print("MIN")
	print(minf)
	cv2.imwrite("5c.jpg",minf)

if (choice==4):
	blur=np.zeros(img.shape,dtype=float64)

	
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			temp=0
			for k in range(n):
				for l in range(n):
					if i+k<(img.shape[0]) and i+k>=0 and j+l<(img.shape[1]) and j+l>=0:
						temp +=img[i+k][j+l]
			blur[i][j] = temp
	blur=blur/(n*n)
	print("BLUR")
	print(blur)
	cv2.imwrite("5d.jpg",blur)




















