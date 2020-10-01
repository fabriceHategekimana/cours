
toVector<-function(matrice){
	return((as.vector(t(matrice))))
}

toMatrix<-function(vecteur){
	m= matrix(vecteur, byrow=TRUE, ncol=3)
	return(m)
}

pop<-function(matrice, num){
	matrice[,1] = matrice[,1]%*%pop
	return(matrice)
}

compare<-function(m1, m2){
	res= FALSE
	dist= sum(toVector(m1)-toVector(m2))
	print(dist)
	if(dist == 0){
		res= TRUE
	}
	return(res)
}

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

a= c(1,2,3)
b= c(4,5,6)
c= c(7,8,9)

m= matrix(c(a,b,c), byrow=TRUE, ncol=3)
n= matrix(c(a,b,b), byrow=TRUE, ncol=3)
pop= matrix(c(0,0,0,1,0,0,0,1,0), byrow=TRUE, ncol=3)

l= list()
l[1]= [m]

print(l)
