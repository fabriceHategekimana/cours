Université de Genève

1. Expliquer l’interprétation géométrique de la méthode des moindres carrés. ([géo_moindre_carrés](géo_moindre_carrés))
2. Enoncer et démontrer le théorème sur la factorisation QR réduite. ([facto_QR](facto_QR))
3. Définir la réflexion de Householder et en donner quelques propriétés. Expliquer comment calculer, pour un vecteur v donné, une telle réflexion H pour que Hv = αe1 , où e1 =(1, 0, . . . , 0)T . ([refl_Householder](refl_Householder))
4. Expliquer les rotations de Givens et leur utilisation pour la décomposition QR. ([rot_Given](rot_Given))
5. En supposant que le rang de la matrice est maximal, présenter trois algorithmes pour la résolution du méthode des moindres carrés (Cholesky pour les équations normales, Gram–Schmidt ou Householder pour QR). Quels sont leurs coûts ? ([3algo_moindre_carré](3algo_moindre_carré))

VII.

Équations non-linéaires

6. Définir la méthode de la bissection. Expliquer sa convergence. ([bissection](bissection))
7. Expliquer comment on peut utiliser une méthode des points fixes pour résoudre des équations non-linéaires. ([co_point_fixe_pour_equa_non_lin](co_point_fixe_pour_equa_non_lin))
8. Enoncer le théorème du point fixe de Banach. Donner un exemple d’une fonction qui est une contraction. ([point_fixe_Banach](point_fixe_Banach))
9. Définir la notion de la convergence d’ordre m. Donner deux exemples qui ont des ordres différents. ([convergence_orde_m](convergence_orde_m))
10. Comment peut-on calculer l’ordre de convergence pour une méthode des points fixes ? Expliquer à l’aide d’un développement de Taylor. ([ordre_convergence_points_fixes](ordre_convergence_points_fixes))
11. Définir les méthodes de Newton scalaire et vectorielle. Expliquer les du point de vue des approximations linéaires. ([Newton_scalaire_vectoriel](Newton_scalaire_vectoriel))
12. Expliquer la méthode de la sécante et comparer avec la méthode de Newton. ([méthode_sécante](méthode_sécante))
13. Calculer l’ordre de convergence pour la méthode de Newton vectorielle à l’aide d’un développement de Taylor. ([ordre_convergence_Newton](ordre_convergence_Newton))
14. Pour une fonction vectorielle f : Rn → Rn , démontrer la convergence quadratique de la méthode de Newton en précisant les hypothèses et les lemmes nécessaires. (convergence_quadratique_Newton)
15. Qu’est-ce qu’un problème de moindres carrés non-linéaire ? Donner deux méthodes pour résoudre un tel problème. Pour quels problèmes ces deux méthodes deviennent-elles identiques ? ([moindre_carré_non_linéaire](moindre_carré_non_linéaire))
16. Expliquer la méthode de Gauss–Newton ainsi que son implémentation. ([Gauss_Newton](Gauss_Newton))

VIII.

Equations différentielles ordinaires

17. A partir des formules de quadrature, expliquer comment obtenir les méthodes explicites d’Euler et de Runge pour l’équation différentielle y ′ (t) = f (t, y(t)) et montrer leur ordre. ([explicite_Euler_Runge](explicite_Euler_Runge))
18. Expliquer comment se ramener au cas autonome pour étudier l’ordre de convergence des méthodes de Runge-Kutta à s étages. Développer en série de Taylor la solution exacte. ([ordre_convergence_Runge_Kutta](ordre_convergence_Runge_Kutta))
19. Expliquer l’ordre d’une méthode de Runge–Kutta à s étages. Montrer que l’erreur globale d’une méthode d’ordre p est ≤ Chp . De quoi dépend la constante C ? ([ordre_Runge_Kutta_s_étages](ordre_Runge_Kutta_s_étages))
20. Expliquer les méthodes de Runge–Kutta à s étages implicites. Expliquer comment obtenir les méthodes du point milieu et du trapèze, et montrer leur ordre. Montrer que l’ordre d’une méthode de Runge–Kutta à s étages explicite ne peut pas dépasser s. ([Runge_Kutta_s_étages_implicite](Runge_Kutta_s_étages_implicite))
21. Expliquer le domaine de stabilité des méthodes de Runge-Kutta. Montrer à quelle condition sur θ la méthode theta est A-stable. Expliquer l’interêt des méthodes A-stables. (domaine_stabilité_Runge_Kutta)
22. Etudier la stabilité des méthodes d’Euler explicite et implicite pour le problème de la chaleur_discrétisé en espace en dimension 1. Quelle méthode est recommandée pour un problème_raide ?_(stabilité_Euler_explicite_implicite)

IX.

Valeurs et vecteurs propres

23. Enoncer et démontrer le théorème de Gerschgorin. Expliquer son utilité pour le calcul numérique des valeurs propres._([théorème_Gerschgorin](théorème_Gerschgorin))
24. Expliquer le théorème sur la différentiabilité des valeurs propres simples. Donner une formule_pour la dérivée λ′ (0) de λ(ε) par rapport à la perturbation A(ε) = A + εC et expliquer son_utilité pour le calcul numérique de la valeur propre en question.([différentiabilité_valeurs_propres_simples](différentiabilité_valeurs_propres_simples))
25. Définir la condition absolue κ d’une valeur propre simple. Quelle est le lien entre la condition_et la dérivée d’une valeur propre par rapport à une perturbation ? Donner des exemples d’une_valeur propre (i) bien conditionnée, (ii) mal conditionnée, (iii) non différentiable par rapport_aux petites perturbation._([condition_absolue_valeur_propre_simple](condition_absolue_valeur_propre_simple))
26. Expliquer l’algorithme pour la méthode de la puissance._([méthode_puissance](méthode_puissance))
27. Expliquer la méthode de la puissance inverse et sa convergence._([méthode_puissance_inverse](méthode_puissance_inverse))
28. Expliquer la décomposition SVD._([décomposition_SVD](décomposition_SVD))

