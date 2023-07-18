from dataclasses import dataclass, field
from functools import cached_property
from content.style import Style
from mechanics.element import Element
from mechanics.rarity import Rarity
# from mechanics.ability import Ability

STAR_UNICODE = "★ "


@dataclass
class Card:

    index: int
    name: str
    element: Element
    rarity: Rarity
    # hp: int
    speed:int
    acceleration:int
    maniability:int
    # abilities: list[Ability] = field(default_factory=list)
    description: str = ""
    part_of_evolution: bool = False
    style: Style = field(default_factory=Style)

    image_prompt: str | None = None
    visual_description: str | None = None

    def __repr__(self):
        rarity_stars = STAR_UNICODE * (self.rarity.index + 1)
        message = f"{self.name} ({self.element.ascii_name()})\n"
        # message += f"HP: {self.hp}\n"
        message += f"SPEED: {self.speed}\n"
        message += f"ACCELERATION: {self.acceleration}\n"
        message += f"MANIABILITY: {self.maniability}\n"
        message += f"Rarity: {rarity_stars} ({self.rarity.name})\n"
        # message += f"Abilities:\n"
        # for ability in self.abilities:
        #     message += f"  {ability}\n"

        message += f"Description:\n"
        message += f"{self.description}\n\n"
        message += f"Image Prompt:\n"
        message += f"{self.image_prompt}\n\n"
        return message

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "image": f"ipfs://bafybeicr4v6rqrrqvgatvw3mwrzdd6rdiqdifdcsz3d5wifnbyw6r7mccu/{self.index}.png",
            "attributes": [
                {
                    "trait_type": "Element",
                    "value": self.element.name.capitalize()
                },
                {
                    "trait_type": "Rarity",
                    "value": self.rarity.name.capitalize()
                },
                {
                    "trait_type": "Speed",
                    "value": self.speed
                },
                {
                    "trait_type": "Acceleration",
                    "value": self.acceleration
                },
                {
                    "trait_type": "Maniability",
                    "value": self.maniability
                }
            ]
        }

    @property
    def image_file(self):
        return f"{self.index}.png"

    @cached_property
    def snake_case_name(self):
        return self.name.lower().replace(" ", "_")
