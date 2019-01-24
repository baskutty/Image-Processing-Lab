import cv2
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
img=cv2.imread("Q2.tif",0)
result1=np.zeros(img.shape)
#multiplication by -1^(x+y)
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		result1[i][j]=img[i][j]*np.power(-1,i+j)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
cv2.imwrite("2_a.jpg",result1)
img=cv2.imread("2_a.jpg",0)
plt.subplot(122),plt.imshow(img, cmap = 'gray')
plt.title('Output Image'), plt.xticks([]), plt.yticks([])
plt.show()
#compute the dft
T_U_X=np.zeros((img.shape[0],img.shape[0]),dtype=complex)
T_U_Y=np.zeros((img.shape[1],img.shape[1]),dtype=complex)
fourier=np.zeros((img.shape),dtype=complex)
n1=result1.shape[0]
n2=result1.shape[1]
for u in range(n1):
	for x in range(n1):
		T_U_X[u][x]=1/np.sqrt(n1)*(np.cos(-2/n1*np.pi*u*x)+1j*np.sin(-2/n1*np.pi*u*x))
for u in range(n2):
	for y in range(n2):
		T_U_Y[u][y]=1/np.sqrt(n2)*(np.cos(-2/n2*np.pi*u*y)+1j*np.sin(-2/n2*np.pi*u*y))		
fourier=np.dot(np.dot(T_U_X,result1),T_U_Y)
print("Fourier Transform of the result:")
print(fourier)
cv2.imwrite("2_b.jpg",np.real(fourier))
img=cv2.imread("2_b.jpg",0)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Fourier'), plt.xticks([]), plt.yticks([])
plt.show()
#Obtain complex conjugate
print("Complex conjugate of the fourier transform:")
complex_conjugate=np.conjugate(fourier)
print(complex_conjugate)
cv2.imwrite("2_c.jpg",np.real(complex_conjugate))
img=cv2.imread("2_c.jpg",0)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Complex conjugate'), plt.xticks([]), plt.yticks([])
plt.show()
#Compute IDFT
I_T_U_X=np.conjugate(T_U_X)
I_T_U_Y=np.conjugate(T_U_Y)
inverse_fourier=np.dot(np.dot(I_T_U_X,complex_conjugate),I_T_U_Y)
print("Inverse Fourier transform:")
print(inverse_fourier)
cv2.imwrite("2_d.jpg",np.real(inverse_fourier))
img=cv2.imread("2_d.jpg",0)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Inverse fourier'),plt.xticks([]),plt.yticks([])
savefig("2_d.jpg")
plt.show()
#multiplication by -1^(x+y) to real part
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		result1[i][j]=inverse_fourier[i][j]*np.power(-1,i+j)
plt.subplot(121),plt.imshow(result1,cmap='gray')
plt.title('-1^(x+y) x real part of inverse fourier'),plt.xticks([]),plt.yticks([])
savefig("2_e.jpg")
plt.show() 
