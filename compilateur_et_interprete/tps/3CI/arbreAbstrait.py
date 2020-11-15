from pile import *
class NoeudAbstrait():

    def __init__(self, valeur):
        #code
        self.gauche= None
        self.droite= None
        self.valeur= valeur
        self.passage= 0

    def isEmpty(self):
        res= False 
        if self.valeur == None:
            res= True
        return res
    
    def explore(self):
        a= self.passage
        self.passage= a+1

class ArbreAbstrait():

    def __init__(self):
        #code
        self.root= NoeudAbstrait(None)
        self.actuel= self.root
        self.pile= Pile([])

    def addValeur(self, valeur):
        if self.actuel.isEmpty():
            #si le noeud est vide, on le rempli
            self.actuel.valeur= valeur
        else:
            #sinon on remplis son enfant gauche et son enfant droit devient actuel
            gauche= NoeudAbstrait(valeur)
            self.actuel.gauche= gauche
            self.actuel.droite= NoeudAbstrait(None)
            self.actuel= self.actuel.droite

    def successeurExiste(self, successeur):
        res= False
        if successeur != None and successeur.valeur != None:
            res= True
        return res
    
    def dejaExplore(self, noeud, n):
        res= False
        if noeud.passage >= n:
            res= True
        return res

    def remonte(self):
        boucle= True
        while boucle:
            #print("Non...")
            if self.pile.isEmpty():
                #print("La pile est vide, on s'arrête")
                boucle= False
            else:
                self.exploration= self.pile.pop()
                #self.explore.append(self.exploration)
                self.exploration.explore()
                #print("On prend le noeud d'avant: ", self.exploration.valeur)
                #print("Il a été exploré: ", self.exploration.passage)
                if not self.dejaExplore(self.exploration, 3):
                    #print("Est-ce qu'il a un successeur droit?")
                    if self.successeurExiste(self.exploration.droite):
                        self.pile.push(self.exploration)
                        self.exploration= self.exploration.droite
                        #print("Oui: ", self.exploration.valeur)
                        boucle= False

    def affichage(self): 
        self.explore= []
        self.res= []
        self.exploration= self.root
        boucle= True
        while boucle:
            #print("Noeud: ", self.exploration.valeur)
            if not self.dejaExplore(self.exploration, 1):
               #on "print" sa valeur
               self.res.append(self.exploration.valeur)
               #on le compte comme exploré
               #self.explore.append(self.exploration)
               self.exploration.explore()
               #print("printé et exploré!")
            #print("Est-ce qu'il a un successeur gauche?")
            if self.successeurExiste(self.exploration.gauche):
               self.pile.push(self.exploration)
               self.exploration= self.exploration.gauche
               #print("Oui: ", self.exploration.valeur)
            else:
               #print("Non...")
               self.remonte()
            if self.pile.isEmpty():
               #print("La pile est vide, on s'arrête")
               boucle= False
        return self.res

    def depart(self):
        self.affichage()
        self.pointeur= 0

    def suivant(self):
        if len(self.res) > self.pointeur:
            res= self.res[self.pointeur] 
            self.pointeur += 1
        else:
            res= None
        return res
