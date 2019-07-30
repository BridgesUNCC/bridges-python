from bridges.gamebase import *
from bridges.input_helper import *
import time

##
# 
#
# \sa NonBlockingGame tutorial at: http://bridgesuncc.github.io/tutorials/NonBlockingGame.html
class NonBlockingGame(GameBase):

    def __init__(self, assid, login, apikey, cols, rows):
        super(NonBlockingGame, self).__init__(assid, login, apikey, cols, rows)
        if cols*rows > 1024:
            print("ERROR: Number of cells in a non-blocking game grid cannot exceed 32x32 or 1024.")
            exit(1)

        self.time_of_last_frame = int(round(time.time() * 1000))
        self.ih = InputHelper()
        self.register_keypress(self.ih)

    def sleep_timer(self, timems=None):
        if timems is None:
            timems = 1000
        try:
            time.sleep(timems/1000)
        except InterruptedError:
            quit()

    def control_framerate(self):
        fps = 30
        hz = 1./fps

        current_time = int(round(time.time() * 1000))
        theoretical_next_frame = self.time_of_last_frame + int(hz*1000)
        wait_time = theoretical_next_frame-current_time

        if wait_time > 0:
            self.sleep_timer(wait_time)

        self.time_of_last_frame = int(round(time.time() * 1000))

    def start(self):
        self.sleep_timer()

        self.render()

        self.initialize()

        self.game_started = True

        while self.game_started:
            self.game_loop()
            self.render()
            self.control_framerate()

    def key_left(self):
        return self.ih.left()

    def key_right(self):
        return self.ih.right()

    def key_up(self):
        return self.ih.up()

    def key_down(self):
        return self.ih.down()

    def key_q(self):
        return self.ih.q()

    def key_space(self):
        return self.ih.space()

    def key_w(self):
        return self.ih.w()

    def key_a(self):
        return self.ih.a()

    def key_s(self):
        return self.ih.s()

    def key_d(self):
        return self.ih.d()
