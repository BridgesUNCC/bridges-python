class ActorMovieIMDB:
    """
    @brief A class to hold actor movie data -- using IMDB dataset.  

    This dataset has a set of actor-movie pairs with movie rating and
    genres, possibly. There are two datasets, the first has 1813 actor
    movie pairs and no other attribute data. The second also has
    movie ratings and genres.

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_actor_movie_imdb_data() and bridges::data_src_dependent::data_source::get_actor_movie_imdb_data2()

    @sa For an example, check out https://bridgesuncc.github.io/tutorials/Data_IMDB.html

    @author Kalpathi Subramanian, Matthew Mcquaigue

    @date 2/18/18, 12/29/20
    """
    
    def __init__(self, a = None, m = None, r = None, genr = None):
        """
        @brief This method initializes an actor movie object with an actor/movie pair.
        Args:
            a: actor  (string)
            m: movie  (string)
            r: rating  (float)
            genr: genres  (vector)
        """
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

    @property
    def actor(self):
        """
        @brief Get actor name

        Returns: 
            actor name (string)
        """
        return self._actor

    @actor.setter
    def actor(self, a):
        """
        Set actor name
        Args:
            a:  actor to set
        """
        self._actor = a

    @property
    def movie(self):
        """
        @brief Get movie name
        Returns:
            movie name 
        """
        return self._movie

    @movie.setter
    def movie(self, m):
        """
        @brief Set movie
        Args:
          m:  movie to set
        """
        self._movie = m

    @property
    def rating(self):
        """
        @brief Get movie rating
        Returns:
           Movie rating 
        """
        return self._rating

    @rating.setter
    def rating(self, r):
        """
        @brief Set movie rating
        Args:
            r:  rating to set
        """
        self._rating = r

    @property
    def genres(self):
        """
        @brief Get movie genres
        Returns:
            movie genres 
        """
        return self._genres

    @genres.setter
    def genres(self, g):
        """
        @brief Set movie genres
        Args:
            g:  genres to set (list of strings)
        """
        self._genres = g
