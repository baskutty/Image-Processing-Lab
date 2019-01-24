import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
img=mpimg.imread("Q4.tif")
T_U_X=np.zeros(img.shape,dtype=complex)
n=img.shape[0]

for u in range(n):
	for x in range(n):
		T_U_X[u][x]=1/np.sqrt(n)*(np.cos(-2/n*np.pi*u*x)+1j*np.sin(-2/n*np.pi*u*x))

fourier=np.dot(np.dot(T_U_X,img),T_U_X)

fourier2=np.dot(np.dot(T_U_X,fourier),T_U_X)
fig=plt.figure(figsize=(20,20))
fig.add_subplot(1, 3, 1)
plt.imshow(img,cmap='gray'),plt.title('Input Image'), plt.xticks([]), plt.yticks([])
fig.add_subplot(1, 3, 2)
cv2.imwrite("4_a.jpg",np.real(fourier))
img=cv2.imread("4_a.jpg",0)
plt.imshow(img,cmap='gray'),plt.title('First Fourier'), plt.xticks([]), plt.yticks([])
fig.add_subplot(1, 3, 3)
plt.imshow(np.real(fourier2),cmap='gray'),plt.title('Second Fourier'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite("4_b.jpg",np.real(fourier2))
