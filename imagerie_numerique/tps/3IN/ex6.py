from skimage.color import rgb2gray
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import mean_squared_error
from skimage.util import random_noise
from skimage.transform import resize

#----------------
#FONCTIONS D'AIDE
#----------------
def MSE(img1, img2):
    return mean_squared_error(img1, img2)

def PSNR(img1, img2):
    #PSNR = 10*(log_10((max(f(x,y))^2))/MSE)
    Up= np.max(img1)**2
    Mse= mean_squared_error(img1, img2)
    PSNR = 10*(np.log10(Up/Mse))
    return PSNR

def getRGB(img):
    #gettting the 3 chanels
    redImg= img[:,:,0]
    greenImg= img[:,:,1]
    blueImg= img[:,:,2]
    return redImg, greenImg, blueImg

#-----------
#FONCTION 6A
#-----------
def plotRGB(img):
    redImg, greenImg, blueImg= getRGB(img)
    #On plot le tout
    plt.subplot(221)
    plt.imshow(img)
    plt.xlabel("Normal", fontsize=17)
    plt.subplot(222)
    plt.imshow(redImg, cmap=plt.cm.gray)
    plt.xlabel("Red channel", fontsize=17)
    plt.subplot(223)
    plt.imshow(greenImg, cmap=plt.cm.gray)
    plt.xlabel("Green channel", fontsize=17)
    plt.subplot(224)
    plt.imshow(blueImg, cmap=plt.cm.gray)
    plt.xlabel("Blue channel", fontsize=17)
    plt.show()

#-------------
#FONCTION 6 (B)
#-------------
def downsample(img, factor):
    return resize(img, ((img.shape[0]*factor), (img.shape[1]*factor)))

#-------------
#DÉBUT DU CODE
#-------------
#-----------------------------
#(a)
reference = mpimg.imread('renoir/reference.bmp')
noisy = mpimg.imread('renoir/noisy.bmp')

gReference= rgb2gray(reference)
gNoisy= rgb2gray(noisy)

#PLOT
plotRGB(reference)
plotRGB(noisy)

nr, ng, nb= getRGB(noisy)
rr, rg, rb= getRGB(reference)

print("psnr red   channel: ", PSNR(rr, nr))
print("psnr green channel: ", PSNR(rg, ng))
print("psnr blue  channel: ", PSNR(rb, nb))
print("psnr total:         ", PSNR(noisy, reference))

#-----------------------------
#(b)
newImg= downsample(noisy, 0.1)
neo= downsample(newImg, 10)
neo=(neo*255).astype('uint8')

plt.subplot(131)
plt.imshow(noisy)
plt.xlabel("noisy", fontsize=17)
plt.subplot(132)
plt.imshow(newImg)
plt.xlabel("downsampled", fontsize=17)
plt.subplot(133)
plt.imshow(neo)
plt.xlabel("resampled", fontsize=17)
plt.show()

print("total color: ", PSNR(reference, neo))

#-----------------------------
#(c)
gNewImg= downsample(gNoisy, 0.1)
gNeo= downsample(gNewImg, 10)

plt.subplot(131)
plt.imshow(gNoisy, cmap=plt.cm.gray)
plt.xlabel("noisy", fontsize=17)
plt.subplot(132)
plt.imshow(gNewImg, cmap=plt.cm.gray)
plt.xlabel("downsampled", fontsize=17)
plt.subplot(133)
plt.imshow(gNeo, cmap=plt.cm.gray)
plt.xlabel("resampled", fontsize=17)
plt.show()

print("psnr total gray: ", PSNR(gReference, gNeo))
