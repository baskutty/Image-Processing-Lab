from PIL import Image
import numpy as np
img=Image.open("add_b.tif")
img=img.convert("L")
ima=np.array(img)
mean=np.mean(ima)
imc = np.zeros(((ima.shape[0]),(ima.shape[1])))
for i in range(ima.shape[0]):
	for j in range(ima.shape[1]):
		if ima[i][j]<=mean:
		  	imc[i][j]=0
		
		else:
			imc[i][j]=255
newi=Image.fromarray(imc)
newi=newi.convert("L")
newi.save("1.jpg")
