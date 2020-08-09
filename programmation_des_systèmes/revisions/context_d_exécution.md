Le contexte d'exécution
========================

L'ensemble des registre utilisé pour une tâche donnée.

## changement de contexte:
1. sauvegarder les registres en mémoire du processus courant
2. retrouver et restaurer le contexte du nouveau processus à exécuter
3. exécuter les instruction du nouveau processus

## États du processeur
ARM, Thumb, Jazelle

ARM: Jeu d'instruction sur 32 bits
Thumb: Jeu d'instructions codé sur 16 bits
Jazelle: jeu d'instruction sur 8 bits destiné à améliorer les performances de programmes écrits en bytecodes

## Execution d'une instruction:
1. Fetch
2. Décode
3. Execute
