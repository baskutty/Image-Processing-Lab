import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *
def fun(x,s):
	return (math.log(1+(math.exp(s)*x)))

def transform(img,s):
	Transform=np.zeros(img.shape,dtype=float64)


	for i in range (img.shape[0]):
		for j in range (img.shape[1]):
			Transform[i][j]=math.log(1+(math.exp(s)*img[i][j]))	
	return (Transform)

img=cv2.imread('q1.tif',0)
print("IMAGE")
print(img)



cv2.imwrite("1a_0.5.jpg",transform(img,0.5) *10)
cv2.imwrite("1a_1.jpg",transform(img,1) *10)
cv2.imwrite("1a_1.5.jpg",transform(img,1.5) *10)
x = np.arange(0, 256, 1)
f= np.vectorize(fun)
plt.plot(x,f(x,0.5),label='s=0.5')
plt.plot(x,f(x,1),label='s=1')
plt.plot(x,f(x,1.5),label='s=1.5')
plt.legend()
plt.savefig("1A")
plt.show()

