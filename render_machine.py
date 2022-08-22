import json
import os
import bpy
import random
from datetime import datetime
import calendar
from material_changer import make_it_colorful
from predefined_categories import materials


def special_character(characters_db, *args):
    """ To render certain character:
                                    'text_cafe'
                                    'note_36'
                                    'note_pface'
                                    'opttas_question'
                                    'opttas_tubule'
    """
    specials = [special for special in args]
    checked_set = set()
    while True:
        character = (random.sample(characters_db, 1))[0]
        body = character.get('body')
        c_id = character.get('id')
        found = False
        missed = False
        for special in specials:
            if special in body:
                found = True
            else:
                missed = True
        if found and (missed is False):
            return body, c_id
        checked_set.add(c_id)
        if len(checked_set) == len(characters_db):
            break


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
    characters_db_file = '/characters_db.json'

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
            character = special_character(characters_db, 'opttas_question')
            #            character = certain_id_character(characters_db, 215020)
            #            character  = random_character(characters_db)
            body = character[0]
            c_id = character[1]
            cache_list = []
            color_cash_list = []

            make_it_colorful('bg', materials, color_cash_list)
            make_it_colorful('cup', materials, color_cash_list)

            for part in body:
                bpy.data.objects[part].hide_render = False
                cache_list.append(part)
                make_it_colorful(part, materials, color_cash_list)

            time_now = calendar.timegm(datetime.utcnow().utctimetuple())
            sequence_dir = save_dir + str(c_id) + '_' + str(time_now)

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
