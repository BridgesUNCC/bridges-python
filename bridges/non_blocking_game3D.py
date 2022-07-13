from bridges.gamebase3D import *
from bridges.input_helper import *
import time


class NonBlockingGame3D(GameBase3D):
    """
	brief This class provides the features necessary to implement  simple non blocking games.

	The games that can be created out of NonBlockingGame are
	based on a simple board grid of at most 1024 cells (e.g.,
	32x32, or any combinations less than 1024 cells). Each
	cell has a background color, and a colored symbol.

	This class is used by having another class derive
	from it and implement the two functions: initialize()
	and GameLoop(). initialize() is called exactly
	once, on the first frame of the game. It is used to
	make first time initializations of the game state
	(such as setting the board in its initial position,
	for instance in chess). However, GameLoop() is called
	at every frame of the game. The game starts when the
	function start() is called on the object you
	created.

	This game does not do anything, but it is the
	minimal code that will run a game. Note that the
	constructor of my_game passes 3 parameters to the
	constructor of NonBlockingGame(). These three
	parameters are the classic parameters that the
	constructor of bridges::Bridges takes (e.g.,
	assignmentID, username, apikey).

	To change the board, two functions are
	used. setBGColor() change the background color of a
	particular cell. It takes three parameters, the
	first two identify the cell of the board to change,
	and the last one is a color from a color palette
	provided by NamedColor. drawSymbol() takes four
	parameters, the first two identify the cell of the
	board to change, the third is a symbol from a
	symbol palette provided by NamedSymbol, the fourth
	is the color that symbol shold be drawn in and
	provided by NamedColor.

	For instance, a very simple initialize() could look like:
	code{.py}
	def initialize():
	    set_bg_color(0, 0, NamedColor.lightsalmon);
	    draw_symbol(0, 0, NamedSymbol.sword, NamedColor.blue);
	endcode

    Note that the size of the board is set by default
	at 10x10 and that drawing on a cell that does not
	exist will lead to an error. One can specify a
	gameboard of a different size by passing additional
	parameters to the NonBlockingGame
	constructor. However, the game can not be more than
	1024 cells in total, so a 15x15 board is possible,
	a 32x32 board is the largest square board possible,
	and a rectangular 64x16 rectangular board is also
	possible. But a 100x20 board would be 2000 cells
	and is not possible. For instance a board of 16
	rows and 64 columns can be created defining the
	my_game constructor as:

	code{.py}
		my_game = NonBlockingGame (1, "myuserid",  "myapikey", 16, 64)
	endcode

	The bridges game engine will call the GameLoop()
	function at each frame of the game. You can write
	this function to modify the state of the game board
	using setBGColor() and drawSymbol(). For instance,
	the following GameLoop() will color the board
	randomly one cell at a time.

	code{.py}
	def game_oop():
		set_BG_Color(rand()%10, rand()%10, NamedColor.lightsalmon);
	endcode

	The gameLoop can also probe the state of some keys
	of the keyboard using functions key_up(), key_left(),
	key_down(), key_right(), key_w(), key_a(), key_s(),
	key_d(), key_space(), and key_q(). These functions
	return a boolean that indicate whether the key is
	pressed at that frame or not. For instance, the
	following code will only color the board randomly
	when the up arrow is pressed.

	code{.py}
	def gameLoop():
		if key_up()
		    set_bg_color(rand()%10, rand()%10, NamedColor.lightsalmon);
	endcode

	@author Erik Saule
	@date 72119

    NonBlockingGame tutorial at: https://bridgesuncc.github.io/tutorials/NonBlockingGame.html
    """

    def __init__(self, assid, login, apikey):
        super(NonBlockingGame3D, self).__init__(assid, login, apikey)


        self.time_of_last_frame = int(round(time.time() * 1000))
        self.ih = InputHelper()
        self.register_keypress(self.ih)
        self._fps = 30

    @property
    def fps(self):
        """
        Get the frame rate at which the game running.
        Returns:
            The target framerate. The game could be somewhat slower depending on how computationally expensive the gameloop is and on the speed of the network
        """
        return self._fps

    @fps.setter
    def fps(self, frames):
        """
        Set the frame rate at which the game running.
        Args:
            frames: frame rate to be set.
        """
        self._fps = frames

    def sleep_timer(self, timems=None):
        if timems is None:
            timems = 1000
        try:
            time.sleep(timems / 1000)
        except InterruptedError:
            quit()

    def control_framerate(self):
        hz = 1. / self._fps

        current_time = int(round(time.time() * 1000))
        theoretical_next_frame = self.time_of_last_frame + int(hz * 1000)
        wait_time = theoretical_next_frame - current_time

        if wait_time > 0:
            self.sleep_timer(wait_time)

        self.time_of_last_frame = int(round(time.time() * 1000))

    def start(self):
        """
        Call this function from main to start game
        """

        frame = 0

        framelimit = os.getenv("FORCE_BRIDGES_FRAMELIMIT", None)
        if (framelimit):
            framelimit = int(framelimit)
            print("limiting number of frame to " + str(framelimit))

        try:
            self.sleep_timer()

            self.initialize()

            self.render()

            self.game_started = True

            while self.game_started:
                self.game_loop()
                self.render()
                self.control_framerate()
                frame = frame + 1
                if (framelimit and frame > framelimit):
                    print("frame limit of " + str(framelimit) + " frames reached")
                    self.quit()
        except:
            self.close()
            raise

        self.close()

    def key_left(self):
        """
        Is left currently pressed?
        Returns:
            true if left is currently pressed
        """
        return self.ih.left()

    def key_right(self):
        """
        Is right currently pressed?
        Returns:
            true if right is currently pressed
        """
        return self.ih.right()

    def key_up(self):
        """
        Is up currently pressed?
        Returns:
            true if up is currently pressed
        """
        return self.ih.up()

    def key_down(self):
        """
        Is down currently pressed?
        Returns:
            true if down is currently pressed
        """
        return self.ih.down()

    def key_q(self):
        """
        Is q currently pressed?
        Returns:
            true if q is currently pressed
        """
        return self.ih.q()

    def key_space(self):
        """
        Is space currently pressed?
        Returns:
            true if space is currently pressed
        """
        return self.ih.space()

    def key_w(self):
        """
        Is w currently pressed?
        Returns:
            true if w is currently pressed
        """
        return self.ih.w()

    def key_a(self):
        """
        Is a currently pressed?
        Returns:
            true if a is currently pressed
        """
        return self.ih.a()

    def key_s(self):
        """
        Is s currently pressed?
        Returns:
            true if s is currently pressed
        """
        return self.ih.s()

    def key_d(self):
        """
        Is right currently pressed?
        Returns:
            true d right is currently pressed
        """
        return self.ih.d()
