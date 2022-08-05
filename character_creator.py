import json
import os
import random
from body_parts_injector import inject_body_parts
from category_builder import texts, notes, doors, opttas
from it_pass_cleaner import clean_it_pass


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
def create_characters_db(f):
    """CREATE DATABASE WITH UNIQUE CHARACTERS"""
    characters_count = 235800
    notes_count = 200
    texts_count = 3000
    opttas_count = 2000
    doors_count = None
    shuffle_iterations = 10

    with open('precooked_products.json') as file:
        result = json.load(file)

    iterations = 0
    while shuffle_iterations != iterations:
        random.shuffle(result)
        iterations += 1

    characters = list(yield_product(result, characters_count))
    # insert body_parts_injector
    clean_it_pass(characters)
    inject_body_parts(characters, notes, notes_count)
    inject_body_parts(characters, texts, texts_count)
    inject_body_parts(characters, doors, doors_count)
    inject_body_parts(characters, opttas, opttas_count)
    character_number = 1
    for character in characters:
        character_n = {"id": character_number, "body": character}
        # print(f'Added: {character_n}')
        json_db = json.dumps(character_n)
        f.write(json_db + ',\n')
        character_number += 1


create_characters_db()
