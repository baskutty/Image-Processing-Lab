import numpy as np

import cv2

from pylab import *

import matplotlib.pyplot as plt

img=cv2.imread("checker.jpg",0)

plt.hist(img.ravel(),256,[0,256]);
plt.savefig("hist.jpg")
plt.show()


blur=np.zeros(img.shape,dtype=float64)

n=3
	
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
cv2.imwrite("blur.jpg",blur)
plt.hist(blur.ravel(),256,[0,256]);
plt.savefig("hist_blur.jpg")
plt.show()
