from bridges import *

class TicTacToe(NonBlockingGame):
    #need to keep track of occupied positions for the board
    #use a suitable data structure

    #building a 3x3 board
    def __init__(self, assid, login, apikey):
        super(TicTacToe, self).__init__(assid, login, apikey, 3, 3)
        self.frame = 0
        self.flag = True
        #do initializations



    def initialize(self):
        #init the board - you shouldnt have to change this
        for i in range(self.board_height):
            for j in range(self.board_width):
                self.set_bg_color(i, j, NamedColor.ivory)
                self.draw_symbol(i, j, NamedSymbol.none, NamedColor.ivory)

    def game_loop(self):
        #this function is executed each frame of the game
        #this is where all your game logic goes

        """
        skip the first frame, so that you get a link to the server and then
        you can connect to the game on the provided link. You must be logged into
        BRIDGES to see board output and enabled the connection to the server.
        """
        if self.frame == 0:
            self.frame += 1
            return

        sym = NamedSymbol.X if self.flag else NamedSymbol.O

        """
         you will need the moves to alternate between the two symbols

        you need to check for a winner (gameOver() will do that; if a player wins, exit,
        use exit(1) call  - no other graceful way to terminate in the current implementation)

        players need to make a move on the board

        before you make a move, print to console a helpful prompt on what value to enter to
        play, for instance, 1 through 9. Use standard input to receive the values from
        the player

        check the move if it is legal, value outside range, moving into an already occupied
        position, both cases forfeit the move, and the other player makes the next move

        the following call simply illustrates how to draw symbols on the board in a particular
        color; we will draw on positions 1 and 9 (opposite diagonal corners
        Check the GameBase class for complete documentation
        """

        self.draw_symbol(0, 0, NamedSymbol.x, NamedColor.blue)
        self.draw_symbol(2, 2, NamedSymbol.o, NamedColor.red)

    def check_move(self, move):
        """
        checks to see if a legal move was made, check for incorrect input
        and making a move into an occupied position - in both cases the player
        forfeits his/her move
        """
        pass


    def draw_board(self):
        #updates the board with given move
        pass

    def clear_board(self):
        #clears the board (use if needed), use NamedSymbol.none to clear symbol
        pass


    def game_over(self):
        #checks the board to see if a player has won: rows, column, diagonal
        pass


def main():
    #put in your bridges credentials
    game = TicTacToe(32, "BRIDGES_USER_ID", "BRIDGES_API_KEY")

    game.set_title("TicTacToe")
    game.start()

if __name__ == '__main__':
    main()