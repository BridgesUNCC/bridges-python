from CircDLelement import *
from Student import*
import Bridges

bridges = Bridges.Bridges(0, "1343747370122", "test")

element = CircDLelement()
element2 = CircDLelement()
element3 = CircDLelement()
element4 = CircDLelement()
element5 = CircDLelement()

element.set_next(element2)
element2.set_next(element3)
element3.set_next(element4)
element4.set_next(element5)
element5.set_next(element)

element.set_prev(element5)
element2.set_prev(element)
element3.set_prev(element2)
element4.set_prev(element3)
element5.set_prev(element4)

bridges.set_data_structure(element)
bridges.visualize()



