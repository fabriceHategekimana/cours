#pour matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Pour numpy
import numpy as np

#pour skimage
from skimage.color import rgb2gray
from skimage.util import crop
from skimage.util import random_noise
from skimage.util.shape import view_as_windows
from skimage.metrics import mean_squared_error

#loading image "lena.png"
img = mpimg.imread('lena.png')

#converting to grayscale
greyS = rgb2gray(img)

print(greyS.shape)

#(a)global mean and variance of the image
#print(np.mean(greyS))
#print(np.var(greyS))

#(b)local mean and variance of the image for a window size 5x5
smallGS1= view_as_windows(greyS, (5,5), step=1)
smallGS3= view_as_windows(greyS, (5,5), step=3)

#print(smallGS.shape)

#plt.imshow(smallGS)
#plt.show()
