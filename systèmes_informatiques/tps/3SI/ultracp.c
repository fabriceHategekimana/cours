
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<time.h>
#include<unistd.h>
#include<sys/stat.h>
#include<sys/types.h>
#include <fcntl.h>
#include <errno.h>

int DROIT_PROP= 2;
int DROIT_GROU= 3;
int DROIT_AUTR= 4;

void getRWX(unsigned short droit){	
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

#include <dirent.h>
void RecursiveFunc(char *entry)
{
	struct dirent *dirbase;
	DIR *dir = opendir(entry);
	while ((dirbase = readdir(dir)) != NULL){
		char newDirbase[256]="";
		strcat(newDirbase, entry);
		strcat(newDirbase, "/");
		strcat(newDirbase, dirbase->d_name);
		//printf(" %s \n", newDirbase);
		displayStat(newDirbase);
		if(dirbase->d_type == DT_DIR && strcmp(dirbase->d_name, ".") != 0 && strcmp(dirbase->d_name, "..") != 0){
			RecursiveFunc(newDirbase);
		}
	}
}

int remplacer(char *source_file, char *target_file){

   FILE *source, *target;
   source = fopen(source_file, "r");

   if (source == NULL)
   {
      printf("Press any key to exit...\n");
      exit(EXIT_FAILURE);
   }

   target = fopen(target_file, "w");

   if (target == NULL)
   {
      fclose(source);
      printf("Press any key to exit...\n");
      exit(EXIT_FAILURE);
   }

   int ch;
   while ((ch = fgetc(source)) != EOF)
      fputc(ch, target);

   fclose(source);
   fclose(target);
}

int estRepertoire(char *chemin){
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

int copy(const char *from, const char *to)
{
    int fd_to, fd_from;
    char buf[4096];
    ssize_t nread;
    int saved_errno;

    fd_from = open(from, O_RDONLY);
    if (fd_from < 0)
        return -1;

    fd_to = open(to, O_WRONLY | O_CREAT | O_EXCL, 0666);
    if (fd_to < 0)
        goto out_error;

    while (nread = read(fd_from, buf, sizeof buf), nread > 0)
    {
        char *out_ptr = buf;
        ssize_t nwritten;

        do {
            nwritten = write(fd_to, out_ptr, nread);

            if (nwritten >= 0)
            {
                nread -= nwritten;
                out_ptr += nwritten;
            }
            else if (errno != EINTR)
            {
                goto out_error;
            }
        } while (nread > 0);
    }

    if (nread == 0)
    {
        if (close(fd_to) < 0)
        {
            fd_to = -1;
            goto out_error;
        }
        close(fd_from);

        /* Success! */
        return 0;
    }

  out_error:
    saved_errno = errno;

    close(fd_from);
    if (fd_to >= 0)
        close(fd_to);

    errno = saved_errno;
    return -1;
}

int main(int argc, char *argv[]){
	char *rootFolder= "";
	char *destination= argv[argc-1];

	//RecursiveFunc(rootFolder);
	//si une entrée
	if(argc == 2 && estRepertoire(argv[1])){
		//displayStat(argv[1]);
		RecursiveFunc(argv[1]);
	}
	// si un seul reste et fichier
	else if(argc == 3 && estRepertoire(argv[2]) == 0){
			remplacer(argv[1], argv[2]);
	}
	//si destination est répertoire
	else if(estRepertoire(destination)){
		for(int i= 1; i < argc-1; i++){
			char newFile[100]="";
			strcat(newFile, destination);
			strcat(newFile, "/");
			strcat(newFile, argv[i]);
			copy(argv[i], newFile);
		}
	}
	//sinon c'est une erreur d'écriture de l'utilisateur
	else{
		printf("Erreur, mauvaise syntaxe");
	}
	
	return 0;
}


