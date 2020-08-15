Université de Genève

I.

## Interpolation polynomiale
1. Enoncer et démontrer le théorème concernant l’existence et l’unicité du polynôme d’interpolation._([théorème_polynôme_interpolation](théorème_polynôme_interpolation))
2. Définir la formule de Lagrange pour son calcul. Estimer son coût en flops._([formule_Lagrange](formule_Lagrange))
3. Définir les différences divisées pour des points donnés. Enoncer et démontrer la formule de_Newton pour l’interpolation en ces points._([Newton_interpolation](Newton_interpolation))
4. Enoncer et démontrer le lemme mettant en relation les dérivées et les différences divisées. En_déduire et démontrer le théorème pour estimer l’erreur de l’approximation par un polynôme_d’interpolation.(lemme_dérivées_différences_divisées)
5. Définir les polynômes de Chebyshev. Esquisser quelques exemples._([polynômes_Chebyshev](polynômes_Chebyshev))
6. Définir les points de Chebyshev. Justifier pourquoi ils sont un bon choix pour des points_d’interpolation. Illustrer par le phénomène de Runge._([points_Chebyshev](points_Chebyshev))
7. Définir l’interpolation d’Hermite. Expliquer son calcul à l’aide des différences divisées._([interpolation_Hermite](interpolation_Hermite))
8. Enoncer et démontrer le théorème pour estimer l’erreur de l’approximation par un polynôme_d’interpolation d’Hermite.([erreur_interpolation_Hermite](erreur_interpolation_Hermite))

II.

Analyse d’erreurs d’arrondi
9. Détailler la représentation des nombres machine en virgule flottante (comme vue en cours)_et définir l’epsilon de la machine. Exemplifier les définitions pour les nombres machine en_double précision._([représentation_virgule_flottante](représentation_virgule_flottante))

10. Expliquer l’arithmétique flottante et le phénomène d’annulation des chiffres._([arithmétique_flottante](arithmétique_flottante))
11. Donner un exemple de calcul susceptible d’annulation des chiffres ainsi qu’une reformulation_qui évite ce problème._([exemple_annulation_chiffres](exemple_annulation_chiffres))

III.

Condition et stabilité

12. Définir la condition (relative) d’un problème. Pourquoi la condition est-elle importante pour_des calculs numériques ?_([définition_condition](définition_condition))
13. Enoncer et démontrer le théorème pour la condition des problèmes différentiables._([condition_problèmes_différentiables](condition_problèmes_différentiables))
14. Définir la norme d’opérateur et donner un exemple concret._([norme_opérateur](norme_opérateur))
15. Définir la notion de la stabilité "forward". Quelle est la distinction entre la condition et la_stabilité ?_([stabilité_forward](stabilité_forward))

16. Définir la notion de la stabilité "backward". Montrer que la stabilité backward implique la_stabilité forward._([stabilité_backward](stabilité_backward))
17. Donner un exemple d’un problème bien conditionné et deux algorithmes pour le résoudre, un_stable et l’autre instable (avec démonstration)._(exemple_algorithme_stable_instable)
18. Donner un exemple d’un algorithme qui est stable en sens backward (avec démonstration)._(exemple_algorithme_stable_backward)

IV.

Intégration numérique

19. Définir les formules de quadrature à s étages et définir leur ordre._([quadrature_s_étages](quadrature_s_étages))
20. Pour s nœuds distincts donnés, montrer l’existence d’une formule de quadrature d’ordre ≥ s._([montrer_existence_quadrature_ordre_supérieur](montrer_existence_quadrature_ordre_supérieur))
21. Expliquer la construction des formules de Newton–Cotes. Donner quelques exemples._([Newton_Cotes](Newton_Cotes))
22. Définir les formules symétriques. Enoncer et démontrer le théorème concernant l’ordre de
celles-ci.
23. Expliquer les formules de quadrature composées._([quadrature_composées](quadrature_composées))
24. Si une formule de quadrature est d’ordre p, énoncer et démontrer le théorème de l’erreur_globale de la quadrature en justifiant le lemme pour l’erreur locale à l’aide des développements_de Taylor._([théorème_erreur_globale](théorème_erreur_globale))
25. Enoncer et démontrer le théorème (ainsi que le lemme) disant que l’ordre d’une formule à s_étages est ≤ 2s._([théorème_ordre_s_étages_2s](théorème_ordre_s_étages_2s))
26. En utilisant le produit scalaire hp, qi des polynômes p et q, énoncer et montrer le théorème_sur l’existence des polynômes de Legendre._([théorème_polynôme_Legendre](théorème_polynôme_Legendre))
27. Enoncer et démontrer le théorème concernant les racines des polynômes de Legendre._([racines_polynôme_Legendre](racines_polynôme_Legendre))
28. Définir les formules de Gauss à s étages et montrer qu’elles sont d’ordre maximale._([Gauss_s_étages](Gauss_s_étages))
29. Démontrer que les poids des formules de Gauss sont positifs. Pourquoi la positivité est-elle_importante ? Comparer avec les formules de Newton–Cotes._([poids_Gauss_positif](poids_Gauss_positif))
30. Comment peut-on construire une matrice symétrique dont les valeurs propres donnent les_nœuds d’une formule de Gauss ?_([matrice_symétrique_noeuds_Gauss](matrice_symétrique_noeuds_Gauss))

V.

Systèmes d’équations linéaires

31. Définir la condition d’une matrice inversible A. Donner quelques exemples des matrices qui_sont bien et mal conditionnées._([condition_matrice_inversible](condition_matrice_inversible))
32. Définir la condition de résoudre un système d’équations linéaires inversible._([condition_résolution_système_équation_linéaire_inversible](condition_résolution_système_équation_linéaire_inversible))
33. Expliquer le lien entre l’algorithme de Gauss et la décomposition LU d’une matrice._([algorithme_Gauss_décomposition_LU](algorithme_Gauss_décomposition_LU))
34. Enoncer et démontrer le théorème sur l’erreur backward d’un système d’équations linéaires_inversible et son résidu._([théorème_erreur_backward_linéaire_inversible](théorème_erreur_backward_linéaire_inversible))
35. Au premier ordre en εmach , montrer que la condition de résoudre un système d’équations_linéaires est bornée par 2κ(A)._([borne_condition_linéaire](borne_condition_linéaire))
36. Montrer l’existence de la factorisation de LU avec changement de pivot partiel en expliquant_en détail l’algorithme de son calcul pour une matrice de taille 5 × 5.([LU_changement_pivot_partiel](LU_changement_pivot_partiel))

VI.

Méthode des moindres carrés

37. Expliquer la méthode des moindres carrés. Enoncer et démontrer le théorème sur les équations_normales._([méthode_moidres_carrés](méthode_moidres_carrés))

