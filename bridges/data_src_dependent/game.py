
class Game:

    def __init__(self, title: str = "", platform: str = "", rating: float = 0.0, genre: str = ""):
            self._title = title
            self._platform = platform
            self._rating = rating
            self._genre = genre

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, p):
        self._platform = p

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, r):
        self._rating = r

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, g):
        self._genre = g
