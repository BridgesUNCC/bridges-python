from bridges import *
import os
user = os.environ.get("BRIDGES_USER_NAME")
key = os.environ.get("BRIDGES_API_KEY")
bridges = Bridges(101, user, key)
bridges.connector.set_server("clone")

len_x = 255
len_y = 255

color_grid = ColorGrid(len_x, len_y)

for x in range(0, len_x):
    for y in range(0, len_y):
        color = Color(x, x, x, 1.0)
        color_grid.set(x, y, color)

bridges.set_title("\"test")
bridges.set_data_structure(color_grid)
bridges.visualize()
