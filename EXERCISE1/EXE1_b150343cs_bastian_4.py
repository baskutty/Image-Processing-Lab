from PIL import Image
import numpy as np
im=Image.open("3.jpg")
im=im.convert("L")
ima=np.array(im)
imc = np.zeros(((ima.shape[0]),(ima.shape[1])))
for i in range(ima.shape[0]):
	for j in range(ima.shape[1]):
		if ima[i][j]<(0.25*255):
		  	imc[i][j]=0
		elif ima[i][j]<(0.5*255):
			imc[i][j]=0.25*255
		elif ima[i][j]<(0.75*255):
			imc[i][j]=0.5*255
		elif ima[i][j]<(1*255):
			imc[i][j]=0.75*255
		else:
			imc[i][j]=255
newi=Image.fromarray(imc)
newi=newi.convert("L")
newi.save("4.jpg")
