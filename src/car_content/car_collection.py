from dataclasses import dataclass
import random
from car_content.car_content_pool import (
    AMBIENCE_BY_TYPE,
    get_closest_match,
    get_model_types,
    get_environments,
    get_random_ambience,
    get_random_detail_adjective,
    get_random_rarity_adjective,
    get_random_style_suffix,
)
from content.collection import Collection
from content.style import Style
from mechanics.element import Element
from mechanics.card import Card
from mechanics.rarity import Rarity
# from mechanics.ability import Ability
from car_content.car_prompts import (
    generate_card_name,
    generate_desc,
    get_image_prompt,
    get_visual_description,
)
# from util.ability_name_library import get_ability_name
from util.gpt_call import gpt_client


@dataclass
class CarCollection(Collection):

    BASE_POINTS = 4
    NEUTRAL_ELEMENT_CHANCE = 0.5
    MIXED_ELEMENT_CHANCE = 0.5

    def generate_card(
        self,
        element: Element,
        rarity: Rarity,
        inherited_style: Style = None,
        subject_override: str = None,
    ) -> Card:

        speed_points = random.randint(25,50)
        acceleration_points = random.randint(25,50)
        maniability_points = random.randint(25,50)
        speed = speed_points + random.randint(0,10) + random.randint(0,rarity.index * 10)
        acceleration = acceleration_points + random.randint(0,10) + random.randint(0,rarity.index * 10)
        maniability = maniability_points + random.randint(0,10) + random.randint(0,rarity.index * 10)

        style = self.generate_style(
            inherited_style, element, rarity, subject_override
        )

        card = Card(
            index=len(self.cards) + 1,
            name="Untitled Card",
            element=element,
            rarity=rarity,
            # abilities=abilities,
            # hp=hp,
            speed=speed,
            acceleration=acceleration,
            maniability=maniability,
            style=style,
        )

        card.image_prompt = get_image_prompt(card)
        card.visual_description = get_visual_description(card)

        # Generate a name for the card.
        if gpt_client().is_openai_enabled:
            card.name = generate_card_name(card, self.card_names_seen)
            card.description = generate_desc(card)

        card.image_prompt = get_image_prompt(card)
        card.visual_description = get_visual_description(card)
        self.card_names_seen.add(card.name)
        self.cards.append(card)
        return card

    def generate_style(
        self,
        inherited_style: Style,
        element: Element,
        rarity: Rarity,
        # series_index: int | None = None,
        subject_override: str = None,
    ) -> Style:

        style = Style(
            style_prefix=self.theme_style.style_prefix,
            style_suffix=self.theme_style.style_suffix,
        )

        style.subject_type = self.theme_style.subject_type

        # Pick the card's subject (car type)
        if inherited_style is not None:
            style.subject = inherited_style.subject
            style.subject_adjectives = inherited_style.subject_adjectives
            style.detail = inherited_style.detail
            style.environment = inherited_style.environment
        else:

            if subject_override is not None:
                subject = get_closest_match(subject_override)
                style.subject = subject.name
            else:
                potential_subjects = get_model_types(element)
                reduced_subjects = set(potential_subjects) - self.subjects_seen
                if len(reduced_subjects) == 0:
                    reduced_subjects = potential_subjects

                subject = random.choice(list(reduced_subjects))
                self.subjects_seen.add(subject)
                style.subject = subject.name

            potential_details = set(subject.details)
            reduced_details = set(potential_details) - self.subjects_seen
            if len(reduced_details) == 0:
                reduced_details = potential_details

            detail_adjective = get_random_detail_adjective(element=element)
            style.detail = detail_adjective

            # Pick the environment
            potential_environments = get_environments(element)
            style.environment = random.choice(potential_environments)

        # Pick adjective(s) for the subject.
        rarity_prefix = get_random_rarity_adjective(rarity.index)
        # series_prefix = get_random_series_adjective(series_index)
        element_prefix = f"{element.name.lower()}-type"

        size_prefix = rarity_prefix

        style.subject_adjectives = [
            *self.theme_style.subject_adjectives,
            size_prefix,
            element_prefix,
            style.detail
        ]

        style.ambience = get_random_ambience(element)

        # Set the style suffix
        style.style_suffix = (
            # f"{get_random_style_suffix(series_index)} {self.theme_style.style_suffix}"
            f"{get_random_style_suffix(element)} {self.theme_style.style_suffix}"
        )

        return style
