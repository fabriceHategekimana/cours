Travaux pratiques d'IA
======================

## Série 1: Complexité & Recherche aveugle

## 1 Les tours de Hanoï

### 1.1 Questions
1. Implémentation de deux algorithmes de recherche BFS et DFS de la tour de Hanoï pour n=3 en affichant à chaque tour:
 	* le noeud traité
	* l'état de la file
2. Complexité:
	1. BFS:
		1. Temps: dans la pire situation (un file de n noeuds) la complexité serait de O(n)
		2. Espace: étant donné que l'on conserve tout les chemins, dans le pire des cas, on aura n chemins pour n entrée donc une complexité en espace de o(n)
	2. DFS:
		1. Temps: dans la pire situation (en étoile) on avance et on backtrack à chaque fois jusqu'à trouver la solution don un facteur de O(2n)
		2. Espace: on ne garde qu'un chemin et on ne garde pas les éléments "inutils" à la recherche: donc dans le pire de cas (pour une file de n noeuds) on a une complexité de o(n)

3. Dans la stratégie en largeur (BFS), on trouve assez rapidement le chemin le plus court qui mène à la solution. Le problème est la quantité d'espace qu'il prend, car il retient toutes les possibilités en cours.  
Dans le cas de la stratégie en profondeur (DFS), on économise beaucoup d'espace, mais le temps pour trouver la solution peut être très long (surtout si on part dans la mauvaise direction). De plus la solution trouvé n'est pas forcément la plus courte.  
Chacun de ces algorithmes peuvent être amélioré, mais pour cela il faudrait que la recherche ne soit plus "aveugle".

4. Dans le cadre de la complétude et de l'optimalité, c'est le BFS qui gagne pour ce genre de problème selon mo:. En effet, ces deux algorithmes nous assurent qu'on va un jour trouver la solution si elle existe (complétude).Certes, l'algorithme en profondeur est bien moins coûteux pour trouver la solution mais elle perds en terme de temps et de qualité quand à la solution.

5. Formalisation du problème  
	* Un état du système peut être représenté par 3 piles contenant les disques. Les disque sont alors représenté comme des entiers (plus c'est grand plus le chiffre est élevé) On a ainsi une liste de 3 piles.   
	* Dans le cas de 3 disques (avec les disques sur la pile de gauche) le système serait [(1,2,3), (0,0,0), (0,0,0)] et l'état final serai [(0,0,0),(0,0,0),(1,2,3)]  
	* Les transitions peuvent être représentés par des couples (départ, arrivé) qui décrivent le mouvement des disque. Les éléments départ et arrivé peuvent chacun prendre trois valeurs: "gauche", "milieu","droite" représentant les piles par leur position. Ainsi ("gauche", "milieu") représente le mouvement du disque au sommet de la pile gauche vers la pile du milieu. Il y a donc 6 transitions possibles.  
6. En comptant tout les état possibles du système, on a:  
	1. Sans les règles (3+6+1)*6= 60 possibilités  
	2. Avec les règles 3+(6*2)+1= 16 possibilités  
7. Voir le code  



## 2 Notation grand "O"
* 1 = O(100)
* 1 < O(n)
* n = O(10n+5)
* n^2 > 100n
* n < O(n^2)
* 10n^3+n^2-5n+100=O(n^3)
* n^50000+1000000= O(2^n)
* n2^n = O(2^n)

