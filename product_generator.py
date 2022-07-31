"""
PRODUCTS EQUAL TO NOT PREPARED CHARACTERS
THEY ARE CREATES BY character_creator.py
"""

import json
import os
from predefined_objects import bases, mouths, eyes


def product_result(*args):
    """ITERTOOLS PRODUCT FUNCTION SUPPORT"""
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args]
    pool_result = [[]]
    for pool in pools:
        pool_result = [x + [y] for x in pool_result for y in pool]
    return pool_result


# bpy.data.objects.keys()
objects_to_sort = [
    'base_bush', 'base_bush_back', 'base_cactus', 'base_stair', 'base_star_sea', 'base_stone', 'base_sup',
    'base_tcan', 'base_tcan_open', 'cream_1_milk', 'cream_2_chocolate', 'cream_3_ice_balls', 'cream_4_ice',
    'door_1', 'door_2', 'door_3', 'door_4', 'eyes_1_normal', 'eyes_2_dead', 'eyes_3_love',
    'eyes_4_surprised', 'eyes_5_hypno', 'eyes_6_hypno_glasses', 'eyes_7_sq_g_glasses', 'lid_1',
    'lid_2', 'lid_3_hat60x', 'lid_4_hat60x_cut', 'lid_5_ribbed', 'lid_6_up', 'note_36', 'note_pface',
    'opttas_question', 'opttas_tubule', 'tcandy_berry', 'tcandy_crystal', 'teeth_1_norm', 'teeth_2_sharp',
    'teeth_norm_wo_tongue', 'text_cafe', 'tongue_1', 'tongue_2_long', 'top_bubs', 'top_eggshell',
    'top_jem_1', 'top_jem_2_drop', 'cream_5_marshmallow', 'top_pills_happy', 'top_star_sweet', 'top_sweet_stick'
]


def caps_creator(creams, tops, lids):
    random_caps = product_result(creams, tops, lids)
    caps = []
    for cap in random_caps:
        if 'top_star_sweet' in cap and 'lid_6_up' in cap:
            pass
        elif 'top_eggshell' in cap and 'cream_1_milk' in cap:
            pass
        elif 'top_eggshell' in cap and 'cream_4_ice' in cap:
            pass
        elif 'top_jem_1' in cap and 'cream_1_milk' in cap:
            pass
        elif 'top_jem_1' in cap and 'cream_4_ice' in cap:
            pass
        elif 'top_jem_1' in cap and 'cream_3_ice_balls' in cap:
            pass
        elif 'top_jem_2_drop' in cap and 'cream_1_milk' in cap:
            pass
        elif 'top_jem_2_drop' in cap and 'cream_4_ice' in cap:
            pass
        elif 'top_jem_2_drop' in cap and 'cream_3_ice_balls' in cap:
            pass
        elif 'top_jem_2_drop' in cap and 'lid_6_up' in cap:
            pass
        elif 'cream_3_ice_balls' in cap and 'top_pills_happy' in cap:
            pass
        elif 'cream_3_ice_balls' in cap and 'top_star_sweet' in cap:
            pass
        elif 'cream_2_chocolate' in cap and 'top_pills_happy' in cap:
            pass
        elif 'cream_2_chocolate' in cap and 'top_star_sweet' in cap:
            pass
        else:
            caps.append(cap)
    return caps


def objects_lists_creator():
    """CREATE LISTS WITH ALL SWITCHABLE PARTS FOR CHARACTERS"""

    bg = ['bg']  # background
    cup = ['cup']  # main sceleton
    doors = []  # just doors
    notes = []  # additional layer for bases
    text = []  # as tattoo on the side of cup
    opttas = []  # instead of creams
    lids = []  # just lids for the cup
    creams = []  # topping over the lids
    tops = []  # additional layer for creams
    tcandys = []  # candies for tongue

    for blender_object in objects_to_sort:
        # optional
        if ("door_" in str(blender_object)) and (str(blender_object) not in doors):
            doors.append(blender_object)
        elif ("note_" in str(blender_object)) and (str(blender_object) not in notes):
            notes.append(blender_object)
        elif ("text_" in str(blender_object)) and (str(blender_object) not in text):
            text.append(blender_object)
        elif ("opttas_" in str(blender_object)) and (str(blender_object) not in opttas):
            opttas.append(blender_object)
        # required
        elif ("tcandy_" in str(blender_object)) and (str(blender_object) not in tcandys):
            tcandys.append(blender_object)
        # caps parts
        elif ("lid_" in str(blender_object)) and (str(blender_object) not in lids):
            lids.append(blender_object)
        elif ("cream_" in str(blender_object)) and (str(blender_object) not in creams):
            creams.append(blender_object)
        elif ("top_" in str(blender_object)) and (str(blender_object) not in tops):
            tops.append(blender_object)

    caps = caps_creator(creams, tops, lids)

    object_lists = [bg, cup, bases, mouths, eyes, caps, tcandys, doors, notes, text, opttas]
    return object_lists


def list_updater(object_list_1, object_list_2, rule):
    """UPDATE object_list_1 WITH COMBINED ELEMENTS WITH object_list_2 BY rule"""
    new_elements = []
    for elements in object_list_1:
        if rule not in str(elements):
            new_element = [*object_list_2, elements]
            new_elements.append(new_element)
    object_list_1 += new_elements


def generate_products():
    """GENERATE PRODUCTS W/O OPTIONALS"""
    objects_list = objects_lists_creator()
    generated_products = product_result(objects_list[0], objects_list[1], objects_list[2], objects_list[3],
                                        objects_list[4], objects_list[5], objects_list[6])
    return generated_products


def result_to_json(result):
    """SAVE result IN result.json FILE"""
    json_file_name = 'result.json'
    if os.path.exists(json_file_name):
        os.remove(json_file_name)
    f = open(json_file_name, 'w')
    json_db = json.dumps(result)
    f.write(json_db)

# result_to_json(generate_products())
