import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def descriptive_statistics(file_path, num_classes):
    """
    Calcule les statistiques descriptives et affiche l'histogramme d'un fichier de données.

    Args:
        file_path (str): Chemin d'accès au fichier de données.
        num_classes (int): Nombre de classes pour l'histogramme.

    Returns:
        None
    """

    # Charger les données à partir du fichier
    data = np.loadtxt(file_path)

    # Calcul des statistiques descriptives
    num_observations = len(data)
    mean = np.mean(data)
    std_dev = np.std(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    kurtosis = stats.kurtosis(data, fisher=False)
    skewness = stats.skew(data)

    # Affichage des résultats
    print("---- Statistiques descriptives pour le fichier", file_path, "----")
    print("Nombre d'observations :", num_observations)
    print("Moyenne empirique :", mean)
    print("Écart-type :", std_dev)
    print("Premier quartile :", q1)
    print("Troisième quartile :", q3)
    print("Kurtosis normalisé :", kurtosis)
    print("Skewness :", skewness)

    # Affichage de l'histogramme
    print("\nAffichage de l'histogramme...")
    plt.hist(data, bins=num_classes, color='blue', alpha=0.7)
    plt.xlabel('Valeurs')
    plt.ylabel('Fréquence')
    plt.title('Histogramme des valeurs - ' + file_path)
    plt.grid(True)
    plt.show(block=False)  # Ne pas bloquer l'exécution

def inferential_statistics(file_path1, file_path2, alpha, alpha1, alpha2, mu0):
    """
    Effectue des tests statistiques et affiche les résultats pour deux fichiers de données.

    Args:
        file_path1 (str): Chemin d'accès au premier fichier de données.
        file_path2 (str): Chemin d'accès au deuxième fichier de données.
        alpha (float): Niveau de confiance pour l'intervalle de confiance.
        alpha1 (float): Niveau alpha du test de comparaison de la moyenne.
        alpha2 (float): Niveau alpha du test d'indépendance du chi-deux.
        mu0 (float): Moyenne à comparer dans le test de comparaison de la moyenne.

    Returns:
        None
    """

    # Charger les données à partir des fichiers
    data1 = np.loadtxt(file_path1)
    data2 = np.loadtxt(file_path2)

    # Estimation de µ et σ pour chaque variable
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    std_dev1 = np.std(data1)
    std_dev2 = np.std(data2)

    # Intervalle de confiance pour µ
    z_critical = stats.norm.ppf(1 - alpha/2)
    margin_of_error = z_critical * np.sqrt((std_dev1**2)/len(data1) + (std_dev2**2)/len(data2))
    confidence_interval = (mean1 - mean2 - margin_of_error, mean1 - mean2 + margin_of_error)

    # Test de comparaison de la moyenne
    t_statistic, p_value = stats.ttest_ind(data1, data2, alternative='greater')
    reject_h0_mean = p_value < alpha1

    # Test d'indépendance du chi-deux
    _, p_value_chi2, _, _ = stats.chi2_contingency([data1, data2])
    reject_h0_chi2 = p_value_chi2 < alpha2

    # Affichage des résultats
    print("---- Statistiques inférentielles ----")
    print("Variable 1 -", file_path1)
    print("Moyenne :", mean1)
    print("Écart-type :", std_dev1)
    print("\nVariable 2 -", file_path2)
    print("Moyenne :", mean2)
    print("Écart-type :", std_dev2)
    print("\nIntervalle de confiance pour la différence des moyennes (niveau {}%) :".format((1-alpha)*100), confidence_interval)
    print("\nRésultats du test de comparaison de la moyenne (H0: µ1 = µ2) :")
    print("T-statistic :", t_statistic)
    print("P-value :", p_value)
    print("H0 rejetée :", reject_h0_mean)
    print("\nRésultats du test d'indépendance du chi-deux :")
    print("P-value :", p_value_chi2)
    print("H0 rejetée :", reject_h0_chi2)

descriptive_statistics("notesproba.txt", num_classes=10)
descriptive_statistics("notestat.txt", num_classes=10)
inferential_statistics("notesproba.txt", "notestat.txt", alpha=0.05, alpha1=0.05, alpha2=0.05, mu0=10.5)
