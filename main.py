'''
Video Stretcher - Take a video and stretch it any way you'd like.

Requirements
----
OpenCV 3.2 or higher
pip3 install opencv-python

Run
----
python3 main.py
'''
from split_video_by_frame import split_video
from stretch_all_frames import stretch_all_frames, upward_stretch_all_frames
from frames_to_video import create_video
from shutil import rmtree
from time import sleep

VIDEO_FILE = 'Short-Waves.mp4'

if __name__ == "__main__":
    FPS = split_video(VIDEO_FILE)
    upward_stretch_all_frames(170)
    create_video(VIDEO_FILE, FPS)
    rmtree('video-frames')
    print('video-frames directory deleted')
    print('Video stretching complete')