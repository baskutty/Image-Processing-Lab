import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *

import random


img=cv2.imread('q1.tif',0)

m=img.shape[0]
n=img.shape[1]


s=0
for i in range(m):
	for j in range(n):
		s=s+img[i][j]

T=s/(m*n)

tres=np.zeros(img.shape,dtype=int)

for i in range(m):
	for j in range(n):
		if img[i][j]>T:
			tres[i][j]=255
cv2.imwrite("tresh_image.jpg",tres)

T0=1
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
cv2.imwrite("seg_image.jpg",temp)

noise=np.zeros(img.shape,dtype=int)
for i in range(m):

    for j in range(n):

        noise[i][j] = random.randint(0,255)

img_noise= np.zeros(img.shape,dtype=np.uint8)

for i in range(m):

    for j in range(n):

        if(noise[i][j]<10):

            img_noise[i][j] = 0

        elif(noise[i][j]>245):

            img_noise[i][j] = 255

        else:

            img_noise[i][j] = seg[i][j]

cv2.imwrite("seg_noise.jpg",img_noise)


med=img
midi=0
midj=0
n=3
to=int(n/2)

for i in range(to,img.shape[0]-to):
	for j in range(to,img.shape[1]-to):
		temp1 = np.zeros((n*n,),float64)
		count=0
		for k in range(n):
			for l in range(n):
				if i+k-midi<(img.shape[0]) and i+k-midi>=0 and j+l-midj<(img.shape[1]) and j+l-midj>=0:
					temp1[count]=img_noise[i+k-midi][j+l-midj]
					count=count+1
			
		med[i][j]=np.median(temp1)

cv2.imwrite("img_final.jpg",med)
			
				
	



