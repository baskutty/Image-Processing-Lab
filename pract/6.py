import numpy as np

import cv2

from pylab import *

import matplotlib.pyplot as plt

img=cv2.imread("blood.png",0)


histogram=np.zeros((256,),dtype=float64)
Transform=np.zeros(img.shape,dtype=float64)
for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		histogram[int(round(img[i][j]))]+=1

p=np.zeros((256,),float64)

for i in range (256):
	p[i]=histogram[i]/(img.shape[0]*img.shape[1])



s=np.zeros((256,),float64)

for i in range (256):
	for j in range (i+1):
		s[i]+=p[j]



m=np.zeros((256,),float64)

for i in range (256):
	for j in range (i+1):
		m[i]+=j*p[j]

mg=m[255]

var=np.zeros((256,),float64)


for i in range (256):
	if s[i]!=0 and s[i]!=1:
		var[i]=(np.power(mg*s[i]-m[i],2))/(s[i]*(1-s[i]))

print(var)
maxi=np.amax(var)
print(maxi)
ks=np.where(var==maxi)
ks2=ks[0]
print(ks2)
k=sum(ks2) / len(ks2)

T=k

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







