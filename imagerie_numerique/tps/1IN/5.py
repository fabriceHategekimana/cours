#pour matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Pour numpy
import numpy as np

#pour skimage
from skimage.color import rgb2gray
from skimage.util import crop
from skimage.util import random_noise
from skimage.metrics import mean_squared_error

def display():
    #loading image "lena.png"
    img = mpimg.imread('lena.png')
    #converting to grayscale
    greyS = rgb2gray(img)
    #grayscale
    WnGs1= random_noise(greyS, mode="s&p", amount=0.0013, clip=True)
    WnGs2= random_noise(greyS, mode="s&p", amount=0.031, clip=True)
    WnGs3= random_noise(greyS, mode="s&p", amount=0.113, clip=True)
    #plot
    plt.subplot(131)
    plt.imshow(WnGs1)
    plt.ylabel("salt & pepper", fontsize=17)
    plt.xlabel("density= 0.0013", fontsize=17)
    plt.subplot(132)
    plt.imshow(WnGs2)
    plt.xlabel("density= 0.031", fontsize=17)
    plt.subplot(133)
    plt.imshow(WnGs3)
    plt.xlabel("density= 0.113", fontsize=17)
    plt.show()

def MSE():
    #loading image "lena.png"
    img = mpimg.imread('lena.png')
    #converting to grayscale
    greyS = rgb2gray(img)
    #grayscale
    WnGs1= random_noise(greyS, mode="s&p", amount=0.0013, clip=True)
    WnGs2= random_noise(greyS, mode="s&p", amount=0.031, clip=True)
    WnGs3= random_noise(greyS, mode="s&p", amount=0.113, clip=True)
    #error comparison
    print(mean_squared_error(greyS, WnGs1))
    print(mean_squared_error(greyS, WnGs2))
    print(mean_squared_error(greyS, WnGs3))

MSE()
