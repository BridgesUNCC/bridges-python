class GutenbergMeta:

    def __init__(self, id = 0, title = "", lang = "", date_added = "", authors = [], genres = [], loc = []):
        self.id = id
        self.title = title
        self.lang = lang
        self.date_added = date_added
        self.authors_list = authors
        self.genres_list = genres
        self.loc_list = loc

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, i):
        self.id = i

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, i):
        self.title = i

    @property
    def lang(self):
        return self.lang
    
    @lang.setter
    def lang(self, i):
        self.lang = i

    @property
    def date(self):
        return self.date_added
    
    @date.setter
    def date(self, i):
        self.date_added = i

    @property
    def authors(self):
        return self.authors_list

    @authors.setter
    def authors(self, i):
        self.authors_list = i

    @property
    def genres(self):
        return self.genres_list

    @genres.setter
    def genres(self, i):
        self.genres_list = i

    @property
    def loc(self):
        return self.loc_list

    @loc.setter
    def loc(self, i):
        self.loc_list = i