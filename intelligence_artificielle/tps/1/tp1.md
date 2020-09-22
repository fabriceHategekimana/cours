Travaux pratiques d'IA
======================

## Série 1: Formalisation

## 1 Les trois missionnaire

### 1.2 Description
Voir le document

### 1.3 Formalisation du problème recherche
**1. Donnez une représentation des états**  
	On a deux rives, un groupe de trois missionnaires et un groupe de trois cannibales.  
	On peut représenter par rive: le nombre de missionnaire et de cannibale par un couple (m,c)  
	Comme il y a deux rives (gauche 0, droite 1 que j'ai choisi pour ce cas) on a (m0, c0, m1, c1)  
	
**2. Quels sont les opérateurs possibles?**  
	* On a des opérateurs `allez` pour aller de la rive gauche vers la rive droite.  
	* On a des opérateur `retour` pour aller de la rive droite vers la rive gauche  
	* Comme le bateau ne peut contenir que deux personnes, on a un ensemble de passagers contenant des couples ou des singletons: {m; c; (m,m); (c,c); (m,c)}.  
	* Les mouvements se font dans les deux sens  
	
**3. Définissez les conditions pour lesquels les opérateurs sont applicables**
	Un opérateur est applicable si:
	1. Le nombre de personnes déplacées n'est pas plus grand que le nombre de personnes disponibles. (par exemple déplacer 2 cannibals alors qu'il y en a que 1)
	2. Il n'y a pas plus de cannibals que de missionnaires dans chaque côtés de la rivière. 
	
**4. Implémenter un algorithme de recherche pour résoudre le problème en utilisant un arbre de recherche correspondant à la description que vous avez choisi.**

```
//Algorithme de recherche
init <- (3,3,0,0)
Transition(init)

function Transition(old)
for transition in transitions
	new <- transition(old)
	if test(new) == true:
		if new == (0,0,3,3)
			print(new)
		else
			recherche(new)
```

**Remarque**: J'ai donné dans le pseudo code une définition récursive. Cependant dans mon implémentation, je ferrai une représentation non récursive

## 2 La tour de Hanoi

## 3 Algorithme de recherche général
