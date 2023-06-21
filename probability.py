from tkinter import simpledialog, messagebox, Tk, Label, Frame, Entry, Button
import random
import math
from fractions import Fraction

from utils.printer import *
from utils.constant import *
from utils.parameters import *
from utils.maths_func import (
    format_fraction,
    convert_to_fraction
)
from src.generator_equation_second_degre import generate_equation_second_degre
from src.ask_question_with_timer import ask_question_with_timer

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
    # Convertir toutes les valeurs
    result = [format_fraction(r) for r in result]
    
    if len(result) == 6:
        a, b, c, delta, solution_1, solution_2 = result
    elif len(result) == 5:
        a, b, c, delta, solution = result
    elif len(result) == 4:
        a, b, c, delta = result

    user_delta = ask_question_with_timer(
        "Équation du second degré",
        f"Résolvez l'équation : {format_coefficient_for_a(a)} {format_coefficient_b_or_c(b, 'x')} {format_coefficient_b_or_c(c)} = 0\nQue vaut le discriminant (delta) de l'équation ? ({point_gagne}pt)"
    )
    
    try:
        user_delta = format_fraction(user_delta)
    except ValueError:
        user_delta = None
        
    print(user_delta)

    if user_delta is None or user_delta != delta:
        # Cas exceptionnel, où il n'y a pas de solution
        if delta >= 0 and a == 0:
            delta = -1

        if delta < 0:
            messagebox.showerror(
                "Mauvaise réponse",
                f"Le discriminant (delta) est : {delta}\nL'équation n'admet pas de solution.",
            )
        elif delta == 0:
            messagebox.showerror(
                "Mauvaise réponse",
                f"Le discriminant (delta) est : {delta}\nL'équation admet une unique solution : x = {convert_to_fraction(solution)}",
            )
        else:
            messagebox.showerror(
                "Mauvaise réponse",
                f"Le discriminant (delta) est : {delta}\nL'équation admet deux solutions :"
                f"\nx1 = {convert_to_fraction(solution_1)}"
                f"\nx2 = {convert_to_fraction(solution_2)}",
            )
        return 0

    points += point_gagne
    messagebox.showinfo("Bonne réponse", f"Tu as obtenu {point_gagne}pt !")

    # Interaction avec le client pour le nombre de solutions
    num_solutions = ask_question_with_timer(
        "Question",
        f"L'équation : {a}x^2 + {b}x + {c} = 0\nLe discriminant (delta) est : {delta}\nQuel est le nombre de solutions de l'équation ? ({point_gagne}pt)",
        20
    )
    # Convertir le str en fraction ou float
    num_solutions = format_fraction(num_solutions)
    
    # au cas où un utilisateur s'amuse à mettre autre chose que 0, 1 ou 2
    num_solutions = num_solutions if num_solutions in {0, 1, 2} else -1

    # Cas exceptionnel, où il n'y a pas de solution
    if delta >= 0 and a == 0:
        delta = -1

    # Vérification du nombre de solutions
    if delta < 0:
        if num_solutions == 0:
            points += point_gagne
            messagebox.showinfo(
                "Bonne réponse !",
                f"L'équation n'admet pas de solution, tu as obtenu {point_gagne}pt !\n",
            )
        else:
            messagebox.showerror(
                "Mauvaise réponse",
                "L'équation n'admet pas de solution.",
            )
    elif delta == 0:
        if num_solutions == 1:
            points += point_gagne
            messagebox.showinfo("Bonne réponse", f"Tu as obtenu {point_gagne}pt !")

            # Demander la solution si l'équation admet une unique solution
            user_solution = ask_question_with_timer(
                "Question",
                f"L'équation : {a}x^2 + {b}x + {c} = 0\nLe discriminant (delta) est : {delta}\nQuelle est la solution de l'équation (sous forme de fraction de préférence) ? ({point_gagne}pt)",
            )
            
            # conversion pour avoir la valeur brute
            user_solution = format_fraction(user_solution)
            
            # Vérifier la solution fournie par l'utilisateur
            if user_solution == solution:
                points += point_gagne
                messagebox.showinfo(
                    "Bonne réponse",
                    f"Tu as obtenu {point_gagne}pt, l'équation admet une unique solution : x = {convert_to_fraction(solution)}",
                )
            else:
                messagebox.showerror(
                    "Mauvaise réponse",
                    f"Mauvaise réponse. La solution est : x = {convert_to_fraction(solution)}",
                )
        else:
            messagebox.showerror(
                "Mauvaise réponse",
                f"Mauvaise réponse. L'équation admet une unique solution : x = {convert_to_fraction(-b / (2 * a))}",
            )
    else:
        if num_solutions == 2:
            points += point_gagne

            messagebox.showinfo("Bonne réponse", f"Tu as obtenu {point_gagne}pt !")

            # Demander les solutions à l'utilisateur
            user_solution_1 = ask_question_with_timer(
                "Question",
                f"L'équation : {a}x^2 + {b}x + {c} = 0\nLe discriminant (delta) est : {delta}\nDonnez la solution 1 de l'équation (sous forme de fraction) qui est :",
            )
            user_solution_2 = ask_question_with_timer(
                "Question",
                f"L'équation : {a}x^2 + {b}x + {c} = 0\nLe discriminant (delta) est : {delta}\nTon x1={user_solution_1}\nDonnez la solution 2 de l'équation (sous forme de fraction) qui est :",
            )
            
            # conversion pour avoir les valeurs brutes
            user_solution_1 = format_fraction(user_solution_1)
            user_solution_2 = format_fraction(user_solution_2)

            # Vérifier les solutions fournies par l'utilisateur
            if (
                user_solution_1 != user_solution_2
                and (
                    user_solution_1 == format_fraction(solution_1)
                    and user_solution_2 == format_fraction(solution_2)
                )
                or (
                    user_solution_1 == format_fraction(solution_2)
                    and user_solution_2 == format_fraction(solution_1)
                )
            ):
                points += 2 * point_gagne
                messagebox.showinfo(
                    "Bonne réponse",
                    f"Tu as obtenu {point_gagne}pt, l'équation admet deux solutions :"
                    f"x1 = {convert_to_fraction(solution_1)}"
                    f"\nx2 = {convert_to_fraction(solution_2)}",
                )
            else:
                messagebox.showerror(
                    "Mauvaise réponse",
                    f"L'équation admet deux solutions : x1 et x2."
                    f"\nLes solutions sont :"
                    f"\nx1 = {convert_to_fraction(solution_1)}"
                    f"\nx2 = {convert_to_fraction(solution_2)}",
                )
        else:
            messagebox.showerror(
                "Mauvaise réponse",
                "L'équation admet deux solutions : x1 et x2."
                "\nLes solutions sont :"
                f"\nx1 = {convert_to_fraction(solution_1)}"
                f"\nx2 = {convert_to_fraction(solution_2)}",
            )

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
        messagebox.showinfo("Intégration", choix)
        sous_choix = random.choices(
            ["f(x) = (cx - d)^α", "f(x) = 1 / (x - c)"],
            weights=[p_puissance_1, p_puissance_2],
        )[0]
        messagebox.showinfo("Sous-question", sous_choix)

        if sous_choix == "f(x) = (cx - d)^α":
            c = format_fraction(choose_parameter_excluding(0))
            d = format_fraction(random.choice(A))
            alpha = format_fraction(choose_parameter_excluding(-1))

            result = (1 / (c * (alpha + 1))) * (
                (b * c - d) ** (alpha + 1) - (a * c - d) ** (alpha + 1)
            )

            user_answer = simpledialog.askfloat(
                "Réponse",
                "Calculez l'intégrale de la fonction donnée : I = ∫(cx - d)^α dx, avec x de a={} à b={}, c={}, d={} et alpha={}".format(
                    a, b, c, d, alpha
                ),
            )
            if math.isclose(user_answer.real, result.real, rel_tol=1e-6):
                messagebox.showinfo(
                    "Bravo !",
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}",
                )
                points = 1
            else:
                messagebox.showerror(
                    "Désolé !",
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}",
                )

        elif sous_choix == "f(x) = 1 / (x - c)":
            c = format_fraction(choose_parameter_excluding([a, b]))

            result = math.log(abs(b - c)) - math.log(abs(a - c))

            user_answer = simpledialog.askfloat(
                "Réponse",
                "Calculez l'intégrale de la fonction donnée : I = ∫1 / (x - c) dx, avec x de a={} à b={} et c={}".format(
                    a, b, c
                ),
            )
            if math.isclose(user_answer, result, rel_tol=1e-6):
                messagebox.showinfo(
                    "Bravo !",
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}",
                )
                points = 1
            else:
                messagebox.showerror(
                    "Désolé !",
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}",
                )

        else:
            messagebox.showerror("Erreur", "Choix invalide.")

    elif choix == "Fonctions trigonométriques":
        messagebox.showinfo("Intégration", choix)
        sous_choix = random.choices(
            ["f(x) = cos(cx)", "f(x) = sin(cx)", "f(x) = tan(cx)"],
            weights=[p_trigonometrie_1, p_trigonometrie_2, p_trigonometrie_3],
        )[0]
        messagebox.showinfo("Sous-question", sous_choix)

        c = format_fraction(choose_parameter_excluding(0))

        if sous_choix == "f(x) = cos(cx)":
            result = (math.sin(b * c) - math.sin(a * c)) / c

            user_answer = simpledialog.askfloat(
                "Réponse",
                "Calculez l'intégrale de la fonction donnée : I = ∫cos(cx) dx, avec x de a={} à b={} et c={}".format(
                    a, b, c
                ),
            )
            if math.isclose(user_answer, result, rel_tol=1e-6):
                messagebox.showinfo(
                    "Bravo !",
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}",
                )
                points = 1
            else:
                messagebox.showerror(
                    "Désolé !",
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}",
                )

        elif sous_choix == "f(x) = sin(cx)":
            result = -(math.cos(b * c) - math.cos(a * c)) / c

            user_answer = simpledialog.askfloat(
                "Réponse",
                "Calculez l'intégrale de la fonction donnée : I = ∫sin(cx) dx, avec x de a={} à b={} et c={}".format(
                    a, b, c
                ),
            )
            if math.isclose(user_answer, result, rel_tol=1e-6):
                messagebox.showinfo(
                    "Bravo !",
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}",
                )
                points = 1
            else:
                messagebox.showerror(
                    "Désolé !",
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}",
                )

        elif sous_choix == "f(x) = tan(cx)":
            result = (
                math.log(abs(math.cos(b * c))) - math.log(abs(math.cos(a * c)))
            ) / c

            user_answer = simpledialog.askfloat(
                "Réponse",
                "Calculez l'intégrale de la fonction donnée : I = ∫tan(cx) dx, avec x de a={} à b={} et c={}".format(
                    a, b, c
                ),
            )
            if math.isclose(user_answer, result, rel_tol=1e-6):
                messagebox.showinfo(
                    "Bravo !",
                    f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}",
                )
                points = 1
            else:
                messagebox.showerror(
                    "Désolé !",
                    f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}",
                )

        else:
            messagebox.showerror("Erreur", "Choix invalide.")

    elif choix == "Fonctions logarithmiques":
        messagebox.showinfo("Intégration", choix)
        messagebox.showinfo("Sous-question", "f(x) = ln(cx)\n")

        c = Fraction(choose_parameter_positive_only())

        # j'ai mis valeur absolue parce que a et b peuvent être négatives
        result = b * math.log(abs(b * c)) - a * math.log(abs(a * c)) - c * (b - a)

        user_answer = simpledialog.askfloat(
            "Réponse",
            "Calculez l'intégrale de la fonction donnée : I = ∫ln(cx) dx, avec x de a={} à b={} et c={}".format(
                a, b, c
            ),
        )
        if math.isclose(user_answer, result, rel_tol=1e-6):
            messagebox.showinfo(
                "Bravo !",
                f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}",
            )
            points = 1
        else:
            messagebox.showerror(
                "Désolé !",
                f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}",
            )
    else:
        messagebox.showerror("Erreur", "Choix invalide.")

    return points


def generate_questions():
    """
    Fonction qui génère les questions aléatoires et affiche les résultats dans des boîtes de dialogue.
    """
    question_count = question_count_entry.get()
    try:
        question_count = int(question_count)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide.")
        return

    points = 0

    for _ in range(question_count):
        theme_choice = random.choices(
            ["equation second degré", "integration"],
            weights=[p_equation, p_integration],
        )[0]

        if afficher_tous_infos_terminal:
            print_yellow(f"Question n°{_+1}, thème : {theme_choice}")

        if theme_choice == "equation second degré":
            points += equation_second_degre()
        else:
            points += integration()

        if afficher_tous_infos_terminal:
            print_new_line()

        messagebox.showinfo(
            "Résultat",
            f"Vous avez obtenu {points} pts sur la question {_+1}",
        )

    messagebox.showinfo(
        "Résultat",
        f"Vous avez obtenu au total {points} pts sur {question_count} questions.",
    )


# Création de la fenêtre principale
window = Tk()
window.title("Générateur de questions")
window.geometry("300x200")

# Création d'un cadre pour contenir le texte et le bouton
frame = Frame(window)

# Création des widgets
question_count_label = Label(frame, text="Nombre de questions :")
question_count_entry = Entry(frame)
generate_button = Button(
    frame, text="Générer les questions", command=generate_questions
)

# Placement des widgets
question_count_label.pack(anchor="center")
question_count_entry.pack(anchor="center")
generate_button.pack(anchor="center")

# Placement du cadre dans la fenêtre
frame.pack(expand=True)

# Lancement de la boucle principale
window.mainloop()
