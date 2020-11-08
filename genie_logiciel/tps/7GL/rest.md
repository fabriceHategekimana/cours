C'est quoi REST?
=================

REST= REpresentational State Transfer
Six contraintes:
Interface uniforme


Basé ressource: 
on parle plus de source que d'action
La représentation n'est pas la ressource
Une représentation est souvent en JSON ou en XML


## 1 Interface uniforme
HTTP verbs (GET, PUT, POST)
URIs (ressource name)
HTTP response (status, body)

## 2 Sans état
Le server ne contient pas l'état du client
Chaque requête contient assez d'information pour d'écrire un "état"
L'état d'une session est gardé chez le client

## 3 Client - Server
Une architecture client server
Une client n'aura pas toujours une connection directe avec un serveur.

## 4 Cachable
Les réponses (représentations) du serveur peuvent être mis dans des fichiers cach.


## 5 Système par couche
Il y a pas mal d'intermédiaires entre le client et le service.
Augmente la scalabilité.

## 6 Code On Demand
Server can temporarily extend client
Peut transmettre une logic à un client que le client peut exécuter.

https://openclassrooms.com/fr/courses/6573181-adoptez-les-api-rest-pour-vos-projets-web/6818136-definissez-des-requetes-et-reponses-typiques
