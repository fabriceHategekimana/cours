import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.metrics import mean_squared_error
from PIL import Image

#-------------
#STARTING CODE
#-------------
img = (mpimg.imread('mnms_512.jpg'))/255
img[:,:,1]= img[:,:,1]-img[:,:,1]
plt.imshow(img2)
plt.show()

