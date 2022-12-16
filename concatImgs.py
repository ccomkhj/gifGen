
import glob
import imageio
import os
import click
import cv2

def concat_tile(im1, im2, im3, im4):
    img1 = cv2.imread(im1)
    img2 = cv2.imread(im2)
    img3 = cv2.imread(im3)
    img4 = cv2.imread(im4)
    return cv2.resize(cv2.vconcat([cv2.hconcat([img1, img2]), cv2.hconcat([img3, img4])]), (img1.shape[1], img1.shape[0]))



@click.command()
@click.argument('in_dir', type=str)
@click.argument('out_dir', type=str)
def main(in_dir, out_dir):
    plots = sorted(glob.glob(os.path.join(in_dir,"*.png")))
    
    for i in range(0, len(plots)//4*4, 4):

        result = concat_tile(plots[i], plots[i+1], plots[i+2], plots[i+3])
        cv2.imwrite(os.path.join(out_dir, f'{i}.png'), result)

if __name__ == "__main__":

    main()