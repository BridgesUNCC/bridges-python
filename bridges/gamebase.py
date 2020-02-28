from bridges.bridges import *
from bridges.game_grid import *
from bridges.socket_connection import *
from abc import ABC, abstractmethod


class GameBase(ABC):
    debug = True

    def __init__(self, assid, login, apikey, cols, rows):
        """
        PROTECTED constructor prevent the object from being
        directly created. Since GameBase is meant to be a purely internal
        class, that seems appropriate.
        """
        self.game_base_init(assid, login, apikey, cols, rows)
        self.grid_state = dict

    def game_base_init(self, id, log, key, c, r):
        self.firsttime = True

        self.bridges = Bridges(id, log, key)

        #self.bridges.set_visualize_JSON(True)

        self.bridges.connector.set_server("games")

        self.grid = GameGrid(r, c)

        self.grid.set_encoding("rle")

        self.sock = SocketConnection(self.bridges)
        self.sock.setup_connection(log, id)

    def close(self):
        self.sock.close()
        
    def register_keypress(self, kl):
        self.sock.add_listener(kl)

    def start(self):
        pass

    def initialize(self):
        pass

    def game_loop(self):
        pass

    def quit(self):
        """
        calling this function causes the game to end.

        Returns:
            None
        """
        self.game_started = False

    def set_title(self, title):
        """
        sets title of game

        Returns:
            None
        """
        self.bridges.set_title(title)

    def set_description(self, desc):
        """
        sets description of the game

        Returns:
            None
        """
        self.bridges.set_description(desc)

    def get_bg_color(self, row, col):
        """
        gets background color of a cell

        Args:
            row: the row of the cell
            col: the column of the cell

        Returns:
            returns a NamedColor
        """
        return self.grid.get_bg_color(row, col)

    def set_bg_color(self, row, col, color):
        """
        sets background color of a cell

        Args:
            row: the row of the cell
            col: the column of the cell

        Returns:
            None
        """
        self.grid.set_bg_color(row, col, color)

    def get_symbol(self, row, col):
        """
        gets symbol of the  cell at row, col

        Args:
            row: the row of the cell
            col: the column of the cell

        Returns:
            Symbol of type NamedSymbol
        """

        return self.grid.get_symbol(row, col)

    def get_symbol_color(self, row, col):
        """
        gets symbol color of the  cell at row, col

        Args:
            row: the row of the cell
            col: the column of the cell

        Returns:
            color of type NamedColor
        """

        return self.grid.get_symbol_color(row, col)

    def draw_symbol(self, row, col, s, c):
        """
        draw symbol s with color col at  cell (row, col)

        Args:
            row: the row of the cell
            col: the column of the cell
            s: symbol
            c: color

        Returns:
            color of type NamedColor
        """
        self.grid.draw_symbol(row, col, s, c)

    def render(self):
        """
        renders the board
		"""

        if self.firsttime:
            self.firsttime = False

            self.bridges.set_data_structure(self.grid)
            try:
                self.bridges.visualize()
            except RuntimeError as e:
                print(e)

        self.grid_state = self.grid.get_data_structure_representation()
        self.sock.send_data(self.grid_state)

    @property
    def board_width(self):
        """
        setter/getter property for board width
        """
        width = self.grid.dimensions
        return width[1]

    @property
    def board_height(self):
        """
        setter/getter property for board height
        """
        height = self.grid.dimensions
        return height[0]

