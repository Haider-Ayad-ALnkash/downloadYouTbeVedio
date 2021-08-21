from pytube import YouTube
link =input("Enty Your link ")
video=YouTube(link)
def finish():
    print("Complated")
video.streams.get_highest_resolution().download(output_path="E:/Downlods")
video.register_on_complete_callback(finish())
# from pytube import Playlist
# playList=playlist(links)
# for video in playList.videos:
#     video.stream.get_highest_resolution().download(output_path="E:/Downlods")
