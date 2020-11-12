Résolution par CSP (Constrains Satisfaction Problem)
======================================================
--------------------------------------
## À faire
	- créer 4 .py (forward_checking et les trois heuristiques)
	- implémenter:
		- Une classe graphe
		- forward_checking
		- Heuristique 1
		- Heuristique 2
		- Heuristique 3
	- Dessiner les graphes (choix de couleur libres)
--------------------------------------

## Backtracking forward checking:
	- programmation logique et contraintes:
		- rassembler les contrainte:
			1. Deux régions adjacentes doivent être coloriées de couleur différentes.
			2. Le nombre de couleur utilisées doit être minimal.
		- Contrainte finalement unique et simple (pas besoin de programmation logique)
	- règles:
		- création de couleur en runtime
		- ordre donnée (Pile):
			1. NB
			2. CA
			3. V
			4. MPLR
			5. RAA
			6. PACA
			7. PLCB
	- Algorithme: forward_checking

## Heuristique région la plus contrainte
	- comment trouver la région la plus contrainte:
		- celle qui a le moins de choix de couleur possible
		- faire le choix dans le get Non affecté
	- commence par NB puis ordre alphabétique
	- écrire algorithme: forward_checking

## Heuristique variable la plus contraignante
	- sélectionner la région qui génère le plus grand nombre de contraintes:
		- = une région qui enlève le plus grand nombre de possibilités
	- Sélection par ordre alphabétique sinon

## Choix de la valeur (=couleur) la moins contraignante
	- hypothèse de la couleur la moins utilisé
		- la couleur qui réduit le moins les chois possibles
	
Un graphe pour les trois heuristique
