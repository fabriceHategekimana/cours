# Exercice 4
import matplotlib.image as mpimg
import numpy as np
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

def bitsDown(image):
    return np.round((image+1)/2+0.1)-1

def encode(num, image):
    n= num
    if n < 8:
        n= 8-n
        for i in range(0, n):
            image= bitsDown(image)
    return image/((2**num)-1)

def grayScale():
    #Partie (a)
    #creation of a line with a gradient
    ligne= []
    for i in range(0, 1):
        for i in range(255, 0, -1):
            ligne.append([i, i, i])
    #Now, we will duplicate this line to get more lines (70 lines)
    image= np.array([ligne]*70)
    return image


image= grayScale()

##original
#plt.subplot(231)
#plt.imshow(image)
#plt.xlabel("original", fontsize=17)
## 7 bits
#plt.subplot(232)
#plt.imshow(encode(7, image))
#plt.xlabel("7 bits", fontsize=17)
## 5 bits
#plt.subplot(233)
#plt.imshow(encode(5, image))
#plt.xlabel("5 bits", fontsize=17)
## 3 bits
#plt.subplot(234)
#plt.imshow(encode(3, image))
#plt.xlabel("3 bits", fontsize=17)
## 2 bits
#plt.subplot(235)
#plt.imshow(encode(2, image))
#plt.xlabel("2 bits", fontsize=17)
## 1 bits
#plt.subplot(236)
#plt.imshow(encode(1, image))
#plt.xlabel("1 bits", fontsize=17)
#plt.show()


img = mpimg.imread('lena.png')*255
image = rgb2gray(img)
#plt.imshow(gImg, cmap=plt.cm.gray)
#original
plt.subplot(231)
plt.imshow(image, cmap=plt.cm.gray)
plt.xlabel("original", fontsize=17)
# 7 bits
plt.subplot(232)
plt.imshow(encode(7, image), cmap=plt.cm.gray)
plt.xlabel("7 bits", fontsize=17)
# 5 bits
plt.subplot(233)
plt.imshow(encode(5, image), cmap=plt.cm.gray)
plt.xlabel("5 bits", fontsize=17)
# 3 bits
plt.subplot(234)
plt.imshow(encode(3, image), cmap=plt.cm.gray)
plt.xlabel("3 bits", fontsize=17)
# 2 bits
plt.subplot(235)
plt.imshow(encode(2, image), cmap=plt.cm.gray)
plt.xlabel("2 bits", fontsize=17)
# 1 bits
plt.subplot(236)
plt.imshow(encode(1, image), cmap=plt.cm.gray)
plt.xlabel("1 bits", fontsize=17)
plt.show()
