from bridges.non_blocking_game import *
from bridges.named_color import *
from bridges.named_symbol import *
import random


class BugStomp(NonBlockingGame):
    board_size = [20, 20]
    loc = [0, 0]
    bugtt1 = 100
    score = 0
    bug = []

    def __init__(self, assid, login, apikey, c, r):
        super(BugStomp, self).__init__(assid, login, apikey, c, r)

        self.set_title("BUG STOMP")
        self.set_description("Use the arrow keys to move the person over the bugs - don't let them escape!")
        self.start()

    def initialize(self):
        self.bug_color = random.choice(list(NamedColor))
        for i in range(0, BugStomp.board_size[0]):
            for j in range(0, BugStomp.board_size[1]):
                self.set_bg_color(i, j, NamedColor.cyan)
                self.draw_object(i, j, NamedSymbol.none, NamedColor.burlywood)

        self.bug = [BugStomp.board_size[0] / 2, BugStomp.board_size[1] / 2]

    def handle_input(self):
        if self.key_left():
            self.loc[1] -= 1
        if self.key_right():
            self.loc[1] += 1
        if self.key_up():
            self.loc[0] -= 1
        if self.key_down():
            self.loc[0] += 1

        if self.loc[0] < 1:
            self.loc[0] = 1
        if self.loc[0] > self.board_size[0] -1:
            self.loc[0] = self.board_size[0] -1
        if self.loc[1] < 0:
            self.loc[1] = 0
        if self.loc[1] > self.board_size[1] -1:
            self.loc[1] = self.board_size[1] -1

    def handle_bug(self):
        if self.bugtt1 < 1:
            self.bug = [random.randint(0, self.board_size[0]-1), random.randint(0, self.board_size[1]-1)]
            self.bugtt1 = random.randint(0, 100-50) + 50
            self.bug_color = random.choice(list(NamedColor))
            self.score -= 1
            if self.score < 0:
                self.score = 0
        else:
            self.bugtt1 -= 1
            if self.overlap(self.bug, self.loc):
                self.bug = [random.randint(0, self.board_size[0]-1), random.randint(0, self.board_size[1]-1)]
                self.bug_color = random.choice(list(NamedColor))
                self.score += 1

    def overlap(self, bug, loc):
        return abs(bug[0] - loc[0]) < 2 and abs(bug[1] - loc[1]) < 2

    def paint_screen(self):
        for i in range(0, self.board_size[0]):
            for j in range(0, self.board_size[1]):
                self.set_bg_color(i, j, NamedColor.crimson)
                self.draw_object(i, j, NamedSymbol.none, NamedColor.cyan)

        if self.score >= 10:
            self.win()
            return

        self.paint_score(self.score)
        self.draw_object(int(self.bug[0]), int(self.bug[1]), NamedSymbol.bug1, NamedColor.cyan)

        self.draw_object(self.loc[0], self.loc[1], NamedSymbol.man, NamedColor.cyan)

    def win(self):
        self.draw_object(0, 0, NamedSymbol.A, NamedColor.cyan)
        self.draw_object(0, 1, NamedSymbol.B, NamedColor.cyan)
        self.draw_object(0, 2, NamedSymbol.B, NamedColor.cyan)
        self.draw_object(0, 3, NamedSymbol.B, NamedColor.cyan)
        self.draw_object(0, 4, NamedSymbol.B, NamedColor.cyan)
        self.draw_object(0, 5, NamedSymbol.B, NamedColor.cyan)
        self.draw_object(0, 6, NamedSymbol.B, NamedColor.cyan)
        self.draw_object(0, 7, NamedSymbol.B, NamedColor.cyan)

    def paint_score(self, score):
        self.draw_object(0, 0, NamedSymbol.S, NamedColor.black)
        self.draw_object(0, 1, NamedSymbol.C, NamedColor.black)
        self.draw_object(0, 2, NamedSymbol.O, NamedColor.black)
        self.draw_object(0, 3, NamedSymbol.R, NamedColor.black)
        self.draw_object(0, 4, NamedSymbol.E, NamedColor.black)
        self.draw_object(0, 6, NamedSymbol.B, NamedColor.black)

    def game_loop(self):
        if self.score >= 10:
            exit(0)
        self.handle_bug()
        self.handle_input()
        self.paint_screen()


if __name__ == "__main__":
    t = BugStomp(0, 'test', '988181220044', BugStomp.board_size[0], BugStomp.board_size[1])