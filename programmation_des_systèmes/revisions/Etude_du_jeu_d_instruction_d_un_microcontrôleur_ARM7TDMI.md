Le microcontrolleur ARM7TDMI
============================

Pourquoi TDMI
T: jeu d'instruction Thumb
D: debbugger hardware JTAG
M: multiplicateur rapide
I: macrocell ICE embarqué (debug)

Type de processeur:
* [RISC](RISC)
* [ARM](ARM)

## Instruction ARM

### Les conditions
EQ= equal
NE= not equal
CS= carry set (=1)
CC= carry clear (=0)
MI= minus
PL= plus
GT= greater than
LE= less or equal
AL= always
VS= V set (=1)
VC= V clear (0)
HI= higher
LS= lower or same
GE= greater or equal
LT= less than
exemple:
ADDVS R8,R9,R10 R8= R9+R10 si V=1

### Les drapeaux
SignedOveflow: la somme des deux nombres positive est négative (V)
UnsignedOverflow: dépassement de capacité nonsigné (C)
Zero: le resultat d'une opération est nul (Z)
Negative: le résultat d'une opération est négatif (N)

[règles](règles):
Le drapeau C suppose une arithmétique non signé
Le drapeau V suppose une [arithmétique_en_complément_à_deux](arithmétique_en_complément_à_deux)

### instructions de manipulation de données entre registres:
[déplacement](-déplacement) (MOVE)
[instructions_arithmétiques](-instructions_arithmétiques)
[instructions_logiques](-instructions_logiques)
[instructions_de_comparaison](-instructions_de_comparaison)
[instructions_de_multiplication](-instructions_de_multiplication)
[instructions_de_branchement](instructions_de_branchement)
[instructions_load_store](instructions_load_store)

[mode_d_adressage](mode_d_adressage)
[transferts_de_multiples_registres](transferts_de_multiples_registres)
[La_pile](La_pile)
[instruction_swap](instruction_swap)
[instruction_d_interruption_logicielle](instruction_d_interruption_logicielle)
[instructions_et_cpsr](instructions_et_cpsr)
[instructions_coprocesseur](instructions_coprocesseur)
[instruction_LDR_ou_ADR](instruction_LDR_ou_ADR)
[instructions_conditionnelles](instructions_conditionnelles)
