class Pile():

    def __init__(self, tab):
        #code
        self.tab= tab

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
        self.dic["gauche"]= Pile(liste)
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
        
#fonction de l'algorithme

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
chemin= [h.state()]
compteurs= [0]

verbose= True
recherche= True

etatFinal= [[],[],[1,2,3]]
tour= 0
while(recherche):
    if verbose:
        print("")
        print("----------------------")
        print("tour ", tour+1)
        print("noeud traité")
    #on prend le dernier état
    actuel= chemin[len(chemin)-1]
    if verbose:
        print(actuel)
        print("état de la file")
        print(chemin)
    compteur= compteurs[len(compteurs)-1]
    h.setState(actuel)
    #on prend la prochaine transition selon le compteur
    transition= transitions[compteur]
    #on trouve le nouvel état
    h.transition(transition)
    #on teste le nouvel état
    if test(h, dejaExplore):
        #si ça passe on regarde si c'est l'état final
        if h.state() == etatFinal:
            #si c'est le cas, on arrête la boucle
            recherche= False
            print("Solution trouvée au tour: ", tour+1)
        #on ajoute le nouvel état et on laisse le reste
        chemin.append(h.state())
        compteurs.append(0)
    else:
        compteur= compteur+1
        #si on a testé toutes les transitions, on backtrack
        if compteur == len(transitions):
            chemin.pop()
            compteurs.pop()
        #sinon on prépare la prochaine transition
        else:
            compteurs[len(compteurs)-1]= compteur
    dejaExplore.append(h.state()) 
    tour= tour+1
    if tour == 100:
        recherche= False
print("")
print("")
print("** FINALEMENT **")
print("chemin:")
print(chemin)
