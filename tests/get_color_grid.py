from Bridges import *

bridges = Bridges(0, "", "")
bridges.connector.set_server("clone")
grid = bridges.get_color_grid_from_assignment("bridges_testing", 3013)

print(grid.get_data_structure_representation())
