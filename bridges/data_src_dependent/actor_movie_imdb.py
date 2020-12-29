
##
#    @brief A class to hold actor movie data -- using IMDB dataset.
#
#
#    This dataset has a set of actor-movie pairs with movie rating and
#    genres, possibly. There are two datasets, the first has 1813 actor
#    movie pairs and no other attribute data. The second also has
#    movie ratings and genres.
#
#  @author Kalpathi Subramanian, Matthew Mcquaigue
#
#  @date 2/18/18, 12/29/20
#

class ActorMovieIMDB():
    ##
    # This method initializes an actor movie object with an actor/movie pair.
    #
    # @param a - actor  (string)
    # @param m - movie  (string)
    # @param r - rating  (float)
    # @param genr - genres  (vector)
    def __init__(self, a = None, m = None, r = None, genr = None):
        if a is not None:
            self._actor = a
        else:
            self._actor = ""
        if m is not None:
            self._movie = m
        else:
            self._movie = ""
        if r is not None:
            self._rating = r
        else:
            self._rating = float
        if genr is not None:
            self._genres = genr
        else:
            self._genres = []

    ##
    #       Get actor name
    #
    #       @return actor name (string)
    #
    @property
    def actor(self):
        return self._actor

    ##
    #    @brief Set actor
    #
    #     @param a  actor to set
    #
    @actor.setter
    def actor(self, a):
        self._actor = a

    ##
    #       Get movie name
    #
    #       @return movie name 
    #
    @property
    def movie(self):
        return self._movie

    ##
    #    @brief Set movie
    #
    #     @param m  movie to set
    #
    @movie.setter
    def movie(self, m):
        self._movie = m

    ##
    #       Get movie rating
    #
    #       @return movie rating 
    #
    @property
    def rating(self):
        return self._rating

    ##
    #    @brief Set movie
    #
    #     @param m  movie to set
    #
    @rating.setter
    def rating(self, r):
        self._rating = r

    ##
    #       @brief Set movie genres
    #
    #       @return movie rating 
    #
    @property
    def genres(self):
        return self._genres

    ##
    #    @brief Set genres
    #
    #     @param g  genres to set (list of strings)
    @genres.setter
    def genres(self, g):
        self._genres = g
