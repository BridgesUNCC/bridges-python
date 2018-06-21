
class Song:

    def __init__(self, artist = None, song = None, album = None, lyrics = None, release_date = None):
        if artist and song and album and lyrics and release_date is not None:
            self.artist = artist
            self.song = song
            self.lyrics = lyrics
            self.album = album
            self.release_date = release_date
        else:
            self.artist = self.song = self.lyrics = self.album = self.release_date = ""

    def getArtist(self):
        return self.artist
    def setArtist(self, artist):
        self.artist = artist

    def getSongTitle(self):
        return self.song
    def setSongTitle(self, song):
        self.song = song

    def getAlbumTitle(self):
        return self.album
    def setAlbumTitle(self, album):
        self.album = album

    def getLyrics(self):
        return self.lyrics
    def setLyrics(self, lyrics):
        self.lyrics = lyrics

    def getReleaseDate(self):
        return self.release_date
    def setReleaseDate(self, date):
        self.release_date = date