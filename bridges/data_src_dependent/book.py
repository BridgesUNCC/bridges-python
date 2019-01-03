
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

    def getAuthorName(self):
        return self.authorName

    def setAuthorName(self, authorName):
        self.authorName = authorName

    def getAuthorBirth(self):
        return self.authorBirth

    def setAuthorBirth(self, authorBirth):
        self.authorBirth = authorBirth

    def getAuthorDeath(self):
        return self.authorDeath

    def setAuthorDeath(self,authorDeath):
        self.authorDeath = authorDeath

    def getTitle(self):
        return self.title

    def setTitle(self,title):
        self.title = title

    def getLang(self):
        return self.lang

    def setLang(self, lang):
        self.lang = lang

    def getGenre(self):
        return self.genre

    def setGenre(self, genre):
        self.genre = genre

    def getSubject(self):
        return self.subject

    def setSubject(self, subject):
        self.subject = subject

    def getURL(self):
        return self.url

    def setURL(self,url):
        self.url = url

    def getNumChars(self):
        return self.numChars

    def setNumChars(self,numChars):
        self.numChars = numChars

    def getNumWords(self):
        return self.numWords

    def setNumWords(self,numWords):
        self.numWords = numWords

    def getNumSentences(self):
        return self.numSentences

    def setNumSentences(self,numSentences):
        self.numSentences = numSentences

    def getNumDifficultWords(self):
        return self.numDifficultWords

    def setNumDifficultWords(self, numDifficultWords):
        self.numDifficultWords = numDifficultWords

