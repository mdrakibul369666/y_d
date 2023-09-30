from pytube import YouTube
import sys

url = sys.argv[1]  # Get the YouTube video URL from command line arguments
yt = YouTube(url)
yt.streams.get_highest_resolution().download()
