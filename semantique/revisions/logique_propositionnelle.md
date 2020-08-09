Logique propositionnelles

Comprendre les fonctions, les applications et les ensembles (théorie des ensembles)

Aspect syntaxique et sémantique

Constantes
Variables
Connecteur

Ensemble B (booléen {0;1})

Définition d'une formule propositionnelles (par induction)
V et C sont des formules
Si A et B sont des formules alors:
non A	est une formule
A ou B	est une formule
A et B 	est une formule
A -> B	est une formule

## Propriété des connecteurs:
les connecteurs logiques sont associatif à gauche
## Convention de priorité:
1. non
2. et
3. ou
4. implique

Comment donner un sens?
En donnant un sens à leur connecteur logique.
Interprétation
Soit V l'ensemble des variables propositionnelles 
On définit Fv un ensemble de toutes les formules dont les variables appartiennent à V.

Une interprétation sur V est une application I de Fv dans B qui vérifie les propriété suivantes:
* I(Faux)= 0
* I(Vrai)= 1
* Pour toute variables (appartenant à V) I(variable) appartient à B
* Pour tout connecteur, l'interprétation se fait en:
* I(connecteur A)= f(I(A))
* I(A connecteur B)= f(I(A),I(B))

Une formule à n variable admet 2^n interprétations (voir table des vérité)

## Satisfaction
On dit qu'une interprétation I **satisfait** une formule A lorque I(A)=1, et qu'elle falsifie A lorsque I(A)=0

modèle de A: toute interprétation qui satisfait A et contre-modèle toute interprétation qui falsifie A.

Une formule est satisfaisable ou cohérente s'il existe au moins un modèle.
Une formule est incohérante ou non satisfaisable s'il n'y a aucun modèle.
Une formule est valide s'il n'existe aucun contre-modèle.

## Sémantique de la conséquence logique
B est conséquence logique de A (A|=B) ssi tout modèle de A est un modèle de B (L'ensemble des modèle de B peut être plus grand tant que A est inclut dedans)

A|=B ssi A->B est une formule valide
