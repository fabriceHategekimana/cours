Vue
===

Table logique obtenue à partir d'autre tables.
CREATE VIEW nom AS requête

But: Multiplier les représentations logiques et indépendance logique entre schéma et applications.

Procédé:
1. FROM substitué
2. SELECT substitué
3. WHERE substitué
4. GROUP BY ajouté

## Types (4)
contextuelle: nouvelle relation (contextuelle) à partir d'un ensemble de relation
interface: adapter les vues à l'application qui utilise la BD 
attributs calculés: La valeur d'un attribut est calculé avec les infos de la BD
déductive: Comme prolog (faits+règles= déduction; clauses de Horn)

Les vues modifiables n'ont pas de:
distinct
jointure
group by
connect by

## Commandes
INSERT INTO [] () VALUES ()
UPDATE [] SET []=[] WHERE []
DELETE FROM [] WHERE []
