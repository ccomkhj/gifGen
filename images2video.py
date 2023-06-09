import cv2
import glob
import click
import re


@click.command()
@click.argument('image_folder', type=click.Path(exists=True))
@click.argument('video_save', type=click.Path())
@click.argument('frame', type=float)
def create_video(image_folder, video_save, frame):
    # Get all image files in the folder with the specified format
    image_files = glob.glob(f'{image_folder}/*.jpg') + glob.glob(
        f'{image_folder}/*.jpeg') + glob.glob(f'{image_folder}/*.png')

    # Sort the image files based on numerical order in the filename
    image_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))

    # Load the first image to get the dimensions
    first_image = cv2.imread(image_files[0])
    height, width, _ = first_image.shape

    # Create a VideoWriter object to save the video
    video = cv2.VideoWriter(video_save, cv2.VideoWriter_fourcc(
        *'mp4v'), frame, (width, height))

    for image_file in image_files:
        # Read each image file
        image = cv2.imread(image_file)

        # Write the image to the video file
        video.write(image)

    # Release the VideoWriter and close the video file
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    create_video()
