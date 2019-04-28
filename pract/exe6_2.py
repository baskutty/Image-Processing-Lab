import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("cameraman.tif",0)
height, width = image.shape[:2]
newimg=np.zeros(image.shape,dtype=int)
gmask=np.zeros(image.shape,dtype=int)
high_boost=np.zeros(image.shape,dtype=int)
t_matrix=np.zeros((height,width),dtype=complex)
fourier=np.zeros((height,width),dtype=complex)
r_fourier=np.zeros((height,width),dtype=complex)


i=0
while (i<height):
	j=0
	while(j<width):
		newimg[i][j]=image[i][j]*np.power(-1,i+j)
		j=j+1
	i=i+1

i = 0
n = height
while (i<height):
	j=0
	while(j<width):
		t_matrix[i][j]=1/np.sqrt(n)*np.exp(-2*np.pi*i*j*1j/n)
		j = j+1
	i = i+1


fourier = np.dot(np.dot(t_matrix,newimg),t_matrix)
r_fourier = np.real(fourier)

t=np.zeros(image.shape,dtype=float)

hmatrixa1=np.zeros(image.shape,dtype=int)
rmatrixa1=np.zeros(image.shape,dtype=complex)

for i in range(height):
	for j in range(width):
		t[i][j] = np.sqrt(np.power((i-height/2),2) + np.power((j-width/2),2))
		if(t[i][j] <= 10):
			hmatrixa1[i][j] = 1
		

for i in range(height):
	for j in range(width):
		rmatrixa1[i][j] = fourier[i][j] * hmatrixa1[i][j]

it_matrix = np.conjugate(t_matrix)
ilpf = np.abs(np.dot(np.dot(it_matrix,rmatrixa1),it_matrix))
		
gmask = image - ilpf
high_boost = image + 1.5 * gmask

cv2.imwrite("2_highboost.jpg",high_boost)


hmatrix_high = np.zeros(image.shape,dtype=int)

for i in range(height):
	for j in range(width):
		t[i][j] = np.sqrt(np.power((i-height/2),2) + np.power((j-width/2),2))
		if(t[i][j] > 10):
			hmatrix_high[i][j] = 1

temp = (1 + 1.5 * hmatrix_high) * fourier
high_emphasis = np.abs(np.dot(np.dot(it_matrix,temp),it_matrix))
cv2.imwrite("2_highemphasis.jpg",high_emphasis)
