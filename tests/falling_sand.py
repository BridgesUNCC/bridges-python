import random

from bridges import *


class FallingSand(NonBlockingGame):
    gridColumns = 30
    gridRows = 30

    CURSOR = 1
    EMPTY = 0
    METAL = 1
    SAND = 2
    WATER = 3
    DELETE = 4

    emptyColor = NamedColor.white
    metalColor = NamedColor.gray
    sandColor = NamedColor.sandybrown
    waterColor = NamedColor.blue
    deleteColor = NamedColor.red
    cursorColor = NamedColor.orange

    emptySymbol = NamedSymbol.none
    metalSymbol = NamedSymbol.square
    sandSymbol = NamedSymbol.waves
    waterSymbol = NamedSymbol.rain
    cursorSymbol = NamedSymbol.circle

    cursorCell = [10, 10]

    def water_behavior(self, col, row):
        randomDirection = int(random.randrange(2))

        if row < self.gridRows - 1:
            if self.container[col][row + 1] == self.EMPTY:
                self.clear_element(col, row)
                self.place_element(self.WATER, col, row + 1)
            elif col > 0 and col < self.gridColumns - 1:
                if self.container[col - 1][row] == self.EMPTY and self.container[col + 1][row] == self.EMPTY:
                    if randomDirection == 0:
                        self.clear_element(col, row)
                        self.place_element(self.WATER, col - 1, row)
                    else:
                        self.clear_element(col, row)
                        self.place_element(self.WATER, col + 1, row)
                elif self.container[col - 1][row] == self.EMPTY:
                    self.clear_element(col, row)
                    self.place_element(self.WATER, col - 1, row)
                elif self.container[col + 1][row] == self.EMPTY:
                    self.clear_element(col, row)
                    self.place_element(self.WATER, col + 1, row)

    def sand_behavior(self, col, row):
        if row < self.gridRows - 1:
            if self.container[col][row + 1] == self.WATER:
                self.place_element(self.WATER, col, row)
                self.place_element(self.SAND, col, row + 1)
            if self.container[col][row + 1] == self.EMPTY:
                self.clear_element(col, row)
                self.place_element(self.SAND, col, row + 1)

    def game_loop(self):
        self.controls()
        self.paint_board()

        for col in range(self.gridColumns):
            for row in range(self.gridRows - 1, 0, -1):
                if self.container[col][row] == self.WATER:
                    self.water_behavior(col, row)
                elif self.container[col][row] == self.SAND:
                    self.sand_behavior(col, row)

    def initialize(self):
        self.emptyColor = NamedColor.white
        self.metalColor = NamedColor.gray
        self.sandColor = NamedColor.sandybrown
        self.waterColor = NamedColor.blue
        self.deleteColor = NamedColor.red
        self.cursorColor = NamedColor.orange

        self.emptySymbol = NamedSymbol.none
        self.metalSymbol = NamedSymbol.square
        self.sandSymbol = NamedSymbol.waves
        self.waterSymbol = NamedSymbol.rain
        self.cursorSymbol = NamedSymbol.circle

        self.cursorCell[0] = 10
        self.cursorCell[1] = 10
        self.paint_board()

    def new_game(self):
        self.container = [[0 for i in range(self.gridColumns)] for j in range(self.gridRows)]
        self.cursorOverlay = [[0 for i in range(self.gridColumns)] for j in range(self.gridRows)]

        self.initialize()

        for col in range(self.gridColumns):
            for row in range(self.gridRows):
                if self.container[col][row] == self.WATER:
                    self.water_behavior(col, row)
                if self.container[col][row] == self.METAL:
                    self.sand_behavior(col, row)

    def place_cursor(self, col, row):
        self.cursorOverlay[col][row] = self.CURSOR

    def clear_cursor(self, col, row):
        self.cursorOverlay[col][row] = self.EMPTY

    def place_element(self, element, col, row):
        self.container[col][row] = element

    def clear_element(self, col, row):
        self.container[col][row] = self.EMPTY

    def get_element(self, col, row):
        return self.container[col][row]

    def get_cursor(self, col, row):
        return self.cursorOverlay[col][row]

    def paint_board(self):
        for col in range(self.gridColumns):
            for row in range(self.gridRows):
                if self.container[col][row] == self.SAND:
                    self.draw_symbol(row, col, self.sandSymbol, self.sandColor)
                if self.container[col][row] == self.WATER:
                    self.draw_symbol(row, col, self.waterSymbol, self.waterColor)
                if self.container[col][row] == self.METAL:
                    self.draw_symbol(row, col, self.metalSymbol, self.metalColor)
                if self.container[col][row] == self.EMPTY:
                    self.draw_symbol(row, col, self.emptySymbol, self.emptyColor)

                if self.cursorOverlay[col][row] == self.CURSOR:
                    self.draw_symbol(row, col, self.cursorSymbol, self.cursorColor)

    def controls(self):
        self.clear_cursor(self.cursorCell[0], self.cursorCell[1])

        if self.key_a():
            self.cursorColor = self.metalColor
            self.CURSOR = self.METAL
        if self.key_w():
            self.cursorColor = self.waterColor
            self.CURSOR = self.WATER
        if self.key_s():
            self.cursorColor = self.sandColor
            self.CURSOR = self.SAND
        if self.key_d():
            self.cursorColor = self.deleteColor
            self.CURSOR = self.DELETE

        if self.key_left() and self.cursorCell[0] > 0:
            self.cursorCell[0] = self.cursorCell[0] - 1
        if self.key_right() and self.cursorCell[0] < self.gridColumns - 1:
            self.cursorCell[0] = self.cursorCell[0] + 1
        if self.key_up() and self.cursorCell[1] > 0:
            self.cursorCell[1] = self.cursorCell[1] - 1
        if self.key_down() and self.cursorCell[1] < self.gridRows - 1:
            self.cursorCell[1] = self.cursorCell[1] + 1

        if self.key_q():
            self.new_game()
        if self.key_space():

            if self.CURSOR == self.DELETE:
                self.clear_element(self.cursorCell[0], self.cursorCell[1])
            else:
                print(self.cursorCell)
                self.place_element(self.CURSOR, self.cursorCell[0], self.cursorCell[1])

        self.place_cursor(self.cursorCell[0], self.cursorCell[1])

    def __init__(self, assid, login, apikey, cols, rows):
        super(FallingSand, self).__init__(assid, login, apikey, cols, rows)

        super(FallingSand, self).set_title("Falling Sand")
        super(FallingSand, self).set_description("Simulate sand and water interactions.")

        self.container = [[0 for i in range(self.gridColumns)] for j in range(self.gridRows)]
        self.cursorOverlay = [[0 for i in range(self.gridColumns)] for j in range(self.gridRows)]

        self.container[5][10] = 1
        self.container[5][11] = 1
        self.container[5][12] = 1
        self.container[6][12] = 1
        self.container[7][12] = 1
        self.container[8][12] = 1
        self.container[8][11] = 1
        self.container[8][10] = 1
        self.container[8][9] = 1


def main():
    my_game = FallingSand(215, "test", "137842425086", 30, 30)
    my_game.start()


if __name__ == '__main__':
    main()