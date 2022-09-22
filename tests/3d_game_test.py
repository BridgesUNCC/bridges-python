from bridges.non_blocking_game3D import *
from bridges.primitives import *
from bridges.data_src_dependent import data_source
from bridges.mesh import *
from bridges.particle_system import *

import math
import json



class TestGame(NonBlockingGame3D):

    def __init__(self, assid, login, apikey):
        super(TestGame, self).__init__(assid, login, apikey)
        self.frame = 0
        self.flag = True
        self.iTime = 0.0


    def initialize(self):
        elev_data = data_source.get_elevation_data([33.394759, -122.299805, 42.747012, -114.916992], 0.2)
        terrain = Terrain_Mesh(elev_data.rows, elev_data.cols, elev_data.data)
        # terrain.rows = elev_data.rows
        # terrain.cols = elev_data.cols
        # terrain.gen_vertices(elev_data.data)


        cube = Primitives('cube', "cube 1")
        cube.set_color("orange")
        cube.position = [0.0, 0.0, 140.0]

        particleSystem = Particle_System('particle system',[0.0, 10.0, 10.0], 200)

        # Opening JSON file
        f = open('objects.json')

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        print(data)

        for i in data['members']:
            object = Primitives(i['type'], i['name'])
            object.set_color("orange")
            self.scene.add(object)

        self.scene.add(cube)
        self.scene.add(terrain)
        self.scene.add(particleSystem)



    def game_loop(self):
        self.iTime += 0.1

        # for i in range(self.scene.get("terr").rows):
        #     for j in range(self.scene.get("terr").cols):
        #         self.scene.get("terr")._vertices[i][j] = math.sin(self.iTime + i + j) * 100

        self.scene.get("cube 1").set_transform(["r", [0.0, 1.0, 0.0], self.iTime])



def main():

    game = TestGame(10, 'test', '988181220044')
    game.set_title("3d scene")
    game.start()



if __name__ == '__main__':
    main()
