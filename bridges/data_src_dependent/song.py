
class Song:

    def __init__(self, artist: str = "", song: str = "", album: str = "", lyrics: str = "", release_date: str = ""):
        self._artist = artist
        self._song = song
        self._lyrics = lyrics
        self._album = album
        self._release_date = release_date

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, a):
        self._artist = a

    @property
    def song_title(self):
        return self._song

    @song_title.setter
    def song_title(self, s):
        self._song = s

    @property
    def album_title(self):
        return self._album

    @album_title.setter
    def album_title(self, a):
        self._album = a

    @property
    def lyrics(self):
        return self._lyrics

    @lyrics.setter
    def lyrics(self, l):
        self._lyrics = l

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, r):
        self._release_date = r

