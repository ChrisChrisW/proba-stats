from fractions import Fraction


def check_number_type(number):
    """
    Checks the type of a number (integer, fraction, or decimal).

    Args:
        number (float or Fraction or int): The number to check.

    Returns:
        str: A string indicating the type of the number: 'integer', 'fraction', or 'decimal'.

    Raises:
        None.

    Examples:
        >>> check_number_type(5)
        'integer'
        >>> check_number_type(Fraction(3, 4))
        'fraction'
        >>> check_number_type(2.5)
        'decimal'
    """
    if isinstance(number, int):
        return 'integer'
    elif isinstance(number, Fraction):
        return 'fraction'
    elif isinstance(number, float):
        return 'decimal'
    else:
        raise ValueError('Invalid number type')


def multiply_non_integer_coefficients(a, b, c, multiplier):
    """
    Multiplies non-integer coefficients 'a', 'b', and 'c' by a specified multiplier.

    Args:
        a (int or float or Fraction): The coefficient 'a' in the equation.
        b (int or float or Fraction): The coefficient 'b' in the equation.
        c (int or float or Fraction): The coefficient 'c' in the equation.
        multiplier (int or float): The value to multiply non-integer coefficients by.

    Returns:
        tuple: The updated coefficients 'a', 'b', and 'c' after applying the multiplication if necessary.

    Raises:
        None.

    Examples:
        >>> multiply_non_integer_coefficients(5, 3, 7, 2)
        (5, 3, 7)
        >>> multiply_non_integer_coefficients(1/2, 3/4, 5, 2)
        (1, 3/2, 10)
        >>> multiply_non_integer_coefficients(3, 4, Fraction(1, 5), 10)
        (3, 4, 10)
    """
    if not isinstance(a, int):
        a *= multiplier

    if not isinstance(b, int):
        b *= multiplier

    if not isinstance(c, int):
        c *= multiplier

    return a, b, c


def multiply_fraction_by_denominator_for_a_b_c(a, b, c):
    """
    Multiplies the coefficients 'a', 'b', and 'c' by their respective denominators to remove the fractions.

    Args:
        a (float or Fraction): The coefficient 'a' in the equation.
        b (float or Fraction): The coefficient 'b' in the equation.
        c (float or Fraction): The coefficient 'c' in the equation.

    Returns:
        tuple: The updated coefficients 'a', 'b', and 'c' after multiplying them by their respective denominators.

    Raises:
        None.
    
    Examples:
        >>> multiply_fraction_by_denominator_for_a_b_c(1/2, 3/4, 5)
        (4, 3, 20)
        >>> multiply_fraction_by_denominator_for_a_b_c(3, 4, Fraction(1, 5))
        (3, 4, 5)
        >>> multiply_fraction_by_denominator_for_a_b_c(0.3, 0.25, 1.2)
        (3, 1, 6)
    """
    if isinstance(a, float):
        mult_a = float(Fraction(a).limit_denominator().denominator)
        a *= mult_a
        b *= mult_a
        c *= mult_a
    if isinstance(b, float):
        mult_b = float(Fraction(b).limit_denominator().denominator)
        a *= mult_b
        b *= mult_b
        c *= mult_b
    if isinstance(c, float):
        mult_c = float(Fraction(c).limit_denominator().denominator)
        a *= mult_c
        b *= mult_c
        c *= mult_c

    return float(a), float(b), float(c)


def process_coefficients_with_multiplier(a, b, c, multiplier=10):
    """
    Processes the coefficients 'a', 'b', and 'c' by removing fractions and multiplying non-integer coefficients.

    Args:
        a (float or Fraction or int): The coefficient 'a' in the equation.
        b (float or Fraction or int): The coefficient 'b' in the equation.
        c (float or Fraction or int): The coefficient 'c' in the equation.
        multiplier (int or float): The value to multiply non-integer coefficients by. Default: 10.

    Returns:
        tuple: The processed coefficients 'a', 'b', and 'c' after removing fractions and applying multiplication if necessary.

    Raises:
        None.

    Examples:
        >>> process_coefficients_with_multiplier(1/2, 3/4, 5)
        (4, 3, 20)
    """
    a_type = check_number_type(a)
    b_type = check_number_type(b)
    c_type = check_number_type(c)
    
    if a_type != 'integer' or b_type != 'integer' or c_type != 'integer':
        a, b, c = multiply_non_integer_coefficients(a, b, c, multiplier)

    return a, b, c

def process_coefficients(a, b, c):
    """
    Processes the coefficients 'a', 'b', and 'c' by removing fractions and multiplying non-integer coefficients.

    Args:
        a (float or Fraction or int): The coefficient 'a' in the equation.
        b (float or Fraction or int): The coefficient 'b' in the equation.
        c (float or Fraction or int): The coefficient 'c' in the equation.
        multiplier (int or float): The value to multiply non-integer coefficients by. Default: 10.

    Returns:
        tuple: The processed coefficients 'a', 'b', and 'c' after removing fractions and applying multiplication if necessary.

    Raises:
        None.

    Examples:
        >>> process_coefficients(3, 4, Fraction(1, 5))
        (3, 4, 5)
        >>> process_coefficients(0.3, 0.25, 1.2)
        (3, 1, 6)
        >>> process_coefficients(2, 3, 4)
        (2, 3, 4)
    """
    a_type = check_number_type(a)
    b_type = check_number_type(b)
    c_type = check_number_type(c)

    if a_type != 'integer' or b_type != 'integer' or c_type != 'integer':
        a, b, c = multiply_fraction_by_denominator_for_a_b_c(a, b, c)

    return a, b, c


def format_fraction(value):
    """
    Convertit une valeur en fraction si elle est un nombre rationnel.

    Args:
        value (float): La valeur à convertir.

    Returns:
        Fraction or float: La valeur convertie en Fraction si c'est possible, sinon la valeur originale en tant que float.
    """
    try:
        fraction = Fraction(str(value)).limit_denominator()
        return fraction if fraction.denominator != 1 else float(value)
    except ValueError:
        return value


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
