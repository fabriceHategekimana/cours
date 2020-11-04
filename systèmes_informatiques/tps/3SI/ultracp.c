#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<time.h>
#include<unistd.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<fcntl.h>
#include<errno.h>
#include<dirent.h>
#include"display.h"
#include"copy.h"

int estRepertoire(char *chemin){
	//Teste si l'élément en question est un répertoire (=dossier)
	int res;
	struct stat buff;
	if(stat(chemin, &buff) == -1){
		perror("lstat");
	}
	if(S_ISDIR(buff.st_mode)){
		res= 1;
	}
	else{
		res= 0;
	}
	return res;
}


int main(int argc, char *argv[]){
	//on choisit le dernier élément des entrées pour faire les testes
	char *destination= argv[argc-1];

	//si on a seulement une entrée on fait un listing de son contenu
	if(argc == 2){
		//listing répertoire
		if(estRepertoire(argv[1])){
			RecursiveDisplay(argv[1]);
		}//listing fichier
		else{
			displayStat(argv[1]);
		}
	}
	// si on a deux entrées (=fichiers) alors on copie le contenu de l'un dans l'autre
	else if(argc == 3 && estRepertoire(argv[2]) == 0){
			remplacer(argv[1], argv[2]);
	}
	//si si on a n entrées (>1) et que la destination est un répertoire on copie tout dant le répertoire
	else if(estRepertoire(destination)){
		printf(" ");
		for(int i= 1; i < argc-1; i++){
			char newFile[100]="";
			strcat(newFile, destination);
			strcat(newFile, "/");
			strcat(newFile, argv[i]);
			if(estRepertoire(argv[i])){
				createDir(newFile);
				RecursiveCopy(argv[i], newFile);
			}
			else{
				printf(" ");
				copy(argv[i], newFile);
			}
		}
	}
	//sinon c'est une erreur d'écriture de l'utilisateur
	else{
		printf("Erreur, mauvaise syntaxe");
	}
	
	return 0;
}


