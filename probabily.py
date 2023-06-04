import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import math
import numpy as np
from fractions import Fraction

from utils.printer import *
from utils.constant import *
from utils.parameters import *
from utils.maths_func import format_fraction, convert_to_fraction

def equation_second_degre():
    """
    Fonction qui génère une équation du second degré aléatoire et demande à l'utilisateur de résoudre l'équation.
    Elle attribue des points en fonction des réponses de l'utilisateur.

    Returns:
        int: Le nombre de points attribués.
    """
    # Générer les valeurs aléatoires pour les paramètres a, b, c
    # Vérification si les paramètres a, b, c peuvent être mis sous forme de fraction
    a = float(format_fraction(random.choice(A)))
    b = float(format_fraction(random.choice(A)))
    c = float(format_fraction(random.choice(A)))

    # Calcul du discriminant
    delta = b**2 - 4*a*c

    # Demande à l'utilisateur de calculer le discriminant
    user_delta = simpledialog.askstring("Équation du second degré", f"Résolvez l'équation : {a}x^2 + {b}x + {c} = 0\nLe discriminant (delta) de l'équation est :")

    try:
        user_delta = Fraction(user_delta)
    except ValueError:
        user_delta = None

    if user_delta is None or user_delta != delta:
        # Cas exceptionnel, où il n'y a pas de solution
        if delta >= 0 and a == 0:
            delta = -1

        if delta < 0:
            messagebox.showerror("Mauvaise réponse", f"Mauvaise réponse. Le discriminant (delta) est : {delta}\nL'équation n'admet pas de solution.")
        elif delta == 0:
            solution = -b / (2 * a)
            messagebox.showerror("Mauvaise réponse", f"Mauvaise réponse. Le discriminant (delta) est : {delta}\nL'équation admet une unique solution : x = {convert_to_fraction(solution)}")
        else:
            solution_1 = (-b - delta**0.5) / (2 * a)
            solution_2 = (-b + delta**0.5) / (2 * a)
            messagebox.showerror("Mauvaise réponse", f"Mauvaise réponse. Le discriminant (delta) est : {delta}\nL'équation admet deux solutions :"
                                f"\nx1 = {convert_to_fraction(solution_1)}"
                                f"\nx2 = {convert_to_fraction(solution_2)}")
        return 0

    messagebox.showinfo("Bonne réponse", "Bonne réponse !")

    # Interaction avec le client pour le nombre de solutions
    num_solutions = simpledialog.askstring("Question", f"L'équation : {a}x^2 + {b}x + {c} = 0\nLe discriminant (delta) est : {delta}\nCombien de solutions cette équation admet-elle ?")

    # Cas exceptionnel, où il n'y a pas de solution
    if delta >= 0 and a == 0:
        delta = -1

    # Vérification du nombre de solutions
    if delta < 0:
        expected_num_solutions = "0"
        if num_solutions == expected_num_solutions:
            points = 1
            messagebox.showinfo("Bonne réponse", "Bonne réponse ! L'équation n'admet pas de solution.")
        else:
            points = 0
            messagebox.showerror("Mauvaise réponse", "Mauvaise réponse. L'équation n'admet pas de solution.")
    elif delta == 0:
        expected_num_solutions = "1"
        if num_solutions == expected_num_solutions:
            points = 1
            solution = -b / (2 * a)
            messagebox.showinfo("Bonne réponse", "Bonne réponse !")

            # Demander la solution si l'équation admet une unique solution
            user_solution = simpledialog.askstring("Question", f"L'équation : {a}x^2 + {b}x + {c} = 0\nLe discriminant (delta) est : {delta}\nDonnez la solution de l'équation (sous forme de fraction) :")

            # Vérifier la solution fournie par l'utilisateur
            if user_solution == convert_to_fraction(solution):
                messagebox.showinfo("Bonne réponse", f"Bonne réponse ! L'équation admet une unique solution : x = {convert_to_fraction(solution)}")
            else:
                messagebox.showerror("Mauvaise réponse", f"Mauvaise réponse. La solution est : x = {convert_to_fraction(solution)}")
                points = 0
        else:
            points = 0
            messagebox.showerror("Mauvaise réponse", f"Mauvaise réponse. L'équation admet une unique solution : x = {convert_to_fraction(-b / (2 * a))}")
    else:
        expected_num_solutions = "2"
        if num_solutions == expected_num_solutions:
            points = 1

            # Calcul des solutions
            solution_1 = (-b - delta**0.5) / (2 * a)
            solution_2 = (-b + delta**0.5) / (2 * a)

            messagebox.showinfo("Bonne réponse", "Bonne réponse !")

            # Demander les solutions à l'utilisateur
            user_solution_1 = simpledialog.askstring("Question", f"L'équation : {a}x^2 + {b}x + {c} = 0\nLe discriminant (delta) est : {delta}\nSolution 1 :")
            user_solution_2 = simpledialog.askstring("Question", f"L'équation : {a}x^2 + {b}x + {c} = 0\nLe discriminant (delta) est : {delta}\nTon x1={user_solution_1}\nSolution 2 :")

            # Vérifier les solutions fournies par l'utilisateur
            if (user_solution_1 == convert_to_fraction(solution_1) and user_solution_2 == convert_to_fraction(solution_2)) or (user_solution_1 == convert_to_fraction(solution_2) and user_solution_2 == convert_to_fraction(solution_1)) :
                messagebox.showinfo("Bonne réponse", "Bonne réponse ! L'équation admet deux solutions :"
                                    f"x1 = {convert_to_fraction(solution_1)}"
                                    f"\nx2 = {convert_to_fraction(solution_2)}")
            else:
                messagebox.showerror("Mauvaise réponse", f"Mauvaise réponse. L'équation admet deux solutions : x1 et x2."
                                                    f"\nLes solutions sont :"
                                                    f"\nx1 = {convert_to_fraction(solution_1)}"
                                                    f"\nx2 = {convert_to_fraction(solution_2)}")
                points = 0
        else:
            points = 0
            messagebox.showerror("Mauvaise réponse", f"Mauvaise réponse. L'équation admet deux solutions : x1 et x2."
                                                    f"\nLes solutions sont :"
                                                    f"\nx1 = {convert_to_fraction((-b - delta**0.5) / (2 * a))}"
                                                    f"\nx2 = {convert_to_fraction((-b + delta**0.5) / (2 * a))}")

    return points

def integration():
    """
    Fonction qui permet de générer une question d'intégration aléatoire basée sur différents types de fonctions.
    Elle demande à l'utilisateur de calculer l'intégrale de la fonction et attribue des points en fonction de la réponse.

    Returns:
        int: Le nombre de points attribués.
    """
    choix = random.choices(["Fonctions puissance", "Fonctions trigonométriques", "Fonctions logarithmiques"], weights=[p_puissance, p_trigonometrie, p_logarithme])[0]

    points = 0
    
    a = format_fraction(random.choice(A))
    b = format_fraction(choose_parameter_excluding(a)) # a != b
    # a > b
    if a < b:
        b, a = a, b 

    if choix == "Fonctions puissance":
        messagebox.showinfo("Intégration", choix)
        sous_choix = random.choices(["f(x) = (cx - d)^α", "f(x) = 1 / (x - c)"], weights=[p_puissance_1, p_puissance_2])[0]
        messagebox.showinfo("Sous-question", sous_choix)

        if sous_choix == "f(x) = (cx - d)^α":
            c = format_fraction(choose_parameter_excluding(0))
            d = format_fraction(random.choice(A))
            alpha = format_fraction(choose_parameter_excluding(-1))

            result = (1 / (c * (alpha + 1))) * ((b * c - d) ** (alpha + 1) - (a * c - d) ** (alpha + 1))

            user_answer = simpledialog.askfloat("Réponse", "Calculez l'intégrale de la fonction donnée : I = ∫(cx - d)^α dx, avec x de a={} à b={}, c={}, d={} et alpha={}".format(a, b, c, d, alpha))
            if math.isclose(user_answer.real, result.real, rel_tol=1e-6):
                messagebox.showinfo("Bravo !", f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}")
                points = 1
            else:
                messagebox.showerror("Désolé !", f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}")

        elif sous_choix == "f(x) = 1 / (x - c)":
            c = format_fraction(choose_parameter_excluding([a, b]))

            result = math.log(abs(b - c)) - math.log(abs(a - c))

            user_answer = simpledialog.askfloat("Réponse", "Calculez l'intégrale de la fonction donnée : I = ∫1 / (x - c) dx, avec x de a={} à b={} et c={}".format(a, b, c))
            if math.isclose(user_answer, result, rel_tol=1e-6):
                messagebox.showinfo("Bravo !", f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}")
                points = 1
            else:
                messagebox.showerror("Désolé !", f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}")

        else:
            messagebox.showerror("Erreur", "Choix invalide.")

    elif choix == "Fonctions trigonométriques":
        messagebox.showinfo("Intégration", choix)
        sous_choix = random.choices(["f(x) = cos(cx)", "f(x) = sin(cx)", "f(x) = tan(cx)"], weights=[p_trigonometrie_1, p_trigonometrie_2, p_trigonometrie_3])[0]
        messagebox.showinfo("Sous-question", sous_choix)

        c = format_fraction(choose_parameter_excluding(0))
        
        if sous_choix == "f(x) = cos(cx)":
            result = (math.sin(b * c) - math.sin(a * c)) / c

            user_answer = simpledialog.askfloat("Réponse", "Calculez l'intégrale de la fonction donnée : I = ∫cos(cx) dx, avec x de a={} à b={} et c={}".format(a, b, c))
            if math.isclose(user_answer, result, rel_tol=1e-6):
                messagebox.showinfo("Bravo !", f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}")
                points = 1
            else:
                messagebox.showerror("Désolé !", f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}")

        elif sous_choix == "f(x) = sin(cx)":
            result = -(math.cos(b * c) - math.cos(a * c)) / c

            user_answer = simpledialog.askfloat("Réponse", "Calculez l'intégrale de la fonction donnée : I = ∫sin(cx) dx, avec x de a={} à b={} et c={}".format(a, b, c))
            if math.isclose(user_answer, result, rel_tol=1e-6):
                messagebox.showinfo("Bravo !", f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}")
                points = 1
            else:
                messagebox.showerror("Désolé !", f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}")

        elif sous_choix == "f(x) = tan(cx)":
            result = (math.log(abs(math.cos(b * c))) - math.log(abs(math.cos(a * c)))) / c

            user_answer = simpledialog.askfloat("Réponse", "Calculez l'intégrale de la fonction donnée : I = ∫tan(cx) dx, avec x de a={} à b={} et c={}".format(a, b, c))
            if math.isclose(user_answer, result, rel_tol=1e-6):
                messagebox.showinfo("Bravo !", f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}")
                points = 1
            else:
                messagebox.showerror("Désolé !", f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}")

        else:
            messagebox.showerror("Erreur", "Choix invalide.")

    elif choix == "Fonctions logarithmiques":
        messagebox.showinfo("Intégration", choix)
        messagebox.showinfo("Sous-question", "f(x) = ln(cx)\n")
        
        c = Fraction(choose_parameter_positive_only())

        # j'ai mis valeur absolue parce que a et b peuvent être négatives
        result = b * math.log(abs(b * c)) - a * math.log(abs(a * c)) - c * (b - a)

        user_answer = simpledialog.askfloat("Réponse", "Calculez l'intégrale de la fonction donnée : I = ∫ln(cx) dx, avec x de a={} à b={} et c={}".format(a, b, c))
        if math.isclose(user_answer, result, rel_tol=1e-6):
            messagebox.showinfo("Bravo !", f"Bravo, votre réponse est correcte ! Le résultat de l'intégrale est : {result}")
            points = 1
        else:
            messagebox.showerror("Désolé !", f"Désolé, votre réponse est incorrecte. Le résultat de l'intégrale est : {result}")
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
        theme_choice = random.choices(["equation second degré", "integration"], weights=[p_equation, p_integration])[0]
        
        if theme_choice == "equation second degré":
            points += equation_second_degre()
        else:
            points += integration()    

    messagebox.showinfo("Résultat", f"Vous avez obtenu {points} points sur {question_count} questions.")


# Création de la fenêtre principale
window = tk.Tk()
window.title("Générateur de questions")
window.geometry("300x200")

# Création d'un cadre pour contenir le texte et le bouton
frame = tk.Frame(window)

# Création des widgets
question_count_label = tk.Label(frame, text="Nombre de questions :")
question_count_entry = tk.Entry(frame)
generate_button = tk.Button(frame, text="Générer les questions", command=generate_questions)

# Placement des widgets
question_count_label.pack(anchor="center")
question_count_entry.pack(anchor="center")
generate_button.pack(anchor="center")

# Placement du cadre dans la fenêtre
frame.pack(expand=True)

# Lancement de la boucle principale
window.mainloop()
