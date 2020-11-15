
def estNombre(entree):
    res= True
    try:
        tmp = int(entree)
    except:
        res= False
    return res

    if len(T) == 2:
        if mot_actuel in T[0]:
            transition= T[0]
        elif estTerminal(mot_actuel) or estNombre(mot_actuel):
            transition= T[1]
        else:
            print("Erreur: l'élément rentré n'est ni un nombre, ni un symbole: ", mot_actuel)
