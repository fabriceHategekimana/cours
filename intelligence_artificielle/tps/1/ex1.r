#exercice 1

teste<-function(etat){
	res= TRUE
	#la fonction doit voir s'il n'y a aucun chiffre négatif (qu'on a enlevé des personnes en trop)
	i=1
       while(i <= 4){
	       if(etat[i] < 0){
		  res= FALSE
	       }
		i= i+1	       
       }	       
	#La fonction doit vérifier qu'il n'y ait pas plus de cannibal que de missionnaire
       if((etat[1] > 0 & etat[2] > etat[1]) | (etat[3] > 0 & etat[4] > etat[3])){
		res= FALSE
       }
       res
}

#--------------
#INITIALISATION
#--------------

#la matrice des transitions possibles
a= c(c(-2,0,2,0),c(0,-2,0,2),c(-1,-1,1,1),c(-1,0,1,0),c(0,-1,0,1))
transitions= matrix(a, byrow=TRUE, ncol=4)

#chemin qui représente la série de noeud qui amènera à la solution
chemin= c(3,3,0,0)

#compteur qui sera attribué à chaque noeuds de la recheche
compteurs= c(1)

#compte le nombre de ligne de la matrice
ligne= dim(transitions)[1]

#gère les mouvements pour faire l'allez et le retour de la barque
allezretour= c(1)

arrivee= c(3,0,0,3)

#-------------
#DÉBUT DU CODE
#------------

recherche= TRUE
while(recherche == TRUE){
	#on affiche la situation
	print("compteur")
	print(compteurs)
	#On prend le dernier noeud enregistré (le plus à droite)
	etatActuel= chemin[(length(chemin)-3):length(chemin)]
	#on prend le dernier compteur enregistré	
	iActuel= compteurs[length(compteurs)]		
	mouvementActuel= allezretour[length(allezretour)]

	#on teste d'abords qu'on est pas au bout de toutes les transitions
	if(iActuel > 5){
		#Si on a tout vu, on backtrack
		chemin= chemin[1:(length(chemin)-4)]	
		compteurs= compteurs[1:(length(compteurs)-1)]
		allezretour= allezretour[1:(length(allezretour)-1)]
		if(length(compteurs) == 0){
			recherche= FALSE
		}
	} else{
		# si on est pas au bout, on continue
		#on prend la prochaine transition
		#print("état actuel")
		#print(etatActuel)
		#print("mouvement actuel")
		#print(mouvementActuel)
		nouvelleTransition= transitions[iActuel,]
		#print("Nouvelle transition:")
		#print(nouvelleTransition)
		nouvelEtat= etatActuel+(nouvelleTransition*mouvementActuel)
		#print("Nouvel état:")
		#print(nouvelEtat)
		#on teste le nouvel état
		if(teste(nouvelEtat)){
			print("état valide")
			#si le teste est positif on enregistre
			chemin= c(chemin, nouvelEtat)
			compteurs= c(compteurs,1)
			mouvementActuel= mouvementActuel-(2*mouvementActuel)
			allezretour= c(allezretour, mouvementActuel)
			if(all(nouvelEtat==arrivee)){
				recherche= FALSE
			}
		} else{
			print("état non validé")
			#si le teste est négatif on passe à la transition suivante
			compteurs[length(compteurs)]= iActuel+1
			print("compteur")
			print(compteurs)
		}
	}
	#On change l'orientation (0 = allez) (le plus à droite)
}
#On affiche le résultat
print(chemin)
print(compteurs)
print(allezretour)

