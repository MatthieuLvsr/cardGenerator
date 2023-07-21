import argparse
import json
import os
import pathlib
from PIL import Image, ImageFont, ImageDraw

from car_content.car_elements import CarElements
from car_content.car_rarity import CarRarity
from mechanics.card import Card
from mechanics.element import Element


CAR_IMAGE_SCALE = 0.3
CAR_IMAGE_SCALE_SQ = 0.355

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
            rescale_factor = CAR_IMAGE_SCALE_SQ
        else:
            rescale_factor = CAR_IMAGE_SCALE

        resized_image_shape = (
            int(card_art_image.size[0] * rescale_factor),
            int(card_art_image.size[1] * rescale_factor),
        )
        card_art_image = card_art_image.resize(resized_image_shape)

        # Center the image.
        card_center_x = card_image.size[0] / 2
        card_center_y = 210
        car_image_x = card_center_x - (card_art_image.size[0] / 2)
        car_image_y = 105
        canvas.paste(card_image, (0, 0), card_image)
        canvas.paste(card_art_image, (int(car_image_x), int(car_image_y)))
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

    # Write the rarity of the Car.
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

    rarity_images = ["common","uncommon","rare","mythical","legendary"]

    rarity_image = Image.open(f"ressources/rarities/{rarity_images[card.rarity.index]}.png")
    rarity_image = rarity_image.resize((ELEMENT_SIZE, ELEMENT_SIZE))
    canvas.paste(rarity_image,(22,40))

    return card_image


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
