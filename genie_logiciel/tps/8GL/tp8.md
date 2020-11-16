C'est quoi un fil d'actualité:

definition:

- moi: C'est une page défilante qui propose les dernières sorties.
- wikitionary: Page d'un site web affichant en temps réel ses mises à jour de manièreantichronologique et sous la forme d'une liste dont les titres renvoient vers le contenu correspondant. 

Les titres renvoient vers le contenu correspondant.
Différent type d'objet:

LISTE A
- livre
- électronique
- meuble
- transport
- divers

objet:
	- Nom
	- propriétaire
	- prix
	- description
	- labels
	- faculte

`Abstract factory:` Fil d'actualité:
	- générateur par:
		- type d'objet
		- par faculté
		- par prix

`Simple facory:`  ObjectTypeFactory
	- LISTE A
	 
`Simple facory:` FacultyFactory 
	- Droit
	- Sciences
	- Médecine
	- Lettres
	- Théologie
	- Psychologie 
	- Traduction 
	- Économie 
	- Centres 

`Simple facory:` PriceFactory 
	- SELECT objet from Objets where price between a b
	
