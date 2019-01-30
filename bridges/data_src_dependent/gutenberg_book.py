

class GutenbergBook:

    def __init__(self, author_name: str = "", author_birth: int = 0, author_death: int = 0, title: str = "",
                 lang: str = "", genre: str = "", subject: str = "", num_chars: int = 0, num_words: int = 0,
                 num_sentences: int = 0, num_difficult_words: int = 0, url: str = "", downloads: int = 0):
            self.author_name = author_name
            self.author_birth = author_birth
            self.author_death = author_death
            self.title = title
            self.lang = lang
            self.genre = genre
            self.subject = subject
            self.num_chars = num_chars
            self.num_words = num_words
            self.num_sentences = num_sentences
            self.num_difficult_words = num_difficult_words
            self.url = url
            self.downloads = downloads

    def get_author_name(self):
        return self.author_name

    def set_author_name(self, author_name):
        self.author_name = author_name

    def get_author_birth(self):
        return self.author_birth

    def set_author_birth(self, author_birth):
        self.author_birth = author_birth

    def get_author_death(self):
        return self.author_death

    def set_author_death(self, author_death):
        self.authorDeath = author_death

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_subject(self):
        return self.subject

    def set_subject(self, subject):
        self.subject = subject

    def get_num_words(self):
        return self.num_words

    def set_num_words(self, num_words):
        self.num_words = num_words

    def get_num_sentences(self):
        return self.num_sentences

    def set_num_sentences(self, num_sentences):
        self.num_sentences = num_sentences

    def get_num_difficult_words(self):
        return self.num_difficult_words

    def set_num_difficult_words(self,_num_difficult_words):
        self.num_difficult_words_=_num_difficult_words

