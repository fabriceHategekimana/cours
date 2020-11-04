#include<stdio.h>
#include<string.h>
#include<time.h>
#include<sys/stat.h>
#include<dirent.h>
#include"display.h"

//Permet de décalage de bits pour le droits (propriétaire, group, autre)
int DROIT_PROP= 2;
int DROIT_GROU= 3;
int DROIT_AUTR= 4;

void getRWX(unsigned short droit){	
	//Petite fonction qui permet d'afficher les droits en rwx
	char c[4];
	switch(droit){ 
		case 0:
		strcpy(c, "---");
		break;
		case 1:
		strcpy(c, "--x");
		break;

		case 2:
		strcpy(c, "-w-");
		break;

		case 3:
		strcpy(c, "-wx");
		break;

		case 4:
		strcpy(c, "r--");
		break;

		case 5:
		strcpy(c, "r-x");
		break;

		case 6:
		strcpy(c, "rw-");
		break;

		case 7:
		strcpy(c, "rwx");
		break;
	}
	printf("%s", c);
}

int droits(unsigned short mode){
	//détermine les droits selon le propriétaire, le groupe ou autre
	//permission du propriétaire
	unsigned short droit= mode << (3*DROIT_PROP);
	droit= droit >> 12;
	getRWX(droit);
		
	//permission du groupe
	droit= mode << (3*DROIT_GROU);
	droit= droit >> 12;
	getRWX(droit);

	//permission des autres
	droit= mode << (3*DROIT_AUTR);
	droit= droit >> 12;
	getRWX(droit);
}

int displayStat(char *element){
	//Fonctions d'affichage qui affiche les stats d'un fichier donné
	struct stat buff;
	if(stat(element, &buff) == -1){
		perror("lstat");
	}
	else{ 
		//type
		if(S_ISDIR(buff.st_mode)){
			printf("d");
		}
		else{
			printf("-");
		}
		//droits
		droits(buff.st_mode);

		//espace/tabulation
		printf("	");

		//taille (octet)
		printf("%8ld", buff.st_size);

		//date de modification (strftime) j'ai dû tricher pour éviter les saut de ligne 
		//(au charactère 25)
		char txt[25];
		strcpy(txt, ctime(&buff.st_mtime));
		for(int i= 0; i < 24; i++){
 			printf("%c", txt[i]);
		}
		//nom relatif du fichier (concat $1)
		printf(" %s\n", element);
	}

}

void RecursiveDisplay(char *entry)
{
	//Fonction qui affiche de façon récursive le contenu d'un dossier
	struct dirent *dirbase;
	DIR *dir = opendir(entry);
	//Pour tout élément du dossier
	while ((dirbase = readdir(dir)) != NULL){
		//On prérare son chemin
		char newDirbase[256]="";
		strcat(newDirbase, entry);
		strcat(newDirbase, "/");
		strcat(newDirbase, dirbase->d_name);
		//On l'affiche
		displayStat(newDirbase);
		//Si cet élément est un dossier (autre que "." et "..")
		if(dirbase->d_type == DT_DIR && strcmp(dirbase->d_name, ".") != 0 && strcmp(dirbase->d_name, "..") != 0){
			//on applique à nouveau la récursivité
			RecursiveDisplay(newDirbase);
		}
	}
}
