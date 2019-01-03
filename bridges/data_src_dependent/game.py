
class Game:

    def __init__(self, title: str = "", platform: str = "", rating: float = 0.0, genre: str = ""):
            self.title = title
            self.platform = platform
            self.rating = rating
            self.genre = genre

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_platform(self):
        return self.platform

    def set_platform(self, platform):
        self.platform = platform

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre
