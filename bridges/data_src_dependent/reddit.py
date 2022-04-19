class reddit:

    def __init__(self, id = 0, title = "", author= "", score = 0, vote_ratio = 0, comment_count = 0, subreddit = "", post_time = 0, url = "", text = ""):
        self.id = id
        self.title = title
        self.author = author
        self.score = score
        self.vote_ratio = vote_ratio
        self.comment_count = comment_count
        self.subreddit = subreddit
        self.post_time = post_time
        self.url = url
        self.text = text

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
    def author(self):
        return self.__author

    @author.setter
    def author(self, i):
        self.__author = i

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, i):
        self.__score = i

    @property
    def vote_ratio(self):
        return self.__vote_ratio

    @vote_ratio.setter
    def vote_ratio(self, i):
        self.__vote_ratio = i

    @property
    def comment_count(self):
        return self.__comment_count

    @comment_count.setter
    def comment_count(self, i):
        self.__comment_count = i

    @property
    def subreddit(self):
        return self.__subreddit

    @subreddit.setter
    def subreddit(self, i):
        self.__subreddit = i

    @property
    def post_time(self):
        return self.__post_time

    @post_time.setter
    def post_time(self, i):
        self.__post_time = i

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, i):
        self.__url = i

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, i):
        self.__text = i