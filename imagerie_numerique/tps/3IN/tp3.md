## Exercice 1
(a)
100x100= 10'000 pixels
256= 2^8 = 8 bits/pixel
finaly= 80'000 bits or 10'000 bytes

(b)
100x100= 10'000 pixels
4= 2^2 = 2 bits/pixel
finaly= 20'000 bits or 2'500 bytes

So a is four times bigger than b

## Exercice 2
Sampling: Cut distance by a regular step (chosing the result for some points)
Quantization: Cut by amplitude by (in)regular step (define an ensemble smaller)

## Exercice 3
Etape:
- faire un plot 3D du sampling et de quantization

## Exercice 4
- faire une fonction qui encode selon n bits (n <= 8)
- faire une fonction qui génère un gradient image (gray scale)
- afficher encoding de 7, 5, 3, 2, 1 pour gradient et lena.png (5 images + originale) 
## Exercice 5
(a)
- Créer une fonction PSNR = 10*(log_10((max(f(x,y))^2))/MSE)
- lena en gray scale 
- faire 10 bruit gaussiens de lena (zero-mean et sigma 25)
(b)
- pour tout noisy: PSNR avec original puis faire une moyen de tout les PSNR
(c)
- somme des 10 images pixel par pixel divisé par 10 (frame averaging)
(d)
- PSNR original et le frame averaging
- Dans quel condition frame averaging marche (pas)

## Exercice 6
(a)
- ouvrir reference et noisy 
- plot de 2x4 (original, Red, Green, Blue)
- Test PSNR pour voir si les canaux de couleur son affecté équitablement
(b)
- downsample 2 fois et unsampling back la référence
- Calculer le PSNR unsampled avec reference
(c)
- Comme b mais avec une grayscale image
- Pourquoi le PSNR est plus grand quand on fait à partir du gray scalPourquoi le PSNR est plus grand quand on fait à partir du gray scale (l'ex 5 peut expliquer)
