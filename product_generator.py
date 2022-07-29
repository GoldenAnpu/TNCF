import json
import os


def product_result(*args):
    """ITERTOOLS PRODUCT FUNCTION SUPPORT"""
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args]
    pool_result = [[]]
    # random.shuffle(pools)
    for pool in pools:
        pool_result = [x + [y] for x in pool_result for y in pool]
    return pool_result


bl_objects = [
    'base_bush', 'base_bush_back', 'base_cactus', 'base_stair', 'base_star_sea', 'base_stone', 'base_sup',
    'base_tcan', 'base_tcan_open', 'cream_1_milk', 'cream_2_chocolate', 'cream_3_ice_balls', 'cream_4_ice',
    'door_1', 'door_2', 'door_3', 'door_4', 'eyes_1_normal', 'eyes_2_dead', 'eyes_3_love',
    'eyes_4_surprised', 'eyes_5_hypno', 'eyes_6_hypno_glasses', 'eyes_7_sq_g_glasses', 'lid_1',
    'lid_2', 'lid_3_hat60x', 'lid_4_hat60x_cut', 'lid_5_ribbed', 'lid_6_up', 'note_36', 'note_pface',
    'opttas_question', 'opttas_tubule', 'tcandy_berry', 'tcandy_crystal', 'teeth_1_norm', 'teeth_2_sharp',
    'teeth_norm_wo_tongue', 'text_cafe', 'tongue_1', 'tongue_2_long', 'top_bubs', 'top_eggshell',
    'top_jem_1', 'top_jem_2_drop', 'cream_5_marshmallow', 'top_pills_happy', 'top_star_sweet', 'top_sweet_stick'
]

bg = ['bg']  # background
cup = ['cup']  # main sceleton
doors = []  # just doors
teeth = ['it_pass']  # just teeth
text = ['it_pass']  # as tattoo on the side of cup
tongues = []  # must be empty for teeth_norm_wo_tongue
lids = []  # just lids for the cup
bases = []  # decoration around the cup, for 2 uses
notes = ['it_pass']  # additional layer for bases
glasses = ['glasses']  # additional layer only for eyes without glasses
eyes = []  # eyes without or with glasses
creams = []  # topping over the lids
opttas = ['it_pass']  # instead of creams
tcandys = ['it_pass']  # candies for tongue
tops = ['it_pass']  # additional layer for creams
object_lists = [bg, cup, doors, teeth, text, tongues, lids, bases, notes, eyes, creams, opttas, tcandys,
                tops]


def objects_lists_creator():
    """CREATE LISTS WITH ALL SWITCHABLE PARTS FOR CHARACTERS"""
    # bl_objects = bpy.data.objects.keys()
    for bl_object in bl_objects:
        if ("door_" in str(bl_object)) and (str(bl_object) not in doors):
            doors.append(bl_object)
        elif ("teeth_" in str(bl_object)) and (str(bl_object) not in teeth):
            teeth.append(bl_object)
        elif ("text_" in str(bl_object)) and (str(bl_object) not in text):
            text.append(bl_object)
        elif ("tongue_" in str(bl_object)) and (str(bl_object) not in tongues):
            tongues.append(bl_object)
        elif ("lid_" in str(bl_object)) and (str(bl_object) not in lids):
            lids.append(bl_object)
        elif ("base_" in str(bl_object)) and (str(bl_object) not in bases):
            bases.append(bl_object)
        elif ("note_" in str(bl_object)) and (str(bl_object) not in notes):
            notes.append(bl_object)
        elif ("eyes_" in str(bl_object)) and (str(bl_object) not in eyes):
            eyes.append(bl_object)
        elif ("cream_" in str(bl_object)) and (str(bl_object) not in creams):
            creams.append(bl_object)
        elif ("opttas_" in str(bl_object)) and (str(bl_object) not in opttas):
            opttas.append(bl_object)
        elif ("tcandy_" in str(bl_object)) and (str(bl_object) not in tcandys):
            tcandys.append(bl_object)
        elif ("top_" in str(bl_object)) and (str(bl_object) not in tops):
            tops.append(bl_object)
    list_updater(eyes, glasses, 'glasses')  # update eyes list with glasses


def list_updater(what_l, which_l, rule):
    """UPDATE what_l WITH COMBINED ELEMENTS what_l+which_l BY rule"""
    new_elements = []
    for elements in what_l:
        if rule not in str(elements):
            new_element = [*which_l, elements]
            new_elements.append(new_element)
    what_l += new_elements


def result_to_json():
    """SAVE result IN result.json FILE"""
    json_file_name = 'result.json'
    if os.path.exists(json_file_name):
        os.remove(json_file_name)
    f = open(json_file_name, 'w')
    json_db = json.dumps(result)
    f.write(json_db)


objects_lists_creator()
result = product_result(object_lists[5], object_lists[9])
result_to_json()
