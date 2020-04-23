import cv2
import os

def create_video(video_filename, fps):
    print(fps)
    image_folder = 'video-frames'
    output_name = 'Stretched_' + video_filename.split('.')[0] + '.mp4'

    images = sorted([img for img in os.listdir(image_folder)])
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_name,
                            cv2.VideoWriter_fourcc(*'mp4v'),
                            fps,
                            (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
    print(f'{output_name} built')


if __name__ == "__main__":
    create_video('Waves-Javier Lemus.mp4', 27)
