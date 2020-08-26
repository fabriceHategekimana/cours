

Exercice 1
==========

## i) Fonctions des bus:
	Donnée: transport des données entre les différentes instances
	Adresses: pointeur sur les différentes destination
	Contrôle: bus qui permettent de spécifier l'action en cours (lecture, écriture, piste libre, etc.)
	
## ii) Description du plan d'adressage
	S1= NOT A9 AND NOT A10
	S2= NOT A8 AND NOT A10
	S3= NOT A8 AND NOT A9
	Donc:
	S1= A0-A8
	S2= A0-A7 AND A9
	S3= A0-A7 AND A10
	
Exercice 2
==========
	**Il y a quatre types de pile:**
	1. vide montante EA
	2. vide descendante ED
	3. pleine montante FA
	4. pleine descendante FD
	
	**Il y a différent mode d'adressage:**
	On a les bytes, halfwords et words
	On a aussi:
	1. Little Endian (les bits les plus significatifs ont la plus petite adresse)
	2. Big Endian (les bits les plus significatifs ont la plus grande adresse)

Exercice 3
==========
	1) on compare r0 et 3
	2) si r0 == 3 alors r0++
	3) Sinon r1= r1+2	
	4) Si r1 == 0 r2= r2+3

if(r0 == 3){ 
	r0++;
}
else{ 
	r1= r1+;
	if(r1 == 0){ 
		r2= r2+3;
	}
}

CMP 	r0,#3

Exercice 4
==========
r1= 0xA0FF9876
r1= 0x2345FA12 et r2= 0x00100008 
r1= 0xDF0C6320 et r2= 0x00100004
r1= 0xFFAA1000 et r2= 0x0010000C
r2= 0x2345FA12 et r1= 0x00100008

Exercice 5
==========
LDRB charge directement un byte de la mémoire dans un registre
LRSB fait comme LDRB mais met à jour le registre cpsr selon le registre de destination

Pas beaucoup d'information pour trouver l'opcode de l'instruction
