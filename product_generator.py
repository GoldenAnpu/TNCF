"""
PRODUCTS EQUAL TO NOT PREPARED CHARACTERS
THEY ARE CREATES BY character_creator.py
"""

import json
import os
from category_builder import objects_lists_creator as olc
from randomizer import product_result


def additional_filter(precooked_characters):
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


def body_parts_extractor(part, body_parts):
    """EXTRACT NESTED LISTS AND TO FILL body_parts"""
    if isinstance(part, list):
        for nested_object in part:
            body_parts.append(nested_object)
    else:
        body_parts.append(part)


def generate_products():
    """GENERATE PRODUCTS W/O OPTIONALS"""

    objects_list = olc()  # objects_lists_creator()
    precooked_products = product_result(objects_list[0], objects_list[1], objects_list[2], objects_list[3],
                                        objects_list[4], objects_list[5], objects_list[6])
    precooked_characters = []
    for character in precooked_products:
        generated_products = []
        for part in character:
            body_parts_extractor(part, generated_products)
        precooked_characters.append(generated_products)
    additional_filter(precooked_characters)
    return precooked_characters


def result_to_json(result):
    """SAVE result IN precooked_products.json FILE"""
    json_file_name = 'precooked_products.json'
    if os.path.exists(json_file_name):
        os.remove(json_file_name)
    f = open(json_file_name, 'w')
    json_db = json.dumps(result)
    f.write(json_db)


result_to_json(generate_products())
