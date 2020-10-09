import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def toRed(img):
    for ligne in img:
        for pixel in ligne:
           pixel[1]= 0
           pixel[2]= 0
    return img

def toGreen(im4):
    for ligne in img:
        for pixel in ligne:
           pixel[0]= 0
           pixel[2]= 0
    return img

def toBlue(img):
    for ligne in img:
        for pixel in ligne:
           pixel[0]= 0
           pixel[1]= 0
    return img


#on prend l'image
img = mpimg.imread('lena.png')

#on prépare l'image à l'affichage
plt.subplot(221)
plt.imshow(img)

#red image
RedI= toRed(np.copy(img))
plt.subplot(222)
plt.imshow(RedI)

#green image
RedI= toGreen(np.copy(img))
plt.subplot(223)
plt.imshow(RedI)

#blue image
RedI= toBlue(np.copy(img))
plt.subplot(224)
plt.imshow(RedI)

#on affiche le tout
plt.show()
        
