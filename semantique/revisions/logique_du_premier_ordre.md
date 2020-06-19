Logique du premier ordre
========================

## Définitions
Quantificateurs (universel et existentielle)

Formule close: toute les variables sont liée (=quantifiés)

Variables libres: Qui ne sont pas attaché à un quantificateur
Variables libres: Qui sont attaché à un quantificateur

Signature: associe à chaque symbole une arité
exemple: plus/2 est une fonction qui addition plus(1,1)= 2

## Contenu d'une formule
atomes
variables
termes fonctionnels

Une formule peut contenir des des sous-formules

Il n'y a pas d'atome dans un atome ni dans un terme fonctionnel

## Ordre et convention:
1. Associatif à gauche
2. Ordre:
	* Quantificateur
	* non
	* et
	* ou
	* ->
	* <->

## La sémantique des formules
**Interprétation (D,If,Ip) d'une signature**
D: domaine d'interprétation (peut être n'importe quel ensemble)
If: une interprétation de chaque symbole fonctionnel f
Ip: une interprétation de chaque symbole de prédicat p

If(constante)= d appartenant à D
If(f)= d appartenant à D si f/n alors on va de D^n à D
If(p)= v appartenant à {0;1} si p/n alors on va de D^n à {0;1}

remarque: une signature a une infinité d'interprétation c à d que l'interprétation dépend de ce que la personne croit lire

Sinon l'interprétation d'une formule marche assez comme la logique propositionnelle (satisfaction,cohérence,etc.)
Donc notre interprétation peut satisfaire ou falsifier des formules données.

## Systèmes de preuve
Règle d'inférence: règle créant une formule à partir d'une ou plusieurs autres formules. (on part des prémisse pour arrivé à la formule déduite)
dérivation: toute suite de formule dans laquelle chaque formule est une formule initial ou une formule obtenue à partir des formules précédente par une règle d'inférence.

Système déductif (ou de preuve):
Soit F et G des formules clauses sur un ensemble A de formules valides appelées axiomes logiques:
S'il existe une dérivation de F à G alors G est conséquence logique de F
La dérivation est donc une preuve formelle.
Permet de produire toutes les conséquences logiques d'une preuve initiale.
