from PIL import Image
import numpy as np
carr=np.zeros((64,64))
for i in range (64):	
	for j in range (64):
		carr[i][j]=np.absolute(np.cos(np.sqrt((i*i+j*j))))

newi=Image.fromarray(carr*255)
newi=newi.convert("L")
newi.show()
newi.save("3.jpg")

