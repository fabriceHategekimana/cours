def PSC_BACKTRACKING(a, d):
    #1. Si A= S_G alors retourner A
    if valide(a):
        return a
    #2. Sélectionner une variable x_p non affectée
    NA= getNonAffecte(a)
    #3. Pour chaque valeur v_pi de D_p faire:
    for v in d[NA]:
        #- Ajouter x_p <- v_pi dans A
        a[NA]= v
        print("Etape "+str(d["etape"])+". AV "+state(a))
        d["etape"]= d["etape"]+1
        #- D <- FORWARD_CHECKING(A,D)
        d= FORWARD_CHECKING(a,d)
        #- si aucun domaine de D n'est vide:
        if not estVide(d):
            #- Retourner PSC_BACKTRACKING(A,D)
            return PSC_BACKTRACKING(a,d)
        #- sinon:
        else:
            #- Retourner échec
            return "Echec!"


