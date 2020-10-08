import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def maxOpacity(img):
    for ligne in img:
        for pixel in ligne:
            pixel[3]= 1.
    return img

def overflow(img):
    for ligne in img:
        for pixel in ligne:
            for i in range(4):
                if pixel[i] < 0:
                    pixel[i]= 0
                elif pixel[i] > 1:
                    pixel[i]= 1
    return img

def adjust(img):
    img= maxOpacity(img)
    img= overflow(img)
    return img

def add(a, b):
    c= adjust(a+b)
    return c

def sub(a, b):
    c= adjust(a-b)
    return c

def mul(a, b):
    c= adjust(a*b)
    return c

def partA():
    #Partie (a)
    #creation of a line with a gradient
    ligne= []
    for i in range(255, 0, -1):
      ligne.append([i, i, i, 255]) 
    #Now, we will duplicate this line to get more lines (70 lines)
    image= np.array([ligne]*70)
    imageplot= plt.imshow(image)
    plt.show()


def partB():
    #bloc creation
    white= [1., 1., 1., 1.]
    black= [0., 0., 0., 1.]
    fig2a= [[black, white],[black, white]]
    fig2b= [[black, black],[white, white]]
    #the 2a and 2b Figures
    a= np.array(fig2a)
    b= np.array(fig2b)
    #on fait la transformation
    res= sub(add(a,b),mul(a,b))

    plt.subplot(131)
    plt.imshow(a)
    plt.subplot(132)
    plt.imshow(b)
    plt.subplot(133)
    plt.imshow(res)
    plt.show()

#BEGINING OF CODE:
#partA()
#partB()
