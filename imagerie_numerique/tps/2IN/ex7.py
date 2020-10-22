import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.metrics import mean_squared_error
from PIL import Image

def blur(img):
    #normal image
    plt.subplot(121) 
    plt.imshow(img)
    plt.xlabel("Normal sight")
    #blured image
    img2 = (mpimg.imread('mnms_512_blured.jpg'))/255
    plt.subplot(122)
    plt.imshow(img2)
    plt.xlabel("Sight with shifted focal point")
    #show
    plt.show()

def color(img):
    #normal image
    plt.subplot(121) 
    plt.imshow(img)
    plt.xlabel("Normal sight")
    #blured image
    img2 = img.copy()
    img2[:,:,1]= img2[:,:,1]-img2[:,:,1]
    plt.subplot(122)
    plt.imshow(img2)
    plt.xlabel("Sight with color blindness (green=0)")
    #show
    plt.show()

#-------------
#STARTING CODE
#-------------
img = (mpimg.imread('mnms_512.jpg'))/255

#blur(img)
color(img)
