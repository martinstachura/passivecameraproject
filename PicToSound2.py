# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:07:49 2019

@author: Jojo
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from tqdm import tqdm

imgStack = {} # Images to work with

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

def loadImages():
    global imgStack
    print("Loading Images to RAM")
    
    for i in tqdm(range(0,10000)):
        #num = 0000 + i
        #print(num)
        imgStack["img{}".format(i)] = LoadImage("img/fc2_save_2019-06-16-132059-" + numToLenFour(i) + ".bmp")
    
    print("fertig")
    
    
loadImages()