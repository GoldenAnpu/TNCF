import json
import os
import random
from category_builder import texts, notes, doors, opttas


def product_yield(generated_products, counter):
    """EXTRACT N RANDOM CHARACTERS"""
    try:
        random.sample(generated_products, k=counter)
    except ValueError:
        print(f'ValueError: Sample larger than population or is negative\nChanged: counter={len(generated_products)}\n')
        counter = len(generated_products)
    finally:
        k_products = random.sample(generated_products, k=counter)
        for prod in k_products:
            yield list(prod)


def body_parts_extractor(part, body_parts):
    """EXTRACT NESTED LISTS AND TO FILL body_parts"""
    if isinstance(part, list):
        for nested_object in part:
            body_parts.append(nested_object)
    else:
        body_parts.append(part)


def body_parts_injector(characters, parts, count=None):
    """ADD OPTIONAL PARTS IN CHARACTERS

    Without argument count all characters get part.
    """
    if count is None:
        count = len(characters)
    if count > len(characters):
        count = len(characters) // 2
    random_characters = random.sample(characters, count)
    for character in random_characters:
        random_parts = random.sample(parts, 1)
        character.append(random_parts[0])
    return characters


def json_wrapper(func):
    """CREATE AND FILL json_file_name"""
    def wrapped():
        json_file_name = 'characters_db.json'
        if os.path.exists(json_file_name):
            os.remove(json_file_name)
        f = open(json_file_name, 'w')
        f.write('[')

        func(f)

        f.seek(0, 2)  # seek to end of file; f.seek(0, os.SEEK_END) is legal
        f.seek(f.tell() - 3, 0)  # seek to the second last char of file; f.seek(f.tell()-2, os.SEEK_SET) is legal
        f.truncate()
        f.write(']')
    return wrapped


@json_wrapper
def characters_database_creator(f):
    """CREATE DATABASE WITH UNIQUE CHARACTERS"""
    with open('precooked_products.json') as file:
        result = json.load(file)
    characters = list(product_yield(result, counter=500))
    # insert body_parts_injector
    characters = body_parts_injector(characters, texts, count=20)
    characters = body_parts_injector(characters, notes, count=20)
    characters = body_parts_injector(characters, doors, count=None)
    character_number = 1
    for character in characters:
        body_parts = []
        for part in character:
            body_parts_extractor(part, body_parts)
        # чистим notes, opttas, lid_3
        character_n = {"id": character_number, "body": body_parts}
        print(f'Added: {character_n}')
        json_db = json.dumps(character_n)
        f.write(json_db + ',\n')
        character_number += 1


characters_database_creator()
