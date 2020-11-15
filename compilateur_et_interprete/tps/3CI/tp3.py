#fiche de test
from arbreExpArrith import *
from arbreAbstrait import *
from fenetre import *
from pile import *

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
        tmp = int(entree)
    except:
        res= False
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
            print("Erreur l'élément que vous avez donné n'est pas reconnu: ", mot_actuel)
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
        #if tour == 1000:
            #boucle= False
    symbolesAdmis= list(map(lambda n: n[0], variables))
    #print("symbolesAdmis: ", symbolesAdmis)
    print("sousArbre: ", a.sousArbre(symbolesAdmis))
    #a.affiche()
    print("-----------")
    print(a.root.Gauche.Gauche.Annexe.valeur)
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
    if element.isnumeric() or estDeclare(element, variables):
        res= True
    return res

def calcule(pile, variables):
    if  pile.length() >= 3:
        #on prend les trois derniers éléments de la liste
        #exp= liste[-3:len(liste)]
        #print(pile.state())
        exp= []
        exp.append(pile.pop())
        exp.append(pile.pop())
        exp.append(pile.pop())
        if estCalculable(exp[0], variables) and estCalculable(exp[1], variables) and (exp[2] in ["+", "*"]):
            gauche= attribution(exp[0], variables)
            droite= attribution(exp[1], variables)
            if exp[2] == "+":
                res= str(int(gauche)+int(droite))
            else:
                res= str(int(gauche)*int(droite))
            pile.push(res)
        else:
            pile.push(exp[2])
            pile.push(exp[1])
            pile.push(exp[0])

def contexte(variables):
    """les variables arrivent sous de chaines séparé pas des espaces"""
    print("variables: ", variables)
    tab= [[""]]
    if variables != "":
        #On coupe par le symbole "#"
        tab= variables.split("# ")
        tab.pop(0)
        for i in range(len(tab)):
            tab[i]= tab[i].split(" = ")
    return tab

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
        expression= programme
    return (variables, expression)


def evaluer(programme):
    #On sépare la déclaration de variable de l'expression mathématique
    #Prog= [listeDeVariable, ExpressionMathématique]
    prog= extraire(programme) 
    #On construit la liste des variables
    variables= contexte(prog[0])
    #on construit l'arbre de dérivation et on retourne les terminaux pour l'arbre abstrait
    sa= derivation(prog[1], True, variables)

    #Construction et remplissage de l'arbre abstrait
    #aa= ArbreAbstrait()
    #for symbole in sa:
        #aa.addValeur(symbole)

    ##début de l'évaluation
    #pile= Pile([])
    #limite= len(sa)+2
    #for symbole in sa:
        #pile.push(symbole)
        #calcule(pile, variables)
    #calcule(pile, variables)
    #print(pile.state())


#-------------
#DÉBUT DU CODE
#-------------

#Exemple d'expression à évaluer
#evaluer(" 3 + 5 * 4")
evaluer("( 4 + 3 ) * 2")
