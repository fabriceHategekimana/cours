Linklayer (fiabilise la liaison: s'assurer que l'info passe)
============================================================

[questions](questions)

voc: 
	* trame= message donné (de donnée ou de contrôle) p.11

On développe des logiciels de détection ou correction d'erreur

## protocoles ARQ
1. [Stop_and_Wait](Stop_and_Wait)
2. [Go_Back_N](Go_Back_N)
3. [Selective_Repeat](Selective_Repeat)

## Automatic Repeat Request
On va répéter la transmission s'il y a une erreur

## Réseaux locaux - MAC
Broadcast: problème => collision. Dans ce cas, les stations reçoivent la superposition des deux signaux
Le protocole ARQ retransmettent le signal si ça ne marche pas.
Nécessite une transition 

Medium Access contrôle (MAC) Sous couche du link layer qui transmet l'adresse que lui donne le linklayer de façon synchronisé.

## LAN:
connexion privé (on maîtrise l'accès au canal.)
délai de transmission faible (pratique pour détecter les collisions)

On a des réseaux point to point, mais on utilisera les réseaux à diffusion (broadcast) pour traiter les cas de collision.
On va voir le protocole ALOA

def: transmission anisotropique = la même propagation dans toute les direction
La probabilité s'appuie sur la loi de Bernoulli
Souvent définit comme une probabilité "sans mémoire" (cad qu'on a pas besoin des événements précédents ne comptent pas)

Slotted ALOHA, les emetteurs sont tous synchronisé

On suppose que la superposition des émission suit un processus de poisson.

débit effectif: le nombre de trames qui ont pu être transmises.
