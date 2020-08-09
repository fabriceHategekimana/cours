Éléments d'un système informatique
=====================================

## Composants principaux d'un ordinateur (ou un système informatique)
1. Le [processeur](processeur)  
2. La [mémoire](mémoire)  
3. Les [périphériques](périphériques)  

## Ces systèmes utilisent des bus pour échanger l'information:
1. [bus_de_données](bus_de_données)  
2. [bus_d_adresses](bus_d_adresses)  
3. [bus_de_contrôle](bus_de_contrôle)  

## Les cycles:
1. [lecture](lecture)  
2. [écriture](écriture)  

## Les modes de fonctionnement
1. [user_mode](user_mode)  
2. [registre_d_etat](registre_d_etat) (cpsr)  
3. abort: lorsque le processeur détecte qu'il n'arrive pas à accéder la mémoire externe  
4. (fast) interrupt request: deux niveau de priorités disponibles pour le traitement des interruptions  
5. supervisor: généralement le mode d'opération du système d'exploitation, c'est le mode après le reset  
6. system: identique au mode user, mais on a accès en lecture écriture au registre cpsr  
7. undefined: état du processeur lorsqu'il doit exécuter une instruction qu'il ne peut pas décoder (undefined) ou qui n'est pas supportée par l'implimentation  
8. user: mode de fonctionnement des applications le seul qui ne peut pas modifier les bits mode du cpsr  

L'intérêt de ce mécanisme est qu'on peut modifier les registre sans altérer leur valeurs  

[context_d_exécution](context_d_exécution)  

## Pipeline
[règles](règles):  
La longueur du pipeline détermine les caractéristiques de l'exécutions.  
Une instruction est exécutée uniquement après qu'elle ait passé tout les étages du pipeline.  

[questions](questions)  

Le pipeline est vidé lors d'une interruption  

-Le registre pc contient l'adresse de la prochaine instruction à transférer de la mémoire vers le processeur.    
