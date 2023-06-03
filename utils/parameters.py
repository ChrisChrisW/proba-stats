import random

from utils.constant import A

def choose_parameter_excluding(excluded_values):
    """
    Fonction qui choisit un paramètre aléatoire parmi une liste de valeurs possibles, en excluant certaines valeurs.

    Args:
        excluded_values (float or list): Valeur(s) à exclure de la sélection.

    Returns:
        float: Le paramètre choisi.
    """
    if isinstance(excluded_values, list):
        valid_values = [x for x in A if x not in excluded_values]
    else:
        valid_values = [x for x in A if x != excluded_values]
    return random.choice(valid_values)

def choose_parameter_positive_only():
    """
    Fonction qui choisit un paramètre aléatoire parmi une liste de valeurs possibles, en ne sélectionnant que des valeurs positives.

    Returns:
        float: Le paramètre choisi.
    """
    valid_values = [x for x in A if x > 0]
    return random.choice(valid_values)