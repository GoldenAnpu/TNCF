import json
import os
import bpy
import random
from material_changer import make_it_colorful
from predefined_categories import materials


def render_characters(output_dir, output_file_pattern_string='render%d.png', number=2):

    tiny_cafe_dir = 'D:/Projects/Blender/Tinycafe/'
    save_dir = tiny_cafe_dir + output_dir + f'{str(number)}/'
    characters_db_file = 'D:/Projects/Python/blender_test/characters_db.json'

    with open(characters_db_file) as file:
        characters_db = json.load(file)

    shuffle_iterations = 3
    shuffles = 0
    while shuffle_iterations != shuffles:
        random.shuffle(characters_db)
        shuffles += 1

    iterations = 0
    if len(characters_db) >= number:
        while number > iterations:
            character = (random.sample(characters_db, 1))[0]
            body = character.get('body')
            cache_list = []
            for part in body:
                bpy.data.objects[part].hide_render = False
                cache_list.append(part)
                make_it_colorful(part, materials)
            make_it_colorful('bg', materials)
            make_it_colorful('cup', materials)
            bpy.context.scene.render.filepath = os.path.join(save_dir, (output_file_pattern_string % iterations))
            bpy.ops.render.render(write_still=True)
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


render_characters('next', 'r_%d.png', 100)