import random
import math
from fractions import Fraction

from utils.printer import *
from utils.constant import *
from utils.parameters import *
from utils.maths_func import (
    format_fraction,
    convert_to_fraction,
)
from src.generator_equation_second_degre import generate_equation_second_degre


def equation_second_degre():
    """
    Fonction qui génère une équation du second degré aléatoire et demande à l'utilisateur de résoudre l'équation.
    Elle attribue des points en fonction des réponses de l'utilisateur.

    Returns:
        int: Le nombre de points attribués.
    """
    points = 0

    # Générer l'équation du 2nd degré
    result = generate_equation_second_degre()

    if len(result) == 6:
        a, b, c, delta, solution_1, solution_2 = result
    elif len(result) == 5:
        a, b, c, delta, solution = result
    elif len(result) == 4:
        a, b, c, delta = result

    print_blue(
        f"Résolvez l'équation : {format_coefficient_for_a(a)} {format_coefficient_b_or_c(b, 'x')} {format_coefficient_b_or_c(c, '')} = 0\n"
    )

    # Demande à l'utilisateur de calculer le discriminant
    user_delta = input(
        f"Que vaut le discriminant (delta) de l'équation ? ({point_gagne}pt)\n"
    )

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
            print_red(
                f"L'équation admet une unique solution : x = {convert_to_fraction(solution)}"
            )
        else:
            print_red("L'équation admet deux solutions :")
            print_red(f"x1 = {convert_to_fraction(solution_1)}")
            print_red(f"x2 = {convert_to_fraction(solution_2)}")

        return 0

    points += point_gagne
    print_green(f"Bonne réponse, tu as obtenu {point_gagne}pt !\n")

    # Interaction avec le client pour le nombre de solutions
    num_solutions = input(
        f"Quel est le nombre de solutions de l'équation ? ({point_gagne}pt)\n"
    )
    print()

    # cas exceptionnel, où il n'y a pas de solution
    if delta >= 0 and a == 0:
        delta = -1

    # Vérification du nombre de solutions
    if delta < 0:
        expected_num_solutions = "0"
        if num_solutions == expected_num_solutions:
            points += point_gagne
            print_green(
                f"Bonne réponse ! L'équation n'admet pas de solution, tu as obtenu {point_gagne}pt !\n"
            )
        else:
            print_red("Mauvaise réponse. L'équation n'admet pas de solution.\n")
    elif delta == 0:
        expected_num_solutions = "1"
        if num_solutions == expected_num_solutions:
            points += point_gagne
            print_green(f"Bonne réponse ! Tu as obtenu {point_gagne}pt !\n")
            # Demander la solution si l'équation admet une unique solution
            user_solution = input(
                f"Quelle est la solution de l'équation (sous forme de fraction de préférence) ? ({point_gagne}pt)\n"
            )
            print()

            # Vérifier la solution fournie par l'utilisateur
            if user_solution == convert_to_fraction(solution):
                points += point_gagne
                print_green(
                    f"Bonne réponse ! Tu as obtenu {point_gagne}pt, l'équation admet une unique solution : x = {convert_to_fraction(solution)}\n"
                )
            else:
                print_red(
                    f"Mauvaise réponse. La solution est : x = {convert_to_fraction(solution)}"
                )
        else:
            print_red(
                f"Mauvaise réponse. L'équation admet une unique solution : x = {convert_to_fraction(solution)}\n"
            )
    else:
        expected_num_solutions = "2"
        if num_solutions == expected_num_solutions:
            points += point_gagne
            print_green(f"Bonne réponse, tu as obtenu {point_gagne}pt !\n")

            # Demander les solutions à l'utilisateur
            print(
                f"Donnez les solutions de l'équation (sous forme de fraction) : ({2*point_gagne}pt)"
            )

            user_solution_1 = input(f"La solution 1 est ({point_gagne}pt) \n")
            print()

            # Vérifier les solutions fournies par l'utilisateur
            if (user_solution_1 == convert_to_fraction(solution_1)) or (
                user_solution_1 == convert_to_fraction(solution_2)
            ):
                points += point_gagne
                print_green(f"Bonne réponse ! Tu as obtenu le premier {point_gagne}pt")

                user_solution_2 = input(f"La solution 2 est ({point_gagne}pt) \n")

                if user_solution_1 != user_solution_2 and (
                    (user_solution_2 == convert_to_fraction(solution_1))
                    or (user_solution_2 == convert_to_fraction(solution_2))
                ):
                    points += point_gagne
                    print_green(
                        f"Bonne réponse ! Tu as obtenu {point_gagne}pt, l'équation admet deux solutions :"
                    )
            else:
                print_red("Mauvaise réponse. Les solutions sont :")

            print(f"x1 = {convert_to_fraction(solution_1)}")
            print(f"x2 = {convert_to_fraction(solution_2)}")
        else:
            print_red("Mauvaise réponse. L'équation admet deux solutions : x1 et x2.\n")
            print_red("Les solutions sont :")
            print_red(f"x1 = {convert_to_fraction(solution_1)}")
            print_red(f"x2 = {convert_to_fraction(solution_2)}")

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


def main():
    # TODO : créer un timer et afficher le temps pour chaque question

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
