import random

# DEFAULT COLORS
def_lid_color = (0.332451, 0.205079, 0.127438, 1)

# SUPPORTED COLORS
rgb_list = [
    (0.8, 0.369807, 0.309031, 1),
    (0.142129, 0.593223, 0.8, 1),
    (0.0718764, 0.8, 0.0689944, 1)
]


def lid_color(rgb):
    """LID COLOR CHANGER"""
    if type(rgb) is list:
        rgb_col = random.choice(rgb)
    elif rgb == def_lid_color:
        rgb_col = def_lid_color
    bpy.data.materials["Material.001"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = rgb_col
