
class Shakespeare:

    def __init__(self, title: str = "", type: str = "", text: str = ""):
        self.title = title
        self.type = type
        self.text = text

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_type(self):
        return self.type

    def set_type(self,type):
        self.type = type

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text
