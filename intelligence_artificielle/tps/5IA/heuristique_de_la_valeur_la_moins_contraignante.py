from graphe import *


def getPossibilites(prochains):
    print("possibilités")
    
# VARIABLES GLOBALES
PROCHAIN= ["NB", "CA", "V", "MPLR", "RAA", "PACA", "PLCB"] 
G= Graphe(["NB", "PLCB", "CA", "RAA", "MPLR", "PACA", "V"], "NB.PLCB NB.V PLCB.V PLCB.CA RAA.PLCB V.RAA CA.RAA CA.MPLR RAA.MPLR RAA.PACA MPLR.PACA")


def estVide(d):
    for i in d:
        res= True
        if d[i] != []:
            res= False
        return res

def couleurValides(couleur):
    return couleur > -1

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
def getNonAffecte(a,d,g):
    #C'est ici qu'il y aura les différentes heuristiques
    #on prends les nonAffecté
    nonAffecte= list(map(lambda item: item[0], list(filter(lambda item: item[1] == -1, a.items()))))
    #On trouve le maximum parmi les voisins
    maximum= 0
    PROCHAINS= []
    for i in nonAffecte:
        if len(g.getVoisins(i)) > maximum:
            maximum= len(g.getVoisins(i))
            PROCHAINS= [i]
        elif len(g.getVoisins(i)) == maximum:
            PROCHAINS.append(i)
    #On trie les élément par odre alphabétique s'il y a plus d'un choix
    if len(PROCHAINS) > 1:
        PROCHAINS.sort()
    return PROCHAIN.pop(0)

# FORWARDCHECKING
def FORWARD_CHECKING(a,d):
    #Ici on doit vérifier que tout les éléments adjacents n'on pas la même couleur (BFS)
    #pour tout noeud non défini, on enlève les valeurs des adjacents
    #Il n'y a en principe, pas plus de 7 couleurs (car il y a 7 régions)
    for i in d:
        if a[i] == -1:
            #print("d[i]= ", d[i])
            #on prends ses voisins
            voisins= G.getVoisins(i)
            #print("voisins= ", voisins)
            #pour chacun d'entre eux, on retir la couleur dans le domaine
            couleurs= []
            for j in voisins:
                couleurs.append(getCouleurs(j, a))
            couleurs= list(filter(couleurValides, couleurs))
            #print("couleurs", couleurs)
            for j in couleurs:
                if j in d[i]:
                    d[i].remove(j)
        else:
           if len(d[i]) < 0:
               d[i]= []
    return d

def getProchaineCouleur(couleurs, d):
    #C'est une couleur qui réduit le moins possible le choix des autres
    #C'est une couleur déjà utilisée si possible
    #On prend la concatenations de toutes les possibilités
    possibilitesTotales= []
    for i in d.values():
        possibilitesTotales.append(i)
    #Pour chaque couleur, on compte son occurence dans la liste
    minimum= len(possibilitesTotales)
    for i in couleurs: 
        if possibilitesTotales.count(i) < minimum:
            minimum= possibilitesTotales.count(i)
            prochain= i
    #On sélectionne la couleure qui a le moins d'occurence
    return prochain

def PSC_BACKTRACKING(a, d, g):
    print("----------------")
    print("Etat actuel:")
    print("a: ", a)
    print("d: ", d)
    print("----------------")
    #1. Si A= S_G alors retourner A
    if valide(a):
        return a
    #2. Sélectionner une variable x_p non affectée
    NA= getNonAffecte(a,d,g)
    print("Variable choisie: ", NA)
    #3. Pour chaque valeur v_pi de D_p faire:
    #for v in d[NA]:
    while d[NA] != 0:
        v= getProchaineCouleur(d[NA], d)
        #- Ajouter x_p <- v_pi dans A
        a[NA]= v
        print("valeur choisie: ", v)
        #- D <- FORWARD_CHECKING(A,D)
        d= FORWARD_CHECKING(a,d)
        #- si aucun domaine de D n'est vide:
        if not estVide(d):
            #- Retourner PSC_BACKTRACKING(A,D)
            return PSC_BACKTRACKING(a,d,g)
        #- sinon:
        else:
            #- Retourner échec
            return "Echec!"

# Définition des éléments
a= { "NB": -1, "CA": -1, "V": -1, "MPLR": -1, "RAA": -1, "PACA": -1, "PLCB": -1}
d= { "NB": [0,1,2,3,4,5,6], "CA": [0,1,2,3,4,5,6], "V": [0,1,2,3,4,5,6], "MPLR": [0,1,2,3,4,5,6], "RAA": [0,1,2,3,4,5,6], "PACA": [0,1,2,3,4,5,6], "PLCB": [0,1,2,3,4,5,6]}

print(PSC_BACKTRACKING(a,d,G))