from PIL import Image
import numpy as np
img=Image.open("q2.jpg")
img=img.convert("L")
ima=np.array(img)
im=ima
for k in range (6):
	imc = np.zeros(((im.shape[0]/2),(im.shape[1]/2)))
	for i in range(im.shape[0]/2):
		for j in range(im.shape[1]/2):
			s = int(im[2*i][2*j])
			s += int(im[2*i+1][2*j])
			s += int(im[2*i+1][2*j+1])
			s += int(im[2*i][2*j+1])
			s = np.uint(s/4)
			imc[i][j] = s
	
	imgn = Image.fromarray(imc)
	imgn=imgn.convert("L")
	
	stri="2_"+str(im.shape[0]/2)+".jpg"
	imgn.save(stri)
	im1024=np.zeros((1024,1024))
	r=1024/imc.shape[0]
	for i in range (1024):
		for j in range (1024):
			im1024[i][j]=imc[i/r][j/r]
	imen=Image.fromarray(im1024)
	imen=imen.convert("L")
	strn="2_"+str(imc.shape[0])+"_1024.jpg"
	imen.save(strn)
	im=imc
