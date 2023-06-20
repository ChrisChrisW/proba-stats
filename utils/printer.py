def print_new_line():
    print("\n========================\n")


def print_green(message):
    """
    Affiche le message en vert.

    Args:
        message (str): Le message à afficher.
    """
    print(f"\033[32m{message}\033[0m")


def print_red(message):
    """
    Affiche le message en rouge.

    Args:
        message (str): Le message à afficher.
    """
    print(f"\033[31m{message}\033[0m")


def print_yellow(message):
    """
    Affiche le message en jaune.

    Args:
        message (str): Le message à afficher.
    """
    print("\033[93m" + message + "\033[0m")


def print_blue(message):
    """
    Affiche le message en bleu.

    Args:
        message (str): Le message à afficher.
    """
    print(f"\033[94m{message}\033[0m")


def format_coefficient_for_a(a):
    """
    Formats the coefficient 'a' for the quadratic term in an equation.

    Args:
        a (int or float): The coefficient for the quadratic term.

    Returns:
        str: The formatted coefficient followed by 'x²'.

    Raises:
        None.

    Examples:
        >>> format_coefficient_for_a(0)
        ''
        >>> format_coefficient_for_a(1)
        'x²'
        >>> format_coefficient_for_a(-1)
        '- x²'
        >>> format_coefficient_for_a(2)
        '2x²'
    """
    # cas par précaution
    if a == 0:
        return ""

    value = str(a)
    if a == -1:
        value = "-"
    elif a == 1:
        value = ""

    return value + "x²"


def format_coefficient_b_or_c(coefficient, string_x_polynom):
    """
    Formats the coefficient 'coefficient' for the linear or constant term in an equation.

    Args:
        coefficient (int, float, complex): The coefficient for the linear or constant term.
        string_x_polynom (str): The string representation of the variable term in the equation.

    Returns:
        str: The formatted coefficient followed by 'x' and the variable term.

    Raises:
        None.

    Examples:
        >>> format_coefficient_b_or_c(0, 'x')
        ''
        >>> format_coefficient_b_or_c(2, 'x')
        '+ 2x'
        >>> format_coefficient_b_or_c(-1, 'x')
        '- x'
        >>> format_coefficient_b_or_c(3 + 2j, 'x')
        '+ 3x - 2ix'
    """
    # Special case when the coefficient is 0
    if coefficient == 0:
        return ""

    # Formatting based on different cases
    if isinstance(coefficient, complex):
        real_part = coefficient.real
        imag_part = coefficient.imag

        value = ""

        # Format the real part
        if real_part != 0:
            if real_part == 1:
                value += "+ "
            elif real_part == -1:
                value += "- "
            elif real_part > 0:
                value += "+ " + str(real_part)
            else:
                value += "- " + str(abs(real_part))

        # Format the imaginary part
        if imag_part != 0:
            if imag_part == 1:
                value += "+ i"
            elif imag_part == -1:
                value += "- i"
            elif imag_part > 0:
                value += "+ " + str(imag_part) + "i"
            else:
                value += "- " + str(abs(imag_part)) + "i"

    else:
        if coefficient == 1:
            value = "+ "
        elif coefficient == -1:
            value = "- "
        elif coefficient > 0:
            value = "+ " + str(coefficient)
        else:
            value = "- " + str(abs(coefficient))

    if isinstance(value, str) and not value:
        return value
    
    return value + string_x_polynom
