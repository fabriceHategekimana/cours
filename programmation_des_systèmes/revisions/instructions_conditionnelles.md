Instructions conditionnelles 
=============================

Permettent de réduire la latence crée par les rupture de séquence.
exemple:
calcul du plus grand commun diviseur
while(a!=b)
{
 if (a>b) a-=b; else b-=a;
}
