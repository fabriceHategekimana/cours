# Exercice 5
from skimage.color import rgb2gray
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import mean_squared_error
from skimage.util import random_noise

def PSNR(img1, img2):
    #PSNR = 10*(log_10((max(f(x,y))^2))/MSE)
    MSE= mean_squared_error(img1, img2)
    PSNR = 10*(np.log10((np.max(img1)**2))/MSE)
    return PSNR

def gaussianNoise(mean, sigma, img):
    # work for gray images only
    white= np.random.normal(mean, sigma/255, size=np.prod(img.shape))
    white= white.reshape(gImg.shape)
    white= (img+white)/2
    return white.copy()

#plt.imshow(gImg, cmap=plt.cm.gray)
#plt.imshow(gImg, cmap=plt.cm.gray)
#plt.imshow(img)

#---------------------
#BEGGINING OF THE CODE
#---------------------
img = mpimg.imread('lena.png')
imgList= []

gImg = rgb2gray(img)

for i in range(0, 10):
    imgList.append(gaussianNoise(0, 25, gImg))

imgList= np.array(imgList)

psnrList= []
for img in imgList:
    psnrList.append(PSNR(gImg, img))
psnrList= np.array(psnrList)
    
#print(psnrList)

imgSum= np.sum(imgList, axis=0)

#psnr= PSNR(gImg, imgSum)
plt.show()



