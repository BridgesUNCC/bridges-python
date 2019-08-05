from bridges.array import *


class Array2D(Array):

    def __init__(self, rows = None, col = None):
        super(Array2D, self).__init__()
        if rows is not None and col is not None:
            dim = [col, rows, 1]
            self.num_rows = rows
            self.num_cols = col
            self.set_size(2, dim)
        else:
            self.size = 0
            self.num_rows = 0
            self.num_cols = 0