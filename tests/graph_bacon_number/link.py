
class Link():

    def __init__(self, nextVal, it = None):
        self.element = it
        self.next = nextVal

    def __call__(self):
        return self.next, self.element

    def next(self):
        return self.next

    def setNext(self, nextVal):
        self.next = nextVal
        return self.next

    def element(self):
        return self.element

    def setElement(self, it):
        self.element = it
        return self.element