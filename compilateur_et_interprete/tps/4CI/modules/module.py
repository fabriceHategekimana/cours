from arbreExpArrith import *
from arbreAbstrait import *
from fenetre import *
from pile import *
import numpy as np

#la grammaire
#NONTERMINAL= ne contient que des non terminaux
#TERMINAL1= ne contient que des terminaux
#TERMINAL2= contient des terminaux mais aussi des non terminaux
g= { }
g["PROG"]= [["LISTVAR", "FORM", NONTERMINAL]]
g["LISTVAR"]= [["DECLVAR", "LISTVAR", NONTERMINAL], ["epsilon", TERMINAL2]]
g["DECLVAR"]= [["#", "id", "=", "nb", TERMINAL1]]
g["E"]= [["T", "D", NONTERMINAL]]
g["D"]= [["+", "E", TERMINAL2], ["epsilon", TERMINAL2]]
g["T"]= [["F", "G", NONTERMINAL]]
g["G"]= [["*", "T", TERMINAL2], ["epsilon", TERMINAL2]]
g["F"]= [["(", "E",")", TERMINAL2], ["nb", TERMINAL1], ["id", TERMINAL1]]

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
        tmp = float(entree)
    except:
        res= False
    return res

def estSymbole(entree):
    res= False
    if entree in ["#", "=", "+", "*", "(", ")"]:
        res= True
    return res

def estVariable(entree, variables):
    print("variables:", variables)
    res= False
    for i in variables:
        if entree in i:
            res= True
    return res
    
def prochaineTransition(sommet, mot_actuel, variables):
    T= g[sommet].copy()
    #Dans le cas où on a deux transitions possibles
    if len(T) >= 2:
        #si on a un symbole terminal prédifinit
        if mot_actuel in T[0]:
            transition= T[0]
        #modifiable
        elif estNombre(mot_actuel) or estTerminal(mot_actuel):
            transition= T[1]
        elif estDeclare(mot_actuel, variables):
            transition= T[len(T)-1]
        else:
            print("=> Erreur l'élément que vous avez donné n'est pas reconnu: ", mot_actuel)
            exit(1)
    #sinon
    elif len(T) == 1:
        transition= T[0]
    return transition.copy()

def estTerminal(symbole):
    res= False
    if symbole in ["+", "epsilon", "*", "(", ")", "nb", "id", None]:
        res= True
    return res

def derivation(expression, etape, variables):
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
            if sommet == "nb" or sommet == "id":
                a.addNoeuds([mot_actuel, TERMINAL2])
                f.suivant()
            elif sommet == mot_actuel:
                f.suivant()
            p.pop()
        else:
            #prochaine transition
            transition= prochaineTransition(sommet, mot_actuel, variables)
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
        tour= tour+1
        #if tour == 22:
            #boucle= False
    symbolesAdmis= list(map(lambda n: n[0], variables))
    return a.sousArbre(symbolesAdmis)

def attribution(element, variables):
    if not element.isnumeric():
        for i in variables:
            if element == i[0]: 
                element= i[1] 
    return element

def estDeclare(element, variables):
    res= False
    for i in variables:
        if element in i:
            res= True
    return res

def estCalculable(element, variables):
    res= False 
    if estNombre(element) or estDeclare(element, variables):
        res= True
    return res

def calcule(pile, variables):
    if  pile.length() >= 3:
        exp= []
        exp.append(pile.pop())
        exp.append(pile.pop())
        exp.append(pile.pop())
        if estCalculable(exp[0], variables) and estCalculable(exp[1], variables) and (exp[2] in ["+", "*"]):
            gauche= attribution(exp[0], variables)
            droite= attribution(exp[1], variables)
            if exp[2] == "+":
                res= str(float(gauche)+float(droite))
            else:
                res= str(float(gauche)*float(droite))
            pile.push(res)
        else:
            pile.push(exp[2])
            pile.push(exp[1])
            pile.push(exp[0])

def contexte(variables):
    """les variables arrivent sous de chaines séparé pas des espaces"""
    tab= [[""]]
    if variables != "":
        #On coupe par le symbole "#"
        tab= variables.split("# ")
        tab.pop(0)
        #on coupe par
        for i in range(len(tab)):
            if tab[i][-1] == " ":
                ligne= tab[i][0:len(tab[i])-1]
            else:
                ligne= tab[i]
            print("'"+ligne+"'")
            tab[i]= ligne.split(" = ")
            #S'il y a bien une affectation qui a eu lieu
            if len(tab[i]) > 1:
                if not estNombre(tab[i][1]) and not estVariable(tab[i][1], tab[0:i]):
                    print("=> Erreur: définition de la variable '"+tab[i][0]+"' non permise:")
                    print( "=> '"+tab[i][1]+"' n'est pas un nombre ni une variable")
                    print("=> '"+ligne+"'")
                    exit(0)
            else:
                print("=> Erreur: aucune affectation pour la variable '"+tab[i][0]+"'")
                print("=> '"+ligne+"'")
                exit(0)
    return tab

def syntaxe(expression, variables):
   tab= expression.split(" ") 
   for i in tab:
       #Si la valeur n'est ni une variable, ni un nombre ou ni un symbole réservé
       if not estVariable(i, variables) and not estNombre(i) and not estSymbole(i):
           #on envoie une erreur
           print("=> Erreur: element non reconnu: '"+i+"'")
           exit(0)

def extraire(programme):
    #vérifie s'il y a un #
    if programme.count("#") > 0:
        tab= programme.split(" ")
        lastIndex= 0
        for i in range(len(tab)):
            if tab[i] == "#":
                lastIndex= i
        #normalement la dernière declaration fini à lastIndex+3 (et +1 encore pour la borne)
        variables= " ".join(tab[0:lastIndex+4].copy())
        expression= " ".join(tab[lastIndex+4:].copy())
    else:
        variables= ""
    #on transforme la chaîne tableau:
    variables= contexte(variables)
    syntaxe(programme, variables)
    return (variables, expression)

def derniereSubstitution(expression, variables):
    for i in  variables:
        if expression == i[0]:
            expression= i[1]
    return expression

def evaluer(programme, variables):
    #on construit l'arbre de dérivation et on retourne les terminaux pour l'arbre abstrait
    sa= derivation(programme, False, variables)
    #Construction et remplissage de l'arbre abstrait
    #aa= ArbreAbstrait()
    #for symbole in sa:
        #aa.addValeur(symbole)

    #début de l'évaluation
    pile= Pile([])
    limite= len(sa)+2
    for symbole in sa:
        pile.push(symbole)
        calcule(pile, variables)
    prevlength= pile.length()+1
    while(pile.length() > 1 and pile.length() < prevlength):
        prevlength= pile.length()
        calcule(pile, variables)
    return derniereSubstitution(pile.state()[0], variables)

