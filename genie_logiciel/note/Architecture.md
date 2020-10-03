
## Architecture
Définition: Définit un haut niveau d'interaction avec l'utilisateur. On ne s'occupe pas du détail.

## La loi de Conway's
La structure d'une entreprise aura un impacte sur l'architecture de notre système.

## Principe de développement
YAGNI= "You aren't gonna need it"
KISS= "keep it simple, stupid" (se poser trois fois pourquoi, donc une fois à chaque réponse)
La loi de Demeter= Pour utiliser un composant, on doit avoir un minimum de connaissance de ce composant et connaître que les composant proche de celui-ci

Système quasi décomposable= (on peut décomposé chaque partie du système qu'on peut analyser séparément)

## Main architecture view
Logical view: Modèle objet du domaine
Process view: Comment le système évolue
Developpement view: Comment je dois faire en tant que développeur
Physical view: Comment ça marche sur une machine

Tout ça nous aide au scénario qu'on va présenter au client

Étape pour créer une architecture:
1. Non-Functiona Requirements
2. Tactics (pour chaque NFR, on doit trouver des tactiques pour y arriver)
3. pattern ([layered](layered), [pipe_and_filters](pipe_and_filters), [Broker](Broker), [publish_subscribe](publish_subscribe))

