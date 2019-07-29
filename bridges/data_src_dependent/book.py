
class Book:

    def __init__(self, authorName, authorBirth, authorDeath, title, lang, genre, subject, numChars, numWords,
                 numSentences, numDifficultWords, url, downloads):
        self._authorName = authorName
        self._authorBirth = authorBirth
        self._authorDeath = authorDeath
        self._title = title
        self._lang = lang
        self._genre = genre
        self._subject = subject
        self._url = url
        self._numChars = numChars
        self._numWords = numWords
        self._numSentences = numSentences
        self._numDifficultWords = numDifficultWords

    @property
    def name(self):
        return self._authorName

    @name.setter
    def name(self, n):
        self._authorName = n

    @property
    def birth(self):
        return self._authorBirth

    @birth.setter
    def birth(self, b):
        self._authorBirth = b

    @property
    def death(self):
        return self._authorDeath

    @death.setter
    def death(self, d):
        self._authorDeath = d

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
        return self._numChars

    @num_chars.setter
    def num_chars(self, n):
        self._numChars = n

    @property
    def num_words(self):
        return self._numWords

    @num_words.setter
    def num_words(self, w):
        self._numWords = w

    @property
    def num_sentences(self):
        return self._numSentences

    @num_sentences.setter
    def num_sentences(self, n):
        self._numSentences = n

    @property
    def num_difficult_words(self):
        return self._numDifficultWords

    @num_difficult_words.setter
    def num_difficult_words(self, w):
        self._numDifficultWords = w

