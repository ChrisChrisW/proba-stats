import numpy as np
from utils.maths_func import repartition_valeurs

# A = −10 : 05 : 10 = {−10, −9.5, −9, . . . , −1, −0.5, 0, 0.5, 1, . . . , 9, 9.5, 10}.
A = np.arange(-10, 10, 0.5).tolist()

# Probabilités des deux thèmes
p_equation = .5
p_integration = .5

# Probabilités des fonctions d'intégration
p_puissance = .5
p_trigonometrie = .25
p_logarithme = .25

# Probabilités de la fonction d'intégration : puissance
p_puissance_1 = .5
p_puissance_2 = .5

# Probabilités de la fonction d'intégration : trigonometrie
p_trigonometrie_1 = 1/3
p_trigonometrie_2 = 1/3
p_trigonometrie_3 = 1/3


# Ne pas toucher
p_equation, p_integration = repartition_valeurs([p_equation, p_integration])
p_puissance, p_trigonometrie, p_logarithme = repartition_valeurs([p_puissance, p_trigonometrie, p_logarithme])
p_puissance_1, p_puissance_2 = repartition_valeurs([p_puissance_1, p_puissance_2])
p_trigonometrie_1, p_trigonometrie_2, p_trigonometrie_3 = repartition_valeurs([p_trigonometrie_1, p_trigonometrie_2, p_trigonometrie_3])
