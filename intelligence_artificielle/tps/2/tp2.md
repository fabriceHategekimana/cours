Travaux pratiques d'IA
======================

## Série 1: Complexité & Recherche aveugle

## 1 Les tours de Hanoï

### 1.1 Questions
1. Formalisez le problème  
	* Un état du système peut être représenté par 3 piles contenant les disques. Les disque sont alors représenté comme des entiers (plus c'est grand plus le chiffre est élevé) On a ainsi une liste de 3 piles.   
	* Dans le cas de 3 disques (avec les disques sur la pile de gauche) le système serait [(1,2,3), (0,0,0), (0,0,0)] et l'état final serai [(0,0,0),(0,0,0),(1,2,3)]  
	* Les transitions peuvent être représentés par des couples (départ, arrivé) qui décrivent le mouvement des disque. Les éléments départ et arrivé peuvent chacun prendre trois valeurs: "gauche", "milieu","droite" représentant les piles par leur position. Ainsi ("gauche", "milieu") représente le mouvement du disque au sommet de la pile gauche vers la pile du milieu. Il y a donc 6 transitions possibles.  
2. En comptant tout les état possibles du système, on a:  
	1. Sans les règles (3+6+1)*6= 60 possibilités  
	2. Avec les règles 3+(6*2)+1= 16 possibilités  
3. Voir le code  

## 2 Notation grand "O"
* 1 =O(100)
* 1 < O(n)
* n = O(10n+5)
* n^2 > 100n
* n< O(n^2)
* 10n^3+n^2-5n+100=O(n^3)
* n^50000+1000000= O(2^n)
* n2^n= O(2^n)

## 2.1 
