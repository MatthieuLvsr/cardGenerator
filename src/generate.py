#!/usr/bin/env python

import sys
import os

# Récupérer le chemin absolu du répertoire contenant le fichier main.py
current_path = os.path.dirname(os.path.abspath(__file__))

# Ajouter le chemin absolu du dossier car_content au chemin de recherche des modules Python
car_content_path = os.path.join(current_path, 'car_content')
sys.path.append(car_content_path)

import argparse
import random
from car_content.car_collection import CarCollection
from car_content.car_elements import CarElements
from content.style import Style
from car_content.car_rarity import CarRarity


def main():

    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-n",
        "--cars",
        type=int,
        default=1,
        help="Number of cars to generate per element.",
    )

    argparser.add_argument(
        "-e",
        "--element",
        type=str,
        default=None,
        choices=[e.name.lower() for e in CarElements.ALL],
        help="Which element to generate cars for.",
    )

    argparser.add_argument(
        "-s",
        "--subject",
        type=str,
        default=None,
        help="What type of car to generate (e.g. monkey, dragon, etc.).",
    )

    argparser.add_argument(
        "-c",
        "--collection",
        type=str,
        default="new-collection",
        help="Name of the collection",
    )

    args = argparser.parse_args()
    number_of_cars = args.n_cars
    element_name = args.element
    subject_override = args.subject
    collection_name = args.collection
    element = (
        None
        if element_name is None
        else CarElements.get_element_by_name(element_name)
    )

    car_style: Style = Style(
        subject_type="car",
        style_suffix="--niji 5",
    )

    classic_collection = CarCollection(
        collection_name,
        theme_style=car_style,
        elements=CarElements.ALL,
        rarities=CarRarity.ALL,
    )

    all_collections = [
        classic_collection,
    ]

    collection_seed = random.randint(0, 1000000)
    for current_collection in all_collections:
        random.seed(collection_seed)
        all_elements = current_collection.elements

        if element is None:
            n_cars_to_generate = number_of_cars * len(all_elements)
        else:
            n_cars_to_generate = number_of_cars

        for i in range(n_cars_to_generate):
            current_element = (
                element if element else all_elements[i % len(all_elements)]
            )
            cars = current_collection.generate_random_cards(
                element=current_element, subject_override=subject_override
            )
            print(*cars, sep="\n\n")
        current_collection.export()


if __name__ == "__main__":
    main()
