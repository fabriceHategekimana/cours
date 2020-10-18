import numpy as np

def rgbToyiq(pixel):
    matrice= np.array([[0.299, 0.587, 0.114], [0.596, -0.274, -0.322], [0.211, -0.523, 0.312]])
    newPixel= np.dot(matrice, pixel)
    return newPixel

def yiqTorgb():
    matrice= np.array([[1, 0.956, 0.621], [1, -0.272, -0.647], 1, -1.106, 1.703])
    newPixel= np.dot(matrice, pixel)
    return newPixel



