# Présentation

## Auteurs
- Christophe Wang
- Pierre Laurent
- Zakaria Mellah

## Ce qui a été fait
Tout a été fait sauf le chronomètre sur la partie `probability_terminal.py` donc l'interface textuelle. 
Le chronomètre fonctionne pour la partie interface graphique mais la boîte de dialogue ne disparaît pas lorsque le temps est écoulé. 
La valeur de la réponse contenue dans la boîte de dialogue est soit nulle (si rien n'y a été écrit) soit la valeur saisie avant que le temps ne soit écoulé.
## Installation
```bash
    pip install -r requirements.txt
```
## Interface textuelle via terminal
Pour cela, lancer le fichier `probability_terminal.py`
> Il n'y a pas de chronomètre dans ce code

Si vous souhaitez voir les réponses (affichées en vert dans le terminal), changez la ligne dans `utils/constant.py` de:
```
afficher_tous_infos_terminal = False 
```
à 
```
afficher_tous_infos_terminal = True 
```

## Interface graphique
Pour cela, lancer le fichier `probability.py`

# Import Statements

```python
import tkinter
import random
import math
import numpy
from fractions import Fraction
import sympy


import matplotlib.pyplot as plt
from scipy import stats