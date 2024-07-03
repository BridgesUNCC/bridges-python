from bridges import *


class Connect4(NonBlockingGame):

    def __init__(self, assID, username, apikey):
        super(Connect4, self).__init__(assID, username, apikey, 7 ,7)
        #attributes of the connect 4 game
        self.board_symbols = []
        self.board_symbols_col = []
        self.board_bg_color = []
        #key frames to process events
        self.frames = 0
        self.key_frames = 10
        #position of disk
        self.curr_x = 0
        self.curr_y = 0
        self.player = False
        #board size
        self.xsize = 0
        self.ysize = 0

        #keep track of disks in columns
        self.counters = [0, 0, 0, 0, 0, 0, 0]

        self.bcnt = 0
        self.rcnt = 0

    def initialize(self):
        #curr position of the disk

        self.xsize = self.board_width
        self.ysize = self.board_height

        self.set_title("game")


        #init board
        for i in range(self.board_height):
            self.board_symbols.append([])
            self.board_symbols_col.append([])
            self.board_bg_color.append([])
            for j in range(self.board_width):
                self.board_symbols[i].append(NamedSymbol.none)
                self.board_symbols_col[i].append(NamedColor.white)
                self.board_bg_color[i].append(NamedColor.ivory)

        #top row a different color
        for i in range(self.xsize):
            self.board_bg_color[0][i] = NamedColor.limegreen

        #player = false, red disk ,else blue disk
        #player symbol is in the top left
        self.board_symbols[0][0] = NamedSymbol.circle
        self.board_symbols_col[0][0] = NamedColor.red if self.player else NamedColor.blue

        self.draw_board()

    def game_loop(self):
        #make move and update the screen
        self.frames += 1
        if(not (self.frames%self.key_frames)):
            self.make_move()

    def make_move(self):
        #left or right moves the place in the top row to choose
        #a column to drop it
        #introduce a delay
        if self.key_right() and self.curr_x < self.xsize - 1:
            self.board_symbols[0][self.curr_x] = NamedSymbol.none
            self.curr_x += 1
            self.board_symbols[0][self.curr_x] = NamedSymbol.circle
            self.board_symbols_col[0][self.curr_x] = NamedColor.red if self.player else NamedColor.blue
            self.draw_board()

        if self.key_left() and self.curr_x > 0:
            self.board_symbols[0][self.curr_x] = NamedSymbol.none
            self.curr_x -= 1
            self.board_symbols[0][self.curr_x] = NamedSymbol.circle
            self.board_symbols_col[0][self.curr_x] = NamedColor.red if self.player else NamedColor.blue

            self.draw_board()

        #drop the disk if it is not full
        if self.key_space():
            #update curr position and top row symbol
            col_cnt = self.counters[self.curr_x]
            if col_cnt < self.ysize-1:
                self.board_symbols[0][self.curr_x] = NamedSymbol.none
                self.board_symbols[self.ysize-1-col_cnt][self.curr_x] = NamedSymbol.circle
                self.board_symbols_col[self.ysize-1-col_cnt][self.curr_x] = NamedColor.red if self.player else NamedColor.blue

                #check for a winner, specify the move position, as only
                #that row, column and diagonals will be checked
                if self.game_over(self.ysize-1-col_cnt, self.curr_x):
                    self.print_message()

                self.player = not self.player #move to other player

                #new player symbol moved to top left
                self.board_symbols[0][0] = NamedSymbol.circle
                self.board_symbols_col[0][0] = NamedColor.red if self.player else NamedColor.blue

                #update counters and curr position
                self.counters[self.curr_x] += 1
                self.curr_x = 0

                self.draw_board()

    def draw_board(self):
        for i in range(self.ysize):
            for j in range(self.xsize):
                self.set_bg_color(i, j, self.board_bg_color[i][j])
                self.draw_symbol(i, j, self.board_symbols[i][j], self.board_symbols_col[i][j])

    def game_over(self, curr_row, curr_col):
        #must check for 4 disks of same color across row, column
        #and diagonals containing the last move

        #the move was made on this position
        row = curr_row
        col = curr_col

        self.rcnt = 0
        self.bcnt = 0

        #check row for win
        for j in range(self.xsize):
            if self.check_matches(row, j):
                return True

        #check column
        self.rcnt = 0
        self.bcnt = 0
        for i in range(1, self.ysize):
            if self.check_matches(i, col):
                return True

        #check diagonal: NW --> SE
        #first go to left edge of grid
        r = row
        c = col
        while ((r > 1) and c > 0):
            r -= 1
            c -= 1

        self.rcnt = 0
        self.bcnt = 0
        while (r < self.ysize and c < self.xsize):
            if self.check_matches(r, c):
                return True
            r += 1
            c += 1

        #check diagonal : NE --> SW

        r = row
        c = col
        while (r < self.ysize - 1 and c > 0):
            r += 1
            c -= 1

        self.rcnt = 0
        self.bcnt = 0
        while r > 0 and c < self.xsize:
            if self.check_matches(r, c):
                return True
            print(self.bcnt)
            r -= 1
            c += 1

        return False

    def check_matches(self, row, col):
        #look for a run of 4 disks of same color
        c = self.board_symbols_col[row][col]
        if c is NamedColor.red:
            self.rcnt+=1
            self.bcnt = 0
        elif c is NamedColor.blue:
            self.bcnt+= 1
            self.rcnt = 0
        elif c is NamedColor.white:
            self.bcnt = 0
            self.rcnt = 0
        if self.rcnt is 4:
            self.player = False
            return True
        elif self.bcnt is 4:
            self.player = True
            return True
        return False

    def print_message(self):
        col = NamedColor.blue if self.player else NamedColor.red
        self.board_symbols[0][0] = NamedSymbol.circle
        self.board_symbols[0][1] = NamedSymbol.none
        self.board_symbols[0][2] = NamedSymbol.w
        self.board_symbols[0][3] = NamedSymbol.i
        self.board_symbols[0][4] = NamedSymbol.n
        self.board_symbols[0][5] = NamedSymbol.s
        self.board_symbols_col[0][0] = col
        for k in range(6):
            self.board_symbols_col[0][k] = NamedColor.green
        self.draw_board()

def main():
    connect = Connect4(132, "test", "988181220044")
    connect.start()

if __name__ == '__main__':
    main()