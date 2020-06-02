import os
from itunesLibrary import library

path = os.path.join(os.getenv("HOME"),"Music/iTunes/iTunes Music Library.xml")

# must first parse...
lib = library.parse(path)

print(len(lib))    # number of items stored

for playlist in lib.playlists:
    for item in playlist.items:
        print(item)          # perform function on each item in the playlist

# get a single playlist
playlist = lib.getPlaylist("David Bowie")
print(playlist)

# get a list of all of the David Bowie songs
bowie_items = lib.getItemsForArtist("David Bowie")

# get a single song
single_song = lib.getItemsById("16116")

# get the iTunes application version
print(lib.applicationVersion)
