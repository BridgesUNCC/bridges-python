from bridges.bridges import *
from bridges.scene import *
from bridges.socket_connection import *
from abc import ABC, abstractmethod


class GameBase3D(ABC):
    """
    @brief This is the base class for all games in BRIDGES

    @author David Burlinson, Erik Saule
    @date 2020, 2021

    """
    debug = True

    def __init__(self, assid, login, apikey):
        """
        PROTECTED constructor prevents the object from being directly created. Since GameBase is meant to be a purely internal class, that seems appropriate.

        Args:
            assid: assignment number
            login: user name
            apikey: authentication id
            rows: height of game grid
            cols: width of game grid
		Returns:
			None
        """
        self.game_base_init(assid, login, apikey)

    def game_base_init(self, id, log, key):
        """
        Initializes the gamebase object
        Args:
            id: assignment number
            log: user name
            key: authentication id
            rows: height of game grid
            cols: width of game grid
        """
        self.firsttime = True

        self.bridges = Bridges(id, log, key)

        # self.bridges.set_visualize_JSON(True)

        self.bridges.connector.set_server("local")

        self.sock = SocketConnection(self.bridges)
        self.sock.setup_connection(log, id)

        self.scene = Scene({'fov': 90, 'type': 'fps', 'position': [0.0, 0.0, 0.0]})

    def close(self):
        """
        close the socket connection (and game)
        """
        self.sock.close()

    def register_keypress(self, kl):
        self.sock.add_listener(kl)

    def start(self):
        """
        "starts the game. Called once at the beginning"
        """
        pass

    def initialize(self):
        """
        "Game initialization. . Called once at the beginning"
        """
        pass

    def game_loop(self):
        """
        "Method contains all of the game logica and can call other user defined methods"
        """
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




    def render(self):
        """
        renders the board
        """

        if self.firsttime:
            self.firsttime = False

            self.bridges.set_data_structure(self.scene)
            try:
                self.bridges.visualize()
            except RuntimeError as e:
                print(e)

        self.scene_state = self.scene.get_data_structure_representation()
        self.sock.send_data(self.scene_state, self.scene.get_data_structure_type())


