import os
import json
from predefined_categories import translator

catalog = 'D:/Projects/Blender/tinycafe/to_prod/'
folders = os.listdir(catalog)
folders_dict = {}
body_path = ''

for path in folders:
    new_item = path.split('_')
    folders_dict.update({new_item[0]: new_item[1]})

dict_for_clean = folders_dict.copy()
dict_old_for_clean = folders_dict.copy()

n = 0
while len(folders_dict) > n:
    for item in folders_dict:
        if int(folders_dict.get(item)) < 1661155500:
            dict_for_clean.pop(item)
        else:
            dict_old_for_clean.pop(item)
        n += 1

id_keys = dict_for_clean.keys()
id_keys_old = dict_old_for_clean.keys()

sorted_id_keys = sorted(list(map(int, id_keys)))
sorted_id_keys_old = sorted(list(map(int, id_keys_old)))


def create_files_with_properties(id_list, db_file):
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
                with open(f'{catalog}{body_folder}/{char_id}.json', mode='w') as meta_file:
                    meta_file.write('[{')
                    for body_item in body:
                        writable_item = translator[body_item]
                        writable_item = writable_item.replace(': ', '": "')
                        meta_file.write('"' + writable_item + '",\n')
                    meta_file.seek(meta_file.tell() - 3, 0)
                    meta_file.truncate()
                    meta_file.write('}]')


create_files_with_properties(sorted_id_keys, 'characters_db.json')
create_files_with_properties(sorted_id_keys_old, 'characters_db_old.json')
print('Properties assigned')
