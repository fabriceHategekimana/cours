#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<string.h>
#include "options.h"
#include "hash.h"

int main(int argc, char *argv[]){
	int index;
	char *fonctionDeHashage;
	int estFichier= option(argc, argv, &index, fonctionDeHashage);
	printf("fonction de hashage: %s", fonctionDeHashage);
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
