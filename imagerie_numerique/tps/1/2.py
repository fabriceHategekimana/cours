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

#imgplot = plt.imshow(img)
#plt.show()
#print(img)

#définition des couleurs
#red= [255, 0, 0, 255]
#green= [0, 255, 0, 255]
#blue= [0, 0, 255, 255]

#Partie (a)
#définition d'une ligne du gradient
#ligne= []
#for i in range(255, 0, -1):
   #ligne.append([i, i, i, 255]) 
#
#image= np.array([ligne]*70)
#print(image)
#imageplot= plt.imshow(image)
#plt.show()


#Partie (b)
#création de blocs
white= [1., 1., 1., 1.]
black= [0., 0., 0., 1.]

fig2a= [[black, white],[black, white]]
fig2b= [[black, black],[white, white]]

a= np.array(fig2a)
b= np.array(fig2b)

#on fait la transformation
res= sub(add(a,b),mul(a,b))

plt.imshow(res)
plt.show()
