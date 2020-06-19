syntaxe du langage assembleur
=============================

## syntaxe générale
<assembleur>= epsilon | <ligne> <assembleur>
<ligne>= <statement>
<statement>= <label> <statement> | <label> <key_symbol>
<label>= <symbole>:
<key_symbol>= .<directive_d_assemblage>
<symbole>= composé d'au moins un caractère, de chiffre et des trois symbole . _ $
<directive_d_assemblage>= instruction connues du langage assembleur

## syntaxe des nombres
* binaire: 0b<nombre_avec_0_et_1>
* octal: 0<nombre_avec_des_chiffres_de_0_à_7>
* hexadecimal: 0x<nombre_avec_des_chiffres_de_0_à_F>
* décimal: commence avec un digit différent de 0
* négatif: commence par un -
* virgule flottante: 0e(+/-)(integer part)(.)(fractional part)(E/e)(+/-)(exponent)

Les sections:
Sont définit par des directives assembleurs.
* .text (contient code et constantes)
* .data (contient les variables)
* .bss

