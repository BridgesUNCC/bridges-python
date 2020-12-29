##
#    @brief  A Gutenberg Book object metadata only, used along with the
#    books data source.
#
#    This is a convenience class provided for  users who wish to use this
#    data source as part of their application. It provides an API that makes
#    it easy to access the attributes of this data set.
#    
#    Refer to tutorial examples to using this data source in data structure
#    assignments.
#    
#    @author Matthew Mcquaigue, Kalpathi Subramanian
#    @date   2/1/17, 12/29/20 


class GutenbergBook:

    ## @brief constructor
    #    @param author_name name of author [string]
    #    @param author_birth author birth date [int]
    #    @param author_death aurthor death date [int]
    #    @param title  title of book [string]
    #    @param lang   language of book [string]
    #    @param genre  genres of book [list of strings]
    #    @param subject subject of book [string]
    #    @param num_chars number of characters [int]
    #    @param num_words number of words [int]
    #    @param num_sentences number of sentences [int]
    #    @param num_difficult_words number of difficult words [int]
    #    @param url  url of book [string]
    #    @param downloads number of downloads of book [int]
    #
    def __init__(self, author_name: str = "", author_birth: int = 0, author_death: int = 0, title: str = "",
                 lang: str = "", genre: str = "", subject: str = "", num_chars: int = 0, num_words: int = 0,
                 num_sentences: int = 0, num_difficult_words: int = 0, url: str = "", downloads: int = 0):
            self._author_name = author_name
            self._author_birth = author_birth
            self.author_death = author_death
            self._title = title
            self._lang = lang
            self._genre = genre
            self._subject = subject
            self._num_chars = num_chars
            self._num_words = num_words
            self._num_sentences = num_sentences
            self._num_difficult_words = num_difficult_words
            self._url = url
            self._downloads = downloads

    ##
    # @brief get name of book's author
    #
    @property
    def name(self):
        return self._author_name

    @name.setter
    def name(self, n):
        self._author_name = n

    ##
    # @brief get birth date of book's author
    #
    @property
    def birth(self):
        return self._author_birth

    @birth.setter
    def birth(self, b):
        self._author_birth = b

    ##
    # @brief get date of death of book's author
    #
    @property
    def death(self):
        return self._author_death

    @death.setter
    def death(self, d):
        self._author_death = d

    ##
    # @brief get title of book
    #
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    ##
    # @brief get language of book
    #
    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, l):
        self._lang = l

    ##
    # @brief get genres of book
    #
    @property
    def genre(self):
        return self._genre

    ##
    # @brief set book's genres
    # @param g genres of book to set
    #
    @genre.setter
    def genre(self, g):
        self._genre = g

    ##
    # @brief get subject of book
    #
    @property
    def subject(self):
        return self._subject

    ##
    # @brief set book's subject
    # @param s subject of book to set
    #
    @subject.setter
    def subject(self, s):
        self._subject = s

    ##
    # @brief get url of book
    #
    @property
    def url(self):
        return self._url

    ##
    # @brief set book's url
    # @param u  url of book to set
    #
    @url.setter
    def url(self, u):
        self._url = u

    ##
    # @brief get number of characters in  the book
    #
    @property
    def num_chars(self):
        return self._num_chars

    ##
    # @brief set number of characters in  the book
    # @param n  number of characters
    #
    @num_chars.setter
    def num_chars(self, n):
        self._num_chars = n

    ##
    # @brief get number of words in  the book
    #
    @property
    def num_words(self):
        return self._num_words

    ##
    # @brief set number of words in the book
    # @param w  number of words 
    #
    @num_words.setter
    def num_words(self, w):
        self._num_words = w

    ##
    # @brief get number of sentences in  the book
    #
    @property
    def num_sentences(self):
        return self._num_sentences

    ##
    # @brief set number of sentences in  the book
    # @param n  number of sentences
    #
    @num_sentences.setter
    def num_sentences(self, n):
        self._num_sentences = n

    ##
    # @brief get number of difficult words in  the book
    #
    @property
    def num_difficult_words(self):
        return self._num_difficult_words

    ##
    # @brief set number of difficult words of  the book
    # @param w  number of difficulty words
    #
    @num_difficult_words.setter
    def num_difficult_words(self, w):
        self._num_difficult_words = w

    ##
    # @brief get number of downloads of  the book
    #
    @property
    def downloads(self):
        return self._downloads

    ##
    # @brief set number of downloads of  the book
    # @param d  number of downloads
    #
    @downloads.setter
    def downloads(self, d):
        self._downloads = d

