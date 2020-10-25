#fiche de test
from arbreExpArrith import *
from fenetre import *

#la grammaire
g= { }
g["E"]= ["T", "D", NONTERMINAL]
g["D"]= [["+", "E", TERMINAL2], ["epsilon", TERMINAL2]]
g["T"]= ["F", "G", NONTERMINAL]
g["G"]= [["*", "T", TERMINAL2], ["epsilon", TERMINAL2]]
g["F"]= [["(", "E",")", TERMINAL2], ["nb", TERMINAL1]]

def remplace(pile, transition):
    terminalOuNon= transition.pop()
    #le sommet doit avoir le symbole tout à gauche
    transition.reverse()
    pile.pop()
    for element in transition:
        pile.push(element)
    #on remet transition à sa place (pour éviter les effets de bord)
    transition.reverse()
    transition.append(terminalOuNon)

def prochaineTransition(sommet, mot_actuel):
    T= g[sommet].copy()
    #Dans le cas où on a deux transitions possibles
    if len(T) == 2:
        if mot_actuel in T[0]:
            transition= T[0]
        else:
            transition= T[1]
    #sinon
    else:
        transition= T
    return transition.copy()

def estTerminal(symbole):
    res= False
    if symbole in ["+", "epsilon", "*", "(", ")", "nb"]:
        res= True
    return res

def derivation(expression, etape):
    #initialisation
    #pile
    p= Pile(["E"])
    #arbre
    a= Arbre()
    a.addNoeuds(["E", NONTERMINAL])
    #fenêtre
    f= Fenetre(expression)

    #boucle
    boucle= True
    verbose= etape
    tour= 0
    while boucle:
        #sommet
        sommet= p.peak()
        #mot actuel
        mot_actuel= f.actuel()
        if verbose:
            print("")
            print("-------------------------")
            print("tour ", tour+1)
            print("-------")
            print("pile: ", p.state())
            print("sommet: ", sommet)
            print("mot actuel: ", mot_actuel)
        #Si le sommet est un symbole terminal
        if estTerminal(sommet):
            if sommet == "nb":
                a.addNoeuds([mot_actuel, TERMINAL2])
                f.suivant()
            elif sommet == mot_actuel:
                f.suivant()
            p.pop()
        else:
            #prochaine transition
            transition= prochaineTransition(sommet, mot_actuel)
            if verbose:
                print("==========")
                print("transition: ", transition)
            #on remplace
            remplace(p, transition)
            #on ajoute le lot à l'arbre
            a.addNoeuds(transition)
            #on quitte si la pile est vide
        if p.isEmpty():
            boucle= False
        #tour= tour+1
        #if tour == 1000:
            #boucle= False
    a.affiche()

derivation("( 5 * 5 ) + 8", False)
