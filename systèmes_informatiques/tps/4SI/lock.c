#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <sys/file.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <ctype.h>
#include <sys/types.h>

//Variable globale (pour afficher les détails des entrées)
int VERBOSE= 0;

//-------------------------------------------------------------
//FONCTIONS DE 3E-4E DEGRÉ (APPELÉS PAR LES FONCTIONS DE 2E DEGRÉ)
//-------------------------------------------------------------
//charToString(), getType(), hasLetter(), createLock(), help()
int charToString(char element, char *buffer){//transforme un caractère en string
	buffer[0]= element;
}

int hasLetter(char *element){ //test si une chaine de caractère à des éléments autre que des chiffres
	int res= 0;
	int l= strlen(element);
	for(int i= 0; i < l; i++){
		//si on trouve des éléments différent de 0 1 2 3 4 5 6 7 8 9 on retourn vrai
		if(element[i] < 48 || element[i] > 57){
			res= 1;
			break;
		}
	}
	return res;
}

//permet de savoir si un l_type est en mode lecteur (=READ), écriture (=WRITE), ou unlock (=UNLOCK)
int getType(short l_type, char *buffer){
	if(l_type == F_RDLCK){
		strcpy(buffer, "READ");
	}
	else if(l_type == F_WRLCK){
		strcpy(buffer, "WRITE");
	}
	else if(l_type == F_UNLCK){
		strcpy(buffer, "UNLOCK");
	}
}

//crée un lock selon les paramètres entrés par l'utilisateur
int createLock(int fd, int newCmd, int newL_type, int newStart, int newLength, int newWhence){
	int res; //sert à voir le retour de F_SETLK

	//creation de la structure flock
	struct flock fl;
	fl.l_type= newL_type;
	fl.l_start= newStart;
	fl.l_len= newLength;
	fl.l_whence= newWhence;
	fl.l_pid= -1;
	
	//lancement de fcntl
	res= fcntl(fd, newCmd, &fl);
	pid_t pid = getpid();
	char type[10];

	//teste du retour de la fonction
	if(newCmd == F_GETLK){ //si on a utiliser F_GETLK
		if(fl.l_pid == -1){ //réussite
			printf("[PID=%d] there is free space\n", pid);	
		}
		else{ //échec
			getType(fl.l_type, type);
			printf("[PID=%d] Denied by %s on %ld/%ld (held by PID %d)\n", pid, type, fl.l_start, fl.l_len, fl.l_pid);
		}
	}
	else{ //si on a utilisé F_SETLK ou F_SETLKW
		if(res == -1){ //echec
			fcntl(fd, F_GETLK, &fl);
			getType(fl.l_type, type);
			printf("[PID=%d] Denied by %s on %ld/%ld (held by PID %d)\n", pid, type, fl.l_start, fl.l_len, fl.l_pid);
		}	
		else{ //réussite
			printf("[PID=%d] got lock\n", pid);	
		}
	}
}

int help(){ //affiche le menu d'aide
	printf("-----------------------------------------------------------------------------------\n");
	printf("Format : cmd l_type start length [ whence ( optional ) ]\n");
	printf("’ cmd ’ --- ’g ’ ( F_GETLK ) , ’s ’ ( F_SETLK ) , or ’w ’ ( F_SETLKW )\n");
	printf("’ l_type ’ --- ’r ’ ( F_RDLCK ) , ’w ’ ( F_WRLCK ) , or ’u ’ ( F_UNLCK )\n");
	printf("’ start ’ --- lock starting offset\n");
	printf("’ length ’ --- number of bytes to lock\n");
	printf("’ whence ’ --- ’s ’ ( SEEK_SET , default ) , ’c ’ ( SEEK_CUR ) , or ’e ’ ( SEEK_END )\n");
	printf("-----------------------------------------------------------------------------------\n");
}



//--------------------------------------------
//FONCTIONS DE 2E DEGRÉ (APPELÉ DANS LE MAIN)
//--------------------------------------------
//showPID(), myRead(), validate(), execute()
int showPID(){
	//on récupère le pid
	pid_t pid = getpid();
	//on affiche le pid
	printf("PID= %d> ", pid);
}

int myRead(char *buffer, int *compteur){
	//le compteur contiendra le nombre d'élément repéré dan l'entrée
	*compteur= 0;
	//le buffer contiendra toute ce que l'utilisateur a entré
	strcpy(buffer,"");
	int last= 0;
	char ret;
	while((ret= getchar())){ 
		if(ret == 32){ //s'il y a un espace, on compte un mot en plus
			*compteur= *compteur+1;
		}
		if(ret == 10){ //si il y a un retour charriot, on compte le dernier mot et on quitte
			if(last != 32){
				*compteur= *compteur+1;
			}
			break;
		}
		//on ajoute le caractère dans le buffer (=entree)
		char lettre[2];
		charToString(ret, lettre);
		strcat(buffer, lettre);
		last= ret;
	}
	return 0;
}

int validate(char *action, int num, char *entree, int *newCmd, int *newL_type, int *newStart, int *newLength, int *newWhence){
	//on déclare le variables pour tester l'entrée de l'utilisateur
	char cmd[20]="", l_type[20]="", start[20]="", length[20]="", whence[20]="";
	sscanf(entree, "%s %s %s %s %s", cmd, l_type, start, length, whence);

	//On afficher les valeurs intermédiaire (si la variable globale VERBOSE est activée (=1))
	if(VERBOSE){
		printf("----------------------------------------------------\n");
		printf("nombre d'entrées: %d\n", num);
		printf("cmd=%s, l_type=%s, start=%s, length=%s, whence=%s\n", cmd, l_type, start, length, whence);
	}

	//DÉBUT DES TESTS
	//Si on a un seul argument
	if(num == 1){
		if(strcmp(cmd,"?") == 0){ //si c'est le ? l'action sera "help"
			strcpy(action, "help");
		}
		else if(strcmp(cmd,"exit") == 0){ //si c'est le "exit" l'action sera "exit"
			strcpy(action, "exit");
		}
		else{ //sinon c'est une erreur
			printf("Error the single argument is not ? or exit\n");
			return 1;
		}
	}
	else{
		// teste pour l'entrée CMD (on affiche les valeurs intermédiaire si VERBOSE est activé (=1))
		if(strcmp(cmd,"g") == 0){
			if(VERBOSE){
				printf("F_GETLK ");
			}
			*newCmd= F_GETLK;	
		}
		else if(strcmp(cmd,"s") == 0){
			if(VERBOSE){
				printf("F_SETLK ");
			}
			*newCmd= F_SETLK;	
		}
		else if(strcmp(cmd,"w") == 0){
			if(VERBOSE){
				printf("F_SETLKW ");
			}
			*newCmd= F_SETLKW;	
		}
		else{
			printf("Error, the first argument is not one of those arguments: g, s, w\n");
			strcpy(action, "error");
		}
		// teste pour l'entrée L_TYPE (on affiche les valeurs intermédiaire si VERBOSE est activé (=1))
		if(strcmp(l_type,"r") == 0){
			if(VERBOSE){
				printf("F_RDLCK ");
			}
			*newL_type= F_RDLCK;	
		}
		else if(strcmp(l_type,"w") == 0){
			if(VERBOSE){
				printf("F_WRLCK ");
			}
			*newL_type= F_WRLCK;	
		}
		else if(strcmp(l_type,"u") == 0){
			if(VERBOSE){
				printf("F_UNLCK ");
			}
			*newL_type= F_UNLCK;	
		}
		else{
			
			printf("Error, the second argument is not one of those arguments: r, w, u\n");
			strcpy(action, "error");
		}
		// teste pour l'entrée START (on affiche les valeurs intermédiaire si VERBOSE est activé (=1))
		if(strcmp(start, "") != 0 && hasLetter(start) == 0){
			*newStart= atoi(start);
			if(VERBOSE){
				printf("%d ", *newStart);
			}
		}
		else{
			printf("Error, the third argument is not a number\n");
			strcpy(action, "error");
		}
		// teste pour l'entrée LENGTH (on affiche les valeurs intermédiaire si VERBOSE est activé (=1))
		if(strcmp(length, "") != 0 && hasLetter(length) == 0){
			*newLength= atoi(length);
			if(VERBOSE){
				printf("%d ", *newLength);
			}
		}
		else{
			printf("Error, the fourth argument is not a number\n");
			if(VERBOSE){
			}
			strcpy(action, "error");
		}
		// teste pour l'entrée WHENCE (on affiche les valeurs intermédiaire si VERBOSE est activé (=1))
		if(strcmp(whence,"s") == 0){
			if(VERBOSE){
				printf("SEEK_SET ");
			}
			*newWhence= SEEK_SET;
		}
		else if(strcmp(whence,"c") == 0){
			if(VERBOSE){
				printf("SEEK_CUR ");
			}
			*newWhence= SEEK_CUR;
		}
		else if(strcmp(whence,"e") == 0){
			if(VERBOSE){
				printf("SEEK_END ");
			}
			*newWhence= SEEK_END;
		}
		else if(strcmp(whence,"") == 0){
			*newWhence= SEEK_SET; //valeur par défaut pour le whence
				printf(" ");
		}
		else{
			printf("Error, the fith argument is not one of those arguments: s, c, e, [BLANK]\n");
			strcpy(action, "error");
	}
		if(VERBOSE){
			printf("\n");
			printf("----------------------------------------------------\n");
		}
		if(strcmp(action, "error") != 0){ //lock s'il n'y a eu aucune erreur dans l'entrée
			strcpy(action, "lock");
		}
	}
	return 0;
}

int execute(char *action, int fd,int  cmd,int  l_type,int  start,int  length, int whence){
	//on fait l'action proposé par la fonction validate
	if(strcmp(action, "error") == 0){
		return 1;
	}
	else if(strcmp(action, "exit") == 0){
		printf("END OF THE APPLICATION");
		exit(0);
		if(VERBOSE){
			printf("\n----------------------------------------------------\n");
		}
	}
	else if(strcmp(action, "help") == 0){
		help();
	}
	else if(strcmp(action, "lock") == 0){
		createLock(fd, cmd, l_type, start, length, whence);
	}
	else{
		return 1;
	}
}



//-------------
//MAIN FUNCTION
//-------------
int main(int argc, char *argv[]){ 
	//On a 3 parties:
	

	//1) DÉCLARATION DES VARIABLES
	int res= 1;
	char entree[255]="";
	char action[20]="";
	int num, cmd, l_type, start, length, whence;


	//2)OUVERTURE DU FICHIER
	int fd;
	if(argc == 2){
		fd= open(argv[1], O_RDWR);
	}
	else{
		printf("Error: there must be one argument (the file name)");
		exit(0);
	}


	//3)LANCEMENT DE L'INTERFACE
	do{
		//fonctions
		//on affiche le menu PID=pid>
		showPID(); 

		//on lit l'entrée de l'utilisateur et le retourne dans la chaine [entree]
		myRead(entree, &num); 

		//on teste si [entree] est valide et on retourne quelle [action] on doit exécuter avec la fonction execute ()
		validate(action, num, entree, &cmd, &l_type, &start, &length, &whence); 

		//execute [action] proposé par la fonction validate
		res= execute(action, fd, cmd, l_type, start, length, whence); 
	} while(res);

	return 0;
}
