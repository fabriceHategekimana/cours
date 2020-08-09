Gestion de la mémoire:
=======================

(à relir car très spécifique)

Un processus ou un thread est déterminé par son état (program state).

[questions](questions):
c'est quoi un thread

L'état d'un processus est définit par les valeurs des registre r0-r15, cpsr et le contenu de la mémoire qu'il peut accéder.
Donc
état= (r0-r15,cpsr,Mem)

La mémoire peut-être classée en:
* le code, exécutable
* les données read-only statiques
* Les données statiques
* le tas (the heap)
* la pile (the stack)

**code du programme**
Les instructions exécutées, en général séquentiellement, par le processeur. Cette zone mémoire peut être read-only

**Allocation de la mémoire (statique vs dynamique)**
Pour stocker la valeur d'une variable d'un programme il faut allouer, réserver, de la mémoire à ce programme.
Cette allocation peut être dynamique ou statique.

Si l'allocation est dynamique, elle se fait au moment ou le programme veut accéder la variable la première fois, l'allocation se fait durant l'exécution du programme.
En général elle se fait soit sur la pile (stack) soit sur le tas (heap). 
[règles](règles):
La durée de vie des variables dynamiques est plus petites que la durée de vie du programme.

L'allocation dynamique d'une variable se fait avant que le programme exécute une instruction qui peut la référencer; 
La variable est visible, cette portion du code source s'appelle la **portée**.
Lorsque le processeur exécute du code hors de la portée de la variable, celle-ci est désallouée.
En C, une variable est allouée avant d'exécuter la première instruction du bloc ou elle est définie et désallouée en quittant le bloc.


