import random
import json
import os


# bpy.data.objects[f'{obj.name}'].hide_set(1)
def mix_and_render(output_dir, output_file_pattern_string='render%d.png', numbers=2):
    # def mix_and_render(numbers=2):
    bunch_of_kruzhek = list(product(cups, eyes))
    iterations = 0
    random.shuffle(bunch_of_kruzhek)
    print(len(bunch_of_kruzhek))
    for kruzhek in bunch_of_kruzhek:
        cache_list = []
        if iterations < numbers and numbers <= len(bunch_of_kruzhek):
            for chasti in kruzhek:
                # bpy.data.objects[chasti].hide_render = False
                cache_list.append(chasti)
            # bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % iterations))
            # bpy.ops.render.render(write_still = True)
            print(cache_list)
            for chasti in cache_list:
                # bpy.data.objects[chasti].hide_render = True
                print(chasti)
            iterations += 1
        else:
            print('shit')
            break


mix_and_render('D:/Projects/Blender/rendered', 'randomrend%d.png', 3)
mix_and_render(5)
