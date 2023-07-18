import argparse
import json
import os
import pathlib
from PIL import Image, ImageFont, ImageDraw

from car_content.car_elements import CarElements
from car_content.car_rarity import CarRarity
from mechanics.card import Card
from mechanics.element import Element


MONSTER_IMAGE_SCALE = 0.3
MONSTER_IMAGE_SCALE_SQ = 0.355

ABILITY_WIDTH = 370
ABILITY_HEIGHT = 72
ABILITY_COST_WIDTH = 76
ABILITY_COST_GAP = 12
ELEMENT_SIZE = 40
ABILITY_GAP = 4
POWER_WIDTH = 64

STATUS_Y_POSITION = 568
STATUS_X_GAP = 82
STATUS_SIZE = 20


def render_cards(collection_path: str):
    card_path = pathlib.Path(collection_path, "cards")
    card_render_path = pathlib.Path(collection_path, "renders")
    os.makedirs(card_render_path, exist_ok=True)

    for card_path in card_path.iterdir():
        index = os.path.splitext(os.path.basename(card_path))[0]

        # Only render .json files.
        if not card_path.suffix == ".json":
            continue

        with open(card_path) as f:
            data = json.load(f)
            card = card_from_json(data,index)
            card_image = render_card(card, collection_path)
            image_name = f"{card.index}.png"
            card_image.save(card_render_path / f"{image_name}")


def render_card(card: Card, collection_path: str):

    print(f"Rendering {card.name} - {card.index}")
    card_template_name = f"{card.element.name.lower()}.png"
    card_image = Image.open(f"ressources/cards/{card_template_name}")

    card_art_path = pathlib.Path(collection_path, "images", card.image_file)
    if pathlib.Path(card_art_path).exists():
        canvas = Image.new("RGBA", card_image.size, (0, 0, 0, 0))
        card_art_image = Image.open(card_art_path)

        if card_art_image.width == card_art_image.height:
            rescale_factor = MONSTER_IMAGE_SCALE_SQ
        else:
            rescale_factor = MONSTER_IMAGE_SCALE

        resized_image_shape = (
            int(card_art_image.size[0] * rescale_factor),
            int(card_art_image.size[1] * rescale_factor),
        )
        card_art_image = card_art_image.resize(resized_image_shape)

        # Center the image.
        card_center_x = card_image.size[0] / 2
        card_center_y = 210
        monster_image_x = card_center_x - (card_art_image.size[0] / 2)
        # monster_image_y = card_center_y - (card_art_image.size[1] / 2)
        monster_image_y = 105
        canvas.paste(card_image, (0, 0), card_image)
        canvas.paste(card_art_image, (int(monster_image_x), int(monster_image_y)))
        card_image = canvas
    else:
        # Print in yellow ASCII.
        print(f"\033[93m [WARN] {card_art_path} not found.\033[0m")

    # Write the name of the card.
    name_text_position = (90, 70)
    title_font = ImageFont.truetype("ressources/font/Cabin-Bold.ttf", 28)
    name_text = card.name

    # Add the element logo
    element_image = Image.open(f"ressources/elements/{card.element.name.lower()}_element.png")
    element_image = element_image.resize((ELEMENT_SIZE, ELEMENT_SIZE))
    canvas.paste(element_image,(340,40))

    # Draw the name text onto the card.
    draw = ImageDraw.Draw(card_image)
    draw.text(
        name_text_position, name_text, font=title_font, fill=(255, 255, 255), anchor="ls"
    )

    # # Draw the HP on the card.
    # hp_x_position = card_image.width - 86
    # hp_y_position = 64
    # hp_font = ImageFont.truetype("ressources/font/Cabin_Condensed-Regular.ttf", 28)
    # hp_text = f"{card.hp} HP"
    # draw.text(
    #     (hp_x_position, hp_y_position),
    #     hp_text,
    #     font=hp_font,
    #     fill=(255, 0, 0),
    #     anchor="rs",
    # )

    # Draw the stats

    # Draw the Speed on the card.
    speed_x_position = 140
    speed_y_position = card_image.height - 165
    speed_font = ImageFont.truetype("ressources/font/Cabin_Condensed-Regular.ttf", 24)
    speed_text = f"Speed :"
    draw.text(
        (speed_x_position, speed_y_position),
        speed_text,
        font=speed_font,
        fill=(255, 255, 255),
        anchor="rs",
    )
    draw.text(
        (card_image.width - 80, speed_y_position),
        f"{card.speed}",
        font=speed_font,
        fill=(255, 255, 255),
        anchor="rs",
    )

    # Draw the Acceleration on the card.
    acceleration_x_position = 190
    acceleration_y_position = card_image.height - 125
    acceleration_font = ImageFont.truetype("ressources/font/Cabin_Condensed-Regular.ttf", 24)
    acceleration_text = f"Acceleration :"
    draw.text(
        (acceleration_x_position, acceleration_y_position),
        acceleration_text,
        font=acceleration_font,
        fill=(255, 255, 255),
        anchor="rs",
    )
    draw.text(
        (card_image.width - 80, acceleration_y_position),
        f"{card.acceleration}",
        font=acceleration_font,
        fill=(255, 255, 255),
        anchor="rs",
    )

    # Draw the Maniability on the card.
    maniability_x_position = 180
    maniability_y_position = card_image.height - 85
    maniability_font = ImageFont.truetype("ressources/font/Cabin_Condensed-Regular.ttf", 24)
    maniability_text = f"Maniability :"
    draw.text(
        (maniability_x_position, maniability_y_position),
        maniability_text,
        font=maniability_font,
        fill=(255, 255, 255),
        anchor="rs",
    )
    draw.text(
        (card_image.width - 80, maniability_y_position),
        f"{card.maniability}",
        font=maniability_font,
        fill=(255, 255, 255),
        anchor="rs",
    )

    # # Draw the abilities on the card.
    # ability_y_position_center = 450
    # # Center the abilities on the card.
    # ability_x_position = (card_image.width - ABILITY_WIDTH) // 2

    # if len(card.abilities) == 1:
    #     ability_y_origin = ability_y_position_center - (ABILITY_HEIGHT // 2)
    # elif len(card.abilities) == 2:
    #     ability_y_origin = ability_y_position_center - (
    #         ABILITY_HEIGHT + ABILITY_COST_GAP // 2
    #     )

    # # Draw the abilities in reverse order so that the first ability is at the bottom.
    # abilities = reversed(card.abilities)
    # for i, ability in enumerate(abilities):

    #     ability_image = render_ability(ability)
    #     ability_y = ability_y_origin + (i * (ABILITY_HEIGHT + ABILITY_COST_GAP))
    #     card_image.paste(
    #         ability_image,
    #         (int(ability_x_position), ability_y),
    #         ability_image,
    #     )

    #     ability_y_position_center += ABILITY_HEIGHT

    # # Draw line between abilities.
    # if len(card.abilities) > 1:
    #     # Draw line between abilities.
    #     line_y = ability_y_origin + ABILITY_HEIGHT
    #     line_extension_gap = 36
    #     draw.line(
    #         (
    #             (line_extension_gap, line_y),
    #             (card_image.width - line_extension_gap, line_y),
    #         ),
    #         fill=(0, 0, 0),
    #         width=2,
    #     )

    # # Render the status of the card (weakness, resistance, etc.)
    # render_weakness_and_resist(card, card_image)

    # Write the rarity of the Pokemon.
    rarity_text_position = (70, 545)
    rarity_font = ImageFont.truetype("ressources/font/Cabin_Condensed-Regular.ttf", 18)
    rarity_text = f"{card.rarity.name} {card.element.name}-type Card"
    draw.text(
        rarity_text_position,
        rarity_text.title(),
        font=rarity_font,
        fill=(255, 255, 255),
        anchor="lm",
    )

    # # Write the rarity of the Pokemon.
    # rarity_symbol_position = (47, 62)
    # symbol_font = ImageFont.truetype("ressources/font/NotoSansSymbols2-Regular.ttf", 22)
    # rarity_symbols = ["⬤", "◆", "★","Þ","¤","Ø"]
    # rarity_symbol_sizes = [10, 14, 22,25,25,25]

    # symbol_text = rarity_symbols[card.rarity.index]
    # symbol_font = ImageFont.truetype(
    #     "ressources/font/NotoSansSymbols2-Regular.ttf",
    #     rarity_symbol_sizes[card.rarity.index],
    # )

    # draw.text(
    #     rarity_symbol_position,
    #     symbol_text,
    #     font=symbol_font,
    #     fill=(255, 255, 255),
    #     anchor="mm",
    # )

    rarity_images = ["common","uncommon","rare","mythical","legendary"]

    # Add the rarity logo
    rarity_image = Image.open(f"ressources/rarities/{rarity_images[card.rarity.index]}.png")
    rarity_image = rarity_image.resize((ELEMENT_SIZE, ELEMENT_SIZE))
    canvas.paste(rarity_image,(22,40))

    return card_image


# def render_ability(ability: Ability):
#     ability_image = Image.new("RGBA", (ABILITY_WIDTH, ABILITY_HEIGHT), (0, 0, 0, 0))
#     cost_image = render_element_cost(ability.costs_as_elements)
#     ability_image.paste(cost_image, (0, 0), cost_image)

#     # Ability name description.
#     name_text_position = (ABILITY_WIDTH // 2, ABILITY_HEIGHT // 2)
#     name_font = ImageFont.truetype("ressources/font/Cabin-Bold.ttf", 24)
#     name_text = ability.name
#     draw = ImageDraw.Draw(ability_image)
#     draw.text(
#         name_text_position, name_text, font=name_font, fill=(0, 0, 0), anchor="mm"
#     )

#     # Draw the ability power text.
#     power_text_position = (ABILITY_WIDTH - 12, ABILITY_HEIGHT // 2)
#     power_font = ImageFont.truetype("ressources/font/Cabin_Condensed-Regular.ttf", 32)
#     power_text = str(ability.power)
#     draw.text(
#         power_text_position,
#         power_text,
#         font=power_font,
#         fill=(0, 0, 0),
#         anchor="rm",
#     )
#     return ability_image


# def render_element_cost(elements: list[str]):

#     cost = len(elements)
#     cost_canvas = Image.new(
#         "RGBA", (ABILITY_COST_WIDTH, ABILITY_HEIGHT), (255, 255, 255, 0)
#     )

#     icon_positions = []

#     # If there are two icons, they are centered and 20 pixels apart.
#     # If there are three icons, they are in a triangle.
#     # If there are four icons, they are in a square.

#     # Work out the positions of the icons based on the number of icons.

#     center_x = ABILITY_COST_WIDTH // 2
#     center_y = ABILITY_HEIGHT // 2
#     x_offset = center_x - (ELEMENT_SIZE // 2 + ABILITY_GAP // 2)
#     x_offset_down = x_offset + ELEMENT_SIZE + ABILITY_GAP
#     y_offset = center_y - (ELEMENT_SIZE + ABILITY_GAP) // 2
#     y_offset_down = y_offset + ELEMENT_SIZE + ABILITY_GAP

#     if cost == 1:
#         # If there is only one icon, it is centered.
#         icon_positions.append((center_x, center_y))
#     elif cost == 2:
#         icon_positions.append((x_offset, center_y))
#         icon_positions.append((x_offset_down, center_y))
#     elif cost == 3:
#         icon_positions.append((x_offset, y_offset))
#         icon_positions.append((x_offset_down, y_offset))
#         icon_positions.append((center_x, y_offset_down))

#     elif cost == 4:
#         icon_positions.append((x_offset, y_offset))
#         icon_positions.append((x_offset_down, y_offset))
#         icon_positions.append((x_offset, y_offset_down))
#         icon_positions.append((x_offset_down, y_offset_down))

#     draw = ImageDraw.Draw(cost_canvas)
#     for i, element in enumerate(elements):
#         # Draw circles for each element.

#         element_image = Image.open(f"ressources/elements/{element.lower()}_element.png")
#         element_image = element_image.resize((ELEMENT_SIZE, ELEMENT_SIZE))
#         cost_canvas.paste(
#             element_image,
#             (
#                 icon_positions[i][0] - ELEMENT_SIZE // 2,
#                 icon_positions[i][1] - ELEMENT_SIZE // 2,
#             ),
#             element_image,
#         )

#     return cost_canvas


# def render_weakness_and_resist(card: Card, image: Image):
#     resist_element = get_resist(card.element)
#     weakness_element = get_weakness(card.element)

#     if weakness_element:
#         weakness_x = STATUS_X_GAP
#         render_status_element(card, image, weakness_element, weakness_x)

#     if resist_element:
#         resist_x = image.width // 2
#         render_status_element(card, image, resist_element, resist_x)

#     retreat_cost_gap = image.width - STATUS_X_GAP
#     render_status_element(card, image, PokemonElements.NEUTRAL, retreat_cost_gap)


def render_status_element(card: Card, image: Image, element: Element, x_position: int):
    element_image = Image.open(f"ressources/elements/{element.name.lower()}_element.png")
    element_image = element_image.resize((STATUS_SIZE, STATUS_SIZE))
    image.paste(
        element_image,
        (
            x_position - STATUS_SIZE // 2,
            STATUS_Y_POSITION - STATUS_SIZE // 2,
        ),
        element_image,
    )


def card_from_json(data: dict,index:int) -> Card:
    card = Card(
        index=index,
        name=data["name"],
        description=data["description"],
        element=CarElements.get_element_by_name(data["attributes"][0]["value"]),
        rarity=CarRarity.get_rarity_by_name(data["attributes"][1]["value"].lower()),
        speed=data["attributes"][2]["value"],
        acceleration=data["attributes"][3]["value"],
        maniability=data["attributes"][4]["value"],
    )
    print(f'rarity : {CarRarity.get_rarity_by_name(data["attributes"][1]["value"].lower())}')
    return card



# def card_from_json(data: dict) -> Card:
#     card = Card(
#         index=data["index"],
#         name=data["name"],
#         description=data["description"],
#         element=CarElements.get_element_by_name(data["element"]),
#         rarity=CarRarity.get_rarity_by_name(data["rarity"]),
#         speed=data["speed"],
#         acceleration=data["acceleration"],
#         maniability=data["maniability"],
#     )
#     # card.abilities = [ability_from_json(ability) for ability in data["abilities"]]
#     return card


# def ability_from_json(data: dict) -> Ability:
#     return Ability(
#         name=data["name"],
#         element=PokemonElements.get_element_by_name(data["element"]),
#         cost=data["cost"],
#         is_mixed_element=data["is_mixed_element"],
#     )


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--collection",
        help="File path to the collection to render",
        default="output/car-nextgen",
    )
    collection_path = argparser.parse_args().collection
    render_cards(collection_path)


if __name__ == "__main__":
    main()
