
class Game:

    def __init__(self, title= None, platform = None, rating = None, genre = None):
        if title is not None and platform is not None and rating is not None and genre is not None:
            self.title = title
            self.platform = platform
            self.rating = rating
            self.genre = genre
        else:
            self.title = self.platform = ""
            self.rating = 0.0

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getPlatform(self):
        return self.platform
    def setPlatform(self, platform):
        self.platform = platform

    def getRating(self):
        return self.rating
    def setRating(self, rating):
        self.rating = rating

    def getGenre(self):
        return self.genre
    def setGenre(self, genre):
        self.genre = genre