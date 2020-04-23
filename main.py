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
from stretch_all_frames import stretch_all_frames
from frames_to_video import create_video
from shutil import rmtree

VIDEO_FILE = 'Beach-@enginakyurt.mp4'

if __name__ == "__main__":
    FPS = split_video(VIDEO_FILE)
    stretch_all_frames()
    create_video(VIDEO_FILE, FPS)
    rmtree('video-frames')
    print('video-frames directory deleted')
    print('Video stretching complete')