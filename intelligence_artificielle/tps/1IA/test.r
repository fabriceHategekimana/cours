

pop<-function(matrice, num){
	matrice[,1] = matrice[,1]%*%pop
	return(matrice)
}



a= c(1,2,3)
b= c(4,5,6)
c= c(7,8,9)

m= matrix(c(a,b,c), byrow=TRUE, ncol=3)
n= matrix(c(a,b,b), byrow=TRUE, ncol=3)
pop= matrix(c(0,0,0,1,0,0,0,1,0), byrow=TRUE, ncol=3)

l= list(m)
l= c(l, list(n))

print(l[[1]][3,])
