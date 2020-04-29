from pathlib import Path
from PIL import Image
from stretching_functions import create_np_array, create_index_list, create_gradient, build_new_image, save_file

def stretch_all_frames(starting_pixel=170, direction=0):
    index_list = create_index_list()
    directory = Path('video-frames').iterdir()
    number_of_frames = len(list(directory))
    current_frame_number = 0

    for frame in Path('video-frames').iterdir():
        current_frame_number += 1
        with Image.open(frame) as _frame:
            _frame = _frame.rotate(direction, expand=True)
            img_array = create_np_array(_frame)
            new_img = build_new_image(index_list, img_array, starting_pixel)
            new_img = new_img.rotate(-direction, expand=True)
            save_file(new_img, frame)
            print(f'{current_frame_number}/{number_of_frames}', frame, 'stretched')

if __name__ == "__main__":
    stretch_all_frames()