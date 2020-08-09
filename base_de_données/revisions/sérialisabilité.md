Schedule= entrelacement des actions d'un ensemble de transactions, où les actions de chaque transaction sont dans l'ordre d'origine.
Les actions sont read et write
Un schedule complet contient aussi des commit et abort

État initial de la BD + Schedule complet -> état final de la BD

**Règles**:
Dans un schedule sérialisé, les transactions sont isolées
Si un graphe de précédence a un cycle, la transaction n'est pas sérialisable sinon n'importe quel ordre de schedule convient.

## Schedule sérialisable:
Schedule avec des transactions entrelacées, s'il existe un schedule sérialisé qui produit le même résultat

## Graphe de précédence
nœuds= transaction
arcs= précédences

la transaction Ti précède Tj (Ti->Tj) dans le graphe s'il y a une action de Ti qui précède et est en conflit avec une action de Tj:
Les deux transactions sont concurrentes
Tj agit sur les objets de Ti
Tj lit un objet de Ti

## Vérification de la sérialisabilité (2)
Optimiste: sérialisabilité vérifiée après les transactions pour décider d'avorter ou non
Pessimiste: éviter la non-sérialisabilité par des verrous au préalable
