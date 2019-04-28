import numpy as np

import cv2

from pylab import *

import matplotlib.pyplot as plt

img=cv2.imread("blood.png",0)
T0=1
ret,th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

T=ret

print(T)
print(ret)

"""def tres (img,T):

	m=img.shape[0]
	n=img.shape[1]
	temp=np.zeros(img.shape,dtype=int)


	while (1):
		for i in range(m):
			for j in range(n):
				if img[i][j]>T:
					temp[i][j]=255
		s1=0
		s2=0
		c1=0
		c2=0
		for i in range(m):
			for j in range(n):
				if temp[i][j]==255:
					s1=s1+img[i][j]
					c1=c1+1
				else:
					s2=s2+img[i][j]
					c2=c2+1
		a1=s1/c1
		a2=s2/c2
		tmp=T
		T=(a1+a2)/2.0
		if (tmp-T)<T0:
			break
		


	for i in range(m):
		for j in range(n):
			if img[i][j]>T:
				temp[i][j]=255
	return temp"""
m=img.shape[0]
n=img.shape[1]
temp=np.zeros(img.shape,dtype=int)
for i in range(m):
	for j in range(n):
		if img[i][j]>T:
			temp[i][j]=255

cv2.imwrite("seg_image.jpg",temp)
temp=np.zeros(img.shape,dtype=int)
for i in range(m):
	for j in range(n):
		if img[i][j]>(T+20):
			temp[i][j]=255

cv2.imwrite("seg_image+20.jpg",temp)
temp=np.zeros(img.shape,dtype=int)
for i in range(m):
	for j in range(n):
		if img[i][j]>(T-20):
			temp[i][j]=255

cv2.imwrite("seg_image-20.jpg",temp)







