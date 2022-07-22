from bridges.non_blocking_game3D import *
from bridges.primitives import *
import time


class TestGame(NonBlockingGame3D):

    def __init__(self, assid, login, apikey):
        super(TestGame, self).__init__(assid, login, apikey)
        self.frame = 0
        self.flag = True
        self.iTime = 0.0

    def initialize(self):

        cube = Primitives('cube', "cube 1")
        cube.set_color("orange")
        cube.position = [0.0, 0.0, 0.0]
        self.scene.add(cube)


    def game_loop(self):
        self.iTime +=1

def main():

    game = TestGame(10, 'test', '988181220044')
    game.set_title("3d scene")
    game.start()



if __name__ == '__main__':
    main()
