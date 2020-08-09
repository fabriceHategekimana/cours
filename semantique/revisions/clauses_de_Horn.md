Les clause de Horn
==================

formule atomique: P(t1,...,tn)
P 	prédicat (symbol)
ti	terme

litteral positif
une clause définie: règle if A alors B
connecteurs: and
A ou non B = A <- B
Comme on peut écrire H et G1 et ... et Gn
alors on peut écrire H ou non G1 ou ... non Gn
on a H <- (G1 et ... et Gn)

On peut donc programmer avec des:
* faits
* règles
* requêtes

La méthode de programmation:
On crée une théorie et on l'intérroge.
**Les clauses de Horn sont turing complet**
