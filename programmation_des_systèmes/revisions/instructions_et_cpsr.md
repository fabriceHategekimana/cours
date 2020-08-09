instructions et cpsr
====================

Le jeu d'instruction ARM met à disposition **deux** instructions pour contrôler le registre cpsr.
Il s'agit d'instructions qui permettent de sauver et restaurer le contenu du registre d'état.

Syntaxe:
MRS{<cond>} Rd, <cpsr|spsr>
MSR{<cond>} <cpsr|spsr>_<fields>, Rm
MSR{<cond>} <cpsr|spsr>_fields, #immediate

MRS
MSR
MSR
