from bridges import *


class Connect4(NonBlockingGame):

    def __init__(self, assID, username, apikey):
        super(Connect4, self).__init__(assID, username, apikey, 7 ,7)
        #key frames to process events
        self.frames = 0
        self.key_frames = 10

    def initialize(self):
        """
        initialize the board, symbols, symbol colors and background colors
		might want to draw the top row in a different color
		draw the start symbol
        """
        pass

    def game_loop(self):
        #make move and update the screen
        self.frames += 1
        if(not (self.frames%self.key_frames)):
            self.make_move()

    def make_move(self):
        """
        left or right moves the piece in the top row to choose
		a column to drop it
		use appropriate keys and ensure you dont go off the board
        """
        pass

    def draw_board(self):
        #draw the board
        pass

    def game_over(self, curr_row, curr_col):
        """
        must check for 4 disks of same color across row,
		column and diagonals containing the last move

		note that the last move might caused a winner, so only need to
		check cases where that move is part of the winning row, column or diagonal

		the following is only to avoid a warning from the compiler:
        """
        return False

    def print_message(self):
        #when a winner is found, print a winning message on the board
        pass

def main():
    connect = Connect4(132, "BRIDGES_USER_ID", "BRIDGES_API_KEY")
    connect.start()

if __name__ == '__main__':
    main()