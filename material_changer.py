import random
import bpy
from predefined_categories import objects_with_changeable_materials as owcm
from predefined_categories import core_owcm


def pick_material(part, p_materials):
    n = 0
    while True:
        passed_1 = 0
        passed_2 = 0
        random.shuffle(p_materials)
        s_material = p_materials[0]
        if part in owcm and '_st' in s_material:

            if part != 'base_star_sea' and s_material == 'corral_st':
                passed_1 += 1

            if s_material == 'white_st':
                if 'lid_' in part or 'cream_' in part:
                    n += 1
                    return s_material
                else:
                    passed_1 += 1

            if 'tongue' in part:
                if s_material == 'brown_st':
                    passed_1 += 1
                elif s_material == 'vaffle_st_bg':
                    passed_1 += 1
                elif s_material == 'chocolate_st':
                    passed_1 += 1

            if 'cream_5_marshmallow' in part:
                if s_material == 'brown_st':
                    passed_1 += 1
                elif s_material == 'vaffle_st_bg':
                    passed_1 += 1
                elif s_material == 'chocolate_st':
                    passed_1 += 1
                elif s_material == 'violet_st_bg':
                    passed_1 += 1
                elif s_material == 'green_st_bg':
                    passed_1 += 1
                elif s_material == 'green_cold_st':
                    passed_1 += 1
                elif s_material == 'green_cold_bg':
                    passed_1 += 1
                elif s_material == 'gradient_violet_green_st_bg':
                    passed_1 += 1
                elif s_material == 'blue_st':
                    passed_1 += 1
                elif s_material == 'gradient_green_blue_st':
                    passed_1 += 1
                elif s_material == 'gradient_rainbow_st':
                    passed_1 += 1
                elif s_material == 'violet_st':
                    passed_1 += 1
                elif s_material == 'gradient_green_blue_bg':
                    passed_1 += 1
                elif s_material == 'pink_natural_st_bg':
                    passed_1 += 1

            if passed_1 < 1:
                n += 1
                return s_material

        if part == 'bg' and '_bg' in s_material:
            n += 1
            return s_material

        if part == 'cup':
            if s_material == 'white_st':
                passed_2 += 1
            elif s_material == 'corral_st':
                passed_2 += 1
            elif s_material == 'brown_st':
                passed_2 += 1
            elif s_material == 'chocolate_st':
                passed_2 += 1
            elif s_material == 'gradient_rainbow_st':
                passed_2 += 1
            if passed_2 < 1:
                n += 1
                return s_material

        if n == 1:
            break


def change_material(part, c_material, slot=0):
    obj = bpy.data.objects[part]
    mat = bpy.data.materials[c_material]

    if obj and mat:
        if obj.material_slots:
            obj.material_slots[slot].material = mat


def count_material_slots(part):
    if part == 'base_bush_back':
        slots = [0, 1]
        return slots
    elif part == 'base_stone':
        slots = [0, 1]
        return slots
    elif part == 'base_sup':
        slots = [0, 1]
        return slots
    elif part == 'top_pills_happy':
        slots = [0, 1]
        return slots
    elif part == 'top_sweet_stick':
        slots = [0, 1]
        return slots
    elif part == 'lid_6_up':
        slots = [0, 1]
        return slots
    elif part == 'cream_3_ice_balls':
        slots = [0, 1, 2, 3]
        return slots
    elif part == 'eyes_6_hypno_glasses':
        slots = [1]
        return slots
    elif part == 'lid_4_hat60x_cut':
        slots = [1]
        return slots
    elif part == 'lid_3_hat60x':
        slots = [1]
        return slots
    else:
        slots = [0]
        return slots


def make_it_colorful(part, m_materials, color_cash_list):
    """ Change materials for certain part """
    if part not in core_owcm:
        pass
    else:
        list_of_slots = count_material_slots(part)  # define slots to be replaced for certain part
        for slot in list_of_slots:
            c_material = pick_material(part, m_materials)  # define material for special slot
            while True:
                if "_bg" in c_material:
                    if color_cash_list.count(c_material) < 2:
                        change_material(part, c_material, slot)
                        color_cash_list.append(c_material)
                        break
                    else:
                        c_material = pick_material(part, m_materials)
                if "_st" in c_material:
                    if color_cash_list.count(c_material) < 2:
                        change_material(part, c_material, slot)
                        color_cash_list.append(c_material)
                        break
                    else:
                        c_material = pick_material(part, m_materials)
