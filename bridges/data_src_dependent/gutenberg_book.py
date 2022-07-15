class GutenbergBook:
    """
    @brief  A Gutenberg Book object metadata only, used along with the books data source.
 
    This is a convenience class provided for  users who wish to use this
    data source as part of their application. It provides an API that makes
    it easy to access the attributes of this data set.

    Objects of this type are not meant to be created directly, but rather returned by a call to bridges::data_src_dependent::data_source::get_gutenberg_book_data()
   
    This data type is deprecated and you may want to use GutenbergMeta instead.

    Refer to tutorial examples to using this data source in data structure
    assignments.
     
    @author Matthew Mcquaigue, Kalpathi Subramanian
    @date   2/1/17, 12/29/20 
    """

    def __init__(self, author_name: str = "", author_birth: int = 0, author_death: int = 0, title: str = "", lang: str = "", genre: str = "", subject: str = "", num_chars: int = 0, num_words: int = 0, num_sentences: int = 0, num_difficult_words: int = 0, url: str = "", downloads: int = 0):
        """ 
        @brief constructor
        Args:
            author_name: name of author [string]
            author_birth: author birth date [int]
            author_death: aurthor death date [int]
            title:  title of book [string]
            lang:   language of book [string]
            genre:  genres of book [list of strings]
            subject: subject of book [string]
            num_chars: number of characters [int]
            num_words: number of words [int]
            num_sentences: number of sentences [int]
            num_difficult_words: number of difficult words [int]
            url:  url of book [string]
            downloads: number of downloads of book [int]
        """
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

    @property
    def name(self):
        """
        @brief get author's name
        Returns:
            name of author
        """
        return self._author_name

    @name.setter
    def name(self, n):
        """
        @brief Set author's name
        Args:
            n:  name of author
        """
        self._author_name = n

    @property
    def birth(self):
        """
        @brief get birth date of book's author
        Returns:
            birthdate of author
        """
        return self._author_birth

    @birth.setter
    def birth(self, b):
        """
        @brief Set author's birth date
        Args:
            b:  author birth date to set
        """
        self._author_birth = b

    @property
    def death(self):
        """
        @brief get date of death of book's author
        Returns:
            date of death of author
        """
        return self._author_death

    @death.setter
    def death(self, d):
        """
        @brief Set date of death of book's author
        Args:
            d: author's date of death to be set
        """
        self._author_death = d

    @property
    def title(self):
        """
        @brief Get title of book
        Returns:
            book title
        """
        return self._title

    @title.setter
    def title(self, t):
        """
        @brief Set book title
        Args:
            t: title to set
        """
        self._title = t

        """
        @brief Get language of book
        Returns:
            book language
        """
    @property
    def lang(self):
        """
        @brief Get book's language
        Returns:
            book's language
        """
        return self._lang

    @lang.setter
    def lang(self, l):
        """
        @brief Set book's language
        Args:
            l: language to set
        """
        self._lang = l

    @property
    def genre(self):
        """
        @brief Get book's genres
        Returns:
            book's genres
        """
        return self._genre

    @genre.setter
    def genre(self, g):
        """
        @brief Set book's genres
        Args:
            g: genres to set
        """
        self._genre = g

    @property
    def subject(self):
        """
        @brief Get book's subject
        Returns:
            book's subject
        """
        return self._subject

    @subject.setter
    def subject(self, s):
        """
        @brief Set book's subject
        Args:
            s: subject to set
        """
        self._subject = s

    @property
    def url(self):
        """
        @brief Get book's url
        Returns:
            book's url
        """
        return self._url

    @url.setter
    def url(self, u):
        """
        @brief Set book's url
        Args:
            u: url to set
        """
        self._url = u

    @property
    def num_chars(self):
        """
        @brief Get number of characters in book
        Returns:
            book's character count
        """
        return self._num_chars

    @num_chars.setter
    def num_chars(self, n):
        """
        @brief Set book's number of characters
        Args:
            n: number of characters to set
        """
        self._num_chars = n

    @property
    def num_words(self):
        """
        @brief Get number of words in book
        Returns:
            book's words count
        """
        return self._num_words

    @num_words.setter
    def num_words(self, w):
        """
        @brief Set book's number of words
        Args:
            w: number of words to set
        """
        self._num_words = w

    @property
    def num_sentences(self):
        """
        @brief Get number of sentences in book
        Returns:
            book's sentence count
        """
        return self._num_sentences

    @num_sentences.setter
    def num_sentences(self, n):
        """
        @brief Set book's number of sentences
        Args:
            n: number of sentences to set
        """
        self._num_sentences = n

    @property
    def num_difficult_words(self):
        """
        @brief Get number of difficulut words in book
        Returns:
            book's difficulut word count
        """
        return self._num_difficult_words

    @num_difficult_words.setter
    def num_difficult_words(self, w):
        """
        @brief Set book's number of difficult words
        Args:
            w: difficult word count to set
        """
        self._num_difficult_words = w

    @property
    def downloads(self):
        """
        @brief Get number of downloads of book
        Returns:
            book's download count
        """
        return self._downloads

    @downloads.setter
    def downloads(self, d):
        """
        @brief Set book's number of downloads
        Args:
            d: download count to set
        """
        self._downloads = d

