Problème de recherche
======================

Recherche par état et transition

Graphe d'état et parcours du graphe

> Exemple: Jeu du tacquin

## Comment formaliser?
Le problème
Le fait de chercher une solution
La difficulté du problème
La solution elle-même
Le fait qu'il y ai ou pas de solution

## On trouve un algorithme et on cherche:
* Sa complexité
* Sa convergence

Définition:
	Un état s (sate) est une configuration d'un système.
	L'espace d'état S d'un système est l'ensemble de tout les états possibles du système.

Une méthode pour résoudre des problèmes est d'énumérer simplement les état et faire un graphe à la main. On peut facilement résoudre des problème
S'il y a beaucoup d'état, on utilise les algorithmes d'exploration de graphe.

## observabilité
Quand quelque chose est observable, on le maîtrise complètement et on peut `revenir en arrière`.
Un système peut être partiellement observable si une transition est irréversible.

## Arbre de recherche
But: explorer le graphe à partir de l'état initial
Noeuds: contiennet les états visité
Racine: correspond à l'état initial

Complétude: Le fait qu'un arlgorithme arrive a trouver la solution si elle existe. (on ne s'intéresse pas de savoir son efficacité).
Optimalité: Le fait qu'un algorithme soit le plus rapide (ou le moins coûteux) pour trouver la solution.

## Type de problèmes de recherches
Recherche recherche aveugle: (On organise la liste de voisin comme ça vient)
recherche heuristique: (On modifie notre recherche par une critère qui influe sur la direction)
