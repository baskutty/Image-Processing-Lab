import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("cameraman.tif",0)
height, width = image.shape[:2]
newimg=np.zeros(image.shape,dtype=int)
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
hmatrixa2=np.zeros(image.shape,dtype=int)
hmatrixa3=np.zeros(image.shape,dtype=int)
rmatrixa1=np.zeros(image.shape,dtype=complex)
rmatrixa2=np.zeros(image.shape,dtype=complex)
rmatrixa3=np.zeros(image.shape,dtype=complex)


for i in range(height):
	for j in range(width):
		t[i][j] = np.sqrt(np.power((i-height/2),2) + np.power((j-width/2),2))
		if(t[i][j] > 10):
			hmatrixa1[i][j] = 1
		if(t[i][j] > 60):
			hmatrixa2[i][j] = 1
		if(t[i][j] > 100):
			hmatrixa3[i][j] = 1



for i in range(height):
	for j in range(width):
		rmatrixa1[i][j] = fourier[i][j] * hmatrixa1[i][j]
		rmatrixa2[i][j] = fourier[i][j] * hmatrixa2[i][j]
		rmatrixa3[i][j] = fourier[i][j] * hmatrixa3[i][j]

cv2.imwrite("1_a_ihpf10.jpg",np.real(rmatrixa1))
cv2.imwrite("1_a_ihpf60.jpg",np.real(rmatrixa2))
cv2.imwrite("1_a_ihpf100.jpg",np.real(rmatrixa3))

hmatrixb1=np.zeros(image.shape,dtype=float)
hmatrixb2=np.zeros(image.shape,dtype=float)
hmatrixb3=np.zeros(image.shape,dtype=float)
rmatrixb1=np.zeros(image.shape,dtype=complex)
rmatrixb2=np.zeros(image.shape,dtype=complex)
rmatrixb3=np.zeros(image.shape,dtype=complex)

for i in range(height):
	for j in range(width):
		hmatrixb1[i][j] = 1 - 1/(1+np.power((t[i][j]/10),2*2))
		hmatrixb2[i][j] = 1 - 1/(1+np.power((t[i][j]/60),2*2))
		hmatrixb3[i][j] = 1 - 1/(1+np.power((t[i][j]/100),2*2))

for i in range(height):
	for j in range(width):
		rmatrixb1[i][j] = fourier[i][j] * hmatrixb1[i][j]
		rmatrixb2[i][j] = fourier[i][j] * hmatrixb2[i][j]
		rmatrixb3[i][j] = fourier[i][j] * hmatrixb3[i][j]

cv2.imwrite("1_b_bhpf10.jpg",np.real(rmatrixb1))
cv2.imwrite("1_b_bhpf60.jpg",np.real(rmatrixb2))
cv2.imwrite("1_b_bhpf100.jpg",np.real(rmatrixb3))


hmatrixc1=np.zeros(image.shape,dtype=float)
hmatrixc2=np.zeros(image.shape,dtype=float)
hmatrixc3=np.zeros(image.shape,dtype=float)
rmatrixc1=np.zeros(image.shape,dtype=complex)
rmatrixc2=np.zeros(image.shape,dtype=complex)
rmatrixc3=np.zeros(image.shape,dtype=complex)
irmatrixc3=np.zeros(image.shape,dtype=complex)

for i in range(height):
	for j in range(width):
		hmatrixc1[i][j] = 1 - np.exp((-t[i][j]**2)/(2*10*10))
		hmatrixc2[i][j] = 1 - np.exp((-t[i][j]**2)/(2*60*60))
		hmatrixc3[i][j] = 1 - np.exp((-t[i][j]**2)/(2*100*100))

for i in range(height):
	for j in range(width):
		rmatrixc1[i][j] = fourier[i][j] * hmatrixc1[i][j]
		rmatrixc2[i][j] = fourier[i][j] * hmatrixc2[i][j]
		rmatrixc3[i][j] = fourier[i][j] * hmatrixc3[i][j]

cv2.imwrite("1_c_ghpf10.jpg",np.real(rmatrixc1))
cv2.imwrite("1_c_ghpf60.jpg",np.real(rmatrixc2))
cv2.imwrite("1_c_ghpf100.jpg",np.real(rmatrixc3))

it_matrix=np.conjugate(t_matrix)
irmatrixc3=np.conjugate(rmatrixa3)
inversea1=np.abs(np.dot(np.dot(it_matrix,rmatrixa1),it_matrix))
inversea2=np.abs(np.dot(np.dot(it_matrix,rmatrixa2),it_matrix))
inversea3=np.abs(np.dot(np.dot(it_matrix,rmatrixa3),it_matrix))
inverseb1=np.abs(np.dot(np.dot(it_matrix,rmatrixb1),it_matrix))
inverseb2=np.abs(np.dot(np.dot(it_matrix,rmatrixb2),it_matrix))
inverseb3=np.abs(np.dot(np.dot(it_matrix,rmatrixb3),it_matrix))
inversec1=np.abs(np.dot(np.dot(it_matrix,rmatrixc1),it_matrix))
inversec2=np.abs(np.dot(np.dot(it_matrix,rmatrixc2),it_matrix))
inversec3=np.abs(np.dot(np.dot(it_matrix,rmatrixc3),it_matrix))

cv2.imwrite("1_d_1revihpf10.jpg",inversea1)
cv2.imwrite("1_d_1revihpf60.jpg",inversea2)
cv2.imwrite("1_d_1revihpf100.jpg",inversea3)
cv2.imwrite("1_d_2revibpf10.jpg",inverseb1)
cv2.imwrite("1_d_2revibpf60.jpg",inverseb2)
cv2.imwrite("1_d_2revibpf100.jpg",inverseb3)
cv2.imwrite("1_d_3revigpf10.jpg",inversec1)
cv2.imwrite("1_d_3revigpf60.jpg",inversec2)
cv2.imwrite("1_d_3revigpf100.jpg",inversec3)


'''plt.subplot(161),plt.imshow(np.real(rmatrixa1),'gray'),plt.title('ILPF 10 DFT')
plt.xticks([]), plt.yticks([])
plt.subplot(162),plt.imshow(inversea1,'gray'),plt.title('ILPF 10')
plt.xticks([]), plt.yticks([])
plt.subplot(163),plt.imshow(np.real(rmatrixa2),'gray'),plt.title('ILPF 60 DFT')
plt.xticks([]), plt.yticks([])
plt.subplot(164),plt.imshow(inversea2,'gray'),plt.title('ILPF 60')
plt.xticks([]), plt.yticks([])
plt.subplot(165),plt.imshow(np.real(rmatrixa3),'gray'),plt.title('ILPF 460 DFT')
plt.xticks([]), plt.yticks([])
plt.subplot(166),plt.imshow(inversea3,'gray'),plt.title('ILPF 460')
plt.xticks([]), plt.yticks([])
plt.show()'''




