from tests.graph_bacon_number.link import *

class LQueue:

    def __init__(self, size = None):
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
        assert self.size != 0, "queue is empty"
        it = self.front.next().element()
        self.front.setNext(self.front.next().next())
        if self.front.next() is None:
            self.rear = self.front
        self.size -= 1
        return it

    def frontValue(self):
        assert self.size != 0, "queue is empty"
        return self.front.next().element()

    def length(self):
        return self.size