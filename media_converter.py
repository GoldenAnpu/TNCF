import os
from codetiming import Timer


def convert_image_sequence(proc_type: int):
    catalog = ''  # path to main catalog with nested ones, which were fulfilled with image sequences
    paths = os.listdir(catalog)
    process = ''
    timer = Timer()

    for path in paths:
        char_id = path.split('_')[0]

        if proc_type == 1:
            # seq_to_gif
            process = f'ffmpeg -i {catalog}{path}/r_00%02d.jpg -framerate 25 {catalog}{path}/{char_id}.mp4 -y'
        elif proc_type == 2:
            # vid_to_gif
            process = f'ffmpeg -i {catalog}{path}/{char_id}.mp4 -filter_complex "[0:v] split [a][b];[a] palettegen=stats_mode=single [p];[b][p] paletteuse=new=1" {catalog}{path}/{char_id}.gif -y'
        elif proc_type == 3:
            # vid_to_webp_opt
            process = f'ffmpeg -i {catalog}{path}/{char_id}.mp4 -vcodec libwebp -lossless 1 -loop 0 -preset none -an -vsync 0 {catalog}{path}/{char_id}.webp -y'
        elif proc_type == 4:
            # vid_to_webp
            process = f'ffmpeg -i {catalog}{path}/{char_id}.mp4 -lossless 1 -compression_level 0 -loop 0 -an {catalog}{path}/{char_id}.webp -y'

        timer.start()
        os.system(process)
        timer.stop()


def convert_file():  # mp4 to webp with the best size-to-quality
    source_catalog = ''  # set yours
    output_catalog = ''  # set yours
    timer = Timer()
    items = os.listdir(source_catalog)
    for item in items:
        char_id = item.split('.')[0]
        process = f'ffmpeg -i {source_catalog}{char_id}.mp4 -lossless 1 -compression_level 0 -loop 0 -an {output_catalog}{char_id}.webp -y'

        timer.start()
        os.system(process)
        timer.stop()
