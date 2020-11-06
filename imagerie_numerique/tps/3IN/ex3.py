from math import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#EXERCICE 3

#-----------------
#VARIABLE GLOBALE
#-----------------
INTERVAL= [-5, 5]


#---------------------------
#MES FONCTIONS Mathématiques
#---------------------------
def f(x,y):
    return np.sin(x)+np.cos(y)

def g(x,y):
    return x+y


#----------------------------------------------------
#SOUS-FONCTIONS D'AIDE  POUR SAMPLING ET QUANTIZATION
#----------------------------------------------------
def nearestValue(element, dataSet):
    delta= max(dataSet)
    nearest= max(dataSet)
    for data in dataSet:
        newDelta= max([element, data])-min([element, data])
        if newDelta < delta:
           delta= newDelta
           nearest= data
    return nearest

def myLinspace(From, To, Step):
    i= From
    tab= [From]
    while(i<To):
        i= i+Step
        tab.append(i)
    return tab

def spaceGen(step):
    delta= max(INTERVAL)-min(INTERVAL)
    nb= round(delta/step)
    X= np.outer(np.linspace(min(INTERVAL), max(INTERVAL), num=nb), np.ones(nb))
    Y= np.outer(np.linspace(min(INTERVAL), max(INTERVAL), num=nb), np.ones(nb)).T
    return (X, Y)


#----------------------------------
#FONCTIONS SAMPLING ET QUANTIZATION
#----------------------------------
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
    plt.xlabel("Sampling")
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
    plt.xlabel("Quantization")
    plt.show()


#-------------
#DÉBUT DU CODE
#-------------
#SAMPLING (prend une fonction et un pas)
sampling(f, 0.5)

#QUANTIZATION (prend une fonction et un interval de valeur pour z)
intervalOfValue= myLinspace(-5, 5, 0.5)
quantization(f, intervalOfValue)
