## Objectif
Backup pour architecture de fichier
Lister le contenu d'un dossier

date de modification strftime
Ou sinon lstat/stat/fstat

## Partie 1: listing
- fonction qui ouvre un dossier ou non
- Fonction qui affiche:
	- type
	- droits
	- taille (octet)
	- date de modification (strftime)
	- nom relatif du fichier (concat $1)
- Si dossier on recommence

## Backup de dossier et fichiers
- control destination
- control arrivé
- si fichier, copie simple
- si dossier, copie contenu
