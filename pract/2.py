import cv2 
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('blob.jpg',0)

img = cv2.medianBlur(img,11)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=30,maxRadius=50)

circles = np.uint16(np.around(circles))
temp = np.zeros(cimg.shape, np.uint16)
temp[:, :] = [255, 255, 255]
for i in circles[0,:]:
    cv2.circle(temp,(i[0],i[1]),i[2],(255,0,0),-1)
    
cv2.imwrite("big_blobs.jpg",temp)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=10,maxRadius=25)

circles= np.uint16(np.around(circles))
temp = np.zeros(cimg.shape, np.uint16)
temp[:, :] = [255, 255, 255]

for i in circles[0,:]:
    cv2.circle(temp,(i[0],i[1]),i[2],(0,0,255),-1)

cv2.imwrite("small_blobs.jpg",temp)



