"""
PRODUCTS EQUAL TO NOT PREPARED CHARACTERS
THEY ARE CREATES BY character_creator.py
"""

import json
import os
from category_builder import objects_lists_creator as olc
from randomizer import product_result


def generate_products():
    """GENERATE PRODUCTS W/O OPTIONALS"""

    objects_list = olc()  # objects_lists_creator()
    generated_products = product_result(objects_list[0], objects_list[1], objects_list[2], objects_list[3],
                                        objects_list[4], objects_list[5], objects_list[6])
    return generated_products


def result_to_json(result):
    """SAVE result IN precooked_products.json FILE"""
    json_file_name = 'precooked_products.json'
    if os.path.exists(json_file_name):
        os.remove(json_file_name)
    f = open(json_file_name, 'w')
    json_db = json.dumps(result)
    f.write(json_db)


result_to_json(generate_products())
