# Importing all necessary libraries
import cv2
import os
import argparse


def video_to_frames(video: str, path_output_dir: str, frame: int):
    # extract frames from a video and save to directory as 'x.png' where
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    count = 0
    numbering = 0
    while vidcap.isOpened():
        count += 1
        success, image = vidcap.read()
        if success:
            if count % int(frame) == 0:
                file_name = os.path.join(path_output_dir, "b_%d.png") % numbering
                print(f"save {file_name}.")
                cv2.imwrite(file_name, image)
                numbering += 1
        else:
            print("out!")
            break
    cv2.destroyAllWindows()
    vidcap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Collect images from a video clip")
    parser.add_argument("video", help="location of video file")
    parser.add_argument(
        "--save", default="images", help="location of directory to save output images"
    )
    parser.add_argument(
        "--frame", default=30, help="frame frequency how often to collect images."
    )
    args = parser.parse_args()

    video_to_frames(args.video, args.save, args.frame)
