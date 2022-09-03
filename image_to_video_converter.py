import os
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")


t = Timer()


def path_converter():
    catalog = 'D:/Projects/Blender/tinycafe/to_prod/'
    paths = os.listdir(catalog)
    for path in paths:
        char_id = path.split('_')[0]

        # TYPES
        type_seq_to_gif = f'ffmpeg -i {catalog}{path}/r_00%02d.jpg -framerate 25 {catalog}{path}/{char_id}.gif -y'
        type_vid_to_gif = f'ffmpeg -i {catalog}{path}/{char_id}.mp4 -filter_complex "[0:v] split [a][b];[a] palettegen=stats_mode=single [p];[b][p] paletteuse=new=1" {catalog}{path}/{char_id}.gif -y'
        type_vid_to_webp_opt = f'ffmpeg -i {catalog}{path}/{char_id}.mp4 -vcodec libwebp -lossless 1 -loop 0 -preset none -an -vsync 0 {catalog}{path}/{char_id}.webp -y'
        type_vid_to_webp = f'ffmpeg -i {catalog}{path}/{char_id}.mp4 -lossless 1 -compression_level 0 -loop 0 -an {catalog}{path}/{char_id}.webp -y'

        # t.start()
        os.system(type_vid_to_webp)
        # t.stop()


def folder_converter():
    mp4_catalog = 'D:/Projects/Blender/tinycafe/mp4/'
    webp_catalog = 'D:/Projects/Blender/tinycafe/webp/'
    items = os.listdir(mp4_catalog)
    for item in items:
        char_id = item.split('.')[0]
        type_vid_to_webp = f'ffmpeg -i {mp4_catalog}{char_id}.mp4 -lossless 1 -compression_level 0 -loop 0 -an {webp_catalog}{char_id}.webp -y'

        # t.start()
        os.system(type_vid_to_webp)
        # t.stop()


folder_converter()