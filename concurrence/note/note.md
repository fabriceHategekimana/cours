
## Interface Runnable
Permet de créer des instances qui s'exécutent indépendemment.
Comment les faire s'exécuter en même temps?

Pourquoi écrire un programme concurrent?
	* optimiser l'utilisation des ressource du processeur
	* Utilisation

Thread:
	Processus qui partagent la même zone mémoire/programme.
	
Modification où la modification n'est pas répercuté dans la mémoire (par ex. dans un registre ou la mémoire cache à la place)
Sans ça, la mémoire n'est pas partagée.

Java a un modèle d'analyse sémantique en 1 thread: Il peut échanger des lignes de code pour des valeurs données.

## Problèmes classiques
* Interblocage (deadlock) les processus s'attendent mutuellement
* Interférence: les processus corrompent une donnée en la modifiant (entrelacement=interlearing: donnée incohérente)
* insuffisance de ressource (starvation): un programme se fait toujours passer devant dans l'accès aux ressources


## Propriétés désiré

Slide 11

Sureté (safety)

vivacité (vicacity)

## Condition d'interblocage
* Exclusion mutuelle: une ressource doit être partagée
* Hold and wait: si interblocage, ils doivent retenir une ressource et attendre
* Pas de préemption: Il n'y a pas de superviseur. Les threads décident d'eux même de "lâcher la ressource"
* Attente circulaire: Deux thread s'attendent

## Solution pour l'interblocage
* On s'assure que l'une des 4 conditions puisse être enlevée (Seulement le Hold an wait et l'attente circulaire)
* On peut utiliser la synchronisation wait-free pour contrer le Hold and wait
* On peut utiliser un ordre d'accès sur les ressource pour contrer les attentes circulaire


Un module est une sorte d'interface avec des procédures et des variable (le but est de diminuer la visibilité des variables)
Un moniteur est un module qui dispose d'un verrou qui limite le nombre d'accès
Un objet est une sorte de module qui peut avoir plusieurs instance. Pour la programmation concurrente, on crée des objets qui sont des moniteurs qui ont plusieurs instances.
