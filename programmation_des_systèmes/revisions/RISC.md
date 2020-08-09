processeur RISC
===============

Architecture cherchant à optimiser les performances en implémentant des instructions simples et optimisées.
Laisse le compilateur responsable d'une part des performances.

Éléments clés:
* Instructions:
	* simples
	* pas de division
	* en un cycle
* Pipelines:
	* instructions divisibles en sous-étapes
	* fetch-decode-execute
* Registres:
	* registres à usage général
	* registres comme paramètre d'entrée sortie souvent
* Architecture Load/Store:
	* Les instructions marchent uniquement sur les données des registres
	* Transfère avec la mémoire externe par des instructions spécifiques
