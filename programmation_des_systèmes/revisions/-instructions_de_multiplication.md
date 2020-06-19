Instruction de multiplication
MLA{<cond>}{S} Ed, Rm, Rs, Rn
MUL{<cond>}{S} Rd, Rm, Rs

multiplication longue
Syntaxe:
<instruction>{<cond>}{S} RdLo, RdHi, Rm, Rs
SMLAL
SMULL
UMLAL
UMULL

règles:
Après l'exécution d'une multiplication, on doit attendre un cycle supplémentaire avant de pouvoir effectuer une nouvelle multiplication
