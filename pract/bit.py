import cv2 
import numpy as np

image = cv2.imread("cameraman.tif",0)
height, width = image.shape[:2]

def convert_to_binary(number):
	i = 7
	binary=np.zeros(8,dtype=int)
	while(i>=0):
		binary[i] = number%2
		number = number/2
		i = i-1
	return binary


new_image_1 = np.zeros(image.shape,dtype=float)
new_image_2 = np.zeros(image.shape,dtype=float)
new_image_3 = np.zeros(image.shape,dtype=float)
new_image_4 = np.zeros(image.shape,dtype=float)
new_image_5 = np.zeros(image.shape,dtype=float)
new_image_6 = np.zeros(image.shape,dtype=float)
new_image_7 = np.zeros(image.shape,dtype=float)
new_image_8 = np.zeros(image.shape,dtype=float)

for i in range(height):
	for j in range(width):
		binary = convert_to_binary(image[i][j])
		if(binary[0] == 1):
			new_image_1[i][j] = 255
		else:
			new_image_1[i][j] = 0
		if(binary[1] == 1):
			new_image_2[i][j] = 255
		else:
			new_image_2[i][j] = 0
		if(binary[2] == 1):
			new_image_3[i][j] = 255
		else:
			new_image_3[i][j] = 0
		if(binary[3] == 1):
			new_image_4[i][j] = 255
		else:
			new_image_4[i][j] = 0
		if(binary[4] == 1):
			new_image_5[i][j] = 255
		else:
			new_image_5[i][j] = 0
		if(binary[5] == 1):
			new_image_6[i][j] = 255
		else:
			new_image_6[i][j] = 0
		if(binary[6] == 1):
			new_image_7[i][j] = 255
		else:
			new_image_7[i][j] = 0
		if(binary[7] == 1):
			new_image_8[i][j] = 255
		else:
			new_image_8[i][j] = 0

cv2.imwrite("4_1.jpg",new_image_1)
cv2.imwrite("4_2.jpg",new_image_2)
cv2.imwrite("4_3.jpg",new_image_3)
cv2.imwrite("4_4.jpg",new_image_4)
cv2.imwrite("4_5.jpg",new_image_5)
cv2.imwrite("4_6.jpg",new_image_6)
cv2.imwrite("4_7.jpg",new_image_7)
cv2.imwrite("4_8.jpg",new_image_8)
