import random

from utils.printer import *
from utils.constant import *
from utils.parameters import *
from utils.maths_func import (
    format_fraction,
    process_coefficients_with_multiplier,
    process_coefficients
)


def generate_equation_second_degre():
    """
    Génère une équation du second degré aléatoire avec ses coefficients et sa valeur de delta.

    Returns:
        tuple: Les coefficients 'a', 'b', 'c', la valeur de 'delta', et les solutions 'x1' et 'x2' de l'équation.

    Raises:
        None.

    Examples:
        >>> generate_equation_second_degre()
        (1, 2, 3, -4, -0.5, -1.5)
        >>> generate_equation_second_degre()
        (2, -3, 5, 0, 1.25, 1.25)
    """
    # delta choisit avec une certaine probabilité
    # type 1 : delta < 0
    # type 2 : delta = 0
    # type 3 : delta > 0
    delta = random.choices(
        [choose_parameter_negative_only(), 0, choose_parameter_positive_only()],
        weights=[p_type_1, p_type_2, p_type_3],
    )[0]

    # par default
    e = delta**0.5
    a = 1

    if delta > 0:
        if afficher_tous_infos_terminal:
            print_blue("delta > 0")

        cas_choice = random.choices(
            ["3.1", "3.2"], weights=[p_equation_delta_sup_3_1, p_equation_delta_sup_3_2]
        )[0]

        h = format_fraction(random.choice(A))
        # probabilité Z=1 et Z!=1 mais il ne peux pas être égal à 0 non plus
        Z = random.choices(
            [1, choose_parameter_excluding([0, 1])],
            weights=[p_Z_egal_1, p_Z_different_1],
        )[0]
        l = format_fraction(Z)

        if cas_choice == "3.1":
            if afficher_tous_infos_terminal:
                print_blue("x1=h/l , x2=k/l")

            k = format_fraction(random.choice(A))

            x1 = format_fraction(h / l)
            x2 = format_fraction(k / l)

            b = -format_fraction(x1 + x2)
            c = format_fraction(x1 * x2)

        elif cas_choice == "3.2":
            if afficher_tous_infos_terminal:
                print_blue("x1=(-h - e*sqrt(p))/l , x2=(-h + e*sqrt(p))/l")

            # p appartient a E+
            p = format_fraction(choose_parameter_positive_only())
            # l appartient a E = {−3, −2, −1, 1, 2, 3}
            l = format_fraction(random.choice([-3, -2, -1, 1, 2, 3]))

            x1 = format_fraction((-h - e * (p**0.5)) / l)
            x2 = format_fraction((-h - e * (p**0.5)) / l)

            b = format_fraction((2*h) / l)
            c = format_fraction(((h**2) - p * (e**2)) / (l**2))

        if afficher_tous_infos_terminal:
            # variables de tempo pour afficher les variables sous forme d'entier dans la console
            tmp_a, tmp_b, tmp_c = a, b, c
            tmp_a, tmp_b, tmp_c = process_coefficients_with_multiplier(tmp_a, tmp_b, tmp_c, l**2)
            print_green(
                f"Pour un delta > 0, delta={delta} et (x1, x2)=({x1},{x2}), on a une equation {format_coefficient_for_a(tmp_a)} {format_coefficient_b_or_c(tmp_b, 'x')} {format_coefficient_b_or_c(tmp_c, '')} avec a={a}, b={b} et c={c}"
            )

        return a, b, c, delta, x1, x2
    elif delta == 0:
        if afficher_tous_infos_terminal:
            print_blue("delta = 0")

        # e² = 0 = delta, c'est pourquoi on doit générer un nouveau e positive strict
        e = format_fraction(random.choice(A))
        # probabilité X=1 | X=[4,9] | X = [2, 3, 5, 6, 7, 8]
        X = random.choices(
            [1, random.choice([4, 9]), random.choice([2, 3, 5, 6, 7, 8])],
            weights=[p_X_egal_1, p_X_different_4_9, p_X_different_autres],
        )[0]
        l = format_fraction(X)

        x0 = format_fraction(e / (l**0.5))

        a = 1
        b = -2 * x0
        c = a * (x0**2)

        if afficher_tous_infos_terminal:
            # variables de tempo pour afficher les variables sous forme d'entier dans la console
            tmp_a, tmp_b, tmp_c = a, b, c
            tmp_a, tmp_b, tmp_c = process_coefficients_with_multiplier(tmp_a, tmp_b, tmp_c, l)
            tmp_a, tmp_b, tmp_c = process_coefficients_with_multiplier(tmp_a, tmp_b, tmp_c, l**0.5)
            print_green(
                f"Pour un delta = 0, delta={delta} et x0={x0}, on a une equation {format_coefficient_for_a(tmp_a)} {format_coefficient_b_or_c(tmp_b, 'x')} {format_coefficient_b_or_c(tmp_c, '')} avec a={a}, b={b} et c={c}"
            )

        return a, b, c, delta, x0

    if afficher_tous_infos_terminal:
        print_blue("delta < 0")

    # e² = (chiffre négatif) -> ex : (e² = -1) est une contradiction, un carré ne peut pas être négatif
    # e² = delta < 0 , c'est pourquoi on doit générer un nouveau e positive strict
    # e appartient a E = {1, 2, 3}
    e = format_fraction(random.choice([1, 2, 3]))

    # il faut que a appartient a E exclue 0 pour éviter un problème de calcul sur c
    a = format_fraction(choose_parameter_excluding(0))
    b = format_fraction(random.choice(A))

    c = ((b**2) + e) / (4 * a)

    if afficher_tous_infos_terminal:
        # variables de tempo pour afficher les variables sous forme d'entier dans la console
        tmp_a, tmp_b, tmp_c = a, b, c
        tmp_a, tmp_b, tmp_c = process_coefficients(tmp_a, tmp_b, tmp_c)

        print_green(
            f"Pour un delta < 0, delta={delta}, on a une equation {format_coefficient_for_a(tmp_a)} {format_coefficient_b_or_c(tmp_b, 'x')} {format_coefficient_b_or_c(tmp_c, '')} avec a={a}, b={b} et c={c}"
        )

    return a, b, c, delta
