import numpy as np
from utils.maths_func import repartition_valeurs

# TODO : Afficher ou non toutes les données de l'équation avant la correction
afficher_tous_infos_terminal = True

# A = −9 : 1 : 9 = {−9, . . . , −1, 0, 1, . . . , 9}.
A = np.arange(-9, 9, 1).tolist()

# point accordés
point_gagne = 0.5

# Probabilités des deux thèmes
p_equation = 1
p_integration = 0

# Probabilité des différents types  1 : delta < 0 | 2 : delta = 0 | 3 : delta > 0
p_type_1 = 1 / 5
p_type_2 = 2 / 5
p_type_3 = 2 / 5

# Probabilité lorsque delta > 0 pour les deux cas
p_equation_delta_sup_3_1 = 1 / 2
p_equation_delta_sup_3_2 = 1 / 2

# Probabilité de Z pour delta > 0, la variable aléatoire à valeur dans E ici A (de cardinal 18)
p_Z_egal_1 = 1 / 2
p_Z_different_1 = 1 / (2 * 17)

# Probabilité de X pour delta = 0, la variable aléatoire à valeur dans E+ ici A+ (de cardinal 18)
p_X_egal_1 = 1 / 2
p_X_different_4_9 = 1 / 6
p_X_different_autres = 1 / (6 * 6)

# Probabilités des fonctions d'intégration
p_puissance = 0.5
p_trigonometrie = 0.25
p_logarithme = 0.25

# Probabilités de la fonction d'intégration : puissance
p_puissance_1 = 0.5
p_puissance_2 = 0.5

# Probabilités de la fonction d'intégration : trigonometrie
p_trigonometrie_1 = 1 / 3
p_trigonometrie_2 = 1 / 3
p_trigonometrie_3 = 1 / 3


# Ne pas toucher
p_equation, p_integration = repartition_valeurs([p_equation, p_integration])
p_puissance, p_trigonometrie, p_logarithme = repartition_valeurs(
    [p_puissance, p_trigonometrie, p_logarithme]
)
p_puissance_1, p_puissance_2 = repartition_valeurs([p_puissance_1, p_puissance_2])
p_trigonometrie_1, p_trigonometrie_2, p_trigonometrie_3 = repartition_valeurs(
    [p_trigonometrie_1, p_trigonometrie_2, p_trigonometrie_3]
)
