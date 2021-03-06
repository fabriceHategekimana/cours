
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

Sureté (safety): être sûre qu'une propriété ne se produise pas

vivacité (vicacity): On doit être sûre que le programme/thread se finissent

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

Les méthodes wait slepp join testent l'état de l'indicateur et lèvent l'exception Interruptedexeption si l'indicateur vaut true.

## Les différents états d'un thread

![les_differents_etas_d_un_thread](../images/les_differents_etas_d_un_thread.png)

l'[ordonnanceur](ordonnanceur)

L'entrée dans un moniteur bloqué (=ressource/objet protégée par un verrou)

La méthode [join](join)

Problème d'exclusion mutuelle

Quand deux threads ne peuvent s'exécuter en même temps sur une mémoire partagée.

## Algorithme de Lamport
1. Chaque processus choisit un numéro plus grand que les numéros déjà attribués.
2. Chaque processus teste s'il peut entrer en SC
	1. S'assure qu'aucun processus est en phase 1
	2. S'assure qu'il possède le plus petit numéro, en cas d'égalité, les identificateurs de processus font la différence

**hypothèses**
- Les processus ont des identificateurs connus (utilisation des booléens)
- Les processus "se connaissent" tous

synchronized est un mot clé qui fait en sorte qu'il n'y ait qu'un seul processus qui s'exécute à la fois.

## Fonction testAndset
Le processus T1 et T2 partagent un lockFlag.
LockFlag possède une valeur et une fonction testAndset()
la fonction test s'il y a un verrou
Donc les processus
On a pas d'attente active
T2 se refera plus tard
