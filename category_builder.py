from predefined_categories import bases, mouths, eyes, objects_to_sort
from randomizer import product_result


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
        elif 'top_eggshell' in cap and 'cream_5_marshmallow' in cap:
            pass
        elif 'top_jem_1' in cap and 'cream_1_milk' in cap:
            pass
        elif 'top_jem_1' in cap and 'cream_2_chocolate' in cap:
            pass
        elif 'top_jem_1' in cap and 'cream_3_ice_balls' in cap:
            pass
        elif 'top_jem_1' in cap and 'cream_5_marshmallow' in cap:
            pass
        elif 'top_jem_2_drop' in cap and 'cream_1_milk' in cap:
            pass
        elif 'top_jem_2_drop' in cap and 'cream_2_chocolate' in cap:
            pass
        elif 'top_jem_2_drop' in cap and 'cream_3_ice_balls' in cap:
            pass
        elif 'top_jem_2_drop' in cap and 'cream_5_marshmallow' in cap:
            pass
        elif 'top_jem_2_drop' in cap and 'lid_6_up' in cap:
            pass
        elif 'cream_3_ice_balls' in cap and 'top_pills_happy' in cap:
            pass
        elif 'cream_3_ice_balls' in cap and 'top_star_sweet' in cap:
            pass
        elif 'cream_3_ice_balls' in cap and 'lid_6_up' in cap:
            pass
        elif 'cream_2_chocolate' in cap and 'top_pills_happy' in cap:
            pass
        elif 'cream_2_chocolate' in cap and 'top_star_sweet' in cap:
            pass
        elif 'cream_2_chocolate' in cap and 'lid_1' in cap:
            pass
        elif 'cream_2_chocolate' in cap and 'lid_2' in cap:
            pass
        elif 'cream_2_chocolate' in cap and 'lid_3_hat60x' in cap:
            pass
        elif 'cream_2_chocolate' in cap and 'lid_4_hat60x_cut' in cap:
            pass
        elif 'cream_2_chocolate' in cap and 'lid_5_ribbed' in cap:
            pass
        elif 'cream_5_marshmallow' in cap and 'lid_1' in cap:
            pass
        elif 'cream_5_marshmallow' in cap and 'lid_2' in cap:
            pass
        elif 'cream_5_marshmallow' in cap and 'lid_3_hat60x' in cap:
            pass
        elif 'cream_5_marshmallow' in cap and 'lid_4_hat60x_cut' in cap:
            pass
        elif 'cream_5_marshmallow' in cap and 'lid_5_ribbed' in cap:
            pass
        elif 'cream_4_ice' in cap and 'lid_3_hat60x' in cap:
            pass
        elif 'cream_4_ice' in cap and 'lid_4_hat60x_cut' in cap:
            pass
        elif 'top_star_sweet' in cap and 'cream_5_marshmallow' in cap:
            pass
        elif 'top_sweet_stick' in cap and 'cream_5_marshmallow' in cap:
            pass
        elif 'top_sweet_stick' in cap and 'cream_2_chocolate' in cap:
            pass
        elif 'top_sweet_stick' in cap and 'cream_3_ice_balls' in cap:
            pass
        else:
            caps.append(cap)
    return caps


def create_category_list_of_objects(predefined_list, category, category_string):
    for blender_object in predefined_list:
        if category_string in blender_object:
            category.append(blender_object)
    return category


def objects_lists_creator():
    """CREATE LISTS WITH ALL SWITCHABLE PARTS FOR CHARACTERS"""
    # bg = ['bg']  # background
    # cup = ['cup']  # main sceleton
    p_doors = []  # just doors
    p_notes = []  # additional layer for bases
    p_text = []  # as tattoo on the side of cup
    p_opttas = []  # instead of creams
    lids = []  # just lids for the cup
    creams = []  # topping over the lids
    tops = []  # additional layer for creams
    tcandys = ['it_pass']  # candies for tongue

    # optional
    create_category_list_of_objects(objects_to_sort, p_doors, 'door_')
    create_category_list_of_objects(objects_to_sort, p_notes, 'note_')
    create_category_list_of_objects(objects_to_sort, p_text, 'text_')
    create_category_list_of_objects(objects_to_sort, p_opttas, 'opttas_')
    # required
    create_category_list_of_objects(objects_to_sort, tcandys, 'tcandy_')
    # caps parts
    create_category_list_of_objects(objects_to_sort, lids, 'lid_')
    create_category_list_of_objects(objects_to_sort, creams, 'cream_')
    create_category_list_of_objects(objects_to_sort, tops, 'top_')
    # caps list
    caps = caps_creator(creams, tops, lids)
    # list of all objects
    list_of_categories = [bases, mouths, eyes, caps, tcandys, p_doors, p_notes, p_text, p_opttas]
    return list_of_categories


created_object_lists = objects_lists_creator()
opttas = created_object_lists[8]
texts = created_object_lists[7]
notes = created_object_lists[6]
doors = created_object_lists[5]
