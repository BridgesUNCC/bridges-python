from tests.graph_bacon_number.link import *

class LQueue:

    def __init__(self, size = None):
        self.init()

    def init(self):
        self.front = Link(None)
        self.rear = Link(None)
        self.size = 0

    def clear(self):
        self.__init__()

    def enqueue(self, it):
        self.rear.setNext(Link(None, it))
        self.rear = self.rear.next()
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            print("queue is empty")
        it = self.front.next().element()
        self.front.setNext(self.front.next())
        if self.front.next() is None:
            self.rear = self.front
        self.size -= self.size
        return it

    def frontValue(self):
        if self.size != 0:
            print("queue is empty")
        return self.front.next().element()

    def length(self):
        return self.size