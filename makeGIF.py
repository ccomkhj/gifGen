import glob
import imageio
import os
import click
import cv2


@click.command()
@click.argument("in_dir", type=str)
@click.argument("out_dir", type=str)
@click.option("--frame", type=int, default=2)
@click.option("--name", type=str, default="movie")
def main(in_dir, out_dir, frame, name):

    plots = sorted(
        list(
            set(glob.glob(os.path.join(in_dir, "*.jpg")))
            | set(glob.glob(os.path.join(in_dir, "*.png")))
        )
    )
    img_size = (640, 360)
    images = []

    for file_name in plots:
        img = imageio.imread(file_name)
        img = cv2.resize(img, img_size)
        images.append(img)

    # Make it pause at the end so that the viewers can ponder
    for _ in range(3):
        img = imageio.imread(file_name)
        img = cv2.resize(img, img_size)
        images.append(img)

    imageio.mimwrite(
        os.path.join(out_dir, f"{name}.gif"), images, format="GIF", fps=frame
    )


if __name__ == "__main__":

    main()
