from fractions import Fraction

def format_fraction(value):
    """
    Convertit une valeur en fraction si elle est un nombre rationnel.
    
    Args:
        value (float): La valeur à convertir.
    
    Returns:
        Fraction or float: La valeur convertie en Fraction si c'est possible, sinon la valeur originale en tant que float.
    """
    fraction = Fraction(value).limit_denominator()
    return fraction if fraction.denominator != 1 else float(value)

def convert_to_fraction(value):
    """
    Convertit une valeur en fraction si elle est un nombre rationnel.
    
    Args:
        value (float or Fraction): La valeur à convertir.
    
    Returns:
        str: La valeur convertie en fraction ou en chaîne de caractères.
    """
    if isinstance(value, float):
        value = Fraction(value).limit_denominator()
    
    if isinstance(value, Fraction):
        return str(value)
    
    return str(value)

def repartition_valeurs(tableau):
    """
    Répartit les valeurs d'un tableau de manière proportionnelle pour obtenir une somme de 1.

    Args:
        tableau (list): Le tableau de valeurs à répartir.

    Returns:
        list: Le tableau réparti de manière proportionnelle.

    Examples:
        >>> valeurs = [0.2, 0.3, 0.1, 0.4]
        >>> resultat = repartition_valeurs(valeurs)
        >>> print(resultat)
        [1/6, 0.25, 0.083..., 1/3]
    """
    somme = sum(tableau)
    
    if somme == 1:
        return tableau
    
    if somme < 1:
        proportion = 1 / somme
        tableau_reparti = [valeur * proportion for valeur in tableau]
        return tableau_reparti
    
    if somme > 1:
        proportion = 1 / somme
        tableau_reparti = [valeur * proportion for valeur in tableau]
        return tableau_reparti