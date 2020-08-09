Formes normales
===============
Permet de modéliser au mieux une situation pour en obtenir tes tables optimisées.


## Dépendances fonctionnelles
Contrainte entre deux ensembles d'attributs de la base de données.
Spécifie une contraintes sur les tuples possible pour former une instance r de R.
En revenant à la notion de clé le reste des attributs du tuple peuvent être trouvés grâce à la clé.

## Formes normales (4)
Formes (ou contraintes) sur les schémas de relation
* 1FN
* 2FN
* 3FN
* FNBC
Par force croissante

## 1FN
1FN si les domaines des attributs d'un schéma contiennent des valeurs indivisibles (atomiques)
Si les valeurs sont des multivalués ("Henri, André, Julien") ou Composées ("5, av. Soret, 1203 Genève")

## 2FN
Basée sur la dépendance fonctionnelle totale.
Une dépendance fonctionnelle est totale si la quantité d'attribut de la clé est déjà minimale.
Un schéma de relation en 1FN est 2FN si pour tout A différent de la clé, A est en dépendance fonctionnelle de celle-ci.

## 3FN
La 3FN est basée sur le concept de dépendance fonctionnelle transitive.
une dépendance fonctionnelle est transitive s'il existe un ensemble d'attributs Z qui n'est sous-ensemble d'aucune
clé de R est qu'il sert d'intermédiaire.
Un schéma de relation en 2FN est en 3FN si aucun attribut A différents de la clé n'est transitivement dépendant de la clé.

Forme normale de Boyce-Codd
Un schéma de relation en 3FN est en FNBC si aucun attribut de R n'est transitivement dépendant de la clé

## **Normalisation**: 
Processus de transformation d'un schéma pour l'amener dans une forme normale de degré supérieur.
Problème, perte d'information après normalisation et parfois difficile de normaliser sans parler de la perte de dépendances  fonctionnelles.
On le fait au moyen de la décomposition.

## Décomposition
Décompose un schéma de relation en schémas plus petits (et si possible normalisés).

Par là, il existe différent types de décompositions
lossless decomposition (sans perte d'information)
dependency-preserving decomposition (sans perte de dépendance)

Règles:
toute relation peut-être décomposée en une collection de relation plus petites en FNBC (mais pas de garantie pour la dépendance fonctionnelle)
Il est toujours possible de décomposer un schéma de relation en 3FN san pert d'information et en préservant les dépendances fonctionnelles.
