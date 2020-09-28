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

estDans<-function(vect, mat){
	if(length(mat) == 0){
		res=FALSE
	} else{
		res=FALSE
		i= 1
		while(i<=dim(mat)[1]){
			#on prend la ligne
			ligne= mat[i,]
			#on teste si c'est pareil
			if(all(vect == ligne)){
				res=TRUE
			}
			i= i+1
		}
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
chemin= matrix(c(3,3,0,0), byrow=TRUE, ncol=4)

#compteur qui sera attribué à chaque noeuds de la recheche
compteurs= c(1)

#compte le nombre de ligne de la matrice
ligne= dim(transitions)[1]

#gère les mouvements pour faire l'allez et le retour de la barque
allezretour= c(1)

arrivee= c(0,0,3,3)

dejaExplore= matrix(c(c(3,3,0,0),c(1)), byrow=TRUE, ncol=4)

#-------------
#DÉBUT DU CODE
#------------

recherche= TRUE
etape= 1
while(recherche == TRUE){
	print("")
	print("------------------------------")
	print("")
	print(etape)
	print("etat début")
	print(chemin)
	#on prend le dernier compteur enregistré	
	iActuel= compteurs[length(compteurs)]		
	iAncien= compteurs[length(compteurs)-1]		
	#On prend le dernier noeud enregistré
	if(length(chemin) == 4){
		etatActuel= chemin
	} else{
		etatActuel= chemin[dim(chemin)[1],]
	}
	mouvementActuel= allezretour[length(allezretour)]
	#on teste d'abords qu'on est pas au bout de toutes les transitions
	if(iActuel > 5){
		#Si on a tout vu, on backtrack
		if(length(chemin) > 4){
			chemin= chemin[1:(dim(chemin)[1]-1),]	
			compteurs= compteurs[1:(length(compteurs)-1)]
			allezretour= allezretour[1:(length(allezretour)-1)]
		}
		else{
			recherche=FALSE
		}
	} else{
		# si on est pas au bout, on continue
		#on prend la prochaine transition
		nouvelleTransition= transitions[iActuel,]
		print("nouvelle transition")
		print(nouvelleTransition)
		ancienneTransition= transitions[iAncien,]
		print("ancienne transition")
		print(ancienneTransition)
		if(sum(nouvelleTransition-ancienneTransition) == 0){
			#si la transition est le mouvement inverse du mouvement précédent on annule
			print("On entre ici")
			compteurs[length(compteurs)]= iActuel+1
		} else{
			nouvelEtat= etatActuel+(nouvelleTransition*mouvementActuel)
			print("nouvelEtat")
			print(nouvelEtat)
			#on teste le nouvel état
			if(teste(nouvelEtat)){
				print("nouvel état accepté")
				mouvementActuel= mouvementActuel-(2*mouvementActuel)
				#si le teste est positif on teste
				if(estDans(c(nouvelEtat, mouvementActuel), dejaExplore)){
					print("nouvel état déjà exploré")
					#si le noeud a déja été exploré, on cherche ailleurs
					compteurs[length(compteurs)]= iActuel+1
				} else{
					print("nouvel état pas déjà exploré")
					#Si le noeud n'a pas encore été exploré, on l'enregistre
					chemin= rbind(chemin, nouvelEtat)
					compteurs= c(compteurs,1)
					allezretour= c(allezretour, mouvementActuel)
					dejaExplore= rbind(dejaExplore, c(nouvelEtat,mouvementActuel))
					#Si on est arrivé sur l'etat désiré
					if(all(nouvelEtat==arrivee)){
						recherche= FALSE
					}
				}
			} else{
				print("nouvel état pas accepté")
				#si le teste est négatif on passe à la transition suivante
				compteurs[length(compteurs)]= iActuel+1
			}
		}
	}
	etape= etape+1
	#if(etape == 50){
		#recherche= FALSE
	#}
}
#On affiche le résultat
#print(chemin)


