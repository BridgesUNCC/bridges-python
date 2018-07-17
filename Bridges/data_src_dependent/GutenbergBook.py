

class GutenbergBook:

    def __init__(self, authorName = None, authorBirth = None, authorDeath = None, title = None, lang = None, genre = None,
                 subject = None, numChars = None, numWords = None, numSentences = None, numDifficultWords = None, url = None, downloads = None):
        if authorName and authorBirth and authorDeath and title and lang and genre and subject and numChars \
                and numWords and numSentences and numDifficultWords and url and downloads is not None:
            self.authorName = authorName
            self.authorBirth = authorBirth
            self.authorDeath = authorDeath
            self.title = title
            self.lang = lang
            self.genre = genre
            self.subject = subject
            self.numChars = numChars
            self.numWords = numWords
            self.numSentences = numSentences
            self.numDifficultWords = numDifficultWords
        else:
            self.authorName = self.title = self.url = ""
            self.authorBirth = self.authorDeath = self.numChars = self.numWords = self.numSentences = self.numDifficultWords = 0

    def getAuthorName(self):
        return self.authorName
    def setAuthorName(self, authorName):
        self.authorName = authorName

    def getAuthorBirth(self):
        return self.authorBirth
    def setAuthroBirth(self, authorBirth):
        self.authorBirth = authorBirth

    def getAuthorDeath(self):
        return self.authorDeath
    def setAuthorDeath(self, authorDeath):
        self.authorDeath = authorDeath

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getGenre(self):
        return self.genre
    def setGenre(self, genre):
        self.genre = genre

    def getSubject(self):
        return self.subject
    def setSubject(self, subject):
        self.subject = subject

    def getNumWords(self):
        return self.numWords
    def setNumWords(self, numWords):
        self.numWords = numWords

    def getNumSentences(self):
        return self.numSentences
    def setNumeSentences(self, numSentences):
        self.numSentences = numSentences

    def getNumDifficultWords(self):
        return self.numDifficultWords
    def setNumDifficultWords(self, numDifficultWords):
        self.numDifficultWords = numDifficultWords
