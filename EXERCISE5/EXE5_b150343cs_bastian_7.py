import numpy as np

import matplotlib.pyplot as plt

import cv2

from pylab import *

def centering (img):
	result=np.zeros(img.shape)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			result[i][j]=img[i][j]*np.power(-1,i+j)	
	return result

def ideal (img,d0):
	result=np.zeros(img.shape)
	p=img.shape[0]
	q=img.shape[1]
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			d=np.sqrt(np.power((i-p/2),2)+np.power((j-q/2),2))
			if(d<=d0):
				result[i][j]=1
			else:
				result[i][j]=0
	return result	

def butter (img,d0,n):
	result=np.zeros(img.shape)
	p=img.shape[0]
	q=img.shape[1]
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			d=np.power((i-p/2),2)+np.power((j-q/2),2)
			result[i][j]=math.exp(-d/(2*np.power(d0,2)))
	return result	

def guass (img,d0):
	result=np.zeros(img.shape)
	p=img.shape[0]
	q=img.shape[1]
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			d=np.sqrt(np.power((i-p/2),2)+np.power((j-q/2),2))
			result[i][j]=1/(1+np.power((d/d0),2*n))
	return result

img=cv2.imread('q1.tif',0)
img=centering(img)
T_U_X=np.zeros(img.shape,dtype=complex)

n=img.shape[0]

for u in range(n):
	for x in range(n):
		T_U_X[u][x]=1/np.sqrt(n)*(np.cos(-2/n*np.pi*u*x)+1j*np.sin(-2/n*np.pi*u*x))


fourier=np.dot(np.dot(T_U_X,img),T_U_X)
I_T_U_X=np.conjugate(T_U_X)

def invert(im):
	image=np.abs(np.dot(np.dot(I_T_U_X,im),I_T_U_X))
	return image
	

filt10=ideal(fourier,10)
filt60=ideal(fourier,60)
filt460=ideal(fourier,460)
cv2.imwrite("7_lpfa.jpg",filt10)
cv2.imwrite("7_lpfb.jpg",filt60)
cv2.imwrite("7_lpfc.jpg",filt460)

res10=np.multiply(fourier,filt10)
res60=np.multiply(fourier,filt60)
res460=np.multiply(fourier,filt460)
cv2.imwrite("7_lpa.jpg",np.real(res10))
cv2.imwrite("7_lpb.jpg",np.real(res60))
cv2.imwrite("7_lpc.jpg",np.real(res460))
cv2.imwrite("7_lpa_inv.jpg",centering(np.real(invert(res10))))
cv2.imwrite("7_lpb.jpg_inv",centering(np.real(invert(res60))))
cv2.imwrite("7_lpc.jpg_inv",centering(np.real(invert(res460))))

filt10=guass(fourier,10)
filt60=guass(fourier,60)
filt460=guass(fourier,460)
cv2.imwrite("7_gfa.jpg",filt10)
cv2.imwrite("7_gfb.jpg",filt60)
cv2.imwrite("7_gfc.jpg",filt460)

res10=np.multiply(fourier,filt10)
res60=np.multiply(fourier,filt60)
res460=np.multiply(fourier,filt460)
cv2.imwrite("7_ga.jpg",np.real(res10))
cv2.imwrite("7_gb.jpg",np.real(res60))
cv2.imwrite("7_gc.jpg",np.real(res460))
cv2.imwrite("7_ga_inv.jpg",centering(np.real(invert(res10))))
cv2.imwrite("7_gb.jpg_inv",centering(np.real(invert(res60))))
cv2.imwrite("7_gc.jpg_inv",centering(np.real(invert(res460))))

s=float(input("n for butter:"))
filt10=butter(fourier,10,s)
filt60=butter(fourier,60,s)
filt460=butter(fourier,460,s)
cv2.imwrite("7_bfa.jpg",filt10)
cv2.imwrite("7_bfb.jpg",filt60)
cv2.imwrite("7_bfc.jpg",filt460)

res10=np.multiply(fourier,filt10)
res60=np.multiply(fourier,filt60)
res460=np.multiply(fourier,filt460)
cv2.imwrite("7_ba.jpg",np.real(res10))
cv2.imwrite("7_bb.jpg",np.real(res60))
cv2.imwrite("7_bc.jpg",np.real(res460))
cv2.imwrite("7_ba_inv.jpg",centering(np.real(invert(res10))))
cv2.imwrite("7_bb.jpg_inv",centering(np.real(invert(res60))))
cv2.imwrite("7_bc.jpg_inv",centering(np.real(invert(res460))))

