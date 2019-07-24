from bridges.input_helper import *
from bridges.gamebase import *
import queue

class BlockingGame(KeyPressListener, GameBase):

    def __init__(self, assid, login, apikey, cols, rows):
        super(BlockingGame, self).__init__(assid, login, apikey, cols, rows)
        self.blocking_init()

    def blocking_init(self):
        self.q = queue.Queue(maxsize = 9)

    def key_press(self, keypress):
        try:
            type = str(keypress.get("key"))
            key = str(keypress.get("key"))
        except ValueError as e:
            traceback.print_tb(e.__traceback__)
            return

        if type == "keydown":
            self.q.put(key)

    def get_keypress(self):
        return self.q.get()

    def start(self):
        self.initialize()
        game_started = True

        while game_started:
            self.game_loop()
            self.render()
