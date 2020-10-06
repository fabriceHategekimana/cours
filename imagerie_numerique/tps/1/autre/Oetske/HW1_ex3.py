import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from PIL import Image

#Reading lena's image
img = mpimg.imread('lena.png')
plt.imshow(img)
plt.show()

gImg = rgb2gray(img)
plt.imshow(gImg)
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(img)
ax[0].set_title("Original")
ax[1].imshow(gImg, cmap=plt.cm.gray)
ax[1].set_title("Grayscale")

fig.tight_layout()
plt.show()

im = Image.open('lena.png')

face = im.crop((150, 100, 375, 380))
face.show()

#Demande de le faire de 2 manières différentes mais pas tout compris