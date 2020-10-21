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

def MSE(im1, img2):
    mse= mean_squared_error(img, img4)
    print(mse)

img = (mpimg.imread('mnms_512.jpg'))/255
img2= rgbToyiq(img)
img3= rgb2yiq(img)
img4= yiq2rgb(img3)

MSE(img, img4)

#---------------------------------------------------------
#PRENDRE LES PARAMÈTRES RGB DES IMAGES YQI COMME GRAY SCALE
#---------------------------------------------------------
greyRed= img2[:,:,0]
greyGreen= img2[:,:,1]
greyBlue= img2[:,:,2]

#Image normale (en haut à gauche)
plt.subplot(231)
plt.imshow(img)

#Image modifiée avec ma propre fonction (en haut au milieu)
plt.subplot(232)
plt.imshow(img2)

#Image modifiée avec la fonction de python (en haut à droite)
plt.subplot(233)
plt.imshow(img3)

#Greyscale pour le rouge (en bas à gauche)
plt.subplot(234)
plt.imshow(greyRed)

#Greyscale pour le vert (en bas au milieu)
plt.subplot(235)
plt.imshow(greyGreen)

#Greyscale pour le bleu (en bas à droite)
plt.subplot(236)
plt.imshow(greyBlue)

#on affiche
plt.show()

