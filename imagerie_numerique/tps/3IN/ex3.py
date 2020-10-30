from math import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#exercice 3

INTERVAL= [-5, 5]

def f(x,y):
    return np.sin(x)+np.cos(y)

def sampling(function, step):
    delta= max(INTERVAL)-min(INTERVAL)
    nb= round(delta/step)
    X= np.outer(np.linspace(min(INTERVAL), max(INTERVAL), num=nb), np.ones(nb))
    Y= np.outer(np.linspace(min(INTERVAL), max(INTERVAL), num=nb), np.ones(nb)).T
    Z= f(X,Y)
    fig = plt.figure(figsize =(5, 5)) 
    ax = plt.axes(projection ='3d') 
    ax.plot_surface(X, Y, Z)
    plt.show()
             


