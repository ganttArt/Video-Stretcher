'''
Using OpenCV, script takes a mp4 video puts each frame in a file called video-frames.

Requirements
----
OpenCV 3.2 or higher
pip3 install opencv-python

Run
----
python3 split-video-by-frame.py
'''
import cv2
import numpy as np
import os

def split_video(filename):
    # Playing video from file:
    cap = cv2.VideoCapture(filename)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

    try:
        if not os.path.exists('video-frames'):
            os.makedirs('video-frames')
    except OSError:
        print ('Error: Creating directory of data')

    currentFrame = 1
    while(True):
        
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Saves image of the current frame in jpg file
        name = './video-frames/frame' + str(currentFrame).zfill(6) + '.png'
        print ('Creating...' + name)
        
        #Code used for video where getting duplicate frames
        # if currentFrame % 2 == 0:
        #     currentFrame += 1
        # else:
        try:
            cv2.imwrite(name, frame)
            currentFrame += 1
        except cv2.error as exception:
            print(exception)
            print('Exception handled gracefully')
            print('All images created')
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    return frame_rate

if __name__ == "__main__":
    split_video('Beach-@enginakyurt.mp4')
