from bridges.keypress_listener import *
import traceback


class InputHelper(KeyPressListener):

    def __init__(self):
        self.up_key = False
        self.down_key  = False
        self.left_key = False
        self.right_key = False
        self.q_key = False
        self.space_key = False
        self.w_key = False
        self.a_key = False
        self.s_key = False
        self.d_key = False

    def key_press(self, keypress):
        try:
            press_type = str(keypress.get("type"))
            key = str(keypress.get("key"))
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            return

        if press_type == "keyup":
            set_to_up = True
        else:
            set_to_up = False

        if press_type == "keydown":
            set_to_down = True
        else:
            set_to_down = False

        if key == "ArrowUp":
            if set_to_up:
                self.up_key = False
            if set_to_down:
                self.up_key = True

        if key == "ArrowDown":
            if set_to_up:
                self.down_key = False
            if set_to_down:
                self.down_key = True

        if key == "ArrowLeft":
            if set_to_up:
                self.left_key = False
            if set_to_down:
                self.left_key = True

        if key == "ArrowRight":
            if set_to_up:
                self.right_key = False
            if set_to_down:
                self.right_key = True

        if key == "q":
            if set_to_up:
                self.q_key = False
            if set_to_down:
                self.q_key = True

        if key == " ":
            if set_to_up:
                self.space_key = False
            if set_to_down:
                self.space_key = True

        if key == "w":
            if set_to_up:
                self.w_key = False
            if set_to_down:
                self.w_key = True

        if key == "a":
            if set_to_up:
                self.a_key = False
            if set_to_down:
                self.a_key = True

        if key == "s":
            if set_to_up:
                self.s_key = False
            if set_to_down:
                self.s_key = True

        if key == "d":
            if set_to_up:
                self.d_key = False
            if set_to_down:
                self.d_key = True

    def status(self):
        print("UP:" + str(self.up()) + " DOWN:" + str(self.down()) + " LEFT:" + str(self.left())
                + " RIGHT:" + str(self.right()))

    def up(self):
        return self.up_key

    def down(self):
        return self.down_key

    def left(self):
        return self.left_key

    def right(self):
        return self.right_key

    def q(self):
        return self.q_key

    def space(self):
        return self.space_key

    def w(self):
        return self.w_key

    def a(self):
        return self.a_key

    def s(self):
        return self.s_key

    def d(self):
        return self.d_key




