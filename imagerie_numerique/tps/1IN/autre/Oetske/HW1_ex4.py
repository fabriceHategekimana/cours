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

#a
mean = 0
sigma1 = 5
sigma2 = 25
sigma3 = 50

def noisyImageA(mean, sigma, img):
    gaussian = np.random.normal(mean, sigma, img.size)
    gaussian = gaussian.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
    noisy_im = img + gaussian
    plt.imshow(noisy_im)
    plt.show()

noisyImageA(mean, sigma1, img)
noisyImageA(mean,sigma2, img)
noisyImageA(mean,sigma3, img)

#b.
noisy_im = random_noise(img, mode='gaussian', seed=None, clip=True)
noisy_im = np.array(255*noisy_im, dtype='uint8')
plt.imshow(noisy_im)
plt.show()

