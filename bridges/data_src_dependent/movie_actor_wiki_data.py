
##    @brief This is a helper class for accessing actor-movie data from Wikidata.
#
#    @author Erik Saule, Matthew Mcquaigue, Kalpathi Subramanian
#    @date  2020, 
#
class MovieActorWikiData:

    ##
    #     Constructor
    #
    def __init__(self):
        self._movie_uri = ""
        self._actor_uri = ""
        self._movie_name = ""
        self._actor_name = ""

    ##
    # get movie uri
    #
    @property
    def movie_uri(self):
        return self._movie_uri

    ##
    # set movie uri
    # @param uri uri of movie
    #
    @movie_uri.setter
    def movie_uri(self, uri):
        self._movie_uri = uri

    ##
    # get actor uri
    #
    @property
    def actor_uri(self):
        return self._actor_uri

    ##
    # set actor uri
    # @param uri uri of actor
    #
    @actor_uri.setter
    def actor_uri(self, uri):
        self._actor_uri = uri

    ##
    # get movie name
    #
    @property
    def movie_name(self):
        return self._movie_name

    ##
    # set movie name
    # @param name name of movie
    #
    @movie_name.setter
    def movie_name(self, name):
        self._movie_name = name

    ##
    # get actor name
    #
    @property
    def actor_name(self):
        return self._actor_name

    ##
    # set actor name
    # @param name name of actor
    #
    @actor_name.setter
    def actor_name(self, name):
        self._actor_name = name
