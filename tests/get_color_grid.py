from bridges import *
import os
user = os.environ.get("BRIDGES_USER_NAME")
key = os.environ.get("BRIDGES_API_KEY")
bridges = Bridges(3100 , user, key)
bridges.connector.set_server("clone")

grid = bridges.get_color_grid_from_assignment(user, 101)
bridges.set_data_structure(grid)
bridges.visualize()

grid = bridges.get_color_grid_from_assignment(user, 100)
bridges.set_data_structure(grid)
bridges.visualize()
