#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include "options.h"
#include "hash.h"

int option(int argc, char *argv[], int *index, char *fonctionDeHashage){
   int estFichier= 0;
   fonctionDeHashage= "SHA1";
   int option;
   while((option = getopt(argc, argv, ":ft:")) != -1){ //get option from the getopt() method
      switch(option){
         case 'f':
            estFichier= 1;
            break;
         case 't': 
            optarg;
            break;
         case '?': 
            printf("unknown option: %c\n", optopt);
            break;
      }
   }
   index= &optind;
   return estFichier;
}

int main(int argc, char *argv[]){
	int index;
	char *fonctionDeHashage;
	int estFichier= option(argc, argv, &index, fonctionDeHashage);
	if(estFichier == 0){
		printf("N'est pas un fichier");
	}
	else{
		printf("Est un fichier");
	}
	return 0;
}

//appelle de options:
//estfichier= options(argc, argv, &index, &fonctiondehashage)
//Segement pour le hashage
//si fichier
//	pour chaque fichier:
//		ouvrir()
//		prendre le contenu
//		hasher le contenu
//		afficher le hashage
//sinon
//	pour chaque élément
//		string= string+élément
//	hasher le string
//	afficher le hashage
//
