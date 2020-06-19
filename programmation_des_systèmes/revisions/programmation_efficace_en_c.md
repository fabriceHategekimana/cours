Programmation efficace en c
===========================

But, avoir un code qui:
* s'exécute le plus rapidement possible
* qui est aussi compacte que possible

## Allocation de registre
Le compilateur essaye d'allouer le moins de registre possible pour les variables.
Lorsque ce nombre de variable en cours d'utilisation dépasse le nombre de registre, la pile est utilisée.
préférer les entiers non signés lorsqu'on divise (la division par la droite entraine un arrondissement vers le bas)
L'utilisation de la pile ralenti le processus.

But:
* minimiser l'utilisation de la pile
* s'assurer que les variables les plus fréquemment utilisées sont stockées dans les registres.

Attention: les chars sont non-signés pour l'ARM7 (alors qu'en c en général, c'est signé)
Il faut donc éviter d'utiliser un caractère comme variable de compteur de boucle avec une condition du type.

rappel: il faut privilégier les types int ou long des types char ou short (qui sont à éviter absolument)

[règles](règles):
1 digit en hexadécimal vaut 4 digit en binaire
préférer les entiers non signés lorsqu'on divise (la division par la droite entraine un arrondissement vers le bas)

a= 0x00000000
b= 0x000000ff
a and b= 0x00000000

conversion en argument de variable
* passage de paramètre large (wide): on suppose les données sur 16 bits et on les modifie pas
* passage de paramètre étroit (narrow): on force les valeurs à être sur 16 bits en étendant le signe des données aux 32 bits des registres 

fonction appelante= paramètre étroit
fonction appelé= paramètre large
selon les valeurs retourné par le compilateur, c'est la fonction appelante ou appelé qui se charge de mettre les données à une bonne forme

## Les boucles
les trois instructions pour faire une boucle:
ADD (incrément)
CMP (comparaison)
BCC (branchement)

parfois même deux instructions suffisent
soustraction avec maj du cpsr
Une instruction conditionnelle de branchement

C'est ce qu'on utilise pour optimiser une boucle

## Les boucle avec nombre itération variable
Si on sait que N>0, alors on utilise do while en c.
Cela évite un test au début de la boucle

## Déroulement de boucle
Une boucle coûte 2 instructions et 4 cycle par boucle (1 cylce pour la soustraction +3 cycles pour le branchement)
Pour diminué ça on a un technique:
Déroulement de la boucle: on recopie le même schéma pour éviter la soustraction et le branchement.
Pas toutes les boucle donnent une gain de cycle quand on les déroule.
C'est pourquoi on s'intéresse principalement aux boucles qui sont utilisées souvent.
Les boucles avec un grand corps ne sont pas beaucoup plus efficace lorsqu'elles sont déroulées.
À moins de 1% de l'augmentation des performances ça sert à rien de dérouler.
Préférer des structures de données qui génèrent des multiples de 2, 4, etc. et qui permettent le déroulement des boucles.

## Convention du passage des paramètres en C
r0-r3: Registre pour le passage de paramètre ainsi que la valeur de retour
r4-r8: Registre d'usage général pour la fonction. Les valeurs de ces registres doivent être sauvées/restaurées pour contenir la même valeur au début et à la fin de l'exécution de la routine.
r9-r11: idem que les registres r4-r8 sauf si certaines options de compilations sont activées.
r12: un "scratch register", la fonction peut l'utiliser sans se soucier de le restaurer
r13: le registre de pil, stack registre, sr, (full descending)
r14: le registre de lien, link register, lr
r15: le compteur de programme, program counter, pc

[règles](règles):
Une bonne habitude est de limiter le nombre de variables locales à 12.
Si le compilateur doit utiliser la pile, il le fait pour les variables le moins fréquemment utilisées.
Le compilateur sélectionne les variables qui se trouvent dans le plus grand nombre de boucles imbriquées.

Le langage C définit le mot clé register pour indiquer qu'une variable doit (si possible) être sauvée dans un registre.

## Appels de fonctions - arguments
ARM Procedure Call Standar (APCS): définit comment les arguments sont passés aux fonctions et comment sont gérées les valeurs de retour.
les registre r0-r3 reçoivent les 4 premiers arguments.
Les autres arguments sont placés sur la pile (full descending)
Les arguments codé sur deux mots sont passés dans deux registres consécutifs et retourné dans r0,r1

[règles](règles):
Les fonctions qui utilisent au maximum 4 arguments sont plus efficace.
si une fonction a plus de 4 arguments, il vaut mieux les regrouper dans une structure et passer en argument un pointeur sur la structure.

[questions](questions)
