
##
#    @brief  A Game object, used along with the Games data source.
#    
#    This is a convenience class provided for  users who wish to use this
#    data source as part of their application. It provides an API that makes
#    it easy to access the attributes of this data set.
#    
#    Each game record has title, platform on which it can be played,
#    rating,  and a list of genres.
#    
#    @author Matthew Mcquaigue, Kalpathi Subramanian
#    @date   2/1/17, 12/29/20


class Game:
    ##
    #     @brief Constructor
    #    @param title  game title
    #    @param rating  game rating
    #    @param genre   game's genres
    #
    def __init__(self, title: str = "", platform: str = "", rating: float = 0.0, genre: str = ""):
            self._title = title
            self._platform = platform
            self._rating = rating
            self._genre = genre

    ##
    # get game title
    #
    @property
    def title(self):
        return self._title

    ##
    # set game title
    # @param t  title of game to set
    #
    @title.setter
    def title(self, t):
        self._title = t

    ##
    # get game platform
    #
    @property
    def platform(self):
        return self._platform

    ##
    # set game platform
    # @param p  platform of game to set
    #
    @platform.setter
    def platform(self, p):
        self._platform = p

    ##
    # get game rating
    #
    @property
    def rating(self):
        return self._rating

    ##
    # set game rating
    # @param r  rating of game to set
    #
    @rating.setter
    def rating(self, r):
        self._rating = r

    ##
    # get game genres (list of strings)
    #
    @property
    def genre(self):
        return self._genre

    ##
    # set game genres (list of strings)
    # @param g  genres of game to set (list of strings)
    #
    @genre.setter
    def genre(self, g):
        self._genre = g
