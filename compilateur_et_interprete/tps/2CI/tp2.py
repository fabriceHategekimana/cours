#fiche de test
from arbreExpArrith import *
from arbreAbstrait import *
from fenetre import *
from pile import *

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

def estNombre(entree):
    res= True
    try:
        tmp = int(entree)
    except:
        res= False
    return res

def prochaineTransition(sommet, mot_actuel):
    T= g[sommet].copy()
    #Dans le cas où on a deux transitions possibles
    if len(T) == 2:
        if mot_actuel in T[0]:
            transition= T[0]
        #modifiable
        elif estNombre(mot_actuel) or estTerminal(mot_actuel):
            transition= T[1]
        else:
            print("Erreur l'élément que vous avez donné n'est pas reconnu: ", mot_actuel)
            exit(1)
    #sinon
    else:
        transition= T
    return transition.copy()

def estTerminal(symbole):
    res= False
    if symbole in ["+", "epsilon", "*", "(", ")", "nb", None]:
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
    #a.affiche()
    return a.sousArbre()

def calcule(pile):
    if  pile.length() >= 3:
        #on prend les trois derniers éléments de la liste
        #exp= liste[-3:len(liste)]
        #print(pile.state())
        exp= []
        exp.append(pile.pop())
        exp.append(pile.pop())
        exp.append(pile.pop())
        #print(exp[0]. isnumeric())
        #print(exp[1].isnumeric())
        #print(exp[2] in ["+", "*"])
        if exp[0].isnumeric() and exp[1].isnumeric() and (exp[2] in ["+", "*"]):
            if exp[2] == "+":
                res= str(int(exp[0])+int(exp[1]))
            else:
                res= str(int(exp[0])*int(exp[1]))
            pile.push(res)
        else:
            pile.push(exp[2])
            pile.push(exp[1])
            pile.push(exp[0])



def evaluer(expression):
    #on constriuit l'arbre de dérivation et on retourne les terminaux pour l'arbre abstrait
    sa= derivation(expression, True)
    #Construction et remplissage de l'arbre abstrait
    aa= ArbreAbstrait()
    for symbole in sa:
        aa.addValeur(symbole)

    ##début de l'évaluation
    pile= Pile([])
    for symbole in sa:
        pile.push(symbole)
        calcule(pile)
    calcule(pile)
    print(pile.state())


#-------------
#DÉBUT DU CODE
#-------------

#Exemple d'expression à évaluer
evaluer(" 3 + 5 * 4")

#détection d'erreur
