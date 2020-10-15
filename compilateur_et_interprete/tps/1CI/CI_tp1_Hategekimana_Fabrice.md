Compilateur et interprète
==========================

type de données:

* variables
* symboles réservés (=, +, *, ',')
* entier
* réel


## Pseudo code

```
	entree
	if estVariable(entree) then
		print(entree+" est une variable")	
	elif symboleReserve(entree) then
		print(entree+" est un symbole réservé")	
	elif entier(entree) then
		print(entree+" est un entier")	
	elif reel(entree) then
		print(entree+" est un reel")	
```

## Fonctions principales
### C'est quoi une variable?
Commence par une lettre. => isLetter()
Le reste peut être des numéros ou des lettre => isLetterNumber() (utilise is letter()et is number)

### C'est quoi un symbole réservé
C'est "=,+,*,'" => isReserved()

### C'est quoi un entier
Composée de chiffre => isNumber()

### C'est quoi un réel
A au moins et au plus un point => onePoint()
Composé de chiffre => is number()

## Fonctions secondaires
### isLetter()
for symbole in mot if no in alphabet false else true

### isNumber()
for symbole in mot if no in number false else true

### isLetterNumber()
for symbole in mot if no (isnumber() or isLetter()) false else true

### isReserved()
for symbol in mot if no in reserved false else true

### onePoint()
if count(mot, ".") != 1 false else true
