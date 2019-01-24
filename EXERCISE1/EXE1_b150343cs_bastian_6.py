from PIL import Image
import numpy as np
im=Image.open("SET 1 IMAGE.tif")
im=im.convert("L")
ima=np.array(im)
b=im.getextrema()
minp=b[0]
maxp=b[1]
imc = np.zeros(((ima.shape[0]),(ima.shape[1])))
for i in range(ima.shape[0]):
	for j in range(ima.shape[1]):
		if ima[i][j]<(maxp/8):
		  	imc[i][j]=0
		elif ima[i][j]<(2*maxp/8):
			imc[i][j]=maxp/8
		elif ima[i][j]<(3*maxp/8):
			imc[i][j]=2*maxp/8
		elif ima[i][j]<(4*maxp/8):
			imc[i][j]=3*maxp/8
		elif ima[i][j]<(5*maxp/8):
			imc[i][j]=4*maxp/8
		elif ima[i][j]<(6*maxp/8):
			imc[i][j]=5*maxp/8
		elif ima[i][j]<(7*maxp/8):
			imc[i][j]=6*maxp/8
		elif ima[i][j]<(maxp):
			imc[i][j]=7*maxp/8
		
		else:
			imc[i][j]=maxp
newi=Image.fromarray(imc)
newi=newi.convert("L")
newi.save("6.jpg")
