from bridges.array import *


class Array1D(Array):

    def __init__(self, sz = None):
        super(Array1D, self).__init__()
        if sz is not None:
            self.size = sz
            dim = [sz, 1, 1]
            self.set_size(1, dim)
        else:
            self.size = 0