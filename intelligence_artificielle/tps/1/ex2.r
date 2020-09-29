#exercice 2
#définition d'une pile
pile=c(1:3)

#définition des fonctions d'une pile
#push
push<-function(){

}
#pop
#peak



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
       #la fonction doit contrôler que l'état n'ai pas déjà été exploré
       res
}

#Algorithme
 #on teste les état
	
