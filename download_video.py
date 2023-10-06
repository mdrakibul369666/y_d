from pytube import YouTube
import sys

url = sys.argv[1]  # Get the YouTube video URL from command line arguments
yt = YouTube(url)
video = yt.streams.get_highest_resolution()
video.download()

print(video.default_filename)  # Print the filename to be captured by app.js

