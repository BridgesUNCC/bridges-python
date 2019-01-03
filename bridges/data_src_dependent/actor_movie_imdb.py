
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
            self.actor = a
        if m is not None:
            self.movie = m
        if r is not None:
            self.rating = r
        if genr is not None:
            self.genres = genr

    ##
	#
	#  	 Get actor name
	#
	#  	 @return actor name (string)
	#
	#
    def get_actor(self):
        return self.actor

    ##
	#
	#  	 Set actor name
	#
	#  	 @param actor name (string)
	#
	#
    def set_actor(self, a):
        self.actor = a

    ##
	#
	#  	 Get movie name
	#
	#  	 @return movie name (string)
	#
	#
    def get_movie(self):
        return self.movie

    ##
	#
	#  	 Set movie name
	#
	#  	 @param movie name (string)
	#
	#
    def set_movie(self, m):
        self.movie = m

    ##
	#
	#  	 Get movie rating
	#
	#  	 @return movie rating  (double)
	#
	#
    def get_rating(self):
        return self.rating

    ##
	#
	#  	 Set movie rating
	#
	#  	 @param movie rating (double)
	#
	#
    def set_rating(self, r):
        self.rating = r

    ##
	#
	#  	 Get movie genres
	#
	#  	 @return movie genres  (vector)
	#
	#
    def get_genres(self):
        return self.genres

    ##
	#
	#  	 Set movie genres
	#
	#  	 @param movie genres (vector)
	#
	#  	
    def set_genres(self, genr):
        self.genres = genr
