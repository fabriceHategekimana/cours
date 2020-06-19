## évaluation d'une requête
1. produit cartésien du FROM
2. selection du WHERE
3. projection du SELECT

## fonction d'agrégation
avg= calcule la moyenne arithmétique
count= nb element liste
min= minimale
max= maximal
sum= somme

## connecteur
* Arithmétique:
	* plus (+)
	* moins (-)
	* multiplication (*)
	* division (/)
* Sur les strings
	* concaténation (|| ou concat)
	* lower (petite casse)
	* replace (remplace)
	* substr (sous chaîne)
	* etc.
* Sur les dates
	* moins (-)
	* add_months
	* last_day
	* months_between
	* sysdate
	* etc.

Pour tester si une valeur est nulle

La jointure
La condition de jointure est aussi placé dans le where

règles:
les opérateur ensembliste union, intersect et minus éliminent automatiquement les doublons

table1 INNER JOIN table2 ON condition

## Interrogation imbriquées:
SELECT [] FROM [] WHERE [] OP (SELECT...)

## Exists
exists ou note exists

## RIGHT/LEFT JOIN
Les jointures définies 

Les GROUP BY
Les HAVING (après le regroupement)
ORDER BY [] asc/desc,..., [] asc/desc

Modèle d'exécution complète de la machine SQL
FROM
WHERE
SELECT
GROUP BY
HAVING
UNION, INTERSECT, MINUS
ORDER BY

