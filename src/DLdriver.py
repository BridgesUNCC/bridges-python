from DLelement import *
import Bridges

bridges = Bridges.Bridges(0, "1343747370122", "test")
element = DLelement()
element.get_visualizer().set_size(1)
element.get_visualizer().set_color("red")
element2 = DLelement()
element.set_next(element2)
element2.set_prev(element)
json_string = element.get_data_structure_representation()
print (json_string)
bridges.set_data_structure(element)
bridges.visualize()