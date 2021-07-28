class GutenbergMeta:

    def __init__(self, id = 0, title = "", lang = "", date_added = "", authors = [], genres = [], loc = []):
        """
        Constructor for a gutenbergmeta object that holds the metadata
        for a gutenberg book
        :param id: book id
        :param title: book title
        :param lang: book language
        :param date_added: data the book was added
        :param authors: authors of the book
        :param genres: book genres
        :param loc:
        """
        self.id = id
        self.title = title
        self.lang = lang
        self.date_added = date_added
        self.authors_list = authors
        self.genres_list = genres
        self.loc_list = loc

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, i):
        self.__id = i

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, i):
        self.__title = i

    @property
    def lang(self):
        return self.__lang
    
    @lang.setter
    def lang(self, i):
        self.__lang = i

    @property
    def date(self):
        return self._date_added
    
    @date.setter
    def date(self, i):
        self.__date_added = i

    @property
    def authors(self):
        return self.__authors_list

    @authors.setter
    def authors(self, i):
        self.__authors_list = i

    @property
    def genres(self):
        return self.__genres_list

    @genres.setter
    def genres(self, i):
        self.__genres_list = i

    @property
    def loc(self):
        return self.__loc_list

    @loc.setter
    def loc(self, i):
        self.__loc_list = i
