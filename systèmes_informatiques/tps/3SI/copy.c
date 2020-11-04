#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<errno.h>
#include<dirent.h>
#include"copy.h"

int createDir(char *folder){
	struct stat st = {0};
	//Crée un dossier s'il n'existe pas
	if(stat(folder, &st) == -1){
		mkdir(folder, 0700);
	}

}	

int copy(const char *from, const char *to)
{
    //Copie un fichier d'une position à une autre
    int fd_to, fd_from;
    char buf[4096];
    ssize_t nread;
    int saved_errno;
	
    //Ouverture du fichier de départ
    fd_from = open(from, O_RDONLY);
    if (fd_from < 0){ 
	printf("Erreur: le fichier de départ %s est inexistant!\n", from);
	return -1;
    }
    //Ouverture du fichier d'arrivé (créé si inexistant)
    fd_to = open(to, O_WRONLY | O_CREAT | O_EXCL, 0666);
    if (fd_to < 0){ 
	return -1;
    }
    //copy du contenu (fichier de départ -> fichier d'arrivé)
    while (nread = read(fd_from, buf, sizeof buf), nread > 0)
    {
        char *out_ptr = buf;
        ssize_t nwritten;
	//boucle d'écriture
        do {
	   //on écrit dans le fichier d'arrivé
            nwritten = write(fd_to, out_ptr, nread);
	   
	    //on contrôle que l'écriture s'est bien faite
            if (nwritten >= 0)
            {
                nread -= nwritten;
                out_ptr += nwritten;
            }
            else if (errno != EINTR)
            {
		printf("Erreur: Un soucis c'est produit dans la copie de %s à %s!\n", from, to);
		exit(EXIT_FAILURE);
            }
        } while (nread > 0);
    }
    //On ferme quand la copie est terminée
    if (nread == 0)
    {
        if (close(fd_to) < 0)
        {
            fd_to = -1;
		printf("Erreur: Un soucis c'est produit dans la fermeture du fichier %s !\n", to);
		exit(EXIT_FAILURE);
        }
        close(fd_from);

        return 0;
    }
}

void RecursiveCopy(char *entry, char *folder)
{
	//copie de façon récursive le contenu d'un dossier dans un autre
	struct dirent *dirbase;
	DIR *dir = opendir(entry);
	while ((dirbase = readdir(dir)) != NULL){

		//On ajoute le nom au point de départ
		char newDirbase[256]="";
		strcat(newDirbase, entry);
		strcat(newDirbase, "/");
		strcat(newDirbase, dirbase->d_name);

		//On ajoute le nom au point d'arrivé
		char newFolderBase[500]="";
		strcat(newFolderBase, folder);
		strcat(newFolderBase, "/");
		strcat(newFolderBase, dirbase->d_name);
		//si c'est un dossier
		if(dirbase->d_type == DT_DIR && strcmp(dirbase->d_name, ".") != 0 && strcmp(dirbase->d_name, "..") != 0){
			createDir(newFolderBase);
			RecursiveCopy(newDirbase, newFolderBase);
		}// sinon
		else if(strcmp(dirbase->d_name, ".") != 0 && strcmp(dirbase->d_name, "..")){
			copy(newDirbase, newFolderBase);

		}
	}
}

int remplacer(char *source_file, char *target_file){
   //On remplace le contenu d'un fichier dans un autre
   FILE *source, *target;
   source = fopen(source_file, "r");
   //on vérifie que le ficheir de départ  existe
   if (source == NULL)
   {
      printf("Press any key to exit...\n");
      exit(EXIT_FAILURE);
   }

   target = fopen(target_file, "w");

   //on vérifie que le fichier d'arrivé existe
   if (target == NULL)
   {
      fclose(source);
      printf("Press any key to exit...\n");
      exit(EXIT_FAILURE);
   }

   //On copie le tout
   int ch;
   while ((ch = fgetc(source)) != EOF)
      fputc(ch, target);

   //on ferme
   fclose(source);
   fclose(target);
}
