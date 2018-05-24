from CircSLelement import *
from Student import*
import Bridges

bridges = Bridges.Bridges(0, "1343747370122", "test")
element = CircSLelement()
element2 = CircSLelement()
element3 = CircSLelement()
element4 = CircSLelement()

element.set_next(element2)
element2.set_next(element3)
element3.set_next(element4)
element4.set_next(element)

bridges.set_data_structure(element)
bridges.visualize()