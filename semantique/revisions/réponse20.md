Sémantique des langages logiques
=================================

20. Expliquez comment représenter la sémantique d'un langage de programmation logique. Quelles sont les limites de la résolution SLD de Prolog.

Syntaxe des [clauses_de_Horn](clauses_de_Horn)

## Composition (syntaxe)
Ensemble des termes est construit par les fonctions.
On peut construire de nouveau termes en les combinant à des fonctions.

**Fonction**
Func= (a,b,c,...,z)

**Prédicat**
Pred= (aa,bb,cc,...,zz) 

Un litéral est composé de fonction et de prédicats

**Literal**
Lit= Lit(Pred,Func) 

On peut faire une conjonction de litéral grâce à l'opérateur "et"

**Conjonction**
Conj= Lit1 et ... et Litn

Les variables et les axioms sont les plus petit éléments qu'on ne peut pas diviser

**Variables et Constantes**
Un ensemble de variable définit

Une clause est construite à l'aide de prédicat, de fonction et d'une variable

**Clauses**
soit x appartenant à Var
Clauses(Pred,Func,X)

**requête**
Une requête est une conjonction de littéraux

si c est un ensemble de literal et h un literal alors c => h est une clause

## Sémantique computationnelle
L'enjeu se trouve dans les variable pour la satisfaction des litéraux.
Rappel: pour satisfaire une clause, il faut trouver une interprétation des variables qui satisfait la clause (= qui rend la clause vrai)

Deux règles pour la sémantique computationnelle

**Substitution**
une fonction qui transforme un terme en un nouveau terme en substituant les variables grâce à une assignation
donc 

**Unification**
Fonction qui trouve la substitution s qui égalise deux termes.
ça se rapport à la résolution d'un système d'équation.

Domaine sémantique: Substitution x requête
on part avec une substitution vide et on fini avec une requête vide

**Points de non-déterminismes**
choix des axioms
choix du litéral à résoudre
choix de l'unificateur

## Sémantique d'évaluation
on part d'un couple substitution (vide) et requête pour finir avec seulement une substitution
