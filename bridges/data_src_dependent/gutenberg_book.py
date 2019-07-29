

class GutenbergBook:

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

    @property
    def name(self):
        return self._author_name

    @name.setter
    def name(self, n):
        self._author_name = n

    @property
    def birth(self):
        return self._author_birth

    @birth.setter
    def birth(self, b):
        self._author_birth = b

    @property
    def death(self):
        return self._author_death

    @death.setter
    def death(self, d):
        self._author_death = d

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, l):
        self._lang = l

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, g):
        self._genre = g

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, s):
        self._subject = s

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, u):
        self._url = u

    @property
    def num_chars(self):
        return self._num_chars

    @num_chars.setter
    def num_chars(self, n):
        self._num_chars = n

    @property
    def num_words(self):
        return self._num_words

    @num_words.setter
    def num_words(self, w):
        self._num_words = w

    @property
    def num_sentences(self):
        return self._num_sentences

    @num_sentences.setter
    def num_sentences(self, n):
        self._num_sentences = n

    @property
    def num_difficult_words(self):
        return self._num_difficult_words

    @num_difficult_words.setter
    def num_difficult_words(self, w):
        self._num_difficult_words = w

    @property
    def downloads(self):
        return self._downloads

    @downloads.setter
    def downloads(self, d):
        self._downloads = d

