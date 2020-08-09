Mécanisme de transactions des SGBD
===================================

Transactions, propriété ACID
Gestion de la concurrence, verrous
Reprise après erreur

Contraintes d'intégrité
* Structurelles (clé primaire)
* Référentielles (clé secondaire)
* Domaine (attributs et tuples)

## Transaction
Séquence d'opération (réussite ou échec total donc commit ou abort)
Transforme une base de données d'un état cohérent à un autre état cohérent

## Problème
Plusieurs utilisateurs et un crash
La solution est un recovery

## Propriétés ACID d'une transaction
* **Atomicité**: toutes les opérations ou aucune n'est exécuté (tout ou rien)
* **Cohérence**: valide les règles d'intégrité de la BD
* **Isolement**: aucune maj n'est visible pour les autres avant commit 
* **Durabilité**: Les changements sont durables (pas de retour en arrière)

(voir [règles](règles))
=======
[règles](règles):
Le SGBD respectent les propriétés ACID.
Toute transaction T2 ne doit pas modifier une chose si elle a été modifiée par T1 sans être validée.
Toute transaction T ne dois pas lire des valeurs non confirmées et manipulées par d'autres transactions.
Aucune transaction ne peut modifier une valeur lue par une autre transaction avant que cette dernière ne soit validée.

## contrôle de la concurrence

## Dirty read
Quand T2 lit une donnée modifiée mais non validée de T1
p.24

## Gestion de la concurrence
[sérialisabilité](sérialisabilité)
verrouillage
