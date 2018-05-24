from MLelement import *
from Student import*
import Bridges

bridges = Bridges.Bridges(0, "1343747370122", "test")
element1 = MLelement()
element2 = MLelement()
element3 = MLelement()
element4 = MLelement()

element1.set_next(element2)
element2.set_next(element3)
element3.set_next(element4)

element5 = MLelement()
element6 = MLelement()
element7 = MLelement()

element5.set_next(element6)
element6.set_next(element7)
element2.set_sub_list(element5)

bridges.set_data_structure(element1)
bridges.visualize()