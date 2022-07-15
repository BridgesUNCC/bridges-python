class Reddit:
    """
    @brief  A reddit object representing a reddit post, used along with the reddit data source.

    This is a convenience class provided for  users who wish to use this
    data source as part of their application. It provides an API that makes
    it easy to access the attributes of this data set.

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::reddit_data()
    
    For an example, check out https://bridgesuncc.github.io/tutorials/

    @author Erik Saule, Jay Strahler
    @date   12/1222
    """

    def __init__(self, id = 0, title = "", author= "", score = 0, vote_ratio = 0.0, comment_count = 0, subreddit = "", post_time = 0, url = "", text = ""):
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
        """
        @brief return id of the reddit post

        Returns:
            string: id 
        """

        return self.__id

    @id.setter
    def id(self, i):
        self.__id = i

    @property
    def title(self):
        """
        @brief return the title of the reddit post

        Returns:
            string: title 
        """
        return self.__title

    @title.setter
    def title(self, i):
        self.__title = i

    @property
    def author(self):
        """
        @brief return the author of the reddit post

        Returns:
            string: author's username
        """
        return self.__author

    @author.setter
    def author(self, i):
        self.__author = i

    @property
    def score(self):
        """
        @brief return the score (upvotes-downvotes) of the reddit post

        Returns:
            int: score (upvotes - downvotes)
        """
        return self.__score

    @score.setter
    def score(self, i):
        self.__score = i

    @property
    def vote_ratio(self):
        """
        @brief ratio of upvote to downvotes of the reddit post

        Returns:
            float: vote ratio
        """
        return self.__vote_ratio

    @vote_ratio.setter
    def vote_ratio(self, i):
        self.__vote_ratio = i

    @property
    def comment_count(self):
        """
        @brief number of comments on that reddit post

        Returns:
            int: number of comments
        """
        return self.__comment_count

    @comment_count.setter
    def comment_count(self, i):
        self.__comment_count = i

    @property
    def subreddit(self):
        """
        @brief name of the subreddit the post appeared in

        Returns:
            string: subreddit name
        """
        return self.__subreddit

    @subreddit.setter
    def subreddit(self, i):
        self.__subreddit = i

    @property
    def post_time(self):
        """
        @brief time the post was made (UNIX time)

        Returns:
            int: unix time
        """
        return self.__post_time

    @post_time.setter
    def post_time(self, i):
        self.__post_time = i

    @property
    def url(self):
        """
        @brief URL associated with the post. 

        This could be the url of the reddit post itself or the URL of an associated article/video

        Returns:
            string: URL
        """
        return self.__url

    @url.setter
    def url(self, i):
        self.__url = i

    @property
    def text(self):
        """
        @brief returns the text of the reddit post.

        The text of the reddit post. Often in markdown format.

        The text could be empty if the reddit post is just a link to a video or an article

        Returns:
            string: full text of the reddit post
        """
        return self.__text

    @text.setter
    def text(self, i):
        self.__text = i
