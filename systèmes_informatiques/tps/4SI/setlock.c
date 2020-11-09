#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <sys/file.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>


//FLOCK
//int flock(int fd, int operation);
//C'est un verrou de signalisation
//Ne peut pas vérouiller de partie du fichier (vérouillage complet seulement)

//FNCTL
//int fcntl(int fd, int cmd, ... /*arg */);
//verrou soit facultatif, soit obligatoire (= mais non POSIX)
//struct flock lock;
//fcntl(fd, cmd, &lock);

int showPID(){
	pid_t pid = getpid();
	printf("PID= %d> ", pid);
}

int charToString(char element, char *buffer){
	buffer[0]= element;
}

int myRead(char *buffer){
	//peut-être contrôler qu'il n'y ait pas d'espace inutil à la fin
	strcpy(buffer,"");
	int compteur=0;
	int last= 0;
	char ret;
	while((ret= getchar())){ 
		if(ret == 32){
			compteur++;
		}
		if(ret == 10){
			if(last != 32){
				compteur++;
			}
			break;
		}
		char lettre[2];
		charToString(ret, lettre);
		strcat(buffer, lettre);
		last= ret;
	}
	return compteur;
}

int help(){
	printf("\n");
	printf("Format : cmd l_type start length [ whence ( optional ) ]\n");
	printf("’ cmd ’ --- ’g ’ ( F_GETLK ) , ’s ’ ( F_SETLK ) , or ’w ’ ( F_SETLKW )\n");
	printf("’ l_type ’ --- ’r ’ ( F_RDLCK ) , ’w ’ ( F_WRLCK ) , or ’u ’ ( F_UNLCK )\n");
	printf("’ start ’ --- lock starting offset\n");
	printf("’ length ’ --- number of bytes to lock\n");
	printf("’ whence ’ --- ’s ’ ( SEEK_SET , default ) , ’c ’ ( SEEK_CUR ) , or ’e ’ ( SEEK_END )\n");
}

int execute(int num, char *entree){
	int res= 1;
	char cmd[20]="", l_type[20]="", start[20]="", length[20]="", whence[20]="";
	sscanf(entree, "%s %s %s %s %s", cmd, l_type, start, length, whence);
	printf("----------------------------------------------------\n");
	printf("nombre d'entrées: %d\n", num);
	printf("cmd=%s, l_type=%s, start=%s, length=%s, whence=%s\n", cmd, l_type, start, length, whence);
	printf("----------------------------------------------------\n");
	//Début des tests
	if(num == 1 && strcmp(cmd,"?") == 0){
		if(strcmp(cmd,"?") == 0){
			help();
		}
		else if(strcmp(cmd,"exit") == 0){
			exit(0);
		}
		else{
			printf("Error!\n");
		}
	}
	//CMD
	if(strcmp(cmd,"g")){

	}
	else if(strcmp(cmd,"s")){
	}
	else if(strcmp(cmd,"w")){
	}
	//L_TYPE
	if(num > 1){
		if(strcmp(l_type,"r")){

		}
		else if(strcmp(l_type,"w")){
		}
		else if(strcmp(l_type,"u")){
		}
	}
	if(num > 2){
		printf("%d", atoi(start));
	}
	if(num > 3){
		printf("%d", atoi(length));
	}
	if(num > 4){
		if(strcmp(whence,"s")){
		}
		else if(strcmp(whence,"c")){
		}
		else if(strcmp(whence,"e")){
		}
	}
	return res;
}

int main(int argc, char *argv[]){ 
	int res;
	char total[255]="";
	int num;

	showPID();
	
	struct flock fl0;
	struct flock fl1;
	//défintion du lock
	fl0.l_type= F_WRLCK;
	//fl0.l_whence= SEEK_SET;
	fl0.l_start= 0;
	fl0.l_len= 5;

	int fd= open("teste.txt", O_RDWR);

	int ret0= 0;

	ret0= fcntl(fd, F_SETLK, &fl0);
	printf("%d\n", ret0);
	while(1){
		sleep(1);
	}

	return 0;
}
