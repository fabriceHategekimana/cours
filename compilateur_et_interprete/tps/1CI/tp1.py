def onePoint(mot):
    res= True
    if mot.count(".") != 1:
        res= False
    return res

def isReserved(symbole):
    reserved= ["=","+","*","'"]
    res= True
    if symbole not in reserved:
        res= False
    return res

def isLetter(mot):
    alphabet= "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    alphabet.append(" ")
    res= True
    for symbole in mot:
        if symbole not in alphabet:
            res= False
    return res

def isNumber(mot):
    number= "0 1 2 3 4 5 6 7 8 9 .".split()
    res= True
    for symbole in mot:
        if symbole not in number:
            res= False
    return res
        
def isLetterNumber(mot):
    res= True
    for symbole in mot:
        if not (isNumber(symbole) or isLetter(symbole)):
            res= False
    return res

def isVariable(mot):
    res= False
    if isLetter(mot[0]) and isLetterNumber(mot):
        res= True
    return res

def isEntier(mot):
    res= False
    if isNumber(mot) and not onePoint(mot):
        res= True
    return res

def isReel(mot):
    res= False
    if isNumber(mot) and onePoint(mot):
        res= True
    return res

def isChaine(mot):
    res= False
    if mot[0] == "'" and mot[len(mot)-1] == "'" and isLetter(mot[1:len(mot)-2]):
        res= True
    return res


#-------
#LE CODE
#-------

entree="Fabrice = 5 Vestin = 'Hello' Redempta = 2 + 2 * 36.7".split()
print(entree)

for mot in entree:
    if isVariable(mot):
        print(mot+" est une variable") 
    elif isReserved(mot):
        print(mot+" est un symbole") 
    elif isEntier(mot):
        print(mot+" est un entier") 
    elif isReel(mot):
        print(mot+" est un réel") 
    else:
        print("Erreur le terme '"+mot+"' est non reconnu")
