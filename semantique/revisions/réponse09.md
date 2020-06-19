sémantique d'un véhicule programmable
=======================================

ch 5 p.11

Pour les programme comme succession d'instruction.
La relation est étendue
(Direct x Coord) x T_{epsilon,_::_}(M) x Direct x Coord
Il faut dans une sémantique par pas que:
(Direct x Coord) x T_{epsilon,_::_}(M) x Direct x Coord x T_{epsilon,_::_}(M)

Les mouvements possibles: M={L,R,F}
Un programme est une liste construite avec (concaténation _::_, liste vide epsilon) de telles instructions.
Les programmes sont donc des termes:
T_{espilon,_::_}({L,R,F}) = T_{epsilon,_::_}(M)

## Fixer un domaine sémantique
position appartient Direct x Coord
Direct= {-1,0,1}^2
Coord= Z x Z

<d,p>,m=><d,p>
transitions L, R, F 

## Définir des règles pour définir une sémantique d'évaluation
