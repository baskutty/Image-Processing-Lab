import numpy as np
N=int(input("Size:"))
A=[]
B=[]
C=[0]*(2*N-1)
print "Enter First",N,"Elements"
for i in range (N):
	A.append(int(input()))
print "Enter Second",N,"Elements"
for i in range (N):
	B.append(int(input()))
for i in range (2*N-1):
	if i>=(N-1):
		kmin=i-(N-1)
	else:
		kmin=0
	if i<(N-1):
		kmax=i
	else:
		kmax=N-1
	for j in range (kmin,kmax+1):
		C[i]+=A[j]*B[i-j]
print C

print "First",N

for i in range (N):
	print (C[i]),
	

