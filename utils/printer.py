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