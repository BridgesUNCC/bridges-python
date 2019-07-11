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
        self.bf_bg = bytearray()
        self.bf_fg = bytearray()
        self.bf_symbols = bytearray
        if rows is None and cols is None:
            super(GameGrid, self).__init__(rows=30, cols=30)
        else:
            super(GameGrid, self).__init__(rows=rows,cols=cols)
        self.initialize_game_Grid()

    def initialize_game_Grid(self):
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                self.set(i,j,GameCell)
        self.bf_bg = bytearray(self.grid_size[0]*self.grid_size[1])
        self.bf_fg = bytearray(self.grid_size[0]*self.grid_size[1])
        self.bf_symbols = bytearray(self.grid_size[0]*self.grid_size[1])

    def set_bg_color(self, row, col, color):
        if type(color) == NamedColor:
            self.get(row,col).bg = color
        else:
            self.get(row, col).bg = NamedColor.__getitem__(color)

    def set_fg_color(self, row, col, color):
        if type(color) == NamedColor:
            self.get(row, col).fg = color
        else:
            self.get(row, col).fg = NamedColor.__getitem__(color)

    def draw_object(self, row, col, symbol, color = None):
        if color is not None:
            if type(color) == str:
                color = NamedColor.__getitem__(color)
            self.get(row, col).symbol = symbol
            self.get(row, col).fg = color
        else:
            self.get(row, col).symbol = symbol

    def get_data_structure_representation(self):
        count = 0

        json_dict = {
            "encoding": self.encoding,
            "dimensions": [self.grid_size[0], self.grid_size[1]]
        }

        if self.encoding == "rle":
            bg = []
            fg = []
            symbols = []

            for i in range(self.grid_size[0]):
                if self.grid.get(i).get(j) is None:
                    for j in range(self.grid_size[1]):
                        if self.grid.get(i).get(j) is None:
                            gc = self.grid.get(i).get(j)
                            bg[count] = gc.bg
                            fg[count] = gc.fg
                            symbols[count] = gc.symbol
                            count += 1

        json_dict['bg'] = run_length(bg)
        json_dict['fg'] = run_length(fg)
        json_dict['symbols'] = run_length(symbols)

        if self.encoding == "raw":
            for i in range(self.grid_size[0]):
                if self.grid.get(i).get(j) is None:
                    for j in range(self.grid_size[1]):
                        if self.grid.get(i).get(j) is None:
                            gc = self.grid.get(i).get(j)
                            self.bf_bg.append(gc.bg)
                            self.bf_fg.append(gc.fg)
