#exercice 1

teste<-function(etat){
	res= TRUE
	#1ER TESTE
	#la fonction doit voir s'il n'y a aucun chiffre négatif (qu'on a enlevé des personnes en trop)
	i=1
       while(i <= 4){
	       if(etat[i] < 0){
		  res= FALSE
	       }
		i= i+1	       
       }	       
       #2E TESTE
	#La fonction doit vérifier qu'il n'y ait pas plus de cannibal que de missionnaire
       if((etat[1] > 0 & etat[2] > etat[1]) | (etat[3] > 0 & etat[4] > etat[3])){
		res= FALSE
       }
       #3E TESTE
       #la fonction doit contrôler que l'etat n'ai pas déjà été exploré
       res
}

pasExplore<-function(vect, mat){
	if(length(mat) == 0){
		res=TRUE
	} else{
		res=TRUE
		i= 1
		while(i<=dim(mat)[1]){
			#on prend la ligne
			ligne= mat[i,]
			#on teste si c'est pareil
			if(all(vect == ligne)){
				res=FALSE
			}
			i= i+1
		}
	}
	res
}

getTransition<-function(numero){
	if(numero <= 5 & numero > 0){
		a= c(c(-2,0,2,0),c(0,-2,0,2),c(-1,-1,1,1),c(-1,0,1,0),c(0,-1,0,1))
		transitions= matrix(a, byrow=TRUE, ncol=4)
		transitions[numero,]
	}
	else{
		-1
	}
}

#Cette fonction est là pour éviter qu'on revienne à l'état précédent avec une transition contraire
pasContraire<-function(nouvelleTransition, historiqueDeTransition,tableauDeTransition){
	#On retrouve la précédente transition
	numeroDeTransition= historiqueDeTransition[length(historiqueDeTransition)-1]	
	ancienneTransition= getTransition(numeroDeTransition)
	#on teste si les transitions sont des opposés
	if(sum(nouvelleTransition-ancienneTransition) == 0){
		#les transitions sont bien contraire et donc pas "pas contraire"
		FALSE
	} else{
		#les transitions sont bien "pas contraire"
		TRUE
	}
}

#--------------
#INITIALISATION
#--------------

#la matrice des transitions possibles
#a= c(c(-2,0,2,0),c(0,-2,0,2),c(-1,-1,1,1),c(-1,0,1,0),c(0,-1,0,1))
#transitions= matrix(a, byrow=TRUE, ncol=4)

#chemin qui représente la série de noeud qui amènera à la solution
chemin= matrix(c(3,3,0,0), byrow=TRUE, ncol=4)

#compteur qui sera attribué à chaque noeuds de la recheche
compteurs= c(1)

#gère les mouvements pour faire l'allez et le retour de la barque
allezretour= c(1)

arrivee= c(0,0,3,3)

dejaExplore= matrix(c(c(3,3,0,0),c(1)), byrow=TRUE, ncol=5)


#-------------
#DÉBUT DU CODE
#------------

recherche= TRUE
etape= 1
while(recherche == TRUE){
	#on sélection le dernier noeud
	if(length(chemin) == 4){
		etatActuel= chemin
		iAncien=0
	} else{
		etatActuel= chemin[dim(chemin)[1],]
		iAncien= compteurs[length(compteurs)-1]		
	}
	#on sélectionne la prochaine transition
	iActuel= compteurs[length(compteurs)]		
	nouvelleTransition= getTransition(iActuel)
	sens= allezretour[length(allezretour)]
	#on obtient le prochain état
	nouvelEtat= etatActuel+(nouvelleTransition*sens)
	sens= sens-(2*sens)
	#on fait des testes (valide, pas encore exploré, pas de sense contraire)
	if(teste(nouvelEtat) & pasExplore(c(nouvelEtat,sens), dejaExplore) & iActuel != iAncien){
		#s'il est valide, on enregistre
		chemin= rbind(chemin, nouvelEtat)
		compteurs= c(compteurs,1)
		allezretour= c(allezretour, sens)
		dejaExplore= rbind(dejaExplore, c(nouvelEtat,sens))
	} else{
		#sinon, on passe au suivant
		compteurs[length(compteurs)]= iActuel+1
	}
	if(all(nouvelEtat == arrivee)){
		recherche= FALSE
	}
}
#On affiche le résultat
print("CHEMIN")
print(chemin)
print("")
print("----------------------------------------------------------------")
print("TRANSITIONS")
print(getTransition(compteurs))
