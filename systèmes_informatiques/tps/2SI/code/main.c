#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<string.h>
#include "options.h"
#include "hash.h"

int concatAll(int index, int argc, char *argv[], char *fonctionDeHashage){
	char message[255];
	for(; index < argc; index++){
		strcat(message, argv[index]);
		strcat(message, " ");
	}
	hashage(message, fonctionDeHashage);
	printf("\n");
}

int main(int argc, char *argv[]){
	int index;
	char *fonctionDeHashage;
	// on fait appelle au module options pour savoir quoi faire
	int estFichier= option(argc, argv, &index, fonctionDeHashage);
	if(estFichier){
		//pour chaque fichiers
		for(; index < argc; index++){
			hasher(argv[index], fonctionDeHashage);
		}
	}
	else{
		//on compte le nombre de caractère des entrées plus les espaces
		concatAll(index, argc, argv, fonctionDeHashage);
	}
	return 0;
}

