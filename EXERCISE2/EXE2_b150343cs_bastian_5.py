import numpy as np
n=int(input("n:"))
m=int(input("m:"))
A = np.zeros((n,n),dtype=int)
B = np.zeros((m,m),dtype=int)
C1 = np.zeros((m,m),dtype=int)
C2 = np.zeros((n,n),dtype=int)


print "Enter First Matrix:"

i = 0

for i in range(n):
   A[i]=raw_input().split(" ")


print "Enter Second Matrix:"

i = 0

for i in range(m):
   B[i]=raw_input().split(" ")

if n%2==1:
        midi = int(n/2) 
        midj = int(n/2)
        mid = int((n*n)/2)

else:
        midi = 0
        midj = 0
        mid = 0
for i in range(m):
	for j in range(m):
		temp = 0
		for k in range(n):
			for l in range(n):
				if i+k-midi<m and i+k-midi>=0 and j+l-midj<m and j+l-midj>=0:
					temp += A[k][l]*B[i+k-midi][j+l-midj]
		C1[i][j] = temp
print "Correlation on 2nd Matrix with 1st Matrix as filter"
print C1
i=0
j=0
k=0
l=0
if m%2==1:
        midi = int(m/2) 
        midj = int(m/2)
        mid = int((m*m)/2)
else:
        midi = 0
        midj = 0
        mid = 0
for i in range(n):
	for j in range(n):
		temp = 0
		for k in range(m):
			for l in range(m):
				if i+k-midi<n and i+k-midi>=0 and j+l-midj<n and j+l-midj>=0:
					temp += B[k][l]*A[i+k-midi][j+l-midj]
		C2[i][j] = temp


print "Correlation on 1st Matrix with 2nd Matrix as filter"
print C2
