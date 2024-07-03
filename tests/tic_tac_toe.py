from bridges import *
import time

class TicTacToe(NonBlockingGame):

    def __init__(self, assid, login, apikey):
        super(TicTacToe, self).__init__(assid, login, apikey, 3, 3, True)
        self.frame = 0
        self.flag = True
        self.counters = [0, 0, 0, 0]
        self.board = []
        self.board_bg_col = []


    def initialize(self):
        self.xsize = self.board_width
        self.ysize = self.board_height
        self.curr_x = 1
        self.curr_y = 1
        for i in range(self.ysize):
            self.board.append([])
            self.board_bg_col.append([])
            for j in range(self.xsize):
                self.board[i].append(NamedSymbol.none)
                self.board_bg_col[i].append(NamedColor.ivory)
        self.draw_board()

    def game_loop(self):
        # self.flag = True
        self.frame += 1
        if self.frame == 0:
            self.frame += 1
            return

        sym = NamedSymbol.X if self.flag else NamedSymbol.O

        if self.flag:
            self.set_title("Player A (O) move..")
        else:
            self.set_title("Player B (X) move..")

        if self.make_move(sym):
            if self.game_over():
                return
            self.flag = not self.flag

    def check_move(self, move):
        if not move.isdigit():
            print("Plese enter an integer")
            return False

        i = int(move)

        if i < 1 or i > 9:
            print("Illegal Move : %d must be in the range (1-9), you lost your move" % i)
            return False
        elif self.board[i - 1]:
            print("Illegal Move : Space %d is already occupied! You lost your move!" % i)
            return False

        return True

    def make_move(self, sym):
        if self.key_up() and self.curr_y > 0:
            if(not self.counters[0]):
                self.curr_y -= 1
                self.counters[0] = 1
            else:
                self.counters[0] -= 1
        if self.key_down() and self.curr_y < self.ysize-1:
            if(not self.counters[1]):
                self.curr_y += 1
                self.counters[1] = 1
            else:
                self.counters[1] -= 1
        if self.key_right() and self.curr_x < self.xsize-1:
            if(not self.counters[2]):
                self.curr_x += 1
                self.counters[2] = 1
            else:
                self.counters[2] -= 1
        if self.key_left() and self.curr_x > 0:
            if(not self.counters[3]):
                self.curr_x -= 1
                self.counters[3] = 1
            else:
                self.counters[3] -= 1
        if self.key_space():
            if self.get_symbol(self.curr_y, self.curr_x) is NamedSymbol.none:
                self.board[self.curr_y][self.curr_x ] = sym
                print(sym)
                self.draw_board()

                return 1

        self.draw_board()

        return 0

    def draw_board(self):
        for i in range(self.ysize):
            for j in range(self.xsize):
                self.set_bg_color(i, j, self.board_bg_col[i][j])
                self.draw_symbol(i, j, self.board[i][j], NamedColor.red)
        self.set_bg_color(self.curr_y, self.curr_x, NamedColor.orange)

    def clear_board(self):
        for i in range(self.board_width):
            for j in range(self.board_height):
                self.set_bg_color(i, j, NamedColor.ivory)
                self.draw_symbol(i, j, NamedSymbol.none, NamedColor.ivory)

    def game_over(self):
        s = NamedSymbol.X
        if self.check_row(0, s) or self.check_row(1, s) or self.check_row(2, s) or self.check_column(0,
                                                                                                     s) or self.check_column(
                1, s) or self.check_column(2, s) or self.check_diags(s):
            self.curr_x=1
            self.curr_y=0
            self.print_message(s)
            return True

        a = NamedSymbol.O
        if self.check_row(0, a) or self.check_row(1, a) or self.check_row(2, a) or self.check_column(0,
                                                                                                     a) or self.check_column(
                1, a) or self.check_column(2, a) or self.check_diags(a):
            self.curr_x = 1
            self.curr_y = 0
            self.print_message(a)
            return True

        return False

    def check_row(self, r, s):
        return self.get_symbol(0, r) == s and self.get_symbol(1, r) == s and self.get_symbol(2, r) == s

    def check_column(self, c, s):
        return self.get_symbol(c, 0) == s and self.get_symbol(c, 1) == s and self.get_symbol(c, 2) == s

    def check_diags(self, s):

        return (self.get_symbol(0, 0) == s and self.get_symbol(1, 1) == s and self.get_symbol(2, 2) == s) or (
                    self.get_symbol(2, 0) == s and self.get_symbol(1, 1) == s and self.get_symbol(0, 2) == s)

    def print_message(self,s):
        for i in range(self.ysize):
            for j in range(self.xsize):
                self.board[i][j] = NamedSymbol.none
                self.board_bg_col[i][j] = NamedColor.ivory
        self.board[0][1] = s
        self.board[2][0] = NamedSymbol.w
        self.board[2][1] = NamedSymbol.o
        self.board[2][2] = NamedSymbol.n

        self.draw_board()
        self.quit()

def main():
    game = TicTacToe(32, "test", "988181220044")


    game.set_title("TicTacToe")
    game.start()

if __name__ == '__main__':
    main()