#implémentation d'un noeud de l'arbre
class Noeud():

    def __init__(self, valeur):
        self.valeur= valeur
        self.Gauche= None
        self.Droite= None
        self.explore_ajout= 0
        self.explore_affiche= 0
        self.enfants= 0

class Pile():

    def __init__(self, liste):
        #code
        self.liste= liste

    def push(self, element):
        self.liste.append(element)

    def pop(self):
        if len(self.liste) == 0:
            return None
        else:
            return self.liste.pop()

class Arbre():

    def __init__(self):
        #code
        self.pile_ajout= Pile([])  
        self.pile_exploration= Pile([])  
        self.root= None
    
    def addNoeuds(self, valeurs):
        if self.root == None:
            if len(valeurs) == 1:
                self.root= Noeud(valeurs[0])
                self.pile_ajout.push(self.root)
        else:
            #on prend le dernier noeud actif
            noeud= self.pile_ajout.pop()
            gauche= Noeud(valeurs[0])
            noeud.Gauche= gauche
            noeud.enfants= 1
            if len(valeurs) == 2:
                droite= Noeud(valeurs[1])
                noeud.Droite= droite
                noeud.enfants= 2
                noeud.explore_ajout= 1
                self.pile_ajout.push(noeud)
                self.pile_ajout.push(gauche)

    def affiche(self):
        #initialisation
        self.pile_exploration.push(self.root)
        recherche= True
        tour= 0
        #boucle
        while recherche:
            #on prend le dernier noeud actif
            noeud= self.pile_exploration.pop()
            print("Noeud= ", noeud)
            if noeud != None:
                if noeud.explore_affiche == 0:
                    print(noeud.valeur)
                    noeud.explore_affiche= noeud.explore_affiche+1
                if noeud.enfants > 0 or (noeud.enfants - noeud.explore_affiche) > 0:
                    if noeud.explore_affiche == 0:
                        noeud.explore_affiche= noeud.explore_affiche+1
                        self.pile_exploration.push(noeud)
                        self.pile_exploration.push(noeud.Gauche)
                    elif noeud.explore_affiche == 1:
                        if noeud.enfants == 2:
                            noeud.explore_affiche= noeud.explore_affiche+1
                            self.pile_exploration.push(noeud)
                            self.pile_exploration.push(noeud.Droite)
                else:
                    res= self.pile_exploration.pop()
                    if res == None:
                        recherche= False
            else:
                recherche= False
            tour= tour+1
            if tour == 2:
                recherche= False
        

a= Arbre()
a.addNoeuds(["0"])
a.addNoeuds(["a","b"])
a.affiche()
