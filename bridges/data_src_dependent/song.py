class Song:
    """
    @brief  A Song object, used along with the Songs data source.

    This is a convenience class provided for  users who wish to use this
    data source as part of their application. It provides an API that makes
    it easy to access the attributes of this data set.

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_song()
    
    For an example, check out https://bridgesuncc.github.io/tutorials/Data_Song_Lyrics.html

    @author Matthew Mcquaigue, Kalpathi Subramanian
    @date   2018, 12/29/20
    """

    def __init__(self, artist: str = "", song: str = "", album: str = "", lyrics: str = "", release_date: str = ""):
        """
        @brief Constructor
        Args:
            artist: song artist
            song: song title
            album: song album
            lyrics: lyrics of song
            release_date: release date of song
        """
        self._artist = artist
        self._song = song
        self._lyrics = lyrics
        self._album = album
        self._release_date = release_date

    @property
    def artist(self):
        """
        @brief return artist of song
        Returns:
            artist name of song
        """
        return self._artist

    @artist.setter
    def artist(self, a):
        """
        @brief Set artist of song
        Args:
            a: artist name to set
        """
        self._artist = a

    @property
    def song_title(self):
        """
        @brief return title of song
        Returns:
            song title
        """
        return self._song

    @song_title.setter
    def song_title(self, s):
        """
        @brief Set the song title
        Args:
            s: artist name to set
        """
        self._song = s

    @property
    def album_title(self):
        """
        @brief return album title
        Returns:
            album title of song
        """
        return self._album

    @album_title.setter
    def album_title(self, a):
        """
        @brief Set title of song
        Args:
            a: album title to set
        """
        self._album = a

    @property
    def lyrics(self):
        """
        @brief return lyrics of song
        Returns:
            lyrics of song
        """
        return self._lyrics

    @lyrics.setter
    def lyrics(self, l):
        """
        @brief Set artist of song
        Args:
            l:  lyrics data to set
        """
        self._lyrics = l

    @property
    def release_date(self):
        """
        @brief return release date of song
        Returns:
            release date of song
        """
        return self._release_date

    @release_date.setter
    def release_date(self, r):
        """
        @brief Set release date of song
        Args:
            r: release date to set
        """
        self._release_date = r

