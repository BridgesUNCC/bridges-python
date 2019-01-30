from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
import sys
import random

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")

    song = get_song("Delicate")

    print(song.get_artist())
    print(song.get_album_title())
    print(song.get_release_date())
    print(song.get_lyrics()[0:min(100, len(song.get_lyrics()))])


if __name__ == '__main__':
    main()