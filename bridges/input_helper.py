from bridges.keypress_listener import *
import traceback

class InputHelper(KeyPressListener):
    """
    @brief This is meant to be an internal class, not something that the library user will use.

    This class provide input device (mouse and keyboard)
    handling for Bridges games
    
    @sa See the Games Tutorials at
    https://bridgesuncc.github.io/tutorials/NonBlockingGame.html
    for more information on keys and mouse device usage.
    
    @author Erik Saule, David Burlinson
    @date 2018, 2019, 2020, 1/2/21
    """

    def __init__(self):
        """
        Constructor. All key initializations done here.
        """
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
        """
        Record a key press event
        Args:
            keypress: keypress event
        """
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
        """
        Get the up arrow key.
        Returns:
            the 'Up Arrow' key
        """
        return self.up_key

    def down(self):
        """
        Get the down arrow key.
        Returns:
            the 'Down Arrow' key
        """
        return self.down_key

    def left(self):
        """
        Get the left arrow key.
        Returns:
            the 'Left Arrow' key
        """
        return self.left_key

    def right(self):
        """
        Get the right arrow key.
        Returns:
            the 'Right Arrow' key
        """
        return self.right_key

    def q(self):
        """
        Get the 'q' arrow key.
        Returns:
            the 'q' key
        """
        return self.q_key

    def space(self):
        """
        Get the ' ' (space) key.
        Returns:
            the 'Space' key
        """
        return self.space_key

    def w(self):
        """
        Get the 'w' (space) key.
        Returns:
            the 'w' key
        """
        return self.w_key

    def a(self):
        """
        Get the 'a' (space) key.
        Returns:
            the 'a' key
        """
        return self.a_key

    def s(self):
        """
        Get the 's' (space) key.
        Returns:
            the 's' key
        """
        return self.s_key

    def d(self):
        """
        Get the 'd' (space) key.
        Returns:
            the 'd' key
        """
        return self.d_key




