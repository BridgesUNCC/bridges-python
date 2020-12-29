##
#    @brief  A Song object, used along with the Songs data source.
#    
#    This is a convenience class provided for  users who wish to use this
#    data source as part of their application. It provides an API that makes
#    it easy to access the attributes of this data set.
#    
#    Refer to tutorial examples to using this data source in data structure
#    assignments.
#    
#    
#    @author Matthew Mcquaigue, Kalpathi Subramanian
#    @date   2018, 12/29/20

class Song:
    ## @brief Constructor
    #    @param artist song artist
    #    @param song song title
    #    @param album song album
    #    @param lyrics lyrics of song
    #    @param release_data release date of song
    #
    def __init__(self, artist: str = "", song: str = "", album: str = "", lyrics: str = "", release_date: str = ""):
        self._artist = artist
        self._song = song
        self._lyrics = lyrics
        self._album = album
        self._release_date = release_date

    ##
    # @brief return artist of song
    #
    @property
    def artist(self):
        return self._artist

    ##
    # @brief set artist name
    # @param a artist name to be set
    #
    @artist.setter
    def artist(self, a):
        self._artist = a

    ##
    # return title of song
    #
    @property
    def song_title(self):
        return self._song

    ##
    # @brief set title of song
    # @param s song title to be set
    #
    @song_title.setter
    def song_title(self, s):
        self._song = s

    ##
    # @brief return album of song
    #
    @property
    def album_title(self):
        return self._album

    ##
    # @brief set album title
    # @param a album title to be set
    #
    @album_title.setter
    def album_title(self, a):
        self._album = a

    ##
    # @brief return lyrics of song
    #
    @property
    def lyrics(self):
        return self._lyrics

    ##
    # @brief set song lyrics
    # @param l song lyrics to be set
    #
    @lyrics.setter
    def lyrics(self, l):
        self._lyrics = l

    ##
    # @brief return release date of song
    #
    @property
    def release_date(self):
        return self._release_date

    ##
    # @brief set song release date
    # @param l song release date to be set
    #
    @release_date.setter
    def release_date(self, r):
        self._release_date = r

