import json
import os
import bpy
import random
from material_changer import make_it_colorful
from predefined_categories import materials


def special_character(characters_db, special):
    """ To render certain character:
                                    'text_cafe'
                                    'note_36'
                                    'note_pface'
                                    'opttas_question'
                                    'opttas_tubule'
    """
    while True:
        character = (random.sample(characters_db, 1))[0]
        body = character.get('body')
        c_id = character.get('id')
        if special in body:
            return body, c_id


def random_character(characters_db):
    """ To render random character """
    character = (random.sample(characters_db, 1))[0]
    body = character.get('body')
    c_id = character.get('id')
    return body, c_id


def certain_id_character(characters_db, certain_id):
    """ To render random character """
    for character in characters_db:
        c_id = character.get('id')
        if c_id == certain_id:
            body = character.get('body')
            return body, c_id


def render_characters(output_dir, output_file_pattern_string='ch%d.png', number=2):
    tiny_cafe_dir = 'D:/Projects/Blender/tinycafe/'
    save_dir = tiny_cafe_dir + output_dir + '/'
    characters_db_file = 'D:/Projects/Python/blender_test/characters_db.json'

    with open(characters_db_file) as file:
        characters_db = json.load(file)

    shuffle_iterations = 0
    shuffles = 0
    while shuffle_iterations != shuffles:
        random.shuffle(characters_db)
        shuffles += 1

    iterations = 0
    if len(characters_db) >= number:
        while number > iterations:
            # body = special_character(characters_db, 'note')
            # body = random_character(characters_db)[0]
            # c_id = random_character(characters_db)[1]
            body = certain_id_character(characters_db, 60690)[0]
            c_id = certain_id_character(characters_db, 60690)[1]
            cache_list = []
            for part in body:
                bpy.data.objects[part].hide_render = False
                cache_list.append(part)
                make_it_colorful(part, materials)
            make_it_colorful('bg', materials)
            make_it_colorful('cup', materials)

            if os.path.isdir(save_dir + str(c_id)):
                sequence_dir = save_dir + str(c_id) + '_' + str(iterations)
            else:
                sequence_dir = save_dir + str(c_id)

            bpy.context.scene.render.filepath = os.path.join(sequence_dir,
                                                             (output_file_pattern_string % iterations))
            bpy.ops.render.render(animation=True, write_still=True)
            for part in cache_list:
                bpy.data.objects[part].hide_render = True
            iterations += 1

    # for character in characters_db:
    #     body = character.get('body')
    #     if len(characters_db) >= number > iterations:
    #         cache_list = []
    #         for part in body:
    #             bpy.data.objects[part].hide_render = False
    #             cache_list.append(part)
    #             make_it_colorful(part, materials)
    #         make_it_colorful('bg', materials)
    #         make_it_colorful('cup', materials)
    #         bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % iterations))
    #         bpy.ops.render.render(write_still=True)
    #         for part in cache_list:
    #             bpy.data.objects[part].hide_render = True
    #         iterations += 1
    #     else:
    #         break


render_characters('animated', 'r_%d', 100)
