class Pile():

    def __init__(self, tab):
        #code
        self.tab= tab.copy()

    def peek(self):
        return self.tab[0]

    def push(self, e):
        self.tab.insert(0, e)

    def pop(self):
        if len(self.tab) == 0:
            e= -1
        else:
            e= self.tab.pop(0)
        return e

    def state(self):
        return self.tab

class Hanoi():

    def __init__(self, liste):
        self.dic= {}
        self.dic["gauche"]= Pile(liste.copy())
        self.dic["milieu"]= Pile([])
        self.dic["droite"]= Pile([])

    def transition(self, couple):
        e= self.dic[couple[0]].pop()
        self.dic[couple[1]].push(e)

    def state(self):
        return [self.dic["gauche"].state(), self.dic["milieu"].state(), self.dic["droite"].state()]

    def setState(self, state):
       self.dic["gauche"]= Pile(state[0].copy())
       self.dic["milieu"]= Pile(state[1].copy())
       self.dic["droite"]= Pile(state[2].copy())

#FONCTION DE L'ALGORITHME

def test(hanoi, explore):
    hanoiSta= hanoi.state()
    #premier teste: valide?
    res= True
    for pile in hanoiSta:
        if -1 in pile:
            res= False
        elif len(pile) == 3:
            if pile[0] > pile[1] or pile[1] > pile[2]:
                res= False
        elif len(pile) == 2:
            if pile[0] > pile[1]:
                res= False
    #deuxième test: déjà traversé?
        for hanoiExp in explore:
            if hanoiSta == hanoiExp:
                res= False
    return res
         

#ALGORITHME DE RECHERCHE
transitions= [("gauche", "milieu"),("gauche", "droite"),("milieu", "gauche"),("milieu", "droite"),("droite", "gauche"),("droite", "milieu")]

h= Hanoi([1,2,3])
dejaExplore= [h.state()]
chemins= [[h.state()]]

final= []
verbose= True
recherche= True

etatFinal= [[],[],[1,2,3]]
tour= 0
while(recherche):
    if verbose:
        print("")
        print("----------------------")
        print("tour ", tour+1)
    #on prend le dernier état
    remplacement= []
    for chemin in chemins:
        actuel= chemin[len(chemin)-1]
        if verbose:
            print("noeud traité:")
            print(actuel)
            print("état de la file:")
            print(chemins)
        h.setState(actuel)
        valide=[]
        #on regroupe tout les états atteignables 
        for transition in transitions:
            h.transition(transition) 
            if test(h, dejaExplore):
                dejaExplore.append(h.state())
                valide.append(h.state())
                #si l'état validé est l'état final qu'on recherche, on met fin à la boucle
                if h.state() == etatFinal:
                    recherche= False
            h.setState(actuel)
        #on combine le tout
        newChemin=[]
        for nouvelEtat in valide:
            chemin.append(nouvelEtat.copy())
            newChemin.append(chemin.copy())
            chemin.pop()
        remplacement= remplacement+newChemin.copy()
    chemins= remplacement.copy()
    tour= tour+1
    if tour == 100:
        recherche= False
    #print("")
    #print("** FINALEMENT: **")
    #print(chemins)
    #print(len(chemins))
    #print(len(chemins[0]))

print("")
print("")
print("###############")
print("SOLUTION FINALE")
print("###############")
print("")
for chemin in chemins:
    if etatFinal in chemin:
        print(chemin)
