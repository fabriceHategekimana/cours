import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage.color import rgb2gray
from skimage.util import crop
from PIL import Image

#on prend l'image
img = mpimg.imread('lena.png')
imHeight= img.shape[0]
imWidth= img.shape[1]

#Dans l'ordre des coordonées: haut, bas, droite, gauche et les 2 zéros je sais pas
#imgcrop = crop(img, ((101,imHeight-380), (imWidth-375,150), (0,0)), copy=False)


#img2= rgb2gray(img)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(imgcrop)
plt.show()
