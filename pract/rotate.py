# Python Program illustrating 
# numpy.rot90() method 

import numpy as geek 

array = geek.arange(12).reshape(3, 4) 
print("Original array : \n", array) 

# Rotating array 4 times : Returns same original array 
print("\nArray being rotated 4 times : \n", geek.rot90(array, 4)) 

# Rotating once 
print("\nRotated array : \n", geek.rot90(array)) 

# Rotating twice 
print("\nRotated array : \n", geek.rot90(array, 2)) 



 """blur = cv2.blur(img,(5,5)) mean filter"""
