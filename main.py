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
from split_video_by_frame import split_video
from stretch_all_frames import stretch_all_frames
from frames_to_video import create_video
from shutil import rmtree
from time import sleep

DIRECTION_DICT = {'down': 0, 'up': 180, 'left': 90, 'right': 270}

VIDEO_FILE = 'Waves_Short.mp4'
STARTING_PIXEL = 170
STRETCH_INTENSITY = 13  # 1 <= STRETCH_INTENSITY <= 13
DIRECTION = DIRECTION_DICT['left']  # change direction here!

if __name__ == "__main__":
    FPS = split_video(VIDEO_FILE)
    stretch_all_frames(STARTING_PIXEL, DIRECTION)
    create_video(VIDEO_FILE, FPS)
    rmtree('video-frames')
    print('video-frames directory deleted')
    rmtree('__pycache__')
    print('pycache cleared')
    print('Video stretching complete')