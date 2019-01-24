import numpy as np
import matplotlib.pyplot as plt
import cv2
from pylab import *
img=cv2.imread('q1.tif',0)
T_U_X=np.zeros(img.shape,dtype=complex)
n=img.shape[0]
for u in range(n):
	for x in range(n):
		T_U_X[u][x]=1/np.sqrt(n)*(np.cos(-2/n*np.pi*u*x)+1j*np.sin(-2/n*np.pi*u*x))

fourier=np.dot(np.dot(T_U_X,img),T_U_X)
fourier_real=np.real(fourier)
print("fourier:",fourier)
#magnetic spectrum
magnitude_spectrum=np.abs(fourier)

#phase spectrum
phase_spectrum=np.angle(fourier)
print(phase_spectrum)
phase_spectrum_magnitude=np.exp(phase_spectrum)
#double_magnitude_spectrum
double=magnitude_spectrum*2

#inverse_discete_fourier
I_T_U_X=np.conjugate(T_U_X)
image_from_fourier=np.abs(np.dot(np.dot(I_T_U_X,fourier),I_T_U_X))
print(np.dot(I_T_U_X,I_T_U_X))


#image from phase spectrum
image_from_phase=np.abs(np.dot(np.dot(I_T_U_X,magnitude_spectrum),I_T_U_X))

#saving all images
cv2.imwrite("1_a.jpg",np.real(fourier))
cv2.imwrite("1_b.jpg",np.log(magnitude_spectrum))
cv2.imwrite("1_c.jpg",phase_spectrum)
cv2.imwrite("1_d.jpg",double)
cv2.imwrite("1_e.jpg",image_from_fourier)
cv2.imwrite("1_f.jpg",np.real(image_from_phase))
#display of images
fig=plt.figure(figsize=(10,10))
fig.add_subplot(331)
img=cv2.imread("q1.tif",0)
plt.imshow(img,cmap='gray'),plt.title('Input'), plt.xticks([]), plt.yticks([])
fig.add_subplot(332)
img=cv2.imread("1_a.jpg",0)
plt.imshow(img,cmap='gray'),plt.title('Fourier Transform'), plt.xticks([]), plt.yticks([])
fig.add_subplot(333)
img=cv2.imread("1_b.jpg",0)
plt.imshow(img,cmap='gray'),plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
fig.add_subplot(334)
img=cv2.imread("1_c.jpg",0)
plt.imshow(img,cmap='gray'),plt.title('Phase Spectrum'), plt.xticks([]), plt.yticks([])
fig.add_subplot(335)
img=cv2.imread("1_d.jpg",0)
plt.imshow(img,cmap='gray'),plt.title('2 x Magnetic Spectrum'), plt.xticks([]), plt.yticks([])
fig.add_subplot(336)
img=cv2.imread("1_e.jpg",0)
plt.imshow(img,cmap='gray'),plt.title('IDFT'), plt.xticks([]), plt.yticks([])
fig.add_subplot(337)
img=cv2.imread("1_f.jpg",0)
plt.imshow(img,cmap='gray'),plt.title('Removing phase spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
