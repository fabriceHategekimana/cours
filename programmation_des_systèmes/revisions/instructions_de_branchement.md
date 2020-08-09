Instruction de branchement
==========================

Syntaxe:
B{<cond>} label
BL{<cond>} label
BX{<cond>} Rm
BLX{<cond>} label | Rm

[règles](règles):
Les instructions BX et BLX permettent de changer l'etat du processeur selon que l'adresse est paire ou impaire.
Ainsi, cela permet de faire des appels de sous-routine

