import cv2 
import numpy as np

def corelation (matrixC,matrixB,height,width,m):
    matrixE = []
    matrixA = []

    if(m%2==1):
        for i in range(0,height+m-1):
            matrixA.append([])
            for j in range(0,width+m-1):
                if (i<m/2 or j<m/2 or i>(height-1+m/2) or j>(width-1+m/2)):
                    matrixA[i].append(0)
                else:
                    x=matrixC[i-m//2][j-m//2]
                    matrixA[i].append(x)
    

        for i in range(0,height):
            matrixE.append([])
            for j in range(0,width):
                sum=0
                for k in range(0,m):
                    for l in range(0,m):
                        sum=sum+matrixA[i+k][j+l]*matrixB[k][l]
                matrixE[i].append(sum)

        return matrixE

image = cv2.imread("in.jpg",0)
height, width = image.shape[:2]
cv2.imwrite("7_a.jpg",image)

laplacian = np.zeros((height,width),dtype=np.float64)
for i in range(height):
	for j in range(width):
		if(i==0 or j==0 or i==(height-1) or j==(width-1)):
			laplacian[i][j] = image[i][j]
		else:
			var = -int(image[i-1][j]) - int(image[i][j-1]) - int(image[i+1][j]) - int(image[i][j+1]) + 4*int(image[i][j])
			if(var>255):
				laplacian[i][j] = 255
			elif(var<0):
				laplacian[i][j] = 0
			else:
				laplacian[i][j] = var
cv2.imwrite("7_b.jpg",laplacian)

new_image_1 = np.zeros((height,width),dtype=np.float64)
for i in range(height):
	for j in range(width):
		var = image[i][j] + laplacian[i][j]
		if(var > 255):
			new_image_1[i][j] = 255
		else:
			new_image_1[i][j] = var
cv2.imwrite("7_c.jpg",new_image_1)

sobel = np.zeros((height,width),dtype=int)
matrixX = [[-1,-2,-1],[0,0,0],[1,2,1]]
matrixY = [[-1,0,1],[-2,0,2],[-1,0,1]] 
gx = corelation(image,matrixX,height,width,3)
gy = corelation(image,matrixY,height,width,3)
for i in range(height):
	for j in range(width):
		sobel[i][j] = np.sqrt(np.power(gx[i][j],2) + np.power(gy[i][j],2))
cv2.imwrite("7_d.jpg",sobel)

n = 5
mean = np.zeros((height,width),dtype=np.uint8)
for i in range(height):
	for j in range(width):
		if(i < n/2 or j < n/2 or i >= (height - n/2) or j >= (width - n/2)):
			mean[i][j] = sobel[i][j]
i=0
while((i+n) <= height):
	j=0
	while((j+n) <= width):
		arr = np.zeros((n,n),dtype=np.uint8)
		for k in range(n):
			for l in range(n):
				arr[k][l] = sobel[i+k][j+l]
		mean_value = np.mean(arr)
		mean[i+n//2][j+n//2] = mean_value
		j = j+1
	i = i+1
cv2.imwrite("7_e.jpg",mean)

new_image_2 = np.zeros((height,width),dtype=np.float64)
for i in range(height):
	for j in range(width):
		var = new_image_1[i][j] * mean[i][j]
		if(var > 255):
			new_image_2[i][j] = 255
		else:
			new_image_2[i][j] = var
cv2.imwrite("7_f.jpg",new_image_2)

new_image_3 = np.zeros((height,width),dtype=np.float64)
for i in range(height):
	for j in range(width):
		var = image[i][j] + new_image_2[i][j]
		if(var > 255):
			new_image_3[i][j] = 255
		else:
			new_image_3[i][j] = var
cv2.imwrite("7_g.jpg",new_image_3)

new_image_4 = np.zeros((height,width),dtype=np.float64)
for i in range(height):
	for j in range(width):
		new_image_4[i][j] = new_image_3[i][j] ** 0.5 
cv2.imwrite("7_h.jpg",new_image_4)
