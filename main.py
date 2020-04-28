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
from stretch_all_frames import stretch_all_frames, upward_stretch_all_frames, stretch_all_frames_left
from frames_to_video import create_video
from shutil import rmtree
from time import sleep

VIDEO_FILE = 'Waves_Short.mp4'
STARTING_PIXEL = 170

# 1 <= STRETCH_INTENSITY <= 13
STRETCH_INTENSITY = 4

if __name__ == "__main__":
    FPS = split_video(VIDEO_FILE)

    # choose one of these two functions to stretch up or down
    # upward_stretch_all_frames(STARTING_PIXEL)
    stretch_all_frames(STARTING_PIXEL)
    # stretch_all_frames_left(STARTING_PIXEL, STRETCH_INTENSITY)

    create_video(VIDEO_FILE, FPS)
    # rmtree('video-frames')
    # print('video-frames directory deleted')
    rmtree('__pycache__')
    print('pycache cleared')
    print('Video stretching complete')