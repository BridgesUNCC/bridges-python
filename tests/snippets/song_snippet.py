from bridges.bridges import *
from bridges.data_src_dependent.data_source import *

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")

    song = get_song("Delicate")

    print(song.artist)
    print(song.album_title)
    print(song.release_date)
    print(song.lyrics[0:min(100, len(song.lyrics))])


if __name__ == '__main__':
    main()