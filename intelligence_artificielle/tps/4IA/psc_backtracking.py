def PSC_BACKTRACKING(affectation, domaines):
    print("Fonction en construction")
    #affectation est un dictionnaire

#1. Si A= S_G alors retourner A
#2. Sélectionner une variable x_p non affectée
#3. Pour chaque valeur v_pi de D_p faire:
	#- Ajouter x_p <- v_pi dans A
	#- D <- FORWARD_CHECKING(A,D)
	#- si aucun domaine de D n'est vide:
		#- Retourner PSC_BACKTRACKING(A,D)
	#- sinon:
		#- Retourner échec

def adjacent(num):
    adj= {1:[2], 2:[1,3], 3:[2,4], 4:[3]}
    return adj[num]

def cote(num):
    cot= {1:"gauche", 2:"gauche", 3:"droite", 4:"droite"}
    return cot[num] 

def myFilter(fonction, liste, entree=None):
    res=[]
    if entree == None:
        res= list(filter(fonction, liste))
    else:
        for element in liste:
            if fonction(element, entree):
                res.append(element)
    return res

#créer FORWARD_CHECKING
def FORWARD_CHECKING(a, d):
    print("en Contraintes")
    #Traiter chaque condition
    #- <C,W>: <piece(W)= X, piece(C)= Y> , X != Y
    #- <C,W>: <piece(W)= X, adjacent(C)= Y> , X != Y
    #- <C,D>: <cote(D)= X, cote(C)= Y> , X != Y
    #- <W>: <nb(adjacent(W)= X)>, X >= 2
    #- <D>: <nb(adjacent(D)= X)>, X >= 2
    for cond in c:
        if len(cond[0]) == 1:
            val= None
            nonAffecte= cond[0][0]
        elif len(cond[0]) == 2:
            val= a[cond[0][0]]
            nonAffecte= cond[0][1]
        
        if val != None:
            d[nonAffecte]= myFilter(cond[1], d[nonAffecte], val)
        else:
            d[nonAffecte]= myFilter(cond[1], d[nonAffecte])
    return d
            
def MONO_FORWARD_CHECKING(a,d): 
    for i in range(3, 5):
        cond= c[i]
        nonAffecte= cond[0][0]
        d[nonAffecte]= myFilter(cond[1], d[nonAffecte])
    return d


#Définition des contraintes
c= []
c.append([("C","W"), lambda C,W: C != W])
c.append([("C","W"), lambda C,W: W not in adjacent(C)])
c.append([("C","D"), lambda C,D: cote(C) != cote(D)])
c.append([("W"), lambda W: len(adjacent(W)) >= 2])
c.append([("D"), lambda D: len(adjacent(D)) >= 2])

#créer affectation
a= {"C":0, "D":0, "W":0}
#créer domaine
d= { "C":[1,2,3,4], "D":[1,2,3,4], "W":[1,2,3,4] }

#print(FORWARD_CHECKING(a,d))
print(MONO_FORWARD_CHECKING(a,d))
             
