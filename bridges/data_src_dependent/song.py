
class Song:

    def __init__(self, artist: str = "", song: str = "", album: str = "", lyrics: str = "", release_date: str = ""):
        self.artist = artist
        self.song = song
        self.lyrics = lyrics
        self.album = album
        self.release_date = release_date

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_song_title(self):
        return self.song

    def set_song_title(self, song):
        self.song = song

    def get_album_title(self):
        return self.album

    def set_album_title(self, album):
        self.album = album

    def get_lyrics(self):
        return self.lyrics

    def set_lyrics(self, lyrics):
        self.lyrics = lyrics

    def get_release_date(self):
        return self.release_date

    def set_release_date(self, date):
        self.release_date = date
