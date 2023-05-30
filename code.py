import tkinter as tk
from tkinter import messagebox
from random import uniform, choice
from scipy.stats import kurtosis, skew, norm, ttest_ind, chi2_contingency
import numpy as np
import matplotlib.pyplot as plt

def generate_quadratic_equation():
    """
    Génère une équation du second degré aléatoire.

    Returns:
        Tuple: Coefficients de l'équation (a, b, c).
    """
    
    a = uniform(-10, 10)
    b = uniform(-10, 10)
    c = uniform(-10, 10)
    return a, b, c

def solve_quadratic_equation(a, b, c):
    """
    Résout une équation du second degré.

    Args:
        a (float): Coefficient a.
        b (float): Coefficient b.
        c (float): Coefficient c.

    Returns:
        str: Solution de l'équation.
    """
    # Validation des entrées
    if not all(isinstance(coeff, (int, float)) for coeff in (a, b, c)):
        raise ValueError("Les coefficients a, b et c doivent être des nombres réels.")
    if a == 0:
        raise ValueError("Le coefficient a ne peut pas être nul.")
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Pas de solution"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Solution unique : x = {x}"
    else:
        x1 = (-b - np.sqrt(discriminant)) / (2*a)
        x2 = (-b + np.sqrt(discriminant)) / (2*a)
        return f"Solutions distinctes : x1 = {x1}, x2 = {x2}"

def generate_integral():
    """
    Génère une intégrale aléatoire.

    Returns:
        Tuple: Paramètres de l'intégrale (a, b, function_type, *args).
    """
    a = uniform(-10, 10)
    b = uniform(-10, 10)
    function_type = choice(['power', 'trigonometric', 'logarithmic'])
    if function_type == 'power':
        c = uniform(-10, 10)
        d = uniform(-10, 10)
        alpha = uniform(-10, 10)
        return a, b, function_type, c, d, alpha
    elif function_type == 'trigonometric':
        c = uniform(-10, 10)
        return a, b, function_type, c
    elif function_type == 'logarithmic':
        c = uniform(0, 10)
        return a, b, function_type, c

def calculate_integral(a, b, function_type, *args):
    """
    Calcule l'intégrale donnée les paramètres.

    Args:
        a (float): Limite inférieure.
        b (float): Limite supérieure.
        function_type (str): Type de fonction ('power', 'trigonometric', 'logarithmic').
        *args: Paramètres supplémentaires de la fonction.

    Returns:
        float: Valeur de l'intégrale.
    """
    # Validation des entrées
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Les limites a et b doivent être des nombres réels.")
    
    if function_type == 'power':
        if len(args) != 3:
            raise ValueError("Le type de fonction 'power' attend 3 paramètres (c, d, alpha).")
        c, d, alpha = args
        if not all(isinstance(param, (int, float)) for param in (c, d, alpha)):
            raise ValueError("Les paramètres de la fonction 'power' doivent être des nombres réels.")
        return (1 / (d*c - a*c)**(alpha+1)) - (1 / (d*c - b*c)**(alpha+1))
    
    elif function_type == 'trigonometric':
        if len(args) != 1:
            raise ValueError("Le type de fonction 'trigonometric' attend 1 paramètre (c).")
        c = args[0]
        if not isinstance(c, (int, float)):
            raise ValueError("Le paramètre de la fonction 'trigonometric' doit être un nombre réel.")
        if c != 0:
            integral = (np.sin(b*c) - np.sin(a*c)) / c
        else:
            integral = b - a
        return integral
    
    elif function_type == 'logarithmic':
        if len(args) != 1:
            raise ValueError("Le type de fonction 'logarithmic' attend 1 paramètre (c).")
        c = args[0]
        if not isinstance(c, (int, float)):
            raise ValueError("Le paramètre de la fonction 'logarithmic' doit être un nombre réel.")
        return b*np.log(b*c) - a*np.log(a*c) - c*(b - a)

def generate_probability_question():
    """
    Génère une question de probabilité aléatoire.

    Returns:
        str: Question de probabilité.
    """
    question_type = choice(['quadratic_equation', 'integral'])
    if question_type == 'quadratic_equation':
        a, b, c = generate_quadratic_equation()
        return question_type, (a, b, c)
    elif question_type == 'integral':
        a, b, function_type, *args = generate_integral()
        return question_type, (a, b, function_type, *args)

def assign_points_probability(question_type):
    """
    Attribue des points en fonction du type de question de probabilité.

    Args:
        question_type (str): Type de question ('quadratic_equation', 'integral').

    Returns:
        float: Points attribués.
    """
    # if question_type == 'quadratic_equation':
    #     return 1
    # elif question_type == 'integral':
    #     return choice([1, 1.5])
    points_mapping = {
        'quadratic_equation': 1,
        'integral': choice([1, 1.5])
    }
    return points_mapping.get(question_type, 0)

def read_data_from_file(file_path):
    """
    Lit les données à partir d'un fichier.

    Args:
        file_path (str): Chemin du fichier.

    Returns:
        list: Données lues à partir du fichier.
    """
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                data.append(float(line))
        return data
    except FileNotFoundError:
        print("Le fichier spécifié est introuvable.")
    except IOError:
        print("Une erreur s'est produite lors de la lecture du fichier.")

def solve_quadratic_equation_probability():
    """
    Résout une équation du second degré dans la partie probabilité.
    """
    a, b, c = generate_quadratic_equation()
    solution = solve_quadratic_equation(a, b, c)
    messagebox.showinfo("Probabilité : Résoudre une équation du second degré", solution)

def calculate_integral_probability():
    """
    Calcule une intégrale dans la partie probabilité.
    """
    a, b, function_type, *args = generate_integral()
    integral = calculate_integral(a, b, function_type, *args)
    messagebox.showinfo("Probabilité : Calcul d'intégrale", f"Valeur de l'intégrale : {integral}")

def calculate_descriptive_statistics(data):
    """
    Calcule les statistiques descriptives pour les données données.

    Args:
        data (list): Données.

    Returns:
        tuple: Statistiques descriptives (n, mean, std_dev, quartile_1, quartile_3, kurtosis, skewness).
    """
    n = len(data)
    mean = np.mean(data)
    std_dev = np.std(data)
    quartile_1 = np.percentile(data, 25)
    quartile_3 = np.percentile(data, 75)
    kurtosis_b = kurtosis(data, fisher=False)
    skewness = skew(data)
    return n, mean, std_dev, quartile_1, quartile_3, kurtosis_b, skewness

def display_histogram(data):
    """
    Affiche l'histogramme des données.

    Args:
        data (list): Données.
    """
    histogram, edges = np.histogram(data, bins='auto')
    print("Histogram:")
    for i in range(len(histogram)):
        print(f"{edges[i]} - {edges[i+1]}: {histogram[i]}")
        
    plt.bar(edges[:-1], histogram, width=np.diff(edges), align='edge')
    plt.xlabel('Valeurs')
    plt.ylabel('Fréquence')
    plt.title('Histogramme')
    plt.show(block=False)

def compare_statistics(probability_data, statistics_data):
    """
    Compare les statistiques des données de probabilité et de statistiques.

    Args:
        probability_data (tuple): Statistiques des données de probabilité.
        statistics_data (tuple): Statistiques des données de statistiques.
    """
    probability_stats = calculate_descriptive_statistics(probability_data)
    statistics_stats = calculate_descriptive_statistics(statistics_data)

    print("\nComparison of Descriptive Statistics:")
    print("Statistics for Probability Notes:")
    print(f"Number of Observations: {probability_stats[0]}")
    print(f"Mean: {probability_stats[1]}")
    print(f"Standard Deviation: {probability_stats[2]}")
    print(f"First Quartile: {probability_stats[3]}")
    print(f"Third Quartile: {probability_stats[4]}")
    print(f"Kurtosis: {probability_stats[5]}")
    print(f"Skewness: {probability_stats[6]}")

    print("\nStatistics for Statistics Notes:")
    print(f"Number of Observations: {statistics_stats[0]}")
    print(f"Mean: {statistics_stats[1]}")
    print(f"Standard Deviation: {statistics_stats[2]}")
    print(f"First Quartile: {statistics_stats[3]}")
    print(f"Third Quartile: {statistics_stats[4]}")
    print(f"Kurtosis: {statistics_stats[5]}")
    print(f"Skewness: {statistics_stats[6]}")

    if probability_stats[1] > statistics_stats[1]:
        print("\nThe level of students was better in Probability.")
    elif probability_stats[1] < statistics_stats[1]:
        print("\nThe level of students was better in Statistics.")
    else:
        print("\nThe level of students was similar in Probability and Statistics.")

    interpret_kurtosis_skewness(probability_stats[5], "Probability")
    interpret_kurtosis_skewness(statistics_stats[5], "Statistics")

    print("\nHistogram for Probability Notes:")
    display_histogram(probability_data)

    print("\nHistogram for Statistics Notes:")
    display_histogram(statistics_data)

# Interprétation du kurtosis et skewness
def interpret_kurtosis_skewness(statistic, subject):
    if statistic < 0:
        print(f"\nThe distribution of {subject} Notes is platykurtic.")
    elif statistic > 0:
        print(f"\nThe distribution of {subject} Notes is leptokurtic.")
    else:
        print(f"\nThe distribution of {subject} Notes is mesokurtic.")

    if statistic < -1:
        print(f"The distribution of {subject} Notes is highly skewed to the left.")
    elif statistic > 1:
        print(f"The distribution of {subject} Notes is highly skewed to the right.")
    elif -1 <= statistic <= 1:
        print(f"The distribution of {subject} Notes is approximately symmetric.")

def descriptive_statistics_menu():
    """
    Affiche le menu pour les statistiques descriptives.
    """
    try:
        file_path = "notesproba.txt"
        data = read_data_from_file(file_path)
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Fichier de notes pour la probabilité introuvable.")
        return
    
    display_histogram(data)
    
    n, mean, std_dev, quartile_1, quartile_3, kurtosis, skewness = calculate_descriptive_statistics(data)
    message = f"Nombre d'observations : {n}\n"
    message += f"Moyenne : {mean}\n"
    message += f"Écart type : {std_dev}\n"
    message += f"Premier quartile : {quartile_1}\n"
    message += f"Troisième quartile : {quartile_3}\n"
    message += f"Kurtosis : {kurtosis}\n"
    message += f"Asymétrie : {skewness}"
    messagebox.showinfo("Statistiques : Statistique descriptive", message)

def inferential_statistics_menu():
    try:
        probability_file_path = "notesproba.txt"
        statistics_file_path = "notestat.txt"
        probability_data = read_data_from_file(probability_file_path)
        statistics_data = read_data_from_file(statistics_file_path)
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Fichier de notes introuvable.")
        return

    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Statistiques : Statistique inférentielle")

    # Ajout des widgets d'entrée de texte pour les valeurs d'alpha
    alpha_label = tk.Label(window, text="Niveau de confiance (1 - alpha) pour l'intervalle de confiance :")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    alpha1_label = tk.Label(window, text="Niveau de signification (alpha_1) pour le test de comparaison de moyenne :")
    alpha1_label.pack()
    alpha1_entry = tk.Entry(window)
    alpha1_entry.pack()

    alpha2_label = tk.Label(window, text="Niveau de signification (alpha_2) pour le test d'indépendance du chi-deux :")
    alpha2_label.pack()
    alpha2_entry = tk.Entry(window)
    alpha2_entry.pack()

    # Fonction pour effectuer les calculs et afficher les résultats
    def calculate_statistics():
        alpha = float(alpha_entry.get())
        alpha_1 = float(alpha1_entry.get())
        alpha_2 = float(alpha2_entry.get())

        compare_statistics(probability_data, statistics_data)

        probability_mean = np.mean(probability_data)
        probability_std_dev = np.std(probability_data)
        statistics_mean = np.mean(statistics_data)
        statistics_std_dev = np.std(statistics_data)

        probability_confidence_interval = norm.interval(1 - alpha, loc=probability_mean, scale=probability_std_dev / np.sqrt(len(probability_data)))
        statistics_confidence_interval = norm.interval(1 - alpha, loc=statistics_mean, scale=statistics_std_dev / np.sqrt(len(statistics_data)))

        probability_output.config(text=f"Intervalle de confiance pour la moyenne des probabilités (1 - alpha) : {probability_confidence_interval}")
        statistics_output.config(text=f"Intervalle de confiance pour la moyenne des statistiques (1 - alpha) : {statistics_confidence_interval}")

        mean_comparison_result = ttest_ind(probability_data, statistics_data, alternative='greater')
        mean_test_output.config(text=f"Statistique de T : {mean_comparison_result.statistic}\nValeur de p : {mean_comparison_result.pvalue}")

        if mean_comparison_result.pvalue < alpha_1:
            mean_hypothesis_output.config(text="L'hypothèse nulle (μ = μ0) est rejetée en faveur de l'hypothèse alternative (μ > μ0).")
        else:
            mean_hypothesis_output.config(text="L'hypothèse nulle (μ = μ0) ne peut pas être rejetée.")

        chi2_statistic, p_value, _, _ = chi2_contingency([probability_data, statistics_data])
        chi2_test_output.config(text=f"Statistique du chi-deux : {chi2_statistic}\nValeur de p : {p_value}")

        if p_value < alpha_2:
            chi2_hypothesis_output.config(text="L'hypothèse nulle (les variables sont indépendantes) est rejetée en faveur de l'hypothèse alternative (les variables sont dépendantes).")
        else:
            chi2_hypothesis_output.config(text="L'hypothèse nulle (les variables sont indépendantes) ne peut pas être rejetée.")

    # Ajout du bouton pour calculer les statistiques
    calculate_button = tk.Button(window, text="Calculer les statistiques", command=calculate_statistics)
    calculate_button.pack()

    # Ajout des widgets pour afficher les résultats
    probability_output = tk.Label(window, text="")
    probability_output.pack()
    statistics_output = tk.Label(window, text="")
    statistics_output.pack()
    mean_test_output = tk.Label(window, text="")
    mean_test_output.pack()
    mean_hypothesis_output = tk.Label(window, text="")
    mean_hypothesis_output.pack()
    chi2_test_output = tk.Label(window, text="")
    chi2_test_output.pack()
    chi2_hypothesis_output = tk.Label(window, text="")
    chi2_hypothesis_output.pack()

def generate_gui():
    """
    Génère l'interface graphique.
    """
    root = tk.Tk()
    root.title("Probabilités et Statistiques")
    root.geometry("400x300")

    main_menu = tk.Menu(root)

    probability_menu = tk.Menu(main_menu, tearoff=0)
    probability_menu.add_command(label="Résoudre une équation du second degré", command=solve_quadratic_equation_probability)
    probability_menu.add_command(label="Calculer une intégrale", command=calculate_integral_probability)
    main_menu.add_cascade(label="Probabilité", menu=probability_menu)

    statistics_menu = tk.Menu(main_menu, tearoff=0)
    statistics_menu.add_command(label="Statistique descriptive", command=descriptive_statistics_menu)
    statistics_menu.add_command(label="Statistique inférentielle", command=inferential_statistics_menu)
    main_menu.add_cascade(label="Statistiques", menu=statistics_menu)

    root.config(menu=main_menu)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    solve_button = tk.Button(button_frame, text="Probabilité", command=solve_quadratic_equation_probability)
    solve_button.pack(side=tk.LEFT, padx=10)

    integral_button = tk.Button(button_frame, text="Probabilité", command=calculate_integral_probability)
    integral_button.pack(side=tk.LEFT, padx=10)

    statistics_frame = tk.Frame(root)
    statistics_frame.pack(pady=20)

    descriptive_button = tk.Button(statistics_frame, text="Statistiques", command=descriptive_statistics_menu)
    descriptive_button.pack(side=tk.LEFT, padx=10)

    inferential_button = tk.Button(statistics_frame, text="Statistiques", command=inferential_statistics_menu)
    inferential_button.pack(side=tk.LEFT, padx=10)

    quit_button = tk.Button(root, text="Quitter", command=root.quit)
    quit_button.pack(pady=10)

    root.mainloop()

generate_gui()
