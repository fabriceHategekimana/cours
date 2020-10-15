import random
import numpy as np
from matplotlib import pyplot as plt 

class Structure():

    def __init__(self, proba):
        #code
        self.hist= [0]
        self.tete= 0
        self.proba= proba

    def next(self):
      r= random.random()  
      if r < self.proba:
            #echec->retransmission
            self.hist.append(self.hist[self.tete]+1)
            self.tete = self.tete+1
      else:
          #réussite
          self.hist.append(0)
          self.tete = self.tete+1

    def showHistory(self):
          return self.hist

    def showLast(self):
        return self.hist[tete]
    
    def S(self, t):
        i= 0
        while(i<t):
            self.next()
            i= i+1
        return self.hist
    def clear(self):
        self.hist= [0]
        self.tete= 0


def comptage(tab):
    m= len(tab)
    element= []
    compte= []
    for i in range(0, m):
        compte.append(tab.count(i)/len(tab))
    return compte 

def matrice(t, proba):
    a= Structure(proba)
    mat= []
    for i in range(0, t):
        #on crée un chemin possible
        v= a.S(i)
        #on compte les instances de ce chemin
        v=comptage(v)
        #on compte les instances de ce chemin
        #on le complète la liste sortante par des zéros complémentaires
        d= t-len(v)
        zero= [0]*d
        v= v+zero
        #on le met dans la matrice
        mat.append(v)
        a.clear()

    ##on change la matrice en array
    mat= np.array(mat)
    ##on transpose la matrice
    mat= np.transpose(mat)
    ##on fait un plot multiple pour chaque ligne de la matrice selon x équidistant de 1 à 1 points
    x= np.arange(0, t)
    borne= 5
    fig, axs = plt.subplots(borne)
    fig.suptitle('Convergence des probabilités avec e= '+str(proba))
    print("x: ", len(x))
    for i in range(0, borne):
        axs[i].plot(x, mat[i])
        axs[i].set_ylabel("S(t) Occurence de "+str(i))
        axs[i].set_xlabel("t")
    plt.show()



#le comptage  pour un temps t
matrice(2000, 0.5)
