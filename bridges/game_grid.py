from bridges.grid import *
from bridges.game_cell import *
import base64


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
        self.bf_symbols = bytearray()
        self.encoding = "raw"
        if rows is None and cols is None:
            super(GameGrid, self).__init__(rows=30, cols=30)
            self.grid_size = [30, 30]
        else:
            super(GameGrid, self).__init__(rows=rows, cols=cols)
            self.grid_size = [rows, cols]
        self.initialize_game_Grid()

    def initialize_game_Grid(self):
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                self.set(i, j, GameCell())
        self.bf_bg = bytearray(self.grid_size[0]*self.grid_size[1])
        self.bf_fg = bytearray(self.grid_size[0]*self.grid_size[1])
        self.bf_symbols = bytearray(self.grid_size[0]*self.grid_size[1])

    def get_bg_color(self, row, col):
        return super(GameGrid, self).get(row, col).bg

    def set_bg_color(self, row, col, color):
        if type(color) == NamedColor:
            self.get(row, col).bg = color
        else:
            self.get(row, col).bg = NamedColor[color]

    def get_fg_color(self, row, col):
        return self.get(row, col).fg

    def set_fg_color(self, row, col, color):
        if type(color) == NamedColor:
            self.get(row, col).fg = color
        else:
            self.get(row, col).fg = NamedColor[color]

    def get_symbol(self, row, col):
        return self.get(row, col).symbol

    def get_symbol_color(self, row, col):
        return self.get(row, col).fg

    def draw_object(self, row, col, symbol, color):
        self.get(row, col).symbol = symbol
        self.get(row, col).fg = color

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
                if self.grid[i] is not None:
                    for j in range(self.grid_size[1]):
                        if self.grid[i][j] is not None:
                            gc = self.grid[i][j]
                            bg.append(gc.bg.value)
                            fg.append(gc.fg.value)
                            symbols.append(gc.symbol.value)
                            count += 1
            json_dict['bg'] = self.run_length(bg)
            json_dict['fg'] = self.run_length(fg)
            json_dict['symbols'] = self.run_length(symbols)

        if self.encoding == "raw":
            for i in range(self.grid_size[0]):
                if self.grid[i] is not None:
                    for j in range(self.grid_size[1]):
                        if self.grid[i][j] is None:
                            gc = self.grid[i][j]
                            self.bf_bg.append(gc.get_bg_byte())
                            self.bf_fg.append(gc.get_fg_byte())
                            self.bf_symbols.append(gc.get_symbol_byte())

            json_dict['bg'] = base64.b64encode(self.bf_bg)
            json_dict['fg'] = base64.b64encode(self.bf_fg)
            json_dict['symbols'] = base64.b64encode(self.bf_symbols)
        return json_dict

    def run_length(self, arr):
        count = 1
        out = str()
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                count += 1
                if len(arr) - i == 1:
                    out += str(arr[i]) + "x" + str(count)
            else:
                out += str(arr[i-1]) + "x" + str(count) + ","
                count = 1
                if len(arr) - i == 1:
                    out += str(arr[i]) + 'x' + str(count)

        return out


