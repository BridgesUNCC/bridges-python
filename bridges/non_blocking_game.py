from bridges.gamebase import *
from bridges.input_helper import *
from bridges.input_state_machine import *
import time


class NonBlockingGame(GameBase):
    """
    @brief This class provides the features necessary to implement  simple non blocking games.

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
    \code{.py}
    def initialize():
        set_bg_color(0, 0, NamedColor.lightsalmon);
        draw_symbol(0, 0, NamedSymbol.sword, NamedColor.blue);
    \endcode

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

    \code{.py}
        my_game = NonBlockingGame (1, "myuserid",  "myapikey", 16, 64)
    \endcode

    The bridges game engine will call the GameLoop()
    function at each frame of the game. You can write
    this function to modify the state of the game board
    using setBGColor() and drawSymbol(). For instance,
    the following GameLoop() will color the board
    randomly one cell at a time.

    \code{.py}
    def game_loop():
        set_BG_Color(rand()%10, rand()%10, NamedColor.lightsalmon);
    \endcode

    The gameLoop can also probe the state of some keys
    of the keyboard using functions key_up(), key_left(),
    key_down(), key_right(), key_w(), key_a(), key_s(),
    key_d(), key_space(), and key_q(). These functions
    return a boolean that indicate whether the key is
    pressed at that frame or not. For instance, the
    following code will only color the board randomly
    when the up arrow is pressed.

    \code{.py}
    def game_loop():
        if key_up():
            set_bg_color(rand()%10, rand()%10, NamedColor.lightsalmon);
    \endcode

    The previous way will have an action executed at each
    frame of the game if the key stays pressed. This
    could be cumbersome for some games and you may want
    a key press to be triggered with a cooldown (so
    that it activates only every so many frames). You can
    configure how many frames will pass between two
    activations of the key with keyUpSetupFire() and
    you can tell whether it is a fire frame with
    keyUpFire(). There are similar functions for all
    keys that are recognized by Bridges. See the
    following code for a simple usage:
    
    \code{.py}
    def initialize() override:
         keyUpSetupFire(20); 

    gameLoop():
         if (keyUpFire()): # will only be true once every 20 frames
              setBGColor(rand()%10, rand()%10, NamedColor.lightsalmon);
    \endcode      
    Bridges supports a third way to use inputs that
    enables you to know the first frame a key is
    pressed and the first frame a key is no longer
    pressed. You can also know whether a key is still
    being pressed (after the first frame it is being
    pressed) and whether it is still not pressed (after
    the first frame it is no longer pressed). The four
    functions are keyUpJustPressed(),
    keyUpStillPressed(), keyUpJustNotPressed(),
    keyUpStillNotPressed(). The following code
    examplifies the usage of these functions.
   
    \code{.py}
        gameLoop():
           if (keyUpJustPressed()):
              setBGColor(0, 0, NamedColor.lightsalmon);
           if (keyUpStillPressed()):
              setBGColor(0, 1, NamedColor.lightsalmon);
           if (keyUpJustNotPressed()):
              setBGColor(0, 2, NamedColor.lightsalmon);
           if (keyUpStillNotPressed()):
              setBGColor(0, 3, NamedColor.lightsalmon);
    \endcode  

    @author Erik Saule
    @date 7-21-19, 1-12-23

    \sa NonBlockingGame tutorial at: https://bridgesuncc.github.io/tutorials/NonBlockingGame.html
    """
    def __init__(self, assid, login, apikey, rows, cols, debug=False):
        super(NonBlockingGame, self).__init__(assid, login, apikey, rows, cols, debug)
        if cols*rows > 1024:
            print("ERROR: Number of cells in a non-blocking game grid cannot exceed 32x32 or 1024.")
            exit(1)
				
        self.time_of_last_frame = int(round(time.time() * 1000))
        self.ih = InputHelper()
        self.register_keypress(self.ih)

        self.upSM = InputStateMachine(lambda:self.ih.up())
        self.downSM = InputStateMachine(lambda:self.ih.down())
        self.leftSM = InputStateMachine(lambda:self.ih.left())
        self.rightSM = InputStateMachine(lambda:self.ih.right())

        self.qSM = InputStateMachine(lambda:self.ih.q())
        self.spaceSM = InputStateMachine(lambda:self.ih.space())

        self.wSM = InputStateMachine(lambda:self.ih.w())
        self.aSM = InputStateMachine(lambda:self.ih.a())
        self.sSM = InputStateMachine(lambda:self.ih.s())
        self.dSM = InputStateMachine(lambda:self.ih.d())
        
        self._fps = 30

    def __update_input_state(self):
        self.upSM.update()
        self.downSM.update()
        self.leftSM.update()
        self.rightSM.update()

        self.qSM.update()
        self.spaceSM.update()

        self.wSM.update()
        self.aSM.update()
        self.sSM.update()
        self.dSM.update()
        
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
            time.sleep(timems/1000)
        except InterruptedError:
            quit()

    def control_framerate(self):
        hz = 1./self._fps

        current_time = int(round(time.time() * 1000))
        theoretical_next_frame = self.time_of_last_frame + int(hz*1000)
        wait_time = theoretical_next_frame-current_time

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

            self.render()

            self.initialize()

            self.game_started = True

            while self.game_started:
                self.__update_input_state()
                self.game_loop()
                self.render()
                self.control_framerate()
                frame = frame + 1
                if (framelimit and frame > framelimit):
                    print ("frame limit of "+ str(framelimit) +" frames reached")
                    self.quit()
        except:
            self.close()
            raise
        
        self.close()

    def key_left(self):
        """
        Is 'left' arrow key currently pressed?
        Returns:
            true if 'left' arrow key is currently pressed
        """
        return self.ih.left()


    def key_left_just_pressed(self):
        """
        indicates whether the Left key has just been pressed this current frame
        """
        return self.leftSM.just_pressed()
    
    def key_left_still_pressed(self):
        """
        indicates whether the Left key is still being  pressed this current frame
        """
        return self.leftSM.still_pressed()

    def key_left_just_not_pressed(self):
        """
        indicates whether the Left key has just been released this current frame
        """
        return self.leftSM.just_not_pressed()

    def key_left_still_not_pressed(self):
        """
        indicates whether the Left key is not pressed and has not been pressed for more than a frame
        """
        return self.leftSM.still_not_pressed()

    def key_left_fire(self):
        """
        indicates whether the current frame is a fire frame for the Left key
        """
        return self.leftSM.fire()
    
    def key_left_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.leftSM.set_fire_cooldown(f)
        

    
    def key_right(self):
        """
        Is 'right' arrow  currently pressed?
        Returns:
            true if 'right' arrow key is currently pressed
        """
        return self.ih.right()


    def key_right_just_pressed(self):
        """
        indicates whether the Right key has just been pressed this current frame
        """
        return self.rightSM.just_pressed()
    
    def key_right_still_pressed(self):
        """
        indicates whether the Right key is still being  pressed this current frame
        """
        return self.rightSM.still_pressed()

    def key_right_just_not_pressed(self):
        """
        indicates whether the Right key has just been released this current frame
        """
        return self.rightSM.just_not_pressed()

    def key_right_still_not_pressed(self):
        """
        indicates whether the Right key is not pressed and has not been pressed for more than a frame
        """
        return self.rightSM.still_not_pressed()

    def key_right_fire(self):
        """
        indicates whether the current frame is a fire frame for the Right key
        """
        return self.rightSM.fire()
    
    def key_right_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.rightSM.set_fire_cooldown(f)
        

    
    def key_up(self):
        """
        Is 'up' arrow currently pressed?
        Returns:
            true if 'up' arrow key is currently pressed
        """
        return self.ih.up()

    def key_up_just_pressed(self):
        """
        indicates whether the Up key has just been pressed this current frame
        """
        return self.upSM.just_pressed()
    
    def key_up_still_pressed(self):
        """
        indicates whether the Up key is still being  pressed this current frame
        """
        return self.upSM.still_pressed()

    def key_up_just_not_pressed(self):
        """
        indicates whether the Up key has just been released this current frame
        """
        return self.upSM.just_not_pressed()

    def key_up_still_not_pressed(self):
        """
        indicates whether the Up key is not pressed and has not been pressed for more than a frame
        """
        return self.upSM.still_not_pressed()

    def key_up_fire(self):
        """
        indicates whether the current frame is a fire frame for the Up key
        """
        return self.upSM.fire()
    
    def key_up_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.upSM.set_fire_cooldown(f)
        
    def key_down(self):
        """
        Is 'down' arrow key currently pressed?
        Returns:
            true if 'down' arrow key is currently pressed
        """
        return self.ih.down()


    def key_down_just_pressed(self):
        """
        indicates whether the Down key has just been pressed this current frame
        """
        return self.downSM.just_pressed()
    
    def key_down_still_pressed(self):
        """
        indicates whether the Down key is still being  pressed this current frame
        """
        return self.downSM.still_pressed()

    def key_down_just_not_pressed(self):
        """
        indicates whether the Down key has just been released this current frame
        """
        return self.downSM.just_not_pressed()

    def key_down_still_not_pressed(self):
        """
        indicates whether the Down key is not pressed and has not been pressed for more than a frame
        """
        return self.downSM.still_not_pressed()

    def key_down_fire(self):
        """
        indicates whether the current frame is a fire frame for the Down key
        """
        return self.downSM.fire()
    
    def key_down_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.downSM.set_fire_cooldown(f)
        

    
    def key_q(self):
        """
        Is 'q' currently pressed?
        Returns:
            true if 'q' is currently pressed
        """
        return self.ih.q()


    def key_q_just_pressed(self):
        """
        indicates whether the Q key has just been pressed this current frame
        """
        return self.qSM.just_pressed()
    
    def key_q_still_pressed(self):
        """
        indicates whether the Q key is still being  pressed this current frame
        """
        return self.qSM.still_pressed()

    def key_q_just_not_pressed(self):
        """
        indicates whether the Q key has just been released this current frame
        """
        return self.qSM.just_not_pressed()

    def key_q_still_not_pressed(self):
        """
        indicates whether the Q key is not pressed and has not been pressed for more than a frame
        """
        return self.qSM.still_not_pressed()

    def key_q_fire(self):
        """
        indicates whether the current frame is a fire frame for the Q key
        """
        return self.qSM.fire()
    
    def key_q_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.qSM.set_fire_cooldown(f)
        

    
    def key_space(self):
        """
        Is 'space' key currently pressed?
        Returns:
            true if 'space' key is currently pressed
        """
        return self.ih.space()


    def key_space_just_pressed(self):
        """
        indicates whether the Space key has just been pressed this current frame
        """
        return self.spaceSM.just_pressed()
    
    def key_space_still_pressed(self):
        """
        indicates whether the Space key is still being  pressed this current frame
        """
        return self.spaceSM.still_pressed()

    def key_space_just_not_pressed(self):
        """
        indicates whether the Space key has just been released this current frame
        """
        return self.spaceSM.just_not_pressed()

    def key_space_still_not_pressed(self):
        """
        indicates whether the Space key is not pressed and has not been pressed for more than a frame
        """
        return self.spaceSM.still_not_pressed()

    def key_space_fire(self):
        """
        indicates whether the current frame is a fire frame for the Space key
        """
        return self.spaceSM.fire()
    
    def key_space_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.spaceSM.set_fire_cooldown(f)
        

    
    def key_w(self):
        """
        Is 'w' currently pressed?
        Returns:
            true if 'w' is currently pressed
        """
        return self.ih.w()


    def key_w_just_pressed(self):
        """
        indicates whether the W key has just been pressed this current frame
        """
        return self.wSM.just_pressed()
    
    def key_w_still_pressed(self):
        """
        indicates whether the W key is still being  pressed this current frame
        """
        return self.wSM.still_pressed()

    def key_w_just_not_pressed(self):
        """
        indicates whether the W key has just been released this current frame
        """
        return self.wSM.just_not_pressed()

    def key_w_still_not_pressed(self):
        """
        indicates whether the W key is not pressed and has not been pressed for more than a frame
        """
        return self.wSM.still_not_pressed()

    def key_w_fire(self):
        """
        indicates whether the current frame is a fire frame for the W key
        """
        return self.wSM.fire()
    
    def key_w_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.wSM.set_fire_cooldown(f)
        

    
    def key_a(self):
        """
        Is 'a' currently pressed?
        Returns:
            true if 'a' is currently pressed
        """
        return self.ih.a()

    def key_a_just_pressed(self):
        """
        indicates whether the A key has just been pressed this current frame
        """
        return self.aSM.just_pressed()
    
    def key_a_still_pressed(self):
        """
        indicates whether the A key is still being  pressed this current frame
        """
        return self.aSM.still_pressed()

    def key_a_just_not_pressed(self):
        """
        indicates whether the A key has just been released this current frame
        """
        return self.aSM.just_not_pressed()

    def key_a_still_not_pressed(self):
        """
        indicates whether the A key is not pressed and has not been pressed for more than a frame
        """
        return self.aSM.still_not_pressed()

    def key_a_fire(self):
        """
        indicates whether the current frame is a fire frame for the A key
        """
        return self.aSM.fire()
    
    def key_a_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.aSM.set_fire_cooldown(f)

    
    def key_s(self):
        """
        Is 's' key currently pressed?
        Returns:
            true if 's' is currently pressed
        """
        return self.ih.s()

    def key_s_just_pressed(self):
        """
        indicates whether the S key has just been pressed this current frame
        """
        return self.sSM.just_pressed()
    
    def key_s_still_pressed(self):
        """
        indicates whether the S key is still being  pressed this current frame
        """
        return self.sSM.still_pressed()

    def key_s_just_not_pressed(self):
        """
        indicates whether the S key has just been released this current frame
        """
        return self.sSM.just_not_pressed()

    def key_s_still_not_pressed(self):
        """
        indicates whether the S key is not pressed and has not been pressed for more than a frame
        """
        return self.sSM.still_not_pressed()

    def key_s_fire(self):
        """
        indicates whether the current frame is a fire frame for the S key
        """
        return self.sSM.fire()
    
    def key_s_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.sSM.set_fire_cooldown(f)

    
    def key_d(self):
        """
        Is 'd' key  currently pressed?
        Returns:
            true 'd' is currently pressed
        """
        return self.ih.d()

    def key_d_just_pressed(self):
        """
        indicates whether the D key has just been pressed this current frame
        """
        return self.dSM.just_pressed()
    
    def key_d_still_pressed(self):
        """
        indicates whether the D key is still being  pressed this current frame
        """
        return self.dSM.still_pressed()

    def key_d_just_not_pressed(self):
        """
        indicates whether the D key has just been released this current frame
        """
        return self.dSM.just_not_pressed()

    def key_d_still_not_pressed(self):
        """
        indicates whether the D key is not pressed and has not been pressed for more than a frame
        """
        return self.dSM.still_not_pressed()

    def key_d_fire(self):
        """
        indicates whether the current frame is a fire frame for the D key
        """
        return self.dSM.fire()
    
    def key_d_setup_fire(self, f: int):
        """
        @param f how many frames between two fire events
        """
        return self.dSM.set_fire_cooldown(f)
