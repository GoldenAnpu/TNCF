import json
import random
from body_parts_injector import inject_body_parts
from category_builder import texts, notes, doors, opttas
from additional_func import clean_it_pass


def yield_product(generated_products, counter):
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


def json_wrapper(func):
    """CREATE AND FILL json_file_name"""
    def wrapped():
        with open('json/characters_db.json', 'w+') as file:
            file.write('[')

            func(file)

            file.seek(0, 2)  # seek to end of file; f.seek(0, os.SEEK_END) is legal
            file.seek(file.tell() - 3, 0)  # seek to the second last char of file; f.seek(f.tell()-2, os.SEEK_SET) is legal
            file.truncate()
            file.write(']')
    return wrapped


@json_wrapper
def create_characters_db(file):
    """CREATE DATABASE WITH UNIQUE CHARACTERS"""
    characters_count = 1235800
    notes_count = 2000
    texts_count = 3000
    opttas_count = 2000
    doors_count = None
    shuffle_iterations = 6

    with open('json/precooked_products.json') as pre_file:
        result = json.load(pre_file)

    iterations = 0
    while shuffle_iterations != iterations:
        random.shuffle(result)
        iterations += 1

    characters = list(yield_product(result, characters_count))
    clean_it_pass(characters)
    inject_body_parts(characters, notes, notes_count)
    inject_body_parts(characters, texts, texts_count)
    inject_body_parts(characters, doors, doors_count)
    inject_body_parts(characters, opttas, opttas_count)
    character_number = 1  # initial id
    for character in characters:
        character_n = {"id": character_number, "body": character}
        json_db = json.dumps(character_n)
        file.write(json_db + ',\n')
        character_number += 1

