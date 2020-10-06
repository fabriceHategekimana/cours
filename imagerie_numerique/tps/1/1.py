import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#on prend l'image
img = mpimg.imread('lena.png')

#on prépare l'image à l'affichage
imgplot = plt.imshow(img, cmap="hot")

#on met la bar de coloration
plt.colorbar(imgplot)

#on affiche le tout
plt.show()
        
