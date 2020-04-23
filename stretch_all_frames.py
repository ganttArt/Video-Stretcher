from pathlib import Path
from PIL import Image
from stretching_functions import create_np_array, create_index_list, create_gradient, build_new_image, save_file

def stretch_all_frames():
    index_list = create_index_list()
    directory = Path('video-frames').iterdir()
    number_of_frames = len(list(directory))
    current_frame_number = 0
    starting_pixel = 500

    for frame in Path('video-frames').iterdir():
        current_frame_number += 1
        with Image.open(frame) as _frame:
            IMG_ARRAY = create_np_array(_frame)
            NEW_IMG = build_new_image(index_list, IMG_ARRAY, starting_pixel)
            save_file(NEW_IMG, frame)
            print(f'{current_frame_number}/{number_of_frames}', frame, 'stretched')


def upward_stretch_all_frames(starting_pixel):
    '''
        Note: When calculating starting pixel for upward stretch,
              Minus the starting pixel from the video height.
    '''
    index_list = create_index_list()
    directory = Path('video-frames').iterdir()
    number_of_frames = len(list(directory))
    current_frame_number = 0

    for frame in Path('video-frames').iterdir():
        current_frame_number += 1
        with Image.open(frame) as _frame:
            _frame = _frame.rotate(180)
            IMG_ARRAY = create_np_array(_frame)
            NEW_IMG = build_new_image(index_list, IMG_ARRAY, starting_pixel)
            NEW_IMG = NEW_IMG.rotate(180)
            save_file(NEW_IMG, frame)
            print(f'{current_frame_number}/{number_of_frames}', frame, 'stretched')


if __name__ == "__main__":
    stretch_all_frames()