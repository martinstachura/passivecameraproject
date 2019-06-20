# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:07:49 2019

@author: Jojo
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def LoadImage(filename):
	return mpimg.imread(filename).astype(np.float)

def ShowImage(title, img):
	plt.figure(title)
	assert img.dtype == np.float
	plt.imshow(np.clip(img, 0, 255).astype(np.uint8))
    
def numToLenFour(num):
    if len(str(num)) == 1:
        return "000"+str(num)
    if len(str(num)) == 2:
        return "00"+str(num)
    if len(str(num)) == 3:
        return "0"+str(num)
    if len(str(num)) == 4:
        return str(num)

imgA = LoadImage("fc2_save_2019-06-16-132059-0000.bmp")
imgB = LoadImage("fc2_save_2019-06-16-132059-0001.bmp")
imgC = imgA - imgB
ShowImage("Meh", imgC)
print(imgC)
#print(imgA)

d = {}
for i in range(0,10000):
    #num = 0000 + i
    #print(num)
    d["img{}".format(i)] = LoadImage("fc2_save_2019-06-16-132059-" + numToLenFour(i) + ".bmp")

print("fertig")