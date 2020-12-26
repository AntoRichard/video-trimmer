from moviepy.editor import *

sec = 2
filename = "SampleVideo.mp4"
part = 1
clip = VideoFileClip("./source/" + filename, audio=True)
duration = int(clip.duration)

def trim(start, end):
    subclip = clip.subclip(start, end)
    subclip.write_videofile( "./out/test"+ str(part) +".mp4", audio=True, threads=8, codec="libx264", audio_codec="aac")


for i in range(0, duration, 2):
    if(duration - i == 1): 
        trim(i, duration)
    else:
        trim(0 + i, sec + i)
    part += 1