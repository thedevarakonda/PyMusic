from pytube import  YouTube
from moviepy.editor import *
import os

def run(url,id):
    yt = YouTube(url)

    t = yt.streams.filter(file_extension="mp4").first()

    t.download("Users/"+id+"/Downloads")

    videoFile = "Users/"+id+"/Downloads/"+yt.title+".mp4"
    audioFile="Users/"+id+"/Downloads/"+yt.title+".mp3"

    convert(videoFile,audioFile)


def convert(mp4file, mp3file):
    video = VideoFileClip(mp4file)
    audio = video.audio
    audio.write_audiofile(mp3file)
    audio.close()
    video.close()

    os.remove(mp4file)
