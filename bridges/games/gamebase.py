from bridges.bridges import *
from bridges.game_grid import *
from bridges.socket_connection import *
from abc import ABC, abstractmethod


class GameBase(ABC):
    debug = True

    def __init__(self, assid, login, apikey, cols, rows):
        self.game_base_init(assid, login, apikey, cols, rows)

    def game_base_init(self, id, log, key, c, r):
        self.firsttime = True

        self.bridges = Bridges(id, log, key)

        if GameBase.debug:
            self.bridges.set_visualize_JSON(True)

        self.bridges.connector.set_server("local")

        self.grid = GameGrid(c, r)

        self.grid.encoding("rle")

        self.sock = SocketConnection(bridges)
        self.sock.setup_connection(log, key)

    def register_keypress(self, kl):
        self.sock.add_listener(kl)

    def start(self):
        pass

    def initialize(self):
        pass

    def game_loop(self):
        pass

    def quit(self):
        self.game_started = False

    def set_title(self, title):
        self.bridges.set_title(title)

    def set_description(self, desc):
        self.bridges.set_description(desc)

    def get_bg_color(self, x, y):
        return self.grid.get_bg_color(x, y)

    def set_bg_color(self, x, y, color):
        self.grid.set_bg_color(x, y, color)

    def get_symbol(self, x ,y):
        return self.grid.get_symbol(x, y)

    def get_symbol_color(self, x, y):
        return self.grid.get_symbol_color(x, y)

    def draw_object(self, x, y, s, c):
        self.grid.draw_object(x, y, s, c)

    def render(self):
        if self.firsttime:
            self.firsttime = False

            self.bridges.set_data_structure(grid)
            try:
                self.bridges.visualize()
            except RuntimeError as e:
                print(e)

        self.grid_state = self.grid.get_data_structure_representation()
        self.sock.send_data(self.grid_state)






