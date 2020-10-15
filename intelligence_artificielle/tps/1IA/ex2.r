#exercice 2

#-----------------------------------
#DÉFINITION DES FONCTIONS D'UNE PILE
#-----------------------------------
#pop
popReste<-function(pile){
	#on prend la matrice qui va faire le pop
	m= matrix(c(0,0,0,1,0,0,0,1,0), byrow=TRUE, ncol=3)
	#on prend le reste
	reste= c(pile%*%m)
	
	return(reste)
}

popSommet<-function(pile){
	#on prend la matrice qui va faire le pop
	m= matrix(c(0,0,0,1,0,0,0,1,0), byrow=TRUE, ncol=3)
	#on prend le sommet
	sommet= pile[1]
	
	return(sommet)
}

#push
push<-function(pile, nombre){
	#on prend la matrice qui va faire le décalage pour le push
	m= matrix(c(0,1,0,0,0,1,0,0,0), byrow=TRUE, ncol=3)
	#on décale
	pile= c(pile%*%m)
	nombre= c(nombre,0,0)	
	pile= pile+nombre
	return(pile)
}

#peak
peak<-function(pile){
	#on prend l'élément le plus au dessus
	return(pile[1])	
}


#---------------------------------------------
#DÉFINITION DES FONCTION POUR LA TOUR DE HANOÏ
#---------------------------------------------
getNum<-function(nom){
	res= 0
	if(nom == "gauche"){
		res= 1	
	} else if(nom == "milieu"){
		res= 2
	}else if(nom == "droite"){
		res= 3
	}
	return(res)
}

getStack<-function(hanoi, nom){
	#on récupère le vecteur de la colonne qui nous intéresse
	num= getNum(nom)
	vect= hanoi[,num]
	return(vect)
}

putStack<-function(hanoi, nom, pile){
	num= getNum(nom)
	hanoi[,num]= pile
	return(hanoi)
}


#--------------------------------------------
#Définition des fonction pour les transitions
#--------------------------------------------

transition<-function(hanoi, depart, arrivee){
	d= getStack(hanoi, depart)
	a= getStack(hanoi, arrivee)

	sommet= popSommet(d)
	reste= popReste(d)

	a= push(a,sommet)

	hanoi= putStack(hanoi,depart,reste)
	hanoi= putStack(hanoi,arrivee,a)

	return(hanoi)
}

getTransition<-function(numero){
	a= c(c("gauche","milieu"),c("gauche","droite"),c("milieu","gauche"),c("milieu","droite"),c("droite","gauche"),c("droite","milieu"))
	ma= matrix(a, byrow=TRUE, ncol=2)
	return(ma[numero,])	
}

#-------------------------------
#DÉFINITION DE LA FONCTION TESTE
#-------------------------------

teste<-function(hanoi){
	res= TRUE

	g= getStack(hanoi, "gauche")
	m= getStack(hanoi, "milieu")
	d= getStack(hanoi, "droite")

	if(((g[1] > g[2]) & (g[2] > 0)) | ((m[1] > m[2]) & (m[2] > 0)) | ((d[1] > d[2]) & (d[2] > 0)) | (g[1] == 0 & g[2] > 0) | (m[1] == 0 & m[2] > 0) | (d[1] == 0 & d[2] > 0)){ 
		res= FALSE	
	}
	
	return(res)
}


append<-function(chemin, tour){
	chemin= c(chemin, list(tour))
	return(chemin)
}

sontContraire<-function(iAncien, iActuel){
	res= FALSE
	if(iAncien > 0){
		tAncien= getTransition(iAncien)
		tActuel= getTransition(iActuel)
		tActuel= rev(tActuel)
		if(all(tAncien == tActuel)){
			res= TRUE
		}
	}
	return(res)
}

toVector<-function(matrice){
	return((as.vector(t(matrice))))
}

toMatrix<-function(vecteur){
	m= matrix(vecteur, byrow=TRUE, ncol=3)
	return(m)
}

compare<-function(m1, m2){
	res= FALSE
	if(all(toVector(m1) == toVector(m2))){
		res= TRUE
	}
	return(res)
}

dejaExplore<-function(explore, nouvelEtat){
	res= FALSE
	l= length(explore)	
	i= 2
	while(i <= l){
		if(compare(nouvelEtat, explore[[i]])){
			res= TRUE	
			i= l+1
		}
		i= i+1
	}
	return(res)
}

mouvementForce<-function(tour, mouvement){
	gauche= getStack(tour, "gauche")	
	milieu= getStack(tour, "milieu")	
	droite= getStack(tour, "droite")	

	if(all(gauche == c(3,0,0)) & all(droite == c(0,0,0))){
		res= c("gauche", "droite")
	} else if(all(milieu == c(3,0,0)) & all(droite == c(0,0,0))){
		res= c("milieu", "droite")
	} else if(all(gauche == c(2,0,0)) & all(droite == c(3,0,0))){
		res= c("gauche", "droite")
	} else if(all(milieu == c(2,0,0)) & all(droite == c(3,0,0))){
		res= c("milieu", "droite")
	} else if(all(gauche == c(1,0,0)) & all(droite == c(2,3,0))){
		res= c("gauche", "droite")
	} else if(all(milieu == c(1,0,0)) & all(droite == c(2,3,0))){
		res= c("milieu", "droite")
	} else{
		res= mouvement
	}
	return(res)
}

#-------------
#DÉBUT DU CODE
#-------------

#définition de la tour de Hanoï
tour= matrix(c(1,0,0,2,0,0,3,0,0), byrow=TRUE, ncol=3)

#définition du chemin et du compteur de transition
chemin= list()
chemin= append(chemin, tour)

compteurs= c(1)

#définition de l'état qu'on cherche
arrivee= matrix(c(0,0,1,0,0,2,0,0,3), byrow=TRUE, ncol=3)

#définition du chemin d'exploration
explore= list()
explore= append(explore, tour)

etape= 1
recherche= TRUE
#variable qui contrôle les prints
verbose= FALSE
while(recherche == TRUE){
	#on sélection le dernier noeud
	if(verbose){
		print("")
		print("------------------------------")
		print(etape)
	}
	etatActuel= chemin[[length(chemin)]]
	if(verbose){
		print("départ")
		print(etatActuel)
	}
	if(length(compteurs) == 1){
		iAncien= 0
	} else{
		iAncien= compteurs[length(compteurs)-1]		
	}
	#on sélectionne la prochaine transition
	iActuel= compteurs[length(compteurs)]		
	nouvelleTransition= getTransition(iActuel)
	#nouvelleTransition= mouvementForce(etatActuel, nouvelleTransition)
	if(verbose){
		print("nouvelle transition")
		print(nouvelleTransition)
	}
	#on obtient le prochain état
	nouvelEtat= transition(etatActuel, nouvelleTransition[1], nouvelleTransition[2])
	if(verbose){
		print("nouvel état")
		print(nouvelEtat)
	}
	##on fait des testes (valide, pas encore exploré, pas de sense contraire)
	if(teste(nouvelEtat) & ! dejaExplore(explore, nouvelEtat) & ! sontContraire(iAncien, iActuel)){
		#s'il est valide, on enregistre
		if(verbose){
			print("accepté")
		}
		chemin= append(chemin, nouvelEtat)
		explore= append(explore, nouvelEtat)
		compteurs= c(compteurs,1)
	} else{
		if(verbose){
			print("refusé")
		}
		#sinon, on passe au suivant
		if(iActuel+1 > 6){
			#si on a fait toutes les transitions on backtrack
			chemin= chemin[1:length(chemin)-1]		
			compteurs= compteurs[1:length(compteurs)-1]		
		} else{
			#sinon on passe à la transition suivante
			compteurs[length(compteurs)]= iActuel+1
		}
	}
	etape= etape+1
	if(compare(nouvelEtat, arrivee) | etape == 100){
		print("on s'arrête")
		recherche= FALSE
	}
}

print(chemin)

