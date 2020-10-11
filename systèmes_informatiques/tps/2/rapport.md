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

## La librairie openssl

