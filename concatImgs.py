
import glob
import imageio
import os
import click
import cv2

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

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