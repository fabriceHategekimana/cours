# Exercice 4
import numpy as np
import matplotlib.pyplot as plt

def myRound(image):
    image= np.round(image)-1
    image[image < 0]= 0
    return image

def encode(num, image):
    n= num
    if n < 8:
        n= 8-n
        image= myRound(image/(2**n))
    return image/((2**num)-1)

def grayScale():
    #Partie (a)
    #creation of a line with a gradient
    ligne= []
    for i in range(0, 1):
        for i in range(255, 0, -1):
            ligne.append([i, i, i])
    #Now, we will duplicate this line to get more lines (70 lines)
    image= np.array([ligne]*70)
    return image


image= grayScale()
#print(encode(7, image[0][0:5]))

# 7 bits
plt.imshow(encode(1, image))
plt.show()
## 5 bits
#plt.imshow(encode(5, image))
#plt.show()
## 3 bits
#plt.imshow(encode(3, image))
#plt.show()
## 2 bits
#plt.imshow(encode(2, image))
#plt.show()
## 1 bits
#plt.imshow(encode(1, image))
#plt.show()

