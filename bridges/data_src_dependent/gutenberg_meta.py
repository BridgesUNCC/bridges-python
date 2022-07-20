class GutenbergMeta:
    """
    @brief Class to hold the meta data of various books from the Gutenberg Project. 

    This is to be used with the Gutenberg request functions. 

    This class holds id, title, language, date_added,
    authors, genres, and library of congress classifications.

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_gutenberg_book_metadata() or bridges::data_src_dependent::data_source::get_a_gutenberg_book_metadata()

    One can get the actual text of a book using bridges::data_src_dependent::data_source::gutenberg_book_text()

    @sa A tutorial of how to use the Gutenberg data in BRIDGES is 
         available: check out https://bridgesuncc.github.io/tutorials/Data_Gutenberg.html
    @author Jay Strahler
    @date 12/28/20 
    """

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
        """
        @brief get book's id
        Returns:
            id of book
        """
        return self.__id

    @id.setter
    def id(self, i):
        """
        @brief Set book's id
        Args:
            i:  id of book
        """
        self.__id = i

    @property
    def title(self):
        """
        @brief get book's title
        Returns:
            title of book
        """
        return self.__title

    @title.setter
    def title(self, i):
        """
        @brief Set book's title
        Args:
            i:  title of book
        """
        self.__title = i

    @property
    def lang(self):
        """
        @brief get book's language
        Returns:
            language of book
        """
        return self.__lang
    
    @lang.setter
    def lang(self, i):
        """
        @brief Set book's language
        Args:
            i:  language of book
        """
        self.__lang = i

    @property
    def date(self):
        """
        @brief get book's date added to gutenberg
        Returns:
            date of book
        """
        return self.__date_added
    
    @date.setter
    def date(self, i):
        """
        @brief Set book's date added to gutenberg
        Args:
            i:  date of book
        """
        self.__date_added = i

    @property
    def authors(self):
        """
        @brief get book's authors
        Returns:
            authors of book
        """
        return self.__authors_list

    @authors.setter
    def authors(self, i):
        """
        @brief Set book's authors
        Args:
            i:  authors of book
        """
        self.__authors_list = i

    @property
    def genres(self):
        """
        @brief get book's genres
        Returns:
            genres of book
        """
        return self.__genres_list

    @genres.setter
    def genres(self, i):
        """
        @brief Set book's genres
        Args:
            i:  genres of book
        """
        self.__genres_list = i

    @property
    def loc(self):
        """
        @brief get book's library of congress classifications
        Returns:
            library of congress calssifications of book
        """
        return self.__loc_list

    @loc.setter
    def loc(self, i):
        """
        @brief Set book's library of congress classifications
        Args:
            i:  library of congress classifications of book
        """
        self.__loc_list = i
