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
	printf("PID= %d>", pid);
}

int charToString(char element, char *buffer){
	buffer[0]= element;
}

int myRead(char *buffer){
	//peut-être contrôler qu'il n'y ait pas d'espace inutil à la fin
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

int main(int argc, char *argv[]){ 
	char cmd[20], l_type[20], start[20], length[20], whence[20];
	int res;
	char total[255]="";
	int num= myRead(total);
	printf("nombre d'éléments: %d\n", num);
	//sscanf("%s %s %s %s %s", cmd, l_type, start, length, whence);
	printf("Okay!\n");
	//do{
		//showPID();
		//res= readAndExecute();
	//} while(res == 1);
	return 0;
}
