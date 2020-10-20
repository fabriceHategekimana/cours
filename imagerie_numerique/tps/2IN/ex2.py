import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.color import rgb2ycbcr
from skimage.color import ycbcr2rgb
from skimage.metrics import mean_squared_error
from PIL import Image

def getNum(color):
    #the default color is red
    num= 0
    if color == "red":
        num= 0
    elif color == "green":
        num= 1
    if color == "blue":
        num= 2
    return num

def scale(img, color):
    num= getNum(color)
    subVect= img[:,:,num]/10
    plt.subplot(2,5,1)
    plt.imshow(img)
    for i in range(2, 11):
        img[:,:,num]= img[:,:,num]-subVect
        plt.subplot(2,5,i)
        plt.imshow(img)
    plt.show()

img = (mpimg.imread('mnms_512.jpg'))/255
scale(img, "blue")
