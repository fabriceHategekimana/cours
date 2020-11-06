#-------------------------
# PSC BACKTRACKING HELPERS
#-------------------------
def estVide(d):
    res= True
    for el in d:
        if len(d[el]) > 0:
            res= False
            break
    return res

def valide(a):
    res= True
    for el in a:
        if a[el] == 0:
            res= False
            break
    return res
    
def getNonAffecte(a):
    res= 0
    for el in a:
        if a[el] == 0:
            res= el
            break
    return res

#-----------------
# PSC BACKTRACKING
#-----------------
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

#-------------------------------
#Petites fonctions particulières
#-------------------------------
def state(a):
    return "C="+str(a["C"])+"; D="+str(a["D"])+"; W="+str(a["W"])

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

#-----------------
# FORWARD_CHECKING
#-----------------
def FORWARD_CHECKING(a, d):
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
    print("Etape "+str(d["etape"])+". FC "+state(a))
    d["etape"]= d["etape"]+1
    return d

#-------------------
#CONTRAINTES UNAIRES            
#-------------------
def MONO_FORWARD_CHECKING(a,d): 
    #Contrainte unitaire
    for i in range(3, 5):
        cond= c[i]
        nonAffecte= cond[0][0]
        d[nonAffecte]= myFilter(cond[1], d[nonAffecte])
    print("Etape "+str(d["etape"])+". CU "+state(a))
    d["etape"]= d["etape"]+1
    return d


#--------------------------
#DÉFINITION DES CONTRAINTES
#--------------------------
c= []
c.append([("C","W"), lambda C,W: C != W])
c.append([("C","W"), lambda C,W: W not in adjacent(C)])
c.append([("C","D"), lambda C,D: cote(C) != cote(D)])
c.append([("W"), lambda W: len(adjacent(W)) >= 2])
c.append([("D"), lambda D: len(adjacent(D)) >= 2])



#-------------
#DÉBUT DU CODE
#-------------
#créer affectation
a= {"C":0, "D":0, "W":0}
#créer domaine
d= { "C":[1,2,3,4], "D":[1,2,3,4], "W":[1,2,3,4], "etape":1}

#On utilise l'argorithme
d=MONO_FORWARD_CHECKING(a,d)
final= PSC_BACKTRACKING(a,d) 

#On afficher l'état final
print("final: ", final)
             
