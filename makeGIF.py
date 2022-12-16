import glob
import imageio
import os
import click
import cv2

@click.command()
@click.argument('in_dir', type=str)
@click.argument('out_dir', type=str)
@click.option('--frame', type=int, default=6)
@click.option('--name', type=str, default='movie')
def main(in_dir, out_dir, frame, name):

    plots = list(set(glob.glob(os.path.join(in_dir,"*.jpg"))) | set(glob.glob(os.path.join(in_dir,"*.png"))))
    
    images = []

    for file_name in plots[:500]:
        img = imageio.imread(file_name)
        img = cv2.resize(img, (64,64))
        images.append(img)

    # Make it pause at the end so that the viewers can ponder
    for _ in range(10):
        img = imageio.imread(file_name)
        img = cv2.resize(img, (64,64))
        images.append(img)

    imageio.mimwrite(os.path.join(out_dir, f"{name}.gif"), images, format='GIF', fps=frame)

if __name__ == "__main__":

    main()