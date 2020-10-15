import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise
from skimage.color import rgb2gray


#Reading lena's image
img = mpimg.imread('lena.png')
plt.imshow(img)
#plt.show()
#Lena's image in grayscale
gImg = rgb2gray(img)
plt.imshow(gImg, cmap=plt.cm.gray)
#plt.show()

#a.
density1 = 0.0013
density2 = 0.031
density3 = 0.113

def saltPepper(img, density):
    salt = random_noise(img, mode='s&p', clip=True, amount=density)
    salt = np.array(255*salt, dtype='uint8')
    plt.imshow(salt)
    plt.show()

saltPepper(img, density1)
saltPepper(img, density2)
saltPepper(img, density3)

#b.
