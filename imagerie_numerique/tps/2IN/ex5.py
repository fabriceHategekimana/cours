import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.metrics import mean_squared_error
from PIL import Image

def rgbTocmy(image):
    vecteur= np.array([1, 1, 1])
    newImage= []
    for ligne in image:
        newLigne= []
        for pixel in ligne:
             newPixel= vecteur-pixel
             newLigne.append(newPixel.tolist())
        newImage.append(newLigne)
    return np.array(newImage)

def cmyTorgb(image):
    vecteur= np.array([1, 1, 1])
    newImage= []
    for ligne in image:
        newLigne= []
        for pixel in ligne:
             newPixel= vecteur-pixel
             newLigne.append(newPixel.tolist())
        newImage.append(newLigne)
    return np.array(newImage)

def MSE(img1, img2):
    mse= mean_squared_error(img1, img2)
    print(mse)


def b(img):
    #preparing images
    original= img 
    converted= rgbTocmy(original)
    grayOriginal= rgb2gray(original) 
    grayConverted= rgb2gray(converted) 
    #showing the results
    plt.subplot(221)
    plt.imshow(original)
    plt.xlabel("original")
    plt.subplot(222)
    plt.imshow(converted)
    plt.xlabel("converted")
    plt.subplot(223)
    plt.imshow(grayOriginal, cmap=plt.cm.gray)
    plt.xlabel("grayOriginal")
    plt.subplot(224)
    plt.imshow(grayConverted, cmap=plt.cm.gray)
    plt.xlabel("grayConverted")
    plt.show()

def c(img):
    print("There is no builtin function for cmy")

def d(img):
   converted= rgbTocmy(img) 
   back= cmyTorgb(converted)
   MSE(img,back) 

#-------------
#STARTING CODE
#-------------
img = (mpimg.imread('mnms_512.jpg'))/255
#b(img)
#c(img)
d(img)