import cv2
import glob
import click


@click.command()
@click.argument('path_a', type=click.Path(exists=True))
@click.argument('path_b', type=click.Path(exists=True))
@click.argument('output_dir', type=click.Path())
def stitch_images(path_a, path_b, output_dir):
    # Get the list of image files in the directories
    images_a = glob.glob(path_a + '/*.jpg')
    images_b = glob.glob(path_b + '/*.jpg')

    # Sort the image files
    images_a.sort()
    images_b.sort()

    # Iterate over the image files and stitch them horizontally
    for img_a, img_b in zip(images_a, images_b):
        # Read the images
        image_a = cv2.imread(img_a)
        image_b = cv2.imread(img_b)

        # Resize images if they have different heights
        if image_a.shape[0] != image_b.shape[0]:
            height = min(image_a.shape[0], image_b.shape[0])
            image_a = cv2.resize(
                image_a, (int(height * image_a.shape[1] / image_a.shape[0]), height))
            image_b = cv2.resize(
                image_b, (int(height * image_b.shape[1] / image_b.shape[0]), height))



        # Stitch the images horizontally
        stitched_image = cv2.hconcat([image_a, image_b])

        # Get the image filename
        filename = img_a.split('/')[-1]

        # Save the stitched image to the output directory
        output_path = output_dir + '/stitched_' + filename
        cv2.imwrite(output_path, stitched_image)

    print('Images stitched and saved successfully!')


if __name__ == '__main__':
    stitch_images()
