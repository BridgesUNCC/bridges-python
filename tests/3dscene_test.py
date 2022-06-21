from bridges.bridges import *
from bridges.mesh import *
from bridges.camera import *
from bridges.scene import *
from bridges.primitives import *
from bridges.data_src_dependent import data_source


class MountPath():
	def __init__(self, elev_data):
		self.width = elev_data.cols
		self.height = elev_data.rows
		self.max_val = elev_data.maxVal
		self.data = elev_data.data
		self.sentinel_val = 99999

	def get_val(self, x, y):
	# Return the color of the pixel at x y
		return self.data[int(y)][int(x)]

	def set_val(self, x, y, val):
		# Set the color of the pixel at x, y
		self.data[int(y)][int(x)] = val

def main():

    points = []

    # mesh = Mesh(vertices)

    scene = Scene()
    scene_camera = Camera("fps")

    scene.add(scene_camera)

    bridges = Bridges(300, "test", "988181220044")

    bridges.connector.set_server("local")

    elev_data = data_source.get_elevation_data([33.394759,-122.299805,42.747012,-114.916992], 0.06)
    mnt_path = MountPath(elev_data)
    print(len(elev_data.data))
    for x in range(elev_data.rows-1):
        for y in range(elev_data.cols-1):

            points.append(x)
            points.append(round(elev_data.data[x][y] * 0.005))
            points.append(y)

            points.append(x + 1)
            points.append(round(elev_data.data[x + 1][y + 1] * 0.005))
            points.append(y + 1)

            points.append(x + 1)
            points.append(round(elev_data.data[x + 1][y] * 0.005))
            points.append(y)

            points.append(x)
            points.append(round(elev_data.data[x][y] * 0.005))
            points.append(y)

            points.append(x)
            points.append(round(elev_data.data[x][y + 1] * 0.005))
            points.append(y + 1)

            points.append(x + 1)
            points.append(round(elev_data.data[x + 1][y + 1] * 0.005))
            points.append(y + 1)

    mesh = Mesh(points)
    scene.add(mesh)

    cube = Primitives("cube")
    cube.color = 'green'
    cube.position = [0.0, 0.0, 0.0]
    cube.transform.append(['T', 1.0, 0.0, 0.0])
    cube.transform.append(['R', 0.0, 1.0, 0.0])
    scene.add(cube)

    cube1 = Primitives("cube")
    cube1.color = 'green'
    cube1.position = [0.0, 0.0, 0.0]
    cube1.transform.append(['T', 100.0, 1.0, 0.0])
    cube1.transform.append(['R', 0.0, 1.0, 0.0])
    scene.add(cube1)

    cube2 = Primitives("cube")
    cube2.color = 'green'
    cube2.position = [0.0, 0.0, 0.0]
    cube2.transform.append(['T', 1.0, 0.0, 100.0])
    cube2.transform.append(['R', 0.0, 1.0, 0.0])
    scene.add(cube2)

    bridges.set_data_structure(scene)
    bridges.visualize()


if __name__ == "__main__":
    main()