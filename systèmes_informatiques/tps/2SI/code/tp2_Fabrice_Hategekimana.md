TP2 Système informatiques
===========================

J'ai écrit "Le manuel disait: Nécessite Windows 7 ou mieux. J'ai donc installé Linux" dans un fichier "teste.txt"

Voila ce que j'ai trouvé avec les fonctions de hachage:

```bash
$ sha1sum teste.txt 
aa91cf14c329a5fe9b1158ae2665b39370f57e37  teste.txt
```

```bash
$ md5sum teste.txt 
120227d6118cfddbd21639644aa0884d  teste.txt
```

J'ai essayer avec echo

```bash
$ echo "Le manuel disait: Nécessite Windows 7 ou mieux. j'ai donc installé Linux" | sha1sum
0e74d338d620608c6f95e76ff609b0f8ca8c1472  -
```

```bash
$ echo "Le manuel disait: Nécessite Windows 7 ou mieux. j'ai donc installé Linux" | md5sum
692518661d39ed10735dd6dd1d296b71  -
```

Je ne sais pas pourquoi ça marche comme ça? BUG

## 2 La librairie openssl
J'ai lancé le code en exemple pour le man 3 EVP_DigestInit.
Ce code me permet de créer des digest de "hello world" et "Test Message" avec la fonction de hashage donnée.
```
./main md5
Digest is: ce73931d2b3da6e60bf18af27494c6cd

./main fabrice
Unknown message digest fabrice
```

## 3 Gestion des paramètres d'un programme
Les exemples proposés se divisaient en deux parties.
Le premier code nous permettait de donner un chiffre (en seconde avec l'indice t) et un nom (avec l'indice n)
Le second code nous permettait de donner les indices abc:d012 et d'établir des réponses les paramètres donnés.

## 4 Intégration: le programme à réaliser
Pour faire ce programme, je me suis inspiré des exemples pour le EVP de openssl et du getopt fait précédemment.
Le module getopt prends les options t et f en paramètre et donne les hash des fonctions en question.  
Mon Makefile est assez pauvre car il n'y a pas la nécessiter d'en faire un complex étant donné la taille du projet.

Voila quelques exemples d'utilisation.
```bash
$ ./hash tp2_Fabrice_Hategekimana.pdf
2fc021286c7be32103ddb3164a27ec672bfe885f
```

```bash
$ ./hash -f tp2_Fabrice_Hategekimana.pdf
2f6c20dcbc0235aa09f58736d6135a0e31071233           tp2_Fabrice_Hategekimana.pdf
```

```bash
$ ./hash -t md5 tp2_Fabrice_Hategekimana.pdf
fbaa3467a517b6d599e514af1d6eff1f
```

```bash
$ ./hash -ft md5 tp2_Fabrice_Hategekimana.pdf
e291d83cc178c084486025b84182402b           tp2_Fabrice_Hategekimana.pdf
```

```bash
$ ./hash -ft md5 tp2_Fabrice_Hategekimana.pdf
e291d83cc178c084486025b84182402b           tp2_Fabrice_Hategekimana.pdf
```
```bash
$ ./hash -ft sha256 main.c options.c hash.c
c3f372a052e7a2b1c0d9cd276383d155dd959cd3f5a70e9db538515c5d242829           main.c
2213c7728fa00a79cd8c8c028fe0d0e7942441d6108bedaf76c5958a5d6ce84b           options.c
8d3b264c0be80f1bffb54f854c5d5d7c63e81002358eff9e349f6f68a9c6f309           hash.c
```
