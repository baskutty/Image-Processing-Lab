from PIL import Image
import numpy as np
im=Image.open("sub_a.tif")
im=im.convert("L")
ima=np.array(im)
im=Image.open("sub_b.tif")
im=im.convert("L")
imb=np.array(im)
imc = np.zeros(((ima.shape[0]),(ima.shape[1])))
for i in range(ima.shape[0]):
	for j in range(ima.shape[1]):
		s=int(ima[i][j])-int(imb[i][j])
		if s<0:
			imc[i][j]=0
		else:
			imc[i][j]=s
newi=Image.fromarray(imc)
newi=newi.convert("L")
newi.save("6b.jpg")
