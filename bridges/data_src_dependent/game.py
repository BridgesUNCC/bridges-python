class Game:
    """
    @brief  A Game object, used along with the Games data source.
    
    This is a convenience class provided for  users who wish to use this
    data source as part of their application. It provides an API that makes
    it easy to access the attributes of this data set.
    
    Each game record has title, platform on which it can be played,
    rating,  and a list of genres.

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_game_data()

    @sa For an example, check out https://bridgesuncc.github.io/tutorials/Data_IGN_Games.html
    
    @author Matthew Mcquaigue, Kalpathi Subramanian
    @date   2/1/17, 12/29/20, 1/6/21
    """

    def __init__(self, title: str = "", platform: str = "", rating: float = 0.0, genre: str = ""):
        """
        @brief Constructor
        Args:
            title:  game title
            platform: game platform
            rating:  game rating
            genre:   game's genres
        """
        self._title = title
        self._platform = platform
        self._rating = rating
        self._genre = genre

    @property
    def title(self):
        """
        @brief get game title
        Returns:
            game title
        """
        return self._title

    @title.setter
    def title(self, t):
        """
        @brief Set game title
        Args:
            t: game title to set
        """
        self._title = t

    @property
    def platform(self):
        """
        @brief get game platform
        Returns:
            game platform
        """
        return self._platform

    @platform.setter
    def platform(self, p):
        """
        @brief Set game platform
        Args:
            p: game platform to set
        """
        self._platform = p

    @property
    def rating(self):
        """
        @brief get game rating
        Returns:
            game rating
        """
        return self._rating

    @rating.setter
    def rating(self, r):
        """
        @brief Set game rating
        Args:
            r: game rating to set
        """
        self._rating = r

    @property
    def genre(self):
        """
        @brief get game genres
        Returns:
            game genres (list of strings)
        """
        return self._genre

    @genre.setter
    def genre(self, g):
        """
        @brief Set game title
        Args:
            g:  game genres to set
        """
        self._genre = g
