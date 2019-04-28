import numpy as np

import cv2

from pylab import *

img=cv2.imread("cameraman.tif",0)
new=np.zeros(img.shape)

for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		if img[i][j]>127:
			new[i][j]=255
		else:
			new[i][j]=0

cv2.imwrite("8bit.jpg",new)

for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		if img[i][j]>63 and img[i][j]<128:
			new[i][j]=255
		else:
			new[i][j]=0

cv2.imwrite("7bit.jpg",new)



for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		if img[i][j]>31 and img[i][j]<64:
			new[i][j]=255
		else:
			new[i][j]=0

cv2.imwrite("6bit.jpg",new)

for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		if img[i][j]>15 and img[i][j]<32:
			new[i][j]=255
		else:
			new[i][j]=0

cv2.imwrite("5bit.jpg",new)

for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		if img[i][j]>7 and img[i][j]<16:
			new[i][j]=255
		else:
			new[i][j]=0

cv2.imwrite("4bit.jpg",new)

for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		if img[i][j]>3 and img[i][j]<8:
			new[i][j]=255
		else:
			new[i][j]=0

cv2.imwrite("3bit.jpg",new)

for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		if img[i][j]>1 and img[i][j]<4:
			new[i][j]=255
		else:
			new[i][j]=0

cv2.imwrite("2bit.jpg",new)

for i in range (img.shape[0]):
	for j in range (img.shape[1]):
		if img[i][j]<2:
			new[i][j]=255
		else:
			new[i][j]=0

cv2.imwrite("1bit.jpg",new)



