

class MovieActorWikiData:
    """
    @brief This is a helper class for accessing actor-movie data from Wikidata.
    
    @author Erik Saule, Matthew Mcquaigue, Kalpathi Subramanian
    @date  2020, 1/6/21
    """

    def __init__(self):
        """
        Constructor
        """
        self._movie_uri = ""
        self._actor_uri = ""
        self._movie_name = ""
        self._actor_name = ""
       

    @property
    def movie_uri(self):
        """
        @brief Return the Movie's URI
        Returns:
             movie uri
        """
        return self._movie_uri

    @movie_uri.setter
    def movie_uri(self, uri):
        """
        @brief Set the Movie's URI
        Args:
             uri: Movie's URI to set 
        """
        self._movie_uri = uri

    @property
    def actor_uri(self):
        """
        @brief Return the actor's URI
        Returns:
             actor uri
        """
        return self._actor_uri

    @actor_uri.setter
    def actor_uri(self, uri):
        """
        @brief Set the actor's URI
        Args:
             uri: actor's URI to set 
        """
        self._actor_uri = uri

    @property
    def movie_name(self):
        """
        @brief Return the Movie's name
        Returns:
             movie name
        """
        return self._movie_name

    @movie_name.setter
    def movie_name(self, name):
        """
        @brief Set the Movie's name
        Args:
             name: Movie's name to set 
        """
        self._movie_name = name

    @property
    def actor_name(self):
        """
        @brief Return the actor's name
        Returns:
             actor name
        """
        return self._actor_name

    @actor_name.setter
    def actor_name(self, name):
        """
        @brief Set the actor's name
        Args:
             name: actor name to set 
        """
        self._actor_name = name
