'''
Video Stretcher - Take a video and stretch it up or down.

Requirements
----
Python 3
OpenCV 3.2 or higher
Numpy
Pillow

To install all dependencies:
pip3 install -r requirements.txt

Run
----
python3 main.py
'''
from Modules.split_video_by_frame import split_video
from Modules.stretching_functions import stretch_all_frames
from Modules.frames_to_video import create_video
from shutil import rmtree

DIRECTION_DICT = {'down': 0, 'up': 180, 'left': 90, 'right': 270}

VIDEO_FILE = 'Waves-JavierLemus-XL.mp4'
STARTING_PIXEL = 478
STRETCH_INTENSITY = 8   # 1 <= STRETCH_INTENSITY <= 13
DIRECTION = DIRECTION_DICT['up'] # change direction here!

if __name__ == "__main__":
    FPS = split_video(VIDEO_FILE)
    stretch_all_frames(STARTING_PIXEL, DIRECTION, STRETCH_INTENSITY)
    create_video(VIDEO_FILE, FPS)
    rmtree('video-frames')
    print('video-frames directory deleted')
    print('Video stretching complete')
