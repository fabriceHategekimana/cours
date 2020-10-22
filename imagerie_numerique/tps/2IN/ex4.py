import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.color import rgb2yuv
from skimage.color import yuv2rgb
from skimage.metrics import mean_squared_error
from PIL import Image

def rgbToyuv(image):
    matrice= np.array([[0.299, 0.587, 0.114], [-0.14713, -0.28886, 0.436], [0.615, -0.51499, -0.10001]])
    newImage= []
    for ligne in image:
        newLigne= []
        for pixel in ligne:
             newPixel= np.dot(matrice, pixel)
             newLigne.append(newPixel.tolist())
        newImage.append(newLigne)
    return np.array(newImage)

def yuvTorgb():
    matrice= np.array([[1, 0, 1.13983], [1, -0.39465, -0.58060], [1, 2.03211, 0]])
    newPixel= np.dot(matrice, pixel)
    return newPixel

def MSE(img1, img2):
    mse= mean_squared_error(img1, img2)
    print(mse)

def b(img):
    #preparing images
    original= img 
    converted= rgbToyuv(original)
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
    convertedWithCustomFunction= rgbToyuv(img)
    convertedWithBuiltinFunction= rgb2yuv(img)
    plt.subplot(121)
    plt.imshow(convertedWithBuiltinFunction)
    plt.xlabel("builtin convertion")
    plt.subplot(122)
    plt.imshow(convertedWithCustomFunction)
    plt.xlabel("custom convertion")
    plt.show()

def d(img):
   converted= rgb2yuv(img) 
   back= yuv2rgb(converted)
   MSE(img,back) 



#-------------
#STARTING CODE
#-------------
img = (mpimg.imread('mnms_512.jpg'))/255
#b(img)
#c(img)
#d(img)
