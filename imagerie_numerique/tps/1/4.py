import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage.color import rgb2gray
from skimage.util import crop
from skimage.util import random_noise

#loading image "lena.png"
img = mpimg.imread('lena.png')

#converting to grayscale
greyS = rgb2gray(img)
#plt.imshow(gImg, cmap=plt.cm.gray)

#creation of the white noise sigma= 5
whiteN5= np.random.normal(0, 5/255, size=np.prod(greyS.shape))
whiteN5= whiteN5.reshape(greyS.shape)

#creation of the white noise sigma= 25
whiteN25= np.random.normal(0, 25/255, size=np.prod(greyS.shape))
whiteN25= whiteN25.reshape(greyS.shape)

#creation of the white noise sigma= 50
whiteN50= np.random.normal(0, 50/255, size=np.prod(greyS.shape))
whiteN50= whiteN50.reshape(greyS.shape)

#the whitenoised grayscale image
WnGs1M5= (greyS+whiteN5)/2
WnGs1M25= (greyS+whiteN25)/2
WnGs1M50= (greyS+whiteN50)/2

#the whitenoised grayscale image 2
WnGs2M5= random_noise(greyS, mode="gaussian", clip=True, var=5/255)
WnGs2M25= random_noise(greyS, mode="gaussian", clip=True, var=25/255)
WnGs2M50= random_noise(greyS, mode="gaussian", clip=True, var=50/255)

plt.subplot(231)
plt.ylabel("matrix manipulation", fontsize=14)
plt.imshow(WnGs1M5)
plt.subplot(232)
plt.imshow(WnGs1M25)
plt.subplot(233)
plt.imshow(WnGs1M50)
plt.subplot(234)
plt.xlabel("σ= 5", fontsize=20)
plt.ylabel("skimage.util.random_noise", fontsize=14)
plt.imshow(WnGs2M5)
plt.subplot(235)
plt.xlabel("σ= 25", fontsize=20)
plt.imshow(WnGs2M25)
plt.subplot(236)
plt.xlabel("σ= 50", fontsize=20)
plt.imshow(WnGs2M50)
plt.show()
