import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.metrics import mean_squared_error
from PIL import Image

def rgbTocmyk(image):
    newImage= []
    for ligne in image:
        newLigne= []
        for pixel in ligne:
             one= 1.00001 #to balance if k=1
             K= 1.-np.max(pixel)
             C= (1.-pixel[0]-K)/(one-K)
             M= (1.-pixel[1]-K)/(one-K)
             Y= (1.-pixel[2]-K)/(one-K)
             newPixel= [C, M, Y, K]
             newLigne.append(newPixel)
        newImage.append(newLigne)
    return np.array(newImage)

def cmykTorgb(image):
    newImage= []
    for ligne in image:
        newLigne= []
        for pixel in ligne:
             R= (1.-pixel[0])*(1.-pixel[3])
             G= (1.-pixel[1])*(1.-pixel[3])
             B= (1.-pixel[2])*(1.-pixel[3])
             newPixel= [R, G, B]
             newLigne.append(newPixel)
        newImage.append(newLigne)
    return np.array(newImage)

def MSE(img1, img2):
    mse= mean_squared_error(img1, img2)
    print(mse)


def b(img):
    #preparing images
    original= img 
    converted= rgbTocmyk(original)
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
    print("There is no builtin function for cmyk")

def d(img):
   converted= rgbTocmyk(img) 
   #print(converted[:,:,3])
   back= cmykTorgb(converted)
   MSE(img,back) 

#-------------
#STARTING CODE
#-------------
img = (mpimg.imread('mnms_512.jpg'))/255
#b(img)
#c(img)
d(img)

