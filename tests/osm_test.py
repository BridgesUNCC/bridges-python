from bridges.data_src_dependent import data_source
from bridges.bridges import Bridges
import os
user = os.environ.get("BRIDGES_USER_NAME")
key = os.environ.get("BRIDGES_API_KEY")
bridges = Bridges(100, user, key)
bridges.connector.set_server("clone")

go = data_source.get_osm_data("uncc_campuS")

print(go.name)
print(go.longitude_range)
print(go.latitude_range)
print(go.cartesian_range_x)
print(go.cartesian_range_y)

try:
    go.edges = [1, 2, 3]
except ValueError:
    print("edge setter works")
try:
    go.vertices = [1, 2, 3]
except ValueError:
    print("vertex setter works")


bridges.set_data_structure(go.get_graph())
bridges.visualize()
