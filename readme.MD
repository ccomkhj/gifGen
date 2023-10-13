## Generate gif from images

input form
```bash
python3 makeGIF.py {path of inputs} {path of outputs} --frame{frame per second} --name {filename}
```

i.e.
```bash
python3 makeGIF.py /mnt/images /mnt/outputs --frame 3 --name {movie}
```

### example
![Example](demo/demo.gif)

## Generate images out of a video

```bash
python3 video2images.py {path of video} --frame {number of frame inbetween}
```