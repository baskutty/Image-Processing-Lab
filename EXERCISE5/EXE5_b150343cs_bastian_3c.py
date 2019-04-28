import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *


img=cv2.imread('cameraman.tif',0)
img=img*0.5
print("IMAGE")
print(img)

"""hist,bins=np.histogram(img.ravel(),256,[0,256])



cdf=hist.cumsum()
cdf_norm=cdf*hist.max()/cdf.max()

cv2.imwrite("dark3.jpg",img)
plt.plot(cdf_norm,color='b')
plt.hist(img.ravel(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.savefig("3c.jpg")
plt.show()"""
histogram=np.zeros((256,),dtype=int64)
Transform=np.zeros(img.shape,dtype=float64)
for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		histogram[int(round(img[i][j]))]+=1

p=np.zeros((256,),float64)

for i in range (256):
	p[i]=histogram[i]/(img.shape[0]*img.shape[1])

print(p)

s=np.zeros((256,),float64)

for i in range (256):
	for j in range (i+1):
		s[i]+=p[j]
s=s*255

for i in range (256):
	s[i]=round(s[i])

print(s)


for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		Transform[i][j]=s[int(round(img[i][j]))]
combine=np.hstack((img,Transform))
cv2.imwrite("3c_equalized.jpg",combine)
plt.hist(Transform.ravel(),256,[0,256]);
plt.savefig("3c.jpg")
plt.show()














