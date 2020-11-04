## Objectif
Lister le contenu d'un dossier

## Partie 1: listing
- fonction qui ouvre un dossier ou non
- Fonction qui affiche:
	- type
	- droits
	- taille (octet)
	- date de modification (strftime)
	- nom relatif du fichier (concat $1)
- Si dossier on recommence
 
 ## Cas possibles:
1. un répertoire
2. fichiers/dossiers à un répertoire
3. un fichier à un fichier

## Question
Dans quel cas les droits ne pourrons pas être les mêmes?
- Cela peut arriver quand on copie des éléments pour lesquels ont a pas tout les droits (comme déplacer le contenu de l'administrateur).
