import pytubefix


def from_playlist(playlist_url):
    playlist = pytubefix.Playlist(playlist_url)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    counter = 0
    for url in playlist.video_urls:
        counter += 1
        print("Downloading video number " + str(counter))

        video = pytubefix.YouTube(url)
        audio = video.streams.filter(only_audio=True).first()
        audio.download("./out")
