
class MovieActorWikiData:

    def __init__(self):
        self._movie_uri = ""
        self._actor_uri = ""
        self._movie_name = ""
        self._actor_name = ""

    @property
    def movie_uri(self):
        return self._movie_uri

    @movie_uri.setter
    def movie_uri(self, uri):
        self._movie_uri = uri

    @property
    def actor_uri(self):
        return self._actor_uri

    @actor_uri.setter
    def actor_uri(self, uri):
        self._actor_uri = uri

    @property
    def movie_name(self):
        return self._movie_name

    @movie_name.setter
    def movie_name(self, name):
        self._movie_name = name

    @property
    def actor_name(self):
        return self._actor_name

    @actor_name.setter
    def actor_name(self, name):
        self._actor_name = name
