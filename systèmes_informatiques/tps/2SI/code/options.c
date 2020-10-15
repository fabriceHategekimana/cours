#include<stdlib.h>
#include<stdio.h>
#include "options.h"
#include<string.h>
#include<unistd.h>

int option(int argc, char *argv[], int *index, char *fonctionDeHashage){
   int estFichier= 0;
   strcpy(fonctionDeHashage, "SHA1");
   int option;
   while((option = getopt(argc, argv, ":ft:")) != -1){ //get option from the getopt() method
      switch(option){
         case 'f':
            estFichier= 1;
            break;
         case 't': 
            strcpy(fonctionDeHashage, optarg);
            break;
         case '?': 
            printf("unknown option: %c\n", optopt);
            break;
      }
   }
   *index= optind;
   return estFichier;
}
