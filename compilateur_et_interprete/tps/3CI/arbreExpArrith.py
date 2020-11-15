from pile import *

#implémentation d'un noeud de l'arbre
NONTERMINAL= 0
TERMINAL1= 1
TERMINAL2= 2

#Les modes
MODE_AJOUT= 0
MODE_AFFICHAGE= 1

class Noeud():

    def __init__(self, valeur):
        self.valeur= valeur
        self.Gauche= None
        self.Droite= None
        self.Annexe= None
        self.explore= [0, 0]
        self.enfants= 0


class Arbre():

    def __init__(self):
        #code
        self.pile= [Pile([]), Pile([])]
        self.root= None

    def estTerminal(self, symbole):
        res= False
        if symbole == 2:
            res= True
        return res
    
    def addNoeuds(self, valeurs):
        #premier élément ajouté (lorsque l'arbre n'a pas encore de racine)
        typeDeSymbole= valeurs.pop()
        if self.root == None:
            if len(valeurs) == 1:
                self.root= Noeud(valeurs[0])
                self.pile[MODE_AJOUT].push(self.root)
        #les autres cas
        else:
            #on prend le dernier noeud actif
            noeud= self.pile[MODE_AJOUT].pop()
            gauche= Noeud(valeurs[0])
            noeud.Gauche= gauche
            noeud.enfants= 1
            if len(valeurs) >= 2:
                droite= Noeud(valeurs[1])
                noeud.Droite= droite
                noeud.enfants= 2
                noeud.explore[MODE_AJOUT]= 1
            if len(valeurs) == 3:
                annexe= Noeud(valeurs[2])
                noeud.Annexe= annexe
                noeud.enfants= 3

            self.pile[MODE_AJOUT].push(noeud)
            if self.estTerminal(typeDeSymbole):
                self.remonte(MODE_AJOUT)
            else:
                self.pile[MODE_AJOUT].push(gauche)

    def estDroiteExplore(self, noeud, mode):
        res= False
        if (noeud.enfants >= 2 and noeud.explore[mode] >= 2) or noeud.enfants <= 1:
            res= True
        return res
    
    def estAffiche(self, mode):
        res= False
        if mode == 1:
            res= True
        return res

    def estAnnexeExplore(self, noeud, mode):
        res= False
        if (noeud.enfants == 3 and noeud.explore[mode] == 3) or noeud.enfants <= 2:
            res= True
        return res

    def remonte(self, mode):
        #remonter dans la pile d'affichage
        if not self.pile[mode].isEmpty():
            rem= True
            while rem:
                if not self.pile[mode].isEmpty():
                    noeud= self.pile[mode].pop()
                    explore= noeud.explore[mode]
                    if not self.estDroiteExplore(noeud, mode):
                       explore= explore+1
                       noeud.explore[mode]= explore
                       self.pile[mode].push(noeud) 
                       self.pile[mode].push(noeud.Droite) 
                       rem= False
                    elif not self.estAnnexeExplore(noeud, mode):
                       explore= explore+1
                       noeud.explore[mode]= explore
                       self.pile[mode].push(noeud) 
                       self.pile[mode].push(noeud.Annexe) 
                       rem= False
                else:
                    rem= False
        else:
            rem= False

    def existeSuccesseurGauche(self, noeud):
        res= False
        if noeud.enfants > 0:
            res= True
        return res

    def affiche(self):
        mode= MODE_AFFICHAGE
        #initialisation on part à partir du root de l'arbre
        pile= self.pile[mode]
        pile.push(self.root)
        recherche= True
        tour= 0
        #boucle
        while recherche:
            if not pile.isEmpty():
                #on prend le dernier noeud actif
                noeud= pile.pop()
                explore= noeud.explore[mode]
                if explore == 0:
                    print(noeud.valeur)
                if self.existeSuccesseurGauche(noeud):
                        explore= explore+1
                        noeud.explore[mode]= explore
                        pile.push(noeud)
                        pile.push(noeud.Gauche)
                else:
                    self.remonte(mode)
                tour= tour+1
                #if tour == 1000:
                    #recherche= False
            else:
                recherche= False

    def symboleValide(self, symbole, symbolesAdmis):
        res= False
        if symbole in ["+", "*"] or symbole.isnumeric() or symbole in symbolesAdmis:
            res= True
        return res

    def getVoisins(self, noeud):
        v= [] 
        if noeud.Gauche != None:
            v.append(noeud.Gauche)
        if noeud.Droite != None:
            v.append(noeud.Droite)
        if noeud.Annexe != None:
            v.append(noeud.Annexe)
        return v

    def sousArbre(self, symbolesAdmis):
        #Exploration en BFS
        recherche= [self.root]
        voisins= []
        symboles= []
        boucle= True
        while(boucle):
            for noeud in recherche:
                if self.symboleValide(noeud.valeur, symbolesAdmis):
                    symboles.append(noeud.valeur)
                v= self.getVoisins(noeud)
                voisins= voisins+v.copy()
            recherche= voisins.copy()
            voisins= []
            if recherche == []:
                boucle= False
        return symboles

             
        #pour chaque élément de la liste
            #on trouve ses voisins
            #on on les met dans la liste des voisins
        
