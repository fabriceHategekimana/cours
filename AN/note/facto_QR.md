2. Enoncer et démontrer le théorème sur la factorisation QR réduite. ([facto_QR](facto_QR))

![Factorisation qr](../images/Th_QR.png)

Soit A alors Il existe Q et R | A= QR

Cette factorisation a la particularité de simplifier la résolution par l'utilisation d'une matrice orthogonale

![Demo 1](../images/QR_demo01.png)
![Demo 2](../images/QR_demo02.png)

qj= aj-somme(i=1; j-1; prodscal(aj,qi)*qi) et on normalise qj

En changeant le sens on obtient:

aj= somme(i=1; j-1; prodscal(aj,qi)*qi)+~qj = somme(i=1; j-1; rij*qi+rjj*qj) rij= prodscal(aj, qi), rjj=norm(~qj)

