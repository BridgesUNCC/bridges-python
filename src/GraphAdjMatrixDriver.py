from GraphAdjMatrix import *
import Bridges

bridges = Bridges.Bridges(1, "1343747370122", "test")

a1 = "Matthew McQuaigue"
a2 = "David Burlinson"
a3 = "krs"

g = GraphAdjMatrix()
g.add_vertex(a1, "")
g.add_vertex(a2, "")
g.add_vertex(a3, "")

g.add_edge(a1, a2, 1)
g.add_edge(a2,a1,1)
g.add_edge(a1, a3, 1)
g.add_edge(a2, a3, 1)


# print (g.get_data_structure_representation())

bridges.set_data_structure(g)
bridges.visualize()