from tkinter import simpledialog, messagebox, Tk, Label, Frame

def ask_question_with_timer(title, prompt, time_limit = 120):
    """
    Affiche une fenêtre de dialogue avec une minuterie et demande à l'utilisateur une question.
    
    Args:
        title (str): Le titre de la fenêtre de dialogue.
        prompt (str): Le message d'invite affiché à l'utilisateur.
        time_limit (int): La limite de temps en secondes pour que l'utilisateur réponde.
        
    Returns:
        str: La réponse de l'utilisateur, ou None si aucune réponse n'a été donnée.
    """
    # Création de la fenêtre Tkinter
    window = Tk()
    window.title(title)
    
    # Initialisation du temps écoulé et de la variable indiquant si la réponse a été donnée
    elapsed_time = 0
    response_given = False
    time_passed = False
    end_test = False

    # Fonction de mise à jour du temps restant
    def update_time():
        nonlocal elapsed_time, response_given, time_passed, end_test
        remaining_time = time_limit - elapsed_time

        # Mise à jour de l'étiquette du temps restant
        time_label.config(text=f"Temps restant : {remaining_time} s")

        time_passed = remaining_time <= 0
        
        if time_passed and not response_given:
            # Affichage du message de temps écoulé
            messagebox.showinfo("Temps écoulé", "Le temps est écoulé !")

            # Cacher la fenêtre de dialogue
            window.withdraw()
            
        elif not time_passed and not end_test:
            # Mise à jour du temps écoulé
            elapsed_time += 1

            # Appel récursif pour la mise à jour du temps restant
            window.after(1000, update_time)
            
        else:
            # La réponse a été donnée ou le temps est écoulé, donc fermer manuellement la fenêtre de dialogue
            window.destroy()
        
    # Étiquette du temps restant
    time_label = Label(window, text="")
    time_label.pack()

    # Lancement de la mise à jour du temps restant
    update_time()

    # Demande de saisie à l'utilisateur
    response = simpledialog.askstring(title, prompt)
    
    # Indiquer la fin de l'épreuve
    end_test = True
    
    # Indiquer que la réponse a été donnée ou que le temps est écoulé
    response_given = response is not None and response != "" and not time_passed
    if not response_given:
        response = None

    # Cacher la fenêtre de dialogue
    window.withdraw()
    
    # Retourner la réponse de l'utilisateur
    return response