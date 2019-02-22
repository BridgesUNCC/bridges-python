from bridges.data_src_dependent import data_source
from bridges.bridges import Bridges
import os
user = os.environ.get("BRIDGES_USER_NAME")
key = os.environ.get("BRIDGES_API_KEY")
bridges = Bridges(100, user, key)
bridges.connector.set_server("clone")

go = data_source.get_osm_data("shrunk_uncc_campus")

print(go.name)
print(go.longitude_range)
print()

bridges.set_data_structure(go.get_graph())
bridges.visualize()

