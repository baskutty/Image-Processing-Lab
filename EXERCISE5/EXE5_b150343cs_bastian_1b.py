import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *

def fun(x,s):
	return (math.exp(s*x/255))


def transform(img,s):
	Transform=np.zeros(img.shape,dtype=float64)


	for i in range (img.shape[0]):
		for j in range (img.shape[1]):
			Transform[i][j]=(math.exp(s*img[i][j]/20))	
	return (Transform)

img=cv2.imread('q1.tif',0)
print("IMAGE")
print(img)



cv2.imwrite("1b_0.5.jpg",transform(img,0.5) *10)
cv2.imwrite("1b_1.jpg",transform(img,1) *10)
cv2.imwrite("1b_1.5.jpg",transform(img,1.5) *10)
#x = np.arange(0, 10, 0.1)
x = np.arange(0, 256, 1)
f= np.vectorize(fun)
plt.plot(x,f(x,0.5),label='s=0.5')
plt.plot(x,f(x,1),label='s=1')
plt.plot(x,f(x,1.5),label='s=1.5')
plt.legend()
plt.savefig("1B")
plt.show()

