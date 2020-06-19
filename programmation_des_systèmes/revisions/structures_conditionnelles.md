Les structures conditionnelles
==============================

.if une expression
Si l'expression est non nulle alors le code est inséré dans le programme à assembler
on peut utiliser .else et .elseif

Il existe des instructions construites sur ce modèle:
.ifdef symbole	si le symbol est défini
.ifeq		si l'expression est nulle
.ifge		si plus grand ou égal à zéro
.igt		si (strictement) plus grand
.ifle		si plus petit ou égal
.iflt		si plus petit

