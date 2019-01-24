from PIL import Image
import numpy as np
im=Image.open("add_b.tif")
im=im.convert("L")
ima=np.array(im)
N=int(input("Factor:"))
imc = np.zeros(((ima.shape[0]),(ima.shape[1])))
for i in range(ima.shape[0]):
	for j in range(ima.shape[1]):
		s=int(ima[i][j])*int(N)
		if s>255:
			imc[i][j]=255
		else:
			imc[i][j]=s
newi=Image.fromarray(imc)
newi=newi.convert("L")
newi.save("6c.jpg")
