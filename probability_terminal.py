import random
import math
import numpy as np
from fractions import Fraction

from utils.printer import *
from utils.constant import *
from utils.parameters import *
from utils.maths_func import (
    is_decimal,
    multiply_fraction_by_denominator,
    format_fraction,
    convert_to_fraction,
)


def equation_second_degre():
    """
    Fonction qui génère une équation du second degré aléatoire et demande à l'utilisateur de résoudre l'équation.
    Elle attribue des points en fonction des réponses de l'utilisateur.

    Returns:
        int: Le nombre de points attribués.
    """
    # Générer les valeurs aléatoires pour les paramètres a, b, c
    # Vérification si les paramètres a, b, c peuvent être mis sous forme de fraction
    a = format_fraction(random.choice(A))
    b = format_fraction(random.choice(A))
    c = format_fraction(random.choice(A))

    # Calcul du discriminant
    delta = b**2 - 4 * a * c

    print_blue(f"Résolvez l'équation : {a}x^2 + {b}x + {c} = 0\n")

    # Demande à l'utilisateur de calculer le discriminant
    user_delta = input(f"Le discriminant (delta) de l'équation est : ")

    try:
        user_delta = Fraction(user_delta)
    except ValueError:
        user_delta = None

    print()

    if user_delta is None or user_delta != delta:
        print_red(f"Mauvaise réponse. Le discriminant (delta) est : {delta}\n")

        # cas exceptionnel, où il n'y a pas de solution
        if delta >= 0 and a == 0:
            delta = -1

        if delta < 0:
            print_red("L'équation n'admet pas de solution.")
        elif delta == 0:
            solution = -b / (2 * a)
            print_red(
                f"L'équation admet une unique solution : x = {convert_to_fraction(solution)}"
            )
        else:
            solution_1 = (-b - delta**0.5) / (2 * a)
            solution_2 = (-b + delta**0.5) / (2 * a)
            print_red(f"L'équation admet deux solutions :")
            print_red(f"x1 = {convert_to_fraction(solution_1)}")
            print_red(f"x2 = {convert_to_fraction(solution_2)}")

        return 0

    print_green("Bonne réponse !\n")
    print("Combien de solutions cette équation admet-elle ?")

    # Interaction avec le client pour le nombre de solutions
    num_solutions = input("Nombre de solutions : \n")
    print()

    # cas exceptionnel, où il n'y a pas de solution
    if delta >= 0 and a == 0:
        delta = -1

    # Vérification du nombre de solutions
    if delta < 0:
        expected_num_solutions = "0"
        if num_solutions == expected_num_solutions:
            points = 1
            print_green("Bonne réponse ! L'équation n'admet pas de solution.\n")
        else:
            points = 0
            print_red(f"Mauvaise réponse. L'équation n'admet pas de solution.\n")
    elif delta == 0:
        expected_num_solutions = "1"
        if num_solutions == expected_num_solutions:
            points = 1
            solution = -b / (2 * a)
            print_green("Bonne réponse !")

            # Demander la solution si l'équation admet une unique solution
            print("Donnez la solution de l'équation (sous forme de fraction) :")
            user_solution = input("Solution : \n")
            print()

            # Vérifier la solution fournie par l'utilisateur
            if user_solution == convert_to_fraction(solution):
                print_green(
                    f"Bonne réponse ! L'équation admet une unique solution : x = {convert_to_fraction(solution)}\n"
                )
            else:
                print_red(
                    f"Mauvaise réponse. La solution est : x = {convert_to_fraction(solution)}"
                )
                points = 0
        else:
            points = 0
            print_red(
                f"Mauvaise réponse. L'équation admet une unique solution : x = {convert_to_fraction(-b / (2 * a))}\n"
            )
    else:
        expected_num_solutions = "2"
        if num_solutions == expected_num_solutions:
            points = 1

            # Calcul des solutions
            solution_1 = (-b - delta**0.5) / (2 * a)
            solution_2 = (-b + delta**0.5) / (2 * a)

            print_green("Bonne réponse !")

            # Demander les solutions à l'utilisateur
            print("Donnez les solutions de l'équation (sous forme de fraction) :")
            user_solution_1 = input("Solution 1 : \n")
            user_solution_2 = input("Solution 2 : \n")
            print()

            # Vérifier les solutions fournies par l'utilisateur
            if user_solution_1 == convert_to_fraction(
                solution_1
            ) and user_solution_2 == convert_to_fraction(solution_2):
                print_green(f"Bonne réponse ! L'équation admet deux solutions :")
            else:
                print_red(f"Mauvaise réponse. Les solutions sont :")
                points = 0

            print(f"x1 = {convert_to_fraction(solution_1)}")
            print(f"x2 = {convert_to_fraction(solution_2)}")
        else:
            points = 0
            print_red(
                f"Mauvaise réponse. L'équation admet deux solutions : x1 et x2.\n"
            )
            print_red(f"Les solutions sont :")
            print_red(f"x1 = {convert_to_fraction((-b - delta**0.5) / (2 * a))}")
            print_red(f"x2 = {convert_to_fraction((-b + delta**0.5) / (2 * a))}")

    return points


def integration():
    """
    Fonction qui permet de générer une question d'intégration aléatoire basée sur différents types de fonctions.
    Elle demande à l'utilisateur de calculer l'intégrale de la fonction et attribue des points en fonction de la réponse.

    Returns:
        int: Le nombre de points attribués.
    """
    choix = random.choices(
        [
            "Fonctions puissance",
            "Fonctions trigonométriques",
            "Fonctions logarithmiques",
        ],
        weights=[p_puissance, p_trigonometrie, p_logarithme],
    )[0]

    points = 0

    a = format_fraction(random.choice(A))
    b = format_fraction(choose_parameter_excluding(a))  # a != b
    # a > b
    if a < b:
        b, a = a, b

    if choix == "Fonctions puissance":
        print_blue(choix)
        sous_choix = random.choices(
            ["f(x) = (cx - d)^α", "f(x) = 1 / (x - c)"],
            weights=[p_puissance_1, p_puissance_2],
        )[0]
        print_blue(sous_choix)

        if sous_choix == "f(x) = (cx - d)^α":
            c = format_fraction(choose_parameter_excluding(0))
            d = format_fraction(random.choice(A))
            alpha = format_fraction(choose_parameter_excluding(-1))

            result = (1 / (c * (alpha + 1))) * (
                (b * c - d) ** (alpha + 1) - (a * c - d) ** (alpha + 1)
            )

            user_answer = Fraction(
                input(
                    "Calculez l'intégrale de la fonction donnée : I = ∫(cx - d)^α dx, avec x de a={} à b={}, c={}, d={} et alpha={}: ".format(
                        a, b, c, d, alpha
                    )
                )
            )
            if math.isclose(user_answer.real, result.real, rel_tol=1e-6):
                print_green(
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est :{result}"
                )
                points = 1
            else:
                print_red(
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est :{result}"
                )

        elif sous_choix == "f(x) = 1 / (x - c)":
            c = format_fraction(choose_parameter_excluding([a, b]))

            result = math.log(abs(b - c)) - math.log(abs(a - c))

            user_answer = Fraction(
                input(
                    "Calculez l'intégrale de la fonction donnée : I = ∫1 / (x - c) dx, avec x de a={} à b={} et c={}: ".format(
                        a, b, c
                    )
                )
            )
            if math.isclose(user_answer, result, rel_tol=1e-6):
                print_green(
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est :{result}"
                )
                points = 1
            else:
                print_red(
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est :{result}"
                )

        else:
            print_red("Choix invalide.")

    elif choix == "Fonctions trigonométriques":
        print_blue(choix)
        sous_choix = random.choices(
            ["f(x) = cos(cx)", "f(x) = sin(cx)", "f(x) = tan(cx)"],
            weights=[p_trigonometrie_1, p_trigonometrie_2, p_trigonometrie_3],
        )[0]
        print_blue(sous_choix)

        c = format_fraction(choose_parameter_excluding(0))

        if sous_choix == "f(x) = cos(cx)":
            result = (math.sin(b * c) - math.sin(a * c)) / c

            user_answer = float(
                input(
                    "Calculez l'intégrale de la fonction donnée : I = ∫cos(cx) dx, avec x de a={} à b={} et c={}: ".format(
                        a, b, c
                    )
                )
            )
            if math.isclose(user_answer, result, rel_tol=1e-6):
                print_green(
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est :{result}"
                )
                points = 1
            else:
                print_red(
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est :{result}"
                )

        elif sous_choix == "f(x) = sin(cx)":
            result = -(math.cos(b * c) - math.cos(a * c)) / c

            user_answer = Fraction(
                input(
                    "Calculez l'intégrale de la fonction donnée : I = ∫sin(cx) dx, avec x de a={} à b={} et c={}: ".format(
                        a, b, c
                    )
                )
            )
            if math.isclose(user_answer, result, rel_tol=1e-6):
                print_green(
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est :{result}"
                )
                points = 1
            else:
                print_red(
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est :{result}"
                )

        elif sous_choix == "f(x) = tan(cx)":
            result = (
                math.log(abs(math.cos(b * c))) - math.log(abs(math.cos(a * c)))
            ) / c

            user_answer = Fraction(
                input(
                    "Calculez l'intégrale de la fonction donnée : I = ∫tan(cx) dx, avec x de a={} à b={} et c={}: ".format(
                        a, b, c
                    )
                )
            )
            if math.isclose(user_answer, result, rel_tol=1e-6):
                print_green(
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est :{result}"
                )
                points = 1
            else:
                print_red(
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est :{result}"
                )

        else:
            print_red("Choix invalide.")

    elif choix == "Fonctions logarithmiques":
        print_blue(choix)
        print_blue("f(x) = ln(cx)\n")

        c = Fraction(choose_parameter_positive_only())

        # j'ai mis valeur absolue parce que a et b peuvent être négatives
        result = b * math.log(abs(b * c)) - a * math.log(abs(a * c)) - c * (b - a)

        user_answer = Fraction(
            input(
                "Calculez l'intégrale de la fonction donnée : I = ∫ln(cx) dx, avec x de a={} à b={} et c={}: ".format(
                    a, b, c
                )
            )
        )
        if math.isclose(user_answer, result, rel_tol=1e-6):
            print_green(
                f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est :{result}"
            )
            points = 1
        else:
            print_red(
                f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est :{result}"
            )
    else:
        print_red("Choix invalide.")

    return points


def generate_equation_second_degre():
    # Demande à l'utilisateur de calculer le discriminant
    delta = input("Donner le discriminant (delta) pour l'équation : ")
    e = math.sqrt(delta)

    a = 1

    if delta > 0:
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
            print_blue("x1=h/l , x2=k/l")

            k = format_fraction(random.choice(A))

            x1 = Fraction(h / l)
            x2 = Fraction(k / l)

            b = -Fraction(x1 + x2)
            c = Fraction(x1 * x2)

        elif cas_choice == "3.2":
            print_blue("x1=(-h - e*sqrt(p))/l , x2=(-h + e*sqrt(p))/l")

            # p appartient a E+
            p = format_fraction(choose_parameter_positive_only())

            x1 = Fraction((-h - e * (p**0.5)) / l)
            x2 = Fraction((-h - e * (p**0.5)) / l)

            a = Fraction(l / 2)
            b = h
            c = Fraction(((h**2) - p * (e**2)) / l)

        # variables de tempo pour afficher les variables sous forme d'entier dans la console
        tmp_a, tmp_b, tmp_c = a, b, c

        # multiplier par le dénominateur pour enlever la fraction a A
        if is_decimal(tmp_a):
            denominator_a = multiply_fraction_by_denominator(tmp_a)
            tmp_a = tmp_a * denominator_a
            tmp_b = tmp_b * denominator_a
            tmp_c = tmp_c * denominator_a

        # multiplier par le dénominateur pour enlever la fraction a B
        if is_decimal(tmp_b):
            denominator_b = multiply_fraction_by_denominator(tmp_b)
            tmp_a = tmp_a * denominator_b
            tmp_b = tmp_b * denominator_b
            tmp_c = tmp_c * denominator_b

        # multiplier par le dénominateur pour enlever la fraction a C
        if is_decimal(tmp_c):
            denominator_c = multiply_fraction_by_denominator(tmp_c)
            tmp_a = tmp_a * denominator_c
            tmp_b = tmp_b * denominator_c
            tmp_c = tmp_c * denominator_c

        print_green(
            f"Pour un delta > 0, delta={delta} et (x1, x2)=({x1},{x2}), on a une equation {tmp_a}x² {['+' if tmp_b>0 else '-'] + tmp_b}x {['+' if tmp_c>0 else '-'] + tmp_c} avec a={a}, b={b} et c={c}"
        )

        return a, b, c, delta, x1, x2
    elif delta == 0:
        print_blue("delta = 0")

        # probabilité X=1 et Z!=1 mais il ne peux pas être égal à 0 non plus
        X = random.choices(
            [1, [4, 9], [2, 3, 5, 6, 7, 8]],
            weights=[p_X_egal_1, p_X_different_4_9, p_X_different_autres],
        )[0]
        l = format_fraction(X)

        x0 = e / (l**0.5)

        a = 1
        b = -2 * x0
        c = a * (x0**2)

        # variables de tempo pour afficher les variables sous forme d'entier dans la console
        tmp_b, tmp_c = b, c

        # multiplier par le dénominateur pour enlever la fraction a B
        if is_decimal(tmp_b):
            denominator_b = multiply_fraction_by_denominator(tmp_b)
            tmp_a = tmp_a * denominator_b
            tmp_b = tmp_b * denominator_b
            tmp_c = tmp_c * denominator_b

        # multiplier par le dénominateur pour enlever la fraction a C
        if is_decimal(tmp_c):
            denominator_c = multiply_fraction_by_denominator(tmp_c)
            tmp_a = tmp_a * denominator_c
            tmp_b = tmp_b * denominator_c
            tmp_c = tmp_c * denominator_c

        print_green(
            f"Pour un delta = 0, delta={delta} et x0={x0}, on a une equation x² {['+' if tmp_b>0 else '-'] + tmp_b}x {['+' if tmp_c>0 else '-'] + tmp_c} avec a={a}, b={b} et c={c}"
        )

        return a, b, c, delta, x0

    else:
        print_blue("delta < 0")

        # il faut que a appartient a E exclue 0 pour éviter un problème de calcul sur c
        a = format_fraction(choose_parameter_excluding(0))
        b = format_fraction(random.choice(A))

        c = ((b**2) + e) / (4 * a)

        # variables de tempo pour afficher les variables sous forme d'entier dans la console
        tmp_a, tmp_b, tmp_c = a, b, c

        # multiplier par le dénominateur pour enlever la fraction a A
        if is_decimal(tmp_a):
            denominator_a = multiply_fraction_by_denominator(tmp_a)
            tmp_a = tmp_a * denominator_a
            tmp_b = tmp_b * denominator_a
            tmp_c = tmp_c * denominator_a

        # multiplier par le dénominateur pour enlever la fraction a C
        if is_decimal(tmp_c):
            denominator_c = multiply_fraction_by_denominator(tmp_c)
            tmp_a = tmp_a * denominator_c
            tmp_b = tmp_b * denominator_c
            tmp_c = tmp_c * denominator_c

        print_green(
            f"Pour un delta < 0, delta={delta}, on a une equation {['' if tmp_a>0 else '-'] + tmp_a}x² {['+' if tmp_b>0 else '-'] + tmp_b}x {['+' if tmp_c>0 else '-'] + tmp_c} avec a={a}, b={b} et c={c}"
        )

        return a, b, c, delta


def main():
    # TODO : créer un timer et afficher le temps pour chaque question

    # TODO : générateur de 2nd degré (ensuite) correction du 2nd degré
    # TODO : question : que vaut le disciminant (delta) de l'équation ? (0.5pts)
    # TODO : question : quel est le nombre de solutions de l'équation ? (0.5pts)
    # TODO : question : rentrer les solutions trouvés ? (une solution = 0.5pts)

    print_new_line()

    # Nombre de questions à générer
    nombre_questions = int(input("Nombres de questions dans la section probabilités: "))
    print_yellow(
        f"Vous avez choisi {nombre_questions} question{'s' if nombre_questions > 1 else ''}, c'est parti !"
    )

    print_new_line()

    points = 0

    for i in range(nombre_questions):
        # Choix du thème
        theme_choice = random.choices(
            ["equation second degré", "integration"],
            weights=[p_equation, p_integration],
        )[0]

        print_yellow(f"Question n°{i+1}, thème : {theme_choice}")

        if theme_choice == "equation second degré":
            points += equation_second_degre()
        else:
            points += integration()
        print_yellow(f"Points obtenus : {points}")
        print_new_line()

    print_yellow(f"Points obtenus au total : {points}")


# Appel de la fonction principale
main()
