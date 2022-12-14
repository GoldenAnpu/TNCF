""" Container with variables """


# to gather this list use bpy.data.objects.keys() in Blender Scripting terminal
objects_to_sort = [
    'base_bush', 'base_bush_back', 'base_cactus', 'base_stair', 'base_star_sea', 'base_stone', 'base_sup',
    'base_tcan', 'base_tcan_open', 'cream_1_milk', 'cream_2_chocolate', 'cream_3_ice_balls', 'cream_4_ice',
    'door_1', 'door_2', 'door_3', 'door_4', 'eyes_1_normal', 'eyes_2_dead', 'eyes_3_love', 'cream_6_3pics',
    'eyes_4_surprised', 'eyes_5_hypno', 'eyes_6_hypno_glasses', 'eyes_7_sq_g_glasses', 'lid_1',
    'lid_2', 'lid_3_hat60x', 'lid_4_hat60x_cut', 'lid_5_ribbed', 'lid_6_up', 'note_36', 'note_pface',
    'opttas_question', 'opttas_tubule', 'tcandy_berry', 'tcandy_crystal', 'teeth_1_norm', 'teeth_2_sharp',
    'teeth_norm_wo_tongue', 'text_cafe', 'tongue_1', 'tongue_2_long', 'top_bubs', 'top_eggshell',
    'top_jem_1', 'top_jem_2_drop', 'cream_5_marshmallow', 'top_pills_happy', 'top_star_sweet', 'top_sweet_stick',
    'top_berries', 'top_decoration'
]

# these are predefined environments of scenes (on your taste) to decrease time of generation algorythm
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

# to decrease time of generation algorythm
mouths = [
    'teeth_norm_wo_tongue',
    ['teeth_1_norm', 'tongue_1'],
    ['teeth_2_sharp', 'tongue_1'],
    ['teeth_1_norm', 'tongue_2_long'],
    ['teeth_2_sharp', 'tongue_2_long'],
]

# to decrease time of generation algorythm
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

# to gather this list use bpy.data.materials.keys() in Blender Scripting terminal
# will be used to "repaint" objects
materials = [
    'blue_st', 'chocolate_st', 'corral_st',
    'gradient_green_blue_st', 'gradient_rainbow_st', 'green_cold_st', 'mint_st', 'violet_st', 'white_st',
    'gradient_green_blue_bg', 'gradient_rainbow_bg', 'green_cold_bg',
    'blue_light_st_bg', 'brown_st', 'gradient_pink_orange_st_bg', 'gradient_violet_green_st_bg',
    'gradient_yellow_orange_st_bg', 'lemon_st_bg', 'green_st_bg', 'orange_st_bg', 'pink_light_st_bg',
    'pink_natural_st_bg', 'vaffle_st_bg', 'violet_st_bg'
]

# owcm - list of objects which will be repainted
objects_with_changeable_materials = [
    'base_bush', 'base_bush_back', 'base_cactus', 'base_stair', 'base_star_sea', 'base_stone', 'base_sup', 'base_tcan',
    'base_tcan_open', 'cream_1_milk', 'cream_2_chocolate', 'cream_3_ice_balls', 'cream_4_ice', 'cream_5_marshmallow',
    'cream_6_3pics', 'door_1', 'door_2', 'door_3', 'door_4', 'eyes_6_hypno_glasses', 'glasses', 'lid_1', 'lid_2',
    'lid_3_hat60x', 'lid_4_hat60x_cut', 'lid_5_ribbed', 'lid_6_up', 'opttas_question', 'opttas_tubule', 'tcandy_berry',
    'tcandy_crystal', 'tongue_1', 'tongue_2_long', 'top_eggshell', 'top_jem_1', 'top_jem_2_drop', 'top_pills_happy',
    'top_star_sweet', 'top_sweet_stick', 'top_berries', 'top_decoration', 'top_bubs'
]

# objects which must be in all characters
core = ['bg', 'cup']

# common list of objects which must be repainted
objects_core_owcm = objects_with_changeable_materials + core


# this dictionary used to prepare metadata
translator = {
    'base_bush': 'Environment: Bush',
    'base_bush_back': 'Environment: Backyard Bush',
    'base_cactus': 'Environment: Cactus',
    'base_stair': 'Environment: Stair',
    'base_star_sea': 'Environment: Star Sea',
    'base_stone': 'Environment: Stones',
    'base_sup': 'Environment: SUP',
    'base_tcan': 'Environment: Trashcan',
    'base_tcan_open': 'Environment: Backyard Trashcan',
    'cream_1_milk': 'Cream: Milk',
    'cream_2_chocolate': 'Cream: Chocolate',
    'cream_3_ice_balls': 'Cream: Milk with Ice Balls',
    'cream_4_ice': 'Cream: Ice',
    'cream_5_marshmallow': 'Cream: Marshmallow',
    'cream_6_3pics': 'Cream: Triple Mousse',
    'door_1': 'Door: Elevator',
    'door_2': 'Door: Carved',
    'door_3': 'Door: With round window',
    'door_4': 'Door: Reinforced',
    'eyes_1_normal': 'Eyes: Ok',
    'eyes_2_dead': 'Eyes: Dead',
    'eyes_3_love': 'Eyes: In Love',
    'eyes_4_surprised': 'Eyes: Surprised',
    'eyes_5_hypno': 'Eyes: Hypno',
    'eyes_6_hypno_glasses': 'Eyes: Hypno Glasses',
    'eyes_7_sq_g_glasses': 'Eyes: SG Glasses',
    'glasses': 'Glasses: Simple',
    'lid_1': 'Lid: Simple',
    'lid_2': 'Lid: Bordered',
    'lid_3_hat60x': 'Lid: Hat from 60x',
    'lid_4_hat60x_cut': 'Lid: Cut Hat from 60x',
    'lid_5_ribbed': 'Lid: Ribbed',
    'lid_6_up': 'Lid: Opened',
    'note_36': 'Note: 36',
    'note_pface': 'Note: Pockerface',
    'opttas_question': 'Optionals: Question',
    'opttas_tubule': 'Optionals: Tubule',
    'tcandy_berry': 'Candy: Berry',
    'tcandy_crystal': 'Candy: Crystal',
    'teeth_1_norm': 'Teeth: Normal',
    'teeth_2_sharp': 'Teeth: Sharp',
    'teeth_norm_wo_tongue': 'Teeth: Double Normal',
    'text_cafe': 'Text: Tiny Cafe',
    'tongue_1': 'Tongue: Normal',
    'tongue_2_long': 'Tongue: Long',
    'top_bubs': 'Adds: BUBS',
    'top_eggshell': 'Adds: Eggshell',
    'top_berries': 'Adds: Berries',
    'top_decoration': 'Adds: Confetti',
    'top_jem_1': 'Adds: Jem Crunchy',
    'top_jem_2_drop': 'Adds: Jem with Drops',
    'top_pills_happy': 'Adds: Pills Happy',
    'top_star_sweet': 'Adds: Sweet Star',
    'top_sweet_stick': 'Adds: Sweet Stick'
}
