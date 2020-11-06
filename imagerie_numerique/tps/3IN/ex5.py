from skimage.color import rgb2gray
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import mean_squared_error
from skimage.util import random_noise
# EXERCICE 5

def PSNR(img1, img2):
    #PSNR = 10*(log_10((max(f(x,y))^2))/MSE)
    Up= np.max(img1)**2
    MSE= mean_squared_error(img1, img2)
    PSNR = 10*(np.log10(Up/MSE))
    return PSNR

def gaussianNoise(mean, sigma, img):
    # work for gray images only
    white= np.random.normal(mean, sigma/255, size=np.prod(img.shape))
    white= white.reshape(img.shape)
    white= (img+white)/2
    return white.copy()

#plt.imshow(gImg, cmap=plt.cm.gray)
#plt.imshow(gImg, cmap=plt.cm.gray)
#plt.imshow(img)

#---------------------
#BEGGINING OF THE CODE
#---------------------
#(a) 10 gaussian noise
lena = mpimg.imread('lena.png')
imgList= []

gLena = rgb2gray(lena)

for i in range(0, 10):
    imgList.append(gaussianNoise(0, 25, gLena))

imgList= np.array(imgList)

#(b) psnr mean
psnrList= []
for img in imgList:
    psnrList.append(PSNR(gLena, img))
psnrList= np.array(psnrList)

psnrmean= np.sum(psnrList)/10
print("psnr mean: ", psnrmean)

#(c) frame averaging
imgAverage= np.sum(imgList, axis=0)/10

#(d) psnr
psnrAverage= PSNR(gLena, imgAverage)
print("psnrAverage: ", psnrAverage)
