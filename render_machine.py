import json
import os
import bpy
import random
from material_changer import make_it_colorful
from predefined_categories import materials


def render_characters(output_dir, output_file_pattern_string='render%d.png', number=2):
    with open('characters_db.json') as file:
        characters_db = json.load(file)
    iterations = 0
    random.shuffle(characters_db)
    for character in characters_db:
        body = character.get('body')
        if len(characters_db) >= number > iterations:
            cache_list = []
            for part in body:
                bpy.data.objects[part].hide_render = False
                cache_list.append(part)
                make_it_colorful(part, materials)
            make_it_colorful('bg', materials)
            make_it_colorful('cup', materials)
            bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % iterations))
            bpy.ops.render.render(write_still=True)
            for part in cache_list:
                bpy.data.objects[part].hide_render = True
            iterations += 1
        else:
            break


render_characters('D:/Projects/Blender/Tinycafe/blender/rendered1000/', 'r_%d.png', 10)