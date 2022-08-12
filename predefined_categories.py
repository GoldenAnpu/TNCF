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

bases = [
    'base_star_sea',
    'base_stone',
    ['base_tcan', 'base_sup'],
    ['base_tcan', 'base_stair'],
    ['base_cactus', 'base_sup'],
    ['base_tcan', 'base_stone'],
    ['base_cactus', 'base_star_sea'],
    ['base_bush', 'base_sup'],
    ['base_bush', 'base_stair'],
    ['base_tcan_open', 'base_star_sea'],
    ['base_tcan_open', 'base_stone'],
    ['base_tcan', 'base_stair', 'base_stone'],
    ['base_tcan', 'base_sup', 'base_stone'],
    ['base_tcan', 'base_bush', 'base_sup'],
    ['base_tcan', 'base_tcan_open', 'base_stone'],
    ['base_cactus', 'base_sup', 'base_star_sea'],
    ['base_cactus', 'base_stair', 'base_star_sea'],
    ['base_cactus', 'base_sup', 'base_tcan_open'],
    ['base_cactus', 'base_stair', 'base_tcan_open'],
    ['base_cactus', 'base_bush', 'base_sup'],
    ['base_cactus', 'base_bush', 'base_stair'],
    ['base_cactus', 'base_bush_back', 'base_sup'],
    ['base_cactus', 'base_bush_back', 'base_stair'],
    ['base_cactus', 'base_tcan_open', 'base_stone'],
    ['base_bush', 'base_bush_back', 'base_sup'],
    ['base_bush', 'base_bush_back', 'base_stair'],
    ['base_bush', 'base_tcan_open', 'base_sup'],
    ['base_bush', 'base_tcan_open', 'base_stair']
]

mouths = [
    'teeth_norm_wo_tongue',
    ['teeth_1_norm', 'tongue_1'],
    ['teeth_2_sharp', 'tongue_1'],
    ['teeth_1_norm', 'tongue_2_long'],
    ['teeth_2_sharp', 'tongue_2_long'],
]

eyes = [
    'eyes_1_normal',
    'eyes_2_dead',
    'eyes_3_love',
    'eyes_4_surprised',
    'eyes_5_hypno',
    'eyes_6_hypno_glasses',
    'eyes_7_sq_g_glasses',
    ['glasses', 'eyes_1_normal'],
    ['glasses', 'eyes_2_dead'],
    ['glasses', 'eyes_3_love'],
    ['glasses', 'eyes_4_surprised'],
    ['glasses', 'eyes_5_hypno']
]

# bpy.data.materials.keys()
materials = [
    'black_st', 'blue_st', 'chocolate_st', 'corral_st', 'glass_brown_st', 'glass_white_st',
    'gradient_green_blue_st', 'gradient_rainbow_st', 'green_cold_st', 'mint_st', 'violet_st', 'white_st',
    'gradient_green_blue_bg', 'gradient_rainbow_bg', 'green_cold_bg',
    'blue_light_st_bg', 'brown_st', 'gradient_pink_orange_st_bg', 'gradient_violet_green_st_bg',
    'gradient_yellow_orange_st_bg', 'lemon_st_bg', 'green_st_bg', 'orange_st_bg', 'pink_light_st_bg',
    'pink_natural_st_bg', 'vaffle_st_bg', 'violet_st_bg'
]

objects_with_changeable_materials = [
    'base_bush', 'base_bush_back', 'base_cactus', 'base_stair', 'base_star_sea', 'base_stone', 'base_sup', 'base_tcan',
    'base_tcan_open', 'cream_1_milk', 'cream_2_chocolate', 'cream_3_ice_balls', 'cream_4_ice', 'cream_5_marshmallow',
    'door_1', 'door_2', 'door_3', 'door_4', 'eyes_6_hypno_glasses', 'glasses', 'lid_1', 'lid_2',
    'lid_3_hat60x', 'lid_4_hat60x_cut', 'lid_5_ribbed', 'lid_6_up', 'opttas_question', 'opttas_tubule', 'tcandy_berry',
    'tcandy_crystal', 'tongue_1', 'tongue_2_long', 'top_eggshell', 'top_jem_1', 'top_jem_2_drop', 'top_pills_happy',
    'top_star_sweet', 'top_sweet_stick'
]

core = ['bg', 'cup']

core_owcm = objects_with_changeable_materials + core
