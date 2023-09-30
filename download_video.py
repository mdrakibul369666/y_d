from pytube import YouTube
import sys

url = sys.argv[1]  # Get the YouTube video URL from command line arguments
yt = YouTube(url)
video = yt.streams.get_highest_resolution()
video.download()

print(video.default_filename)  # Print the filename to be captured by app.js






# from pytube import YouTube
# import sys

# url = sys.argv[1]  # Get the YouTube video URL from command line arguments
# resolution = sys.argv[2]  # Get the resolution choice from command line arguments
# yt = YouTube(url)

# # Filter streams based on the chosen resolution
# if resolution == '1080p':
#     video = yt.streams.filter(res="1080p").first()
# elif resolution == '720p':
#     video = yt.streams.filter(res="720p").first()
# elif resolution == '360p':
#     video = yt.streams.filter(res="360p").first()
# elif resolution == '144p':
#     video = yt.streams.filter(res="144p").first()
# else:
#     # Default to highest resolution if choice is not recognized
#     video = yt.streams.get_highest_resolution()

# video.download()
# print(video.default_filename)





# from pytube import YouTube
# import sys

# url = sys.argv[1]  # Get the YouTube video URL from command line arguments
# resolution = sys.argv[2] if len(sys.argv) > 2 else 'highest'  # Get the resolution choice or default to highest

# yt = YouTube(url)

# # Filter streams based on the chosen resolution
# if resolution == '1080p':
#     video = yt.streams.filter(res="1080p").first()
# elif resolution == '720p':
#     video = yt.streams.filter(res="720p").first()
# elif resolution == '360p':
#     video = yt.streams.filter(res="360p").first()
# elif resolution == '144p':
#     video = yt.streams.filter(res="144p").first()
# else:
#     # Default to highest resolution if choice is not recognized
#     video = yt.streams.get_highest_resolution()

# video.download()
# print(video.default_filename)


# from pytube import YouTube
# import sys

# url = sys.argv[1]  # Get the YouTube video URL from command line arguments
# yt = YouTube(url)

# # Mapping of resolutions to stream quality
# resolutions = {
#     "1080p": "1080p",
#     "720p": "720p",
#     "480p": "480p",
#     "360p": "360p",
#     "240p": "240p",
#     "144p": "144p"
# }

# resolution_choice = sys.argv[2] if len(sys.argv) > 2 else 'highest'  # Get the resolution choice or default to 'highest'

# # Check if the chosen resolution is available, otherwise default to highest
# if resolution_choice in resolutions and yt.streams.filter(res=resolutions[resolution_choice]):
#     video = yt.streams.filter(res=resolutions[resolution_choice]).first()
# else:
#     video = yt.streams.get_highest_resolution()

# video.download()
# print(video.default_filename)
