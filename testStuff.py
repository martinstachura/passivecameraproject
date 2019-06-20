# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:15:03 2019

@author: SiltC
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
    

imgA = LoadImage("fc2_save_2019-06-16-132059-0000.bmp")
imgB = LoadImage("fc2_save_2019-06-16-132059-0001.bmp")
imgC = imgA - imgB
ShowImage("Meh", imgC)
print(imgC)
#print(imgA)