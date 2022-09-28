"""
This tool collects properties and translates them via translator, prepares json files with metadata for every rendered character
and store this file in character's directory
"""

import os
import json
from predefined_categories import translator

catalog = 'rendered'  # path to catalog with nested ones which have db IDs of rendered characters in names


def sort_id_keys(catalog_path=catalog):
    folders = os.listdir(catalog_path)
    folders_dict = {}
    for path in folders:
        new_item = path.split('_')
        folders_dict.update({new_item[0]: new_item[1]})
    dict_for_clean = folders_dict.copy()
    id_keys = dict_for_clean.keys()
    sorted_id_keys = sorted(list(map(int, id_keys)))
    return sorted_id_keys, folders


def write_to_metadata_files(body_folder, char_id, body):
    with open(f'{catalog}{body_folder}/{char_id}.json', mode='w') as meta_file:
        meta_file.write('[{')
        for body_item in body:
            writable_item = translator[body_item]
            writable_item = writable_item.replace(': ', '": "')
            meta_file.write('"' + writable_item + '",\n')
        meta_file.seek(meta_file.tell() - 3, 0)
        meta_file.truncate()
        meta_file.write('}]')


def create_metadata_files(db_file='characters_db.json'):
    id_list, folders = sort_id_keys()
    body_folder = None
    with open(db_file) as file:
        characters_db = json.load(file)
    for char_id in id_list:
        for char in characters_db:
            if char['id'] == char_id:
                body = char['body']
                for folder in folders:
                    if str(char_id) + '_' in folder:
                        body_folder = folder
                write_to_metadata_files(body_folder, char_id, body)
    print('Properties assigned')


if __name__ == "__main__":
    create_metadata_files()
