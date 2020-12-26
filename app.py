from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

video = VideoFileClip("./sample/SampleVideo.mp4")
duration = video.duration
part = 1

for i in range(0, int(duration), 2):
    ffmpeg_extract_subclip("./sample/SampleVideo.mp4", 0 + i, 2 + i, targetname="./out/test"+ str(part) +".mp4")
    part += 1