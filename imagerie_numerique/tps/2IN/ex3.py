import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.color import rgb2yiq
from skimage.color import yiq2rgb
from skimage.metrics import mean_squared_error
from PIL import Image

def rgbToyiq(image):
    matrice= np.array([[0.299, 0.587, 0.114], [0.596, -0.274, -0.322], [0.211, -0.523, 0.312]])
    newImage= []
    for ligne in image:
        newLigne= []
        for pixel in ligne:
             newPixel= np.dot(matrice, pixel)
             newLigne.append(newPixel.tolist())
        newImage.append(newLigne)
    return np.array(newImage)

def yiqTorgb():
    matrice= np.array([[1, 0.956, 0.621], [1, -0.272, -0.647], 1, -1.106, 1.703])
    newPixel= np.dot(matrice, pixel)
    return newPixel

def MSE(img1, img2):
    mse= mean_squared_error(img1, img2)
    print(mse)


def b(img):
    #preparing images
    original= img 
    converted= rgbToyiq(original)
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
    convertedWithCustomFunction= rgbToyiq(img)
    convertedWithBuiltinFunction= rgb2yiq(img)
    plt.subplot(121)
    plt.imshow(convertedWithBuiltinFunction)
    plt.xlabel("builtin convertion")
    plt.subplot(122)
    plt.imshow(convertedWithCustomFunction)
    plt.xlabel("custom convertion")
    plt.show()

def d(img):
   converted= rgb2yiq(img) 
   back= yiq2rgb(converted)
   MSE(img,back) 

#-------------
#STARTING CODE
#-------------
img = (mpimg.imread('mnms_512.jpg'))/255
#b(img)
#c(img)
d(img)
