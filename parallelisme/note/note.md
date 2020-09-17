Paralellisme
============

examen 1/3 TP + 2/3 Oral
Oral: pas de préparation, liste de questions fournies

C'est quoi le parallélisme?

## 1.1 Concepts et définition
### **Def**: Le parallélisme c'est la résolution d'un `même problème` par la `coopération` de plusieurs processeurs.

Le but qu'on va explorer dans ce cours C'est le gain de performance que le parallélisme apporte.

Le parallélisme est naturel: on est habitué à collaborer. Les gens ont déjà pensés à faire ça pour les math et la physique.
Les premières machines avec des composants de calcul activables en même temps.

Si c'est naturel, c'est difficile à gérer (coordination à imposer)

À l'époque, le matériel n'était pas fiable et surtout un manque de modèle de calcul qui permet d'exploiter ces machines.

Problème résolut par l'architecture de von Neuman ("la machine séquentielle" par abus de langage).
Permet le développement des hardware et le développement des programmes car cela a donnée un modèle de calcul. Le parallélisme est mis de côté.
Les besoins de performances de calcul ne font qu'augmenter.

Les machine actuellement les plus puissantes offrent 200 [pflops](pflops)/s de puissance. Pour 2 gigawatt par machine (la puissance pour faire fonctionner 40 jet d'eau de Genève)

vers 1990 High performance computing ([HPC](HPC)) indique que le parallélisme est une méthode de performance.
Aujourd'hui si on a plus de 100 processeur, on peut parler de HPC.

### Limite de l'architecture de Von Neuman
* On peut accélérer la vitesse d'horloge de notre machine. Mais ça consomme plus d'énergie et produit beaucoup de chaleur.
* Memory Wall, Von Neuman (bottleneck= bouteille d'étranglement) 
	* ce qui vide la batterie est le transport des données du CPU à la mémoire (1000x plus gourmand que les calculs, en plus c'est lent de base)
	* roofline model:
	![roofline_model](../images/roofline_model.png)	
	* Le plateau représente la puissance maximale. La pente montre que la bande passante est limitée.

### Historique du parallélisme
1. ILLIAC 1970 météo (qui est une machine qui faisait du parallélisme) (prévu avec 256 pro, mais construite avec 64 seulement, et pour 4x le prix)
2. Rapidement supplantée par les [machines_vectorielles](machines_vectorielles)
3. Dès les années 1990, réaparition des machines parallèle: SIMD, MIMD, SNP,... (plein de producteurs américains survivant aux subvention) On supplenté les [machines_vectorielles](machines_vectorielles)
4. Dans les années 2000, l'expantion des clusters -> démocratisation du parallélisme
5. Par la suite les GPU se sont aussi développer et imposés pour le HPC.
6. Cloud computing / GRID

Nouveau classement: GREEN COMPUTING (=voir le bon rapport puissances/consomation)

## 1.2 Où trouver des performances?
1. Améliorer la technologie (actuellement, on utilise du silicium comme semi-conducteur)
2. Améliorer l'architecture
3. Optimiser l'application

La fréquence max n'augmente plus depuis 2004
La miniaturisation permet de mettre plus de transistor dans une surface donnée. On est actuellement à 7 nanomètres, on annonce jusqu'à 3 nanomètres
	Limite: effet tunnel.
