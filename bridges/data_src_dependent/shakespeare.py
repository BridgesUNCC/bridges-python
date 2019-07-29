
class Shakespeare:

    def __init__(self, title: str = "", type: str = "", text: str = ""):
        self._title = title
        self._type = type
        self._text = text

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, t):
        self._type = t

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, t):
        self._text = t
