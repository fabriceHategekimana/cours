from skimage.color import rgb2gray
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import mean_squared_error
from skimage.util import random_noise
from skimage.transform import resize

def PSNR(img1, img2):
    #PSNR = 10*(log_10((max(f(x,y))^2))/MSE)
    MSE= mean_squared_error(img1, img2)
    PSNR = 10*(np.log10((np.max(img1)**2))/MSE)
    return PSNR

def getRGB(img):
    #gettting the 3 chanels
    redImg= img[:,:,0]
    greenImg= img[:,:,1]
    blueImg= img[:,:,2]
    return redImg, greenImg, blueImg

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

#(a)
reference = mpimg.imread('renoir/reference.bmp')
noisy = mpimg.imread('renoir/noisy.bmp')

newImg= resize(noisy, ((noisy.shape[0]*0.5), (noisy.shape[1]*0.5)))
plt.imshow(newImg)
plt.show()

#plotRGB(noisy)

#nr, ng, nb= getRGB(noisy)
#rr, rg, rb= getRGB(reference)
#
#print(PSNR(rr, nr))
#print(PSNR(rg, ng))
#print(PSNR(rb, nb))



#(b)
