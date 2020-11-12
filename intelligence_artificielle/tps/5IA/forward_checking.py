from graphe import *

# FONCTIONS
PROCHAIN= ["NB", "CA", "V", "MPLR", "RAA", "PACA", "PLCB"] 

def getCouleurs(indice, a):
    return a[indice]

# valide
def valide(a):
    res= True
    for i in a:
        if a[i] == -1:
            res= False
    return res
        
# getNonAffecte
def getNonAffecte(a):
    #C'est ici qu'il y aura les différentes heuristiques
    return PROCHAIN.pop()

# FORWARDCHECKING
def FORWARD_CHECKING(a,d):
    #Ici on doit vérifier que tout les éléments adjacents n'on pas la même couleur (BFS)
    #pour tout noeud non défini, on enlève les valeurs des adjacents
    #Il n'y a en principe, pas plus de 7 couleurs (car il y a 7 régions)
    for i in d:
        if a[i] == -1:
            #on prends ses voisins
            voisins= G.getVoisins(i)
            #pour chacun d'entre eux, on retir la couleur dans le domaine
            couleurs= list(map(getCouleurs, voisins))
            for j in couleurs:
                d[i].remove(j)
        else:
           if len(d[i]) < 0:
               d[i]= []

def PSC_BACKTRACKING(a, d):
    #1. Si A= S_G alors retourner A
    if valide(a):
        return a
    #2. Sélectionner une variable x_p non affectée
    NA= getNonAffecte(a)
    #3. Pour chaque valeur v_pi de D_p faire:
    for v in d[NA]:
        #- Ajouter x_p <- v_pi dans A
        a[NA]= v
        print("Etape "+str(d["etape"])+". AV "+state(a))
        d["etape"]= d["etape"]+1
        #- D <- FORWARD_CHECKING(A,D)
        d= FORWARD_CHECKING(a,d)
        #- si aucun domaine de D n'est vide:
        if not estVide(d):
            #- Retourner PSC_BACKTRACKING(A,D)
            return PSC_BACKTRACKING(a,d)
        #- sinon:
        else:
            #- Retourner échec
            return "Echec!"

# Définition des éléments
a= { "NB": -1, "CA": -1, "V": -1, "MPLR": -1, "RAA": -1, "PACA": -1, "PLCB": -1}
d= { "NB": [0,1,2,3,4,5,6], "CA": [0,1,2,3,4,5,6], "V": [0,1,2,3,4,5,6], "MPLR": [0,1,2,3,4,5,6], "RAA": [0,1,2,3,4,5,6], "PACA": [0,1,2,3,4,5,6], "PLCB": [0,1,2,3,4,5,6]}

#g= Graphe("abcd", "a.b b.c c.d d.a")

