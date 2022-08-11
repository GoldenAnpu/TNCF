import os

catalog = 'D:/Projects/Blender/tinycafe/animated/'
paths = os.listdir(catalog)

for path in paths:
    os.system(f'ffmpeg -i {catalog}{path}/r_00%02d.jpg -framerate 25 {catalog}{path}/anim.mp4 -y')
