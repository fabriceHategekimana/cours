from math import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#exercice 3

INTERVAL= [-5, 5]
def nearestValue(element, dataSet):
    delta= max(dataSet)
    nearest= max(dataSet)
    for data in dataSet:
        newDelta= max([element, data])-min([element, data])
        if newDelta < delta:
           delta= newDelta
           nearest= data
    return nearest

def f(x,y):
    return np.sin(x)+np.cos(y)

def g(x,y):
    return x+y

def spaceGen(step):
    delta= max(INTERVAL)-min(INTERVAL)
    nb= round(delta/step)
    X= np.outer(np.linspace(min(INTERVAL), max(INTERVAL), num=nb), np.ones(nb))
    Y= np.outer(np.linspace(min(INTERVAL), max(INTERVAL), num=nb), np.ones(nb)).T
    return (X, Y)

def sampling(function, step):
    XY= spaceGen(step)
    X= XY[0]
    Y= XY[1]
    Z= function(X,Y)
    #print("X: ", X)
    #print("Y: ", Y)
    #print("Z: ", Z)
    fig = plt.figure(figsize =(5, 5)) 
    ax = plt.axes(projection ='3d') 
    ax.plot_surface(X, Y, Z)
    plt.show()
             
def quantization(function, dataSet):
    step= 0.1
    XY= spaceGen(step)
    X= XY[0]
    Y= XY[1]
    z= function(X,Y)
    Z= []
    for line in z:
        Z0= []
        for el in line:
            Z0.append(nearestValue(el, dataSet))
        Z.append(Z0)
    Z= np.array(Z)
    fig = plt.figure(figsize =(5, 5)) 
    ax = plt.axes(projection ='3d') 
    ax.plot_surface(X, Y, Z)
    plt.show()
         
        
#Quantization
#Définir un ensemble de résultats définis
#Faire une approche linéaire qui suit ces pas

sampling(f, 0.5)
quantization(f, [x/5 for x in range(-5*5, 5*5)])
