import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import *
img=mpimg.imread("Q3.tif")
size_padding=int(input("Padding Size:"))
n1=img.shape[0]
n2=img.shape[1]
n11=img.shape[0]+2*size_padding
n22=img.shape[1]+2*size_padding
T_U_X=np.zeros((n1,n1),dtype=complex)
T_U_Y=np.zeros((n2,n2),dtype=complex)
T_U_X_pd=np.zeros((n11,n11),dtype=complex)
T_U_Y_pd=np.zeros((n22,n22),dtype=complex)
new_img=np.zeros((n11,n22))
#padding takes place
for i in range(n1):
	for j in range(n2):
		new_img[i+size_padding][j+size_padding]=img[i][j]
#fourier transform of image
for u in range(n1):
	for x in range(n1):
		T_U_X[u][x]=1/np.sqrt(n1)*(np.cos(-2/n1*np.pi*u*x)+1j*np.sin(-2/n1*np.pi*u*x))
for u in range(n2):
	for y in range(n2):
		T_U_Y[u][y]=1/np.sqrt(n2)*(np.cos(-2/n2*np.pi*u*y)+1j*np.sin(-2/n2*np.pi*u*y))	
		
fourier=np.dot(np.dot(T_U_X,img),T_U_Y)
fourier=np.fft.fftshift(fourier)
#fourier transform of padded image
for u in range(n11):
	for x in range(n11):
		T_U_X_pd[u][x]=1/np.sqrt(n11)*(np.cos(-2/n11*np.pi*u*x)+1j*np.sin(-2/n11*np.pi*u*x))
for u in range(n22):
	for y in range(n22):
		T_U_Y_pd[u][y]=1/np.sqrt(n22)*(np.cos(-2/n22*np.pi*u*y)+1j*np.sin(-2/n22*np.pi*u*y))	
fourier_pd=np.dot(np.dot(T_U_X_pd,new_img),T_U_Y_pd)
fourier_pd=np.fft.fftshift(fourier_pd)
normalize=255*np.power(np.abs(fourier)/amax(np.abs(fourier)),.3)
cv2.imwrite("3_a.jpg",normalize)
normalize1=255*np.power(np.abs(fourier_pd)/amax(np.abs(fourier_pd)),.3)
cv2.imwrite("3_b.jpg",normalize1)

