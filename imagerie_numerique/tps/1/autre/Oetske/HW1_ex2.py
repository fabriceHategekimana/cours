import numpy as np
import matplotlib.pyplot as plt

# Exercice 2.a

x = np.linspace(0, 1, 100)
image1 = np.tile(x, (100, 1))

c = plt.imshow(image1, cmap='gray')
#plt.colorbar(c)
plt.show()

# Exercice 2.b

# Figure 2.b:
# half white matrix
w = 255 * np.ones((50, 100, 3), np.uint8)
# hafl black matrix
b = 1 * np.ones((50, 100, 3), np.uint8)
# concatenation of the two matrices
wb1 = np.concatenate((w,b))
plt.imshow(wb1)
plt.show()

# Figure 2.a:
# I just rotate the matrix from before
wb2 = np.rot90(wb1)
plt.imshow(wb2)
plt.show()

# Figure 2.c:

wb = wb1 * wb2
wb3 = np.rot90(wb)
plt.imshow(wb3)
plt.show()
