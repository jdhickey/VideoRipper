import pytubefix
import os
import subprocess


def from_file():
    url_file = open("out/url_list.txt", "r")  # opens the list of videos
    url_list = []

    for i in url_file:  # every line with content is added to a list of urls
        if not i.isspace():
            url_list.append(i.strip())

    for url in url_list:  # iterates through the url list
        video = pytubefix.YouTube(url)  # grabs the video from the given url

        # grabs the first audio only stream of the given video
        audio = video.streams.filter(only_audio=True).first()
        audio.download("./out")  # downloads the stream to an output folder


def to_m4a():
    for filename in os.listdir("out"):  # iterates through downloaded videos
        # exclude non-videos
        if not (os.path.splitext(filename)[-1].lower() == ".mp4"):
            continue

        name = os.path.basename(filename)  # gets the filename of the file
        # sets the desired name
        new_name = os.path.splitext(filename)[0] + ".mp3"

        directory = "out/" + name  # gets the used directory of the file
        new_directory = "out/" + new_name  # sets the directory of the new file

        subprocess.run([
            "ffmpeg", "-i", directory, new_directory
        ])  # converts from mp4 to mp3

        os.remove(directory)
