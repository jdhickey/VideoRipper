from original_code import from_file
from original_code import to_m4a
from playlist_addition import from_playlist

choice = input("0 for file, 1 for playlist\n")

from_playlist(input("Enter playlist url\n")) if choice == "1" else from_file()
to_m4a()
