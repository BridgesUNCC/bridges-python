from bridges.bridges import *
from bridges.color import *
from bridges.color_grid import *

def split_lyrics(lyrics):
    lyrics = lyrics.split("\\[.+\\]").join("")
    lyrics.trim()
    lyrics_split = lyrics.split("\\s+")



def main():
    # Init a Bridges Connection with your credentials
    bridges = Bridges(36, "test", "")

    # Set assignment title
    bridges.set_title("ListEQ Example")

    bridges.connector.set_server("local")

