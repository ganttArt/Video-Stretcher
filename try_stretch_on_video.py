import cv2
from PIL import Image
from stretching_functions import create_np_array, create_index_list, create_gradient, build_new_image, save_file

DIRECTION_DICT = {'down': 0, 'up': 180, 'left': 90, 'right': 270}

VIDEO_FILE = 'Waves_Short.mp4'
STARTING_PIXEL = 170
STRETCH_INTENSITY = 13   # 1 <= STRETCH_INTENSITY <= 13
DIRECTION = DIRECTION_DICT['right']


def get_one_frame(filename):
    cap = cv2.VideoCapture(filename)
    ret, frame = cap.read()
    cv2.imwrite('unstretched.png' , frame) 
    cap.release()
    cv2.destroyAllWindows()
    print('Frame saved as unstretched.png')

def stretch_image():
    index_list = create_index_list(STRETCH_INTENSITY)
    with Image.open('unstretched.png') as frame:
        frame = frame.rotate(DIRECTION, expand=True)
        img_array = create_np_array(frame)
        new_img = build_new_image(index_list, img_array, STARTING_PIXEL)
        new_img = new_img.rotate(-DIRECTION, expand=True)
        save_file(new_img, 'stretched.png')
        new_img.show()
    print('Image stretched and saved as stretched.png')

if __name__ == "__main__":
    get_one_frame(VIDEO_FILE)
    stretch_image()
