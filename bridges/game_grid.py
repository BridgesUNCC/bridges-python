from bridges.color import *
from bridges.game_cell import *


class GameGrid(Grid):

    def set_encoding(self, encoding):
        if encoding == "raw" or encoding == "rle":
            self.encoding = encoding
        else:
            print("Unrecognized encoding \'" + encoding +
                  "\', defaulting to raw. Options: raw, rle")
            self.encoding = "raw"

    def get_data_structure_type(self):
        return "GameGrid"

    def __init__(self, rows = None, cols = None):
        if rows is None and cols is None:
            super(GameGrid, self)__init__(30, 30)
        else:
            super(GameGrid, self)__init__(rows,cols)

    def initialize_game_Grid(self):
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                self.set(i,j,GameCell)
        bf_bg = Byte