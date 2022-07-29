import json
import os
import random


def product_yield(product_result, counter):
    """TO EXTRACT N RANDOM CHARACTERS"""
    try:
        random.sample(product_result, k=counter)
    except ValueError:
        print(f'ValueError: Sample larger than population or is negative\nChanged: counter={len(product_result)}\n')
        counter = len(product_result)
    finally:
        k_products = random.sample(product_result, k=counter)
        for prod in k_products:
            yield tuple(prod)


def body_parts_extender(part, body_parts):
    """TO EXTRACT NESTED LISTS AND TO FILL body_parts"""
    if isinstance(part, list):
        for nested_object in part:
            body_parts.append(nested_object)
    else:
        body_parts.append(part)


def json_wrapper(func):
    """TO CREATE AND FILL json_file_name"""
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
    with open('result.json') as file:
        result = json.load(file)
    characters = list(product_yield(result, counter=4))
    character_number = 0
    for character in characters:
        body_parts = []
        for part in character:
            body_parts_extender(part, body_parts)
        character_number += 1
        character_n = {"id": character_number, "body": body_parts}
        print(character_n)
        json_db = json.dumps(character_n)
        f.write(json_db + ',\n')



characters_database_creator()
