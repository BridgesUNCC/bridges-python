
##
#  @brief A class to hold actor movie data -- using IMDB dataset
#
#
#  @author Kalpathi Subramanian
#  @date 2/18/18
#
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
	#
	#  	 Get actor name
	#
	#  	 @return actor name (string)
	#
	#
    @property
    def actor(self):
        return self._actor

    @actor.setter
    def actor(self, a):
        self._actor = a

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, m):
        self._movie = m

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, r):
        self._rating = r

    @property
    def generes(self):
        return self._genres

    @generes.setter
    def generes(self, g):
        self._genres = g
