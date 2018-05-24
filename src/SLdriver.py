from SLelement import *
from Student import*
import Bridges

bridges = Bridges.Bridges(0, "1343747370122", "test")
element = SLelement()
element.set_label("Hello")
print(element.get_label())
print("some")
element2 = SLelement()
print("some")
element3 = SLelement()
element2.set_next(element3)
element.set_next(element2)
element.get_visualizer().set_size(1)
element.get_visualizer().set_color("red")
element2.get_visualizer().set_size(5)
print (element.get_data_structure_representation())
bridges.set_data_structure(element)
bridges.visualize()