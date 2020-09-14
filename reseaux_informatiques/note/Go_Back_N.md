2. Go_Back_N
============

On transmet N trames dans un tampon (un conteneur). On envoie maximum N trames par acquittement sinon, on attends.

fenêtre de transmission:
	Nombre de trame dans un tampons

Si nous avons une erreur ou un timeout, on doit renvoyer le tampon en entier.
Le récepteur, ne mémorise pas les données qui ne sont pas dans l'ordre.

[questions](questions)
