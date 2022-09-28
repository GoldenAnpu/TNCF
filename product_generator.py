"""
PRODUCTS ARE NOT PREPARED CHARACTERS
TO CREATE CHARACTERS USE character_creator.py
"""

import json
from category_builder import objects_lists_creator as olc
from additional_func import product_result


def additional_filter(precooked_characters):
    """ Remove forbidden products as additional layer of filtration """
    pointer = 0
    while True:
        character = precooked_characters[pointer]
        if 'lid_3_hat60x' in character and 'base_sup' in character:
            precooked_characters.remove(character)
        elif 'lid_6_up' in character and 'base_sup' in character:
            precooked_characters.remove(character)
        elif 'lid_3_hat60x' in character and 'base_stair' in character:
            precooked_characters.remove(character)
        else:
            pointer += 1
        if pointer == len(precooked_characters):
            break
    return precooked_characters


def additional_filter_2(precooked_characters):
    """ Get only special products with "cream_6_3pics", "top_berries", "top_decoration" """
    pointer = 0
    bingo = 0
    while True:
        character = precooked_characters[pointer]
        if 'cream_6_3pics' in character:
            bingo += 1
        if 'top_berries' in character:
            bingo += 1
        if 'top_decoration' in character:
            bingo += 1
        if bingo == 0:
            precooked_characters.remove(character)
        else:
            bingo = 0
            pointer += 1
        if pointer == len(precooked_characters):
            break
    return precooked_characters


def body_parts_extractor(part, body_parts):
    """EXTRACT NESTED LISTS AND FILL body_parts"""
    if isinstance(part, list):
        for nested_object in part:
            body_parts.append(nested_object)
    else:
        body_parts.append(part)


def generate_products():
    """GENERATE PRODUCTS W/O OPTIONALS"""

    objects_list = olc()  # objects_lists_creator()
    precooked_products = product_result(objects_list[0],
                                        objects_list[1],
                                        objects_list[2],
                                        objects_list[3],
                                        objects_list[4])
    precooked_characters = []
    for character in precooked_products:
        generated_products = []
        for part in character:
            body_parts_extractor(part, generated_products)
        precooked_characters.append(generated_products)
    additional_filter(precooked_characters)
    # additional_filter_2(precooked_characters)
    return precooked_characters


def result_to_json(result):
    """SAVE result IN precooked_products.json FILE"""
    with open('json/precooked_products.json', 'w+') as file:
        json_db = json.dumps(result)
        file.write(json_db)


if __name__ == "__main__":
    result_to_json(generate_products())
