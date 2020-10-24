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

    def isEmpty(self):
        if len(self.liste) == 0:
            return True
        else:
            return False

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

    def estDroiteExplore(self, noeud):
        res= False
        if noeud.enfants == 2 and noeud.explore_affiche == 2 or noeud.enfants == 1:
            res= True
        return res

    def remonte(self):
        if not self.pile_exploration.isEmpty():
            rem= True
            while rem:
                if not self.pile_exploration.isEmpty():
                    noeud= self.pile_exploration.pop()
                    if not self.estDroiteExplore(noeud):
                       noeud.explore_affiche= noeud.explore_affiche+1
                       self.pile_exploration.push(noeud) 
                       self.pile_exploration.push(noeud.Droite) 
                       rem= False
                else:
                    rem= False

    def existeSuccesseurGauche(self, noeud):
        res= False
        if noeud.enfants > 0:
            res= True
        return res

    def affiche(self):
        #initialisation
        self.pile_exploration.push(self.root)
        recherche= True
        tour= 0
        #boucle
        while recherche:
            if not self.pile_exploration.isEmpty():
                #on prend le dernier noeud actif
                noeud= self.pile_exploration.pop()
                if noeud.explore_affiche == 0:
                    print(noeud.valeur)
                if self.existeSuccesseurGauche(noeud):
                        noeud.explore_affiche= noeud.explore_affiche+1
                        self.pile_exploration.push(noeud)
                        self.pile_exploration.push(noeud.Gauche)
                else:
                    self.remonte()
                tour= tour+1
                if tour == 100:
                    recherche= False
            else:
                recherche= False
        

a= Arbre()
a.addNoeuds(["E"])
a.addNoeuds(["T","D"])
a.addNoeuds(["F","G"])
a.addNoeuds(["nb"])
a.addNoeuds(["3"])
#print(a.root.Gauche.Droite.valeur)
a.affiche()
