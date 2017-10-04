# ThumbGifs

## What does it do
Takes a video file, reads 2 seconds each 15 seconds and concatenates all these
sub-videos into one short video which is then converted to a low-size GIF which
can easily be used for a thumbnail.

## Setup
- Install **moviepy** with:

   ```shell
   pip install moviepy
   ```
   
- Finally, install FFMPEG
    - You have ffmpeg installed: well, you're done here.
    - You don't have it, the program will just install it by itself it seems
    - Otherwise, you can install ffmpeg manually (and add to the path on Windows OSes!)

## Run it
- Enter `python thumbgifs.py myvideo.mp4` and it will write myvideo.gif
- OR enter `python thumbgifs.py myvideo1.mp4 myvideo2.mp4 ...` and it will write myvideo1.gif, myvideo2.gif...
- OR enter `python thumbgifs.py list.txt` where list.txt is a list of paths on each line.
    - For example, that would be
    ```
    ../videos/video1.mp4
    ../videos/video2.mp4
    ../videos/video3.mp4
    ```
	
## More configuration
In the Python script, you can modify the framerates, the resolution in the main code at the bottom