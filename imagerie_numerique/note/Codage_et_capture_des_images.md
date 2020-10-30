La caméra 3-CCD
=================

Chaque pixel est prise dans chaque canal

utilise la demosaic interpolation
![3_ccd_fonction](../../images/3_ccd_fonction.png)

Constantes:
f	fonction continue
H	fonction de blur
P	morceau d'image
Q	une fonction de quantization

L'oeil humain est plus sensible au vert du spectre color.

## Retour sur l'interpolation mosaic du 3_ccd_fonction
En faisant une moyenne des pixels existant pour créer les manquant (la fonction de moyenne peut changer selon l'écart d'intensité entre les pixels voisins pour éviter une moyenne qui mettrait trop de "flou" entre les pixels)
