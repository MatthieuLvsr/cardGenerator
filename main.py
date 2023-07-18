import sys
import os

from src.car_content.car_content_pool import get_random_ambience
from src.car_content.car_elements import get_element_by_name

# Récupérer le chemin absolu du répertoire contenant le fichier main.py
current_path = os.path.dirname(os.path.abspath(__file__))

# Ajouter le chemin absolu du dossier car_content au chemin de recherche des modules Python
car_content_path = os.path.join(current_path, 'car_content')
sys.path.append(car_content_path)

# element = get_element_by_name("Techno blade")
# print(get_random_ambience(element))