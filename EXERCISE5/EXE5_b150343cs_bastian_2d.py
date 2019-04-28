import math

import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *


img=cv2.imread('q1.tif',0)
print("IMAGE")
print(img)
v=0.1
Transform=np.zeros(img.shape,dtype=float64)

g=np.random.normal(0,v**0.5,img.shape)
g=g.reshape(img.shape)
print("Noise")
print(g)
Transform=img+g*100
print("Transform")
print(Transform)

combine=np.hstack((img,Transform))
cv2.imwrite("2d_noice.jpg",g*255)
cv2.imwrite("2D.jpg",Transform)
cv2.imwrite("2d.jpg",combine)
