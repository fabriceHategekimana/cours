#exercice 2

#-----------------------------------
#DÉFINITION DES FONCTIONS D'UNE PILE
#-----------------------------------
#pop
pop<-function(pile){
	#on prend la matrice qui va faire le pop
	m= matrix(c(0,0,0,1,0,0,0,1,0), byrow=TRUE, ncol=3)
	#on prend le sommet
	sommet= pile[1]
	#on prend le reste
	reste= c(pile%*%m)
	
	return(list(sommet, reste))
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
getStack<-function(hanoi, nom){
	#on récupère le vecteur de la colonne qui nous intéresse
	vect= unlist(hanoi[nom], use.name=FALSE)
	return(vect)
}

putStack<-function(hanoi, nom, pile){
	hanoi[nom]= pile
	return(hanoi)
}


#--------------------------------------------
#Définition des fonction pour les transitions
#--------------------------------------------

transition<-function(hanoi, depart, arrivee){
	d= getStack(hanoi, depart)
	a= getStack(hanoi, arrivee)
	
	sr= pop(d)

	sommet= unlist(sr[1], use.name=FALSE)
	reste= unlist(sr[2], use.name=FALSE)

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

	if(g[1] > g[2] | m[1] > m[2] | d[1] > d[2]){ 
		res= FALSE	
	}
	
	return(res)
}

tour= data.frame(gauche= c(1:3), milieu= c(0), droite= c(0))

print(teste(tour))
