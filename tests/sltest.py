import random

from bridges import *


class SpreadingFire(NonBlockingGame):
    gridColumns = 30
    gridRows = 30

    spreadingProbability = 20

    forest_density = 90

    FIRE = 2
    TREE = 1
    EMPTY = 0

    fireColor = NamedColor.red
    treeColor = NamedColor.green
    emptyColor = NamedColor.yellow

    fireSymbol = NamedSymbol.campfire
    treeSymbol = NamedSymbol.triangle_up
    emptySymbol = NamedSymbol.none

    def cell_contains_forest(self, col, row):
        probabilityTest = random.randrange(0, 100)
        nearbyFire = False

        if (col > 0 and self.treeMap[col - 1][row] == 2 or
                col < self.gridColumns - 1 and self.treeMap[col + 1][row] == 2 or
                row > 0 and self.treeMap[col][row - 1] == 2 or
                row < self.gridRows - 1 and self.treeMap[col][row - 1] == 2):
            nearbyFire = True

        if nearbyFire and probabilityTest < self.spreadingProbability:
            self.ignite(col, row)

    def cell_contains_fire(self, col, row):
        prob_test = int(random.randrange(0, 100))
        if (prob_test > self.forest_density):
            self.burn_out(col, row)

    def ignite(self, col, row):
        self.set_bg_color(col, row, self.fireColor)
        self.draw_symbol(col, row, self.fireSymbol, self.fireColor)
        self.treeMap[col][row] = self.FIRE

    def burn_out(self, col, row):
        self.set_bg_color(col, row, self.emptyColor)
        self.draw_symbol(col, row, self.emptySymbol, self.emptyColor)
        self.treeMap[col][row] = self.EMPTY

    def grow_tree(self, col, row):
        self.set_bg_color(col, row, self.treeColor)
        self.draw_symbol(col, row, self.treeSymbol, self.treeColor)
        self.treeMap[col][row] = self.TREE

    def game_loop(self):
        self.check_for_restart_request()
        for i in range(self.gridColumns):
            for j in range(self.gridRows):
                if self.treeMap[i][j] == self.TREE:
                    self.cell_contains_forest(i, j)
                if self.treeMap[i][j] == self.FIRE:
                    self.cell_contains_fire(i, j)
                if self.treeMap[i][j] == self.EMPTY:
                    pass  # Empty

    def initialize(self):
        self.simulation_two()

    def __init__(self, assid, login, apikey, cols, rows):
        super(SpreadingFire, self).__init__(assid, login, apikey, cols, rows)

        super(SpreadingFire, self).set_title("Spreading Fire")
        super(SpreadingFire, self).set_description("Simulation of fire in a forest.")

        self.treeMap = [[0 for i in range(self.gridColumns)] for j in range(self.gridRows)]

    def simulation_one(self):
        self.treeMap = [[0 for i in range(self.gridColumns)] for j in range(self.gridRows)]
        for i in range(self.gridColumns):
            for j in range(self.gridRows):
                if i == int(self.gridColumns / 2) and int(j == self.gridRows / 2):
                    self.ignite(i, j)
                else:
                    self.grow_tree(i, j)
                j += 1
            i += 1

    # Creates a forest within an inner square of empty cells with a fire in the center
    def simulation_two(self):
        self.treeMap = [[0 for i in range(self.gridColumns)] for j in range(self.gridRows)]
        # This grid desplays a full forest with a fire in the center.
        for col in range(self.gridColumns):
            for row in range(self.gridRows):
                if (col == 3 or row == 3 or col == self.gridColumns - 4 or row == self.gridRows - 4):
                    self.burn_out(col, row)
                else:
                    self.grow_tree(col, row)

                if (row == int(self.gridRows / 2) and col == int(self.gridColumns / 2)):
                    self.ignite(col, row)

    def simulation_three(self):
        self.treeMap = [[0 for i in range(self.gridColumns)] for j in range(self.gridRows)]
        # This grid desplays a full forest with a fire in the center.
        for col in range(self.gridColumns):
            for row in range(self.gridRows):
                self.grow_tree(col, row)

                self.burn_out(row, row)
                self.burn_out(row, self.gridRows - (row + 1))

                if (row == 0 and col == self.gridColumns / 2 or
                        col == 0 and row == self.gridRows / 2 or
                        row == self.gridRows - 1 and col == self.gridColumns / 2 or
                        col == self.gridColumns - 1 and row == self.gridRows / 2):
                    self.ignite(col, row)

    def simulation_four(self):
        self.treeMap = [[0 for i in range(self.gridColumns)] for j in range(self.gridRows)]

    def check_for_restart_request(self):
        if (self.key_down()):
            self.simulation_one()

        if (self.key_up()):
            self.simulation_two()

        if (self.key_left()):
            self.simulation_three()

        if (self.key_right()):
            self.simulation_four()


def main():
    my_game = SpreadingFire(214, "test", "988181220044", 30, 30)
    my_game.start()


if __name__ == '__main__':
    main()