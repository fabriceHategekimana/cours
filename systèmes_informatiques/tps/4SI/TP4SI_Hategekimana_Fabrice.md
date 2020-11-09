## 2 Description
Il existe flock() et fcntl()

[X] Fonction pour afficher le PID
[X] Faire l'interface utilisateur
[X] Faire le help
[] Analyser extrait de code
[] Coder pour les actions (s'inspirer du help):
	- dé/verouiller une partie du fichier
	- obtenir les infos de verrouillage
	- choisir le type de verrouillage
	- définir le décalage pour le verouillage
Étudier l'extrait de code

## 5 Questions
Questions
• Que se passera-t-il si nous déverrouillons un fichier (ou une partie du fichier) qui n’est pas
verrouillé?
• Que se passera-t-il si nous mettons un nouveau verrou sur une section déjà verrouillée?
Le type de verrou changera-t-il le résultat? Expliquer dans la situation avec le même processus et avec 2 processus différents

--------------------------------------------------------

// EXTRAIT DE CODE
for (;;) { 
/* Prompt for locking command and carry it out */
printf("PID=%ld> ", (long) getpid());
fflush(stdout);
// use fgets to read user input and then handle it
// process user unput into the 'cmd' variable and the various elements of 'fl' struct
status = fcntl(fd, cmd, &fl);
/* Perform request... */
// interpret results of request and inform user
if (cmd == F_GETLK) { 
/* F_GETLK*/
// check status and handle errors (look at manual for possible errors)
if (status ==0 ){ 
// process results and print informative text
}else if (errno == SOME_ERROR){ 
// process results and print informative text
}
} else { 
/* F_SETLK, F_SETLKW */
// check status and handle errors (look at manual for possible errors)
if (status ==0 ){ 
// process results and print informative text
}else if (errno == SOME_ERROR){ 
// process results and print informative text
}
}
