Analyseur récursif
====================

But: comprendre le fonctionnement des générateurs de parser descendants.

On ne fait que des lectures et des expansions.
Mais la pile peut diminuer.

## Deux différence avec l'automate des items:
analyse déterministe dite prédictive
Plus d'item et de réduction explicite


On "prédit" quelle production utiliser en analysant les k prochains symboles.
Conséquences:
Ne fonctionne qu'avec certaines grammaire dites LL(k) qui ne sont pas toujours très facile à lire.
marqueur de fin de mot #

K=1 est facilement généralisable

Plus d'item mais des mots étendus
L'alphabet est composé des non-/terminaux 
Dérivation de gauche: les éléments le plus à gauche sont au sommet de la pile.
Condition d'acceptation= pile vide et le symbole # à la fin

## Transition de lecture
Si le sommet est un terminal:
- on contrôle que le symbole est bien sous la tête de lecture (sinon echec)
- on le consomme
- on le déplie

## Transition d'expansion
Si le sommet est un non terminal et que la tête de lecture est sur un caractère et si Table [non-terminal, caractère] contient non-terminal -> nt1...ntn
On déplie non-terminal et on emplit à sa place nt1...ntn

Pour se faire, on utilise une table d'analyse

Table d'annalyse:
Indicé par les symboles non-terminaux (en ligne haut)
Indicé par les symboles terminaux (en colonne gauche)

## Construction de la table d'analyse
### par intuition
Codé par un ensemble de fonctions
Ces fonctions s'appellent les unes les autres
N'utilise pas de pile explicite: pile implicite des appels

Une fonction X() par non-terminal X appartenant au non-terminaux

### Par ensemble Premier
