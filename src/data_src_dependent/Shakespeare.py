
class Shakespeare:

    def __init__(self, title = None, type = None, text = None):
        if title is not None and type is not None and text is not None:
            self.title = title
            self.type = type
            self.text = text
        else:
            self.title = self.type = self.text = ""

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getType(self):
        return self.type
    def setType(self,type):
        self.type = type

    def getText(self):
        return self.text
    def setText(self, text):
        self.text = text