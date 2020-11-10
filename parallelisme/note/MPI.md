Exercices?

## Lancement de MPI
MPI_Init(&argc, &argv);

## Définition du rang de chaque nœud
MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

## Définition du nombre de processus
MPI_Comm_size(MPI_COMM_WORLD, &nProc); 

## Fin de MPI
MPI_Finalize();

## permet de recevoir les données d'un autre processeur
MPI_Recv();
MPI_IRecv();
MPI_SRecv();
MPI_BRecv();

## permet d'envoyer les données à un autre processeur
MPI_Send();
MPI_ISend();
MPI_SSend();
MPI_BSend();

## attente de la completion locale
MPI_Wait

## attente de la completion locale
MPI_Test

## structure permettant d'obtenir le status d'un transfère (envoie)
MPI_Status

Completion locale: quand un espace de mémoire de partage peut-être retirer sans problème
Completion globale: quand tout les processus impliqué dans la communication on eu leur completion locale

Un routine est bloquante ssi elle attend la completion locale avant de se terminer et de permettre au programme de poursuivre.

## Enveloppe
	- Source/destination
	- tag
	- communicateur

MPI_ANY_SOURCE: v.g. permettant de recevoir s'affranchir de la source à la reception.

Le tag: élément numérique permettant d'identifier les messages (pour ainsi créer des cannaux dans un même groupe d'envoie)

MPI_ANY_TAG: v.g. permettant de s'affranchir du tag à la réception.

## MPI_Status
- MPI_SOURCE: la source du message
- MPI_TAG: le tag attaché au message
- MPI_ERROR: erreur si un problème a été rencontré lors de la communication

## MPI_Bcast()
Permet à tout les processus de partager rapidement les données.

## MPI_Barrier
methode permettant de synchroniser tout les processus

<!-- Les Threads -->
## Thread
Objet à qui on passe un callable

## thread.join()
Retiens le thread appellant jusqu'à ce que le processus appelé aye terminé.

## future
Structure de donnée permettant la récupération asynchrone d'une donnée.

## compare exchange
Permet un échange de valeur sans qu'un autre processus ne puisse accéder à la mémoire.

## variable condition
permet de mettre un ou plusieurs threads en attente jusqu'à ce qu'une condition soit remplie.
