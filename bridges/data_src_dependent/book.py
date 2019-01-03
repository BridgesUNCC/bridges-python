
class Book:

    def __init__(self, authorName, authorBirth, authorDeath, title, lang, genre, subject, numChars, numWords,
                 numSentences, numDifficultWords, url, downloads):
        self.authorName = authorName
        self.authorBirth = authorBirth
        self.authorDeath = authorDeath
        self.title = title
        self.lang = lang
        self.genre = genre
        self.subject = subject
        self.url = url
        self.numChars = numChars
        self.numWords = numWords
        self.numSentences = numSentences
        self.numDifficultWords = numDifficultWords

    def get_author_name(self):
        return self.authorName

    def set_author_name(self, author_name):
        self.authorName = author_name

    def get_author_birth(self):
        return self.authorBirth

    def set_author_birth(self, author_birth):
        self.authorBirth = author_birth

    def get_author_death(self):
        return self.authorDeath

    def set_author_death(self,author_death):
        self.authorDeath = author_death

    def get_title(self):
        return self.title

    def set_title(self,title):
        self.title = title

    def get_lang(self):
        return self.lang

    def set_lang(self, lang):
        self.lang = lang

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_subject(self):
        return self.subject

    def set_subject(self, subject):
        self.subject = subject

    def get_url(self):
        return self.url

    def set_url(self,url):
        self.url = url

    def get_num_chars(self):
        return self.numChars

    def set_num_chars(self,num_chars):
        self.numChars = num_chars

    def get_num_words(self):
        return self.numWords

    def set_num_words(self,num_words):
        self.numWords = num_words

    def get_num_sentences(self):
        return self.numSentences

    def set_num_sentences(self,num_sentences):
        self.numSentences = num_sentences

    def get_num_difficult_words(self):
        return self.numDifficultWords

    def set_num_difficult_words(self, num_difficult_words):
        self.numDifficultWords = num_difficult_words

