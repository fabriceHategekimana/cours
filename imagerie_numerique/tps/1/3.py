import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage.color import rgb2gray
from skimage.util import crop

#on prend l'image
img = mpimg.imread('lena.png')
imHeight= img.shape[0]
imWidth= img.shape[1]

#Dans l'ordre des coordonées: haut, bas, droite, gauche et les 2 zéros je sais pas
imgcrop1 = crop(img, ((100,imHeight-380), (imWidth-375,150), (0,0)), copy=False)

#Normal crop with a sub matrix
imgcrop2 = img[99:381, 149:376]

plt.subplot(131)
plt.imshow(img)
plt.xlabel("original")
plt.subplot(132)
plt.imshow(imgcrop1)
plt.xlabel("croped (first method)")
plt.subplot(133)
plt.xlabel("croped (second method)")
plt.imshow(imgcrop2)
plt.show()
