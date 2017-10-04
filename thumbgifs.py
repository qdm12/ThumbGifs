from sys import argv
from os.path import isfile
from moviepy.editor import VideoFileClip, concatenate_videoclips
from tqdm import tqdm


def generate_glimpses(path, each_percent=0.1, during=2, max_duration=float("inf"), fps=5):
    video = (VideoFileClip(path)
            .resize( (400, 220 ) ))
    video.set_fps(fps)
    video.audio = None
    duration = video.duration
    step = int(each_percent * duration)
    start_times = [t for t in range(0, int(duration) - step, step)]
    new_duration = 0
    stop = False
    subclips = []
    for i in tqdm(range(len(start_times)), desc="Sub-clipping"):
        subclip = video.subclip(start_times[i], start_times[i] + during)
        subclips.append(subclip)
        new_duration += during
        if stop:
            break
        if new_duration + during > max_duration: # about to exceed on next run
            during = max_duration - new_duration # less than initial during
            if during < 0.4: #too short anyway
                break
            stop = True
    glimpses = concatenate_videoclips(subclips)
    del subclips
    return glimpses

if __name__ == "__main__":
    # Parameters
    fps = 5
    max_duration = 20
    
    
    video_paths = []
    if len(argv) == 1:
        raise Exception("You need to pass at least one argument")
    elif len(argv) == 2 and argv[1][-3:] == "txt":
        with open(argv[1], "rb") as f:
            video_paths = f.read().splitlines()
    else:
        for i in range(1, len(argv)):
            video_paths.append(argv[i])
    for i in range(len(video_paths)):
        print("Working on video "+str(i+1)+"...")
        if not isfile(video_paths[i]):
            print("!!! Video file "+video_paths[i]+" was not found !!!")
            continue
        glimpses = generate_glimpses(video_paths[i], max_duration=max_duration, fps=fps)
        output_name = video_paths[i].split('/')[-1][:-3] + "gif"
        glimpses.write_gif(output_name, program='ffmpeg', fps=fps)
        #glimpses.write_videofile("output.mp4", program='ffmpeg', fps=fps)
        print()
        print()
        
            
            