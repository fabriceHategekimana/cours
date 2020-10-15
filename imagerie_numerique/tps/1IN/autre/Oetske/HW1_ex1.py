import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#Reading lena's image
img = mpimg.imread('lena.png')
c = plt.imshow(img)
plt.colorbar(c)
plt.show()


#red = img[:,:,0]
#ligne20 = red[20,:]
#plt.figure(figsize=(8,4))
#plt.plot(ligne20)
#plt.show()
#plt.colorbar()
