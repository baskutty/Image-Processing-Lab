from PIL import Image
import numpy as np
im=Image.open("SET 1 IMAGE.tif")
im=im.convert("L")
im.show()
b=im.getextrema()
print "MINIMUM IS =",b[0]
print "MAXIMUM IS =",b[1]
