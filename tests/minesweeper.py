from bridges import *

import random
from datetime import datetime


class Cell(object):
    # Represents on cell of a minesweeper game
    position = [0, 0]
    has_mine = False
    shown = False
    number = 0
    flagged = False

    def __init__(self, position):
        self.position = position


class Minesweeper(NonBlockingGame):
    # The cursor is used to select cells
    cursor = [0, 0]
    mines_count = 10
    key_pressed = False
    cells = []

    numbers = [NamedSymbol.none, NamedSymbol.one, NamedSymbol.two, NamedSymbol.three, NamedSymbol.four,
               NamedSymbol.five, NamedSymbol.six, NamedSymbol.seven, NamedSymbol.eight, NamedSymbol.nine]

    number_colors = [NamedColor.floralwhite, NamedColor.blue, NamedColor.green, NamedColor.darkred, NamedColor.darkblue,
                     NamedColor.darkred, NamedColor.cadetblue, NamedColor.black, NamedColor.blue, NamedColor.blue]

    directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

    def __init__(self, assid, login, apikey):
        super(Minesweeper, self).__init__(assid, login, apikey, 10, 10)

    def initialize(self):
        self.set_title("Minesweeper")
        self.set_description("Controls -\nArrow Keys: Move\nSpace: Click\nQ: Restart\nS: Flag")

        self.cursor = [10 // 2, 10 // 2]

        for y in range(10):
            for x in range(10):
                self.cells.append(Cell([x, y]))

        self.restart()

    def restart(self):
        random.seed(datetime.now())

        # Reset all cells
        for cell in self.cells:
            cell.shown = False
            cell.has_mine = False
            cell.number = 0
            cell.flagged = False

        # Place the mines until the max is reached
        mines_placed = 0
        while mines_placed < self.mines_count:
            r = random.randint(0, len(self.cells) - 1)
            if not self.cells[r].has_mine:
                self.cells[r].has_mine = True
                mines_placed += 1

        # Set the numbers for surrounding cells at each mine
        for cell in self.cells:
            for d in self.directions:
                n = [cell.position[0] + d[0], cell.position[1] + d[1]]

                if n[0] < 0 or n[0] > 10 - 1 or n[1] < 0 or n[1] > 10 - 1:
                    continue

                if self.cells[n[0] + n[1] * 10].has_mine:
                    cell.number += 1

    def show_all(self):
        # Reveal all cell
        for cell in self.cells:
            cell.shown = True

    def is_game_key_pressed(self):
        # Return true if any key used in this game is pressed
        return self.key_right() or self.key_left() or self.key_up() or self.key_down() or self.key_s() or self.key_space() or self.key_q()

    def handle_input(self):
        if not self.is_game_key_pressed():
            self.key_pressed = False

        # Only take input once until released and pressed again
        if not self.key_pressed:
            h_input = int(self.key_right()) - int(self.key_left())
            v_input = int(self.key_down()) - int(self.key_up())

            self.cursor[0] = min(10 - 1, max(self.cursor[0] + h_input, 0))
            self.cursor[1] = min(10 - 1, max(self.cursor[1] + v_input, 0))

            if self.key_s():
                self.cells[self.cursor[0] + self.cursor[1] * 10].flagged = not self.cells[
                    self.cursor[0] + self.cursor[1] * 10].flagged

            if self.key_space():
                if not self.cells[self.cursor[0] + self.cursor[1] * 10].flagged:
                    self.show_cell(self.cursor)

            if self.key_q():
                self.restart()
                return

        if self.is_game_key_pressed():
            self.key_pressed = True

    def show_cell(self, pos):
        # Show a single cell and open surrounding cells with no surrounding bombs
        current = self.cells[pos[0] + pos[1] * 10]
        current.shown = True

        if current.has_mine:
            self.show_all()

        if current.number == 0:
            for d in self.directions:
                n = [current.position[0] + d[0], current.position[1] + d[1]]

                if n[0] < 0 or n[0] > 10 - 1 or n[1] < 0 or n[1] > 10 - 1:
                    continue

                neighbor = self.cells[n[0] + n[1] * 10]

                if neighbor.shown:
                    continue

                neighbor.shown = True

                if neighbor.number == 0:
                    self.show_cell(n)

    def check_win(self):
        # Check if all cells that are not bombs are revealed
        count = 0
        for cell in self.cells:
            if cell.shown:
                count += 1

        if len(self.cells) - count <= self.mines_count:
            self.show_all()

    def draw(self):
        for cell in self.cells:
            self.set_bg_color(cell.position[1], cell.position[0], NamedColor.gray)
            if cell.shown:
                if cell.has_mine:
                    self.draw_symbol(cell.position[1], cell.position[0], NamedSymbol.bomb, NamedColor.black)
                else:
                    self.draw_symbol(cell.position[1], cell.position[0], self.numbers[cell.number],
                                     self.number_colors[cell.number])
            elif cell.flagged:
                self.draw_symbol(cell.position[1], cell.position[0], NamedSymbol.flag, NamedColor.darkred)
            else:
                self.draw_symbol(cell.position[1], cell.position[0], NamedSymbol.square, NamedColor.darkgray)

        self.set_bg_color(self.cursor[1], self.cursor[0], NamedColor.gold)

    def game_loop(self):
        self.handle_input()
        self.draw()
        self.check_win()


def main():
    game = Minesweeper(220, "test", "137842425086")

    # Start the game
    game.start()


if __name__ == '__main__':
    main()