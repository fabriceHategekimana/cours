## Algèbre relationnelle
Chaque opérateur prend en entré une relation et met en sortie une relation.


Le SGBD respectent les propriétés ACID.
Toute transaction T2 ne doit pas modifier une chose si elle a été modifiée par T1 sans être validée.
Toute transaction T ne dois pas lire des valeurs non confirmées et manipulées par d'autres transactions.
Aucune transaction ne peut modifier une valeur lue par une autre transaction avant que cette dernière ne soit validée.
