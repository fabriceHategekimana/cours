from pile import *

#implémentation d'un noeud de l'arbre
NONTERMINAL= 0
TERMINAL1= 1
TERMINAL2= 2

#Les modes
MODE_AJOUT= 0
MODE_AFFICHAGE= 1

def estNombre(entree):
    res= True
    try:
        tmp = float(entree)
    except:
        res= False
    return res

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
            #on met la valeur directement à gauche
            gauche= Noeud(valeurs[0])
            noeud.Gauche= gauche
            #on met le nombre d'enfant à 1 (car au moins 1 enfant à gauche)
            noeud.enfants= 1
            #S'il y a une 2e valeur alors on la met à droite
            if len(valeurs) >= 2:
                droite= Noeud(valeurs[1])
                noeud.Droite= droite
                noeud.enfants= 2
                #on met aussi le compteur de noeud exploré à 1?
                noeud.explore[MODE_AJOUT]= 1
            #si on a une troisième valeur, on l'ajoute
            if len(valeurs) == 3:
                annexe= Noeud(valeurs[2])
                noeud.Annexe= annexe
                noeud.enfants= 3
            #on remet le dernier noeud à sa place (il devient l'avant-dernier)
            self.pile[MODE_AJOUT].push(noeud)
            #si le symbole est terminal 
            if self.estTerminal(typeDeSymbole):
                #on remonte au dernier noeud sans enfant 
                self.remonte(MODE_AJOUT)
            else:
                #sinon on place le gauche comme le noeud le plus ressent
                self.pile[MODE_AJOUT].push(gauche)

    def estDroiteExplore(self, noeud, mode):
        res= False
        #si
        #le noeud a plus de 2 enfants
        #le nombre de noeud exploré dépasse 1
        #ou si le nombre d'enfant est inférieur ou égal à 1
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
            #on debute la rem (=remonté)
            rem= True
            while rem:
                #Si on est pas tout en haut de l'arbre (donc on peut encore monter)
                if not self.pile[mode].isEmpty():
                    #On prend le dernier noeud
                    noeud= self.pile[mode].pop()
                    #on regarde son compteur d'enfant exploré (mode affichage) existant (mode ajout)
                    explore= noeud.explore[mode]
                    #Si la droite n'est pas explorée
                    if not self.estDroiteExplore(noeud, mode):
                       #on augmente le compteur
                       if mode == MODE_AJOUT:
                           explore= 3
                       else:
                           explore= explore+1
                       #on met à jour le compteur
                       noeud.explore[mode]= explore
                       #on remet le noeud
                       self.pile[mode].push(noeud) 
                       #on ajoute son enfant à droite
                       self.pile[mode].push(noeud.Droite) 
                       #on quitte la boucle (car on a trouvé le prochain à explorer)
                       rem= False
                    #Si l'annexe n'est pas encore exploré
                    elif not self.estAnnexeExplore(noeud, mode):
                       #on augmente le compteur
                       explore= explore+1
                       #on met à jour le compteur
                       noeud.explore[mode]= explore
                       #on remet le noeud
                       self.pile[mode].push(noeud) 
                       #on ajoute son enfant dans l'Annexe
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
        print("Fin de l'affichage")

    def symboleValide(self, symbole, symbolesAdmis):
        res= False
        if symbole in ["+", "*"] or estNombre(symbole) or symbole in symbolesAdmis:
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
        #on commence par la racine
        symboles= self.sousArbreHelper(self.root, symbolesAdmis)
        return symboles

    def sousArbreHelper(self, noeud, symbolesAdmis):
        #on crée le tableau qui contiendra les noeuds explorés
        recherche= [noeud]
        #on définit les voisins et les symboles à retourner
        voisins= []
        symboles= []
        #on définit la variable pour gérer les parenthèses
        parenthese= 0
        recure= None
        #on commence l'exploration
        boucle= True
        while(boucle):
            #Pour chaque noeud dans la recherche
            for noeud in recherche:
                if noeud.valeur == "E" and parenthese == 1:
                    #On garde ce noeud pour faire un recursion juste après
                    recure= noeud
                else:
                    #si le symbole est valide, on le met dans symboles
                    if self.symboleValide(noeud.valeur, symbolesAdmis):
                        symboles.append(noeud.valeur)
                    elif noeud.valeur in ["(", ")"]:
                        parenthese= 1
                    #on prends tout ses enfant (=voisins)
                    v= self.getVoisins(noeud)
                    #on les gardes ensemble
                    voisins= voisins+v.copy()
            if parenthese == 1:
                   symboles= symboles+self.sousArbreHelper(recure, symbolesAdmis) 
                   parenthese= 0
            recherche= voisins.copy()
            voisins= []
            if recherche == []:
                boucle= False
        return symboles

             
        #pour chaque élément de la liste
            #on trouve ses voisins
            #on on les met dans la liste des voisins
        
