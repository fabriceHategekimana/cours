## Mémoire:
1. Plus la mémoire est rapide, plus elle est proche.
2. Une adresse pointe sur une donnée de 8 bits.
3. La taille du bus de données défini la l'organisation des données.
4. Le temps d'accès est de l'ordre des nanosecond pour les registre et des millisecond pour le disque dur

## bus_d_adresse
Chaque élément constituant le système informatique est désigné par une adresse ou une plage d'adresses.

## pipeline
La longueur du pipeline détermine les caractéristiques de l'exécutions.
Une instruction est exécutée uniquement après qu'elle ait passé tout les étages du pipeline.

## Drapeaux
Le drapeaux C suppose une arithmétique non signé

## Instructions de branchement
Les instructions BX et BLX permettent de changer l'etat du processeur selon que l'adresse est paire ou impaire.

## Transfère de multiples registres
Une seule instruction peut transférer le contenu de plusieurs registres vers/depuis la mémoire.

## L'instruction swap
L'instruction swap est une instruction atomique.

## Gestion de la mémoire
La durée de vie des variables dynamiques est plus petites que la durée de vie du programme.

## Conversion
1 digit en hexadécimal vaut 4 digit en binaire
préférer les entiers non signés lorsqu'on divise (la division par la droite entraine un arrondissement vers le bas)

## Optimisation en C
Une bonne habitude est de limiter le nombre de variable locales à 12.
Si le compilateur doit utiliser la pile, il le fait pour les variables le moins fréquemment utilisées.
Le compilateur sélectionne les variables qui se trouvent dans le plus grand nombre de boucles imbriquées.
Les fonctions qui utilisent au maximum 4 arguments sont plus efficace.
