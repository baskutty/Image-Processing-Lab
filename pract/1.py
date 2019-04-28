import numpy as np

import cv2

from pylab import *
import collections
import matplotlib.pyplot as plt

img=cv2.imread("cameraman.tif",0)


CB=np.zeros(img.shape,dtype=float64)


for u in range(img.shape[0]):
	for x in range(img.shape[0]):
		if u==0:
			CB[u][x]=np.sqrt(1/img.shape[0])*(np.cos((2*x+1)*np.pi*u/(2*img.shape[0])))
		else:
			CB[u][x]=np.sqrt(2/img.shape[0])*(np.cos((2*x+1)*np.pi*u/(2*img.shape[0])))


DCT=np.dot(np.dot(CB,img),np.transpose(CB))


Q=np.zeros(img.shape)
for u in range(img.shape[0]):
	for v in range(img.shape[1]):
		Q[u][v]=1+u+v

def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]
def zigzag(img):
	rows=img.shape[0]
	columns=img.shape[1]
	solution=[[] for i in range(rows+columns-1)] 
	for i in range(rows): 
		for j in range(columns):
			sum=i+j 
			if(sum%2 ==0): 
				solution[sum].insert(0,img[i][j]) 
			else: 
				solution[sum].append(img[i][j]) 
	return flatten(solution)

sol=zigzag(np.divide(np.abs(DCT),Q))
sol=np.array(sol)

#print(sol)
print(len(sol))
def huffman(lis):
	huffman_encoding=[]
	count=1
	for i in range(1,len(lis)):
		if lis[i]==lis[i-1] :
			count+=1
		else:
			huffman_encoding.append(lis[i-1])
			huffman_encoding.append(count)
			count=1
	huffman_encoding.append(lis[i])
	huffman_encoding.append(count)
	print(huffman_encoding)
huffman(sol.astype(int))





