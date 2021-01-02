from module import *
from math import sqrt

#Variables globales pour les variables est la sortie standard
VARIABLES= []
STDOUT= ""
SOUSSCRIPT=""
COMPTEBOUCLE= 0

def estDeclarationDeVariable(instruction):
    res= False
    if "=" in instruction:
        res= True
    return res

def getID(variables):
    tab= []
    for i in variables:
        tab.append(i[0])
    return tab

def preEvaluer(instruction, variables):
    if "inv " in instruction:
        instruction= instruction.replace("inv ", "")
        instruction= str(1/float(evaluer(instruction, variables)))
    elif "racine " in instruction:
        instruction= instruction.replace("racine ", "")
        instruction= str(sqrt(float(evaluer(instruction, variables))))
    else:
        instruction= evaluer(instruction, variables)
    return instruction

def parseVariable(instruction):
    parts= instruction.split(" = ")
    if parts[0] in getID(VARIABLES):
        pos= getID(VARIABLES).index(parts[0])
        VARIABLES[pos]= [parts[0], preEvaluer(parts[1], VARIABLES)]
    else:
        VARIABLES.append([parts[0], preEvaluer(parts[1], VARIABLES)])

def estAffichage(instruction):
    res= False
    if "afficher" in instruction:
        res= True
    return res

def estRetourALaLigne(instruction):
    res= False
    if "aff_ral" == instruction:
        res= True
    return res

def estBoucle(instruction):
    res= False
    if "boucle" in instruction:
        res= True
    return res

def sortieStandard(instruction):
    if "afficher" in instruction:
        instruction= evaluer(instruction.replace("afficher ", ""), VARIABLES)
    elif "aff_ral":
        instruction="\n"
    global STDOUT
    STDOUT += instruction

#vérifie si le programme a un crochet fermant
def aCrochetFermant(instruction):
    res= False
    if "}" in instruction:
        res= True
    return res

def aCrochetOuvrant(instruction):
    res= False
    if "{" in instruction:
        res= True
    return res

def addDansSousScript(instruction):
    global SOUSSCRIPT
    SOUSSCRIPT += instruction+"; "

def executeSousScript():
    global COMPTEBOUCLE
    global SOUSSCRIPT
    s= SOUSSCRIPT
    c= COMPTEBOUCLE
    SOUSSCRIPT=""
    COMPTEBOUCLE=0
    for i in range(c):
        execution(s)

def extraireBoucle(i):
    global COMPTEBOUCLE
    COMPTEBOUCLE= int(evaluer(i.replace("boucle ", "").replace(" {", ""), VARIABLES))

def enleverTabulation(texte):
    limite= texte.count("\t")
    if limite > 0:
        texte= texte.replace("\t", "")
    return texte

def enleverEspaceInutil(texte):
    limite= texte.count("  ")
    while(limite > 0):
        texte= texte.replace("  ", " ")
        limite= texte.count("  ")
    return texte

def pointVirguleSuplementaire(texte):
    texte= texte.replace("{", "{;", texte.count("{"))
    texte= texte.replace("}", "};", texte.count("}"))
    return texte

def formater(texte):
    return pointVirguleSuplementaire(enleverEspaceInutil(enleverTabulation(texte)))

def execution(script):
    instructions= script.split("; ")
    crochetOuvert= 0
    for i in instructions:
        print("Sous-script: ", SOUSSCRIPT)
        print("instruction: ", i)
        if aCrochetOuvrant(i) and crochetOuvert > 0:
            crochetOuvert= crochetOuvert+1
            addDansSousScript(i)
        elif aCrochetFermant(i):
            crochetOuvert= crochetOuvert-(i.count("}"))
            if crochetOuvert > 0:
                addDansSousScript(i)
            else:
                executeSousScript()
        elif crochetOuvert > 0:
            addDansSousScript(i)
        else:
            if estBoucle(i):
                crochetOuvert= crochetOuvert+1
                extraireBoucle(i)
            elif estDeclarationDeVariable(i):
                parseVariable(i)
            elif estAffichage(i) or estRetourALaLigne(i):
                sortieStandard(i)

#----
#CODE
#----
f = open("pi2.txt", "r")
script= formater(f.read().replace("\n", " ")) 
execution(script)
print(STDOUT)

