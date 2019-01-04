from bridges import *
import os
user = os.environ.get("BRIDGES_USER_NAME")
key = os.environ.get("BRIDGES_API_KEY")
bridges = Bridges(100, user, key)
bridges.connector.set_server("clone")

len_x = 256
len_y = 256

color_grid = ColorGrid(len_x, len_y)

for x in range(0, len_x):
    for y in range(0, len_y):
        color = Color(y, y, y, 1.0)
        color_grid.set(x, y, color)

bridges.set_data_structure(color_grid)
bridges.visualize()
