from Modules.stretching_functions import stretch_all_frames
from Modules.frames_to_video import create_video
from shutil import rmtree
import cv2
import numpy as np
import os

DIRECTION_DICT = {'down': 0, 'up': 180, 'left': 90, 'right': 270}

VIDEO_FILE = 'Waves-JavierLemus-XL.mp4'
STARTING_PIXEL = 478
STRETCH_INTENSITY = 8   # 1 <= STRETCH_INTENSITY <= 13
DIRECTION = DIRECTION_DICT['up'] # change direction here!


def split_video(filename):
    '''A revised split_video function to only create 90 frames '''
    cap = cv2.VideoCapture(filename)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    try:
        if not os.path.exists('video-frames'):
            os.makedirs('video-frames')
    except OSError:
        print ('Error: Creating directory of data')

    for num in range(90):
        ret, frame = cap.read()
        name = './video-frames/frame' + str(num).zfill(6) + '.png'
        print ('Creating...' + name)
        try:
            cv2.imwrite(name, frame)
        except cv2.error as exception:
            print(exception)
            print('Exception handled gracefully')
            print('All images created')
            break

    cap.release()
    cv2.destroyAllWindows()
    print('All images created')
    return frame_rate


if __name__ == "__main__":
    FPS = split_video(VIDEO_FILE)
    stretch_all_frames(STARTING_PIXEL, DIRECTION, STRETCH_INTENSITY)
    create_video('Short_'+VIDEO_FILE, FPS)
    rmtree('video-frames')
    print('video-frames directory deleted')
    print('Video stretching complete')
