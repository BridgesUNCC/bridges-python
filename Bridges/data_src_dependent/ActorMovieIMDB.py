

class ActorMovieIMDB():

    def __init__(self, a = None, m = None, r = None, genr = None):
        if a is not None:
            self.actor = a
        if m is not None:
            self.movie = m
        if r is not None:
            self.rating = r
        if genr is not None:
            self.genres = genr

    def get_Actor(self):
        return self.actor

    def set_Actor(self, a):
        self.actor = a

    def get_Movie(self):
        return self.movie

    def set_movie(self, m):
        self.movie = m

    def get_rating(self):
        return self.rating

    def set_rating(self, r):
        self.rating = r

    def get_genres(self):
        return self.genres

    def set_genres(self, genr):
        self.genres = genr




