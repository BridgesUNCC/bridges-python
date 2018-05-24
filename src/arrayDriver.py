from Array import *
from Element import *
import Bridges

bridges = Bridges.Bridges(0, "1343747370122", "test")

dim = [4,1,1]
arr = Array(1, dim)
arr.set_value(0, None,None,None, Element("0", 0))
arr.set_value(1, None,None,None, Element("1", 1))
arr.set_value(2, None,None,None, Element("2", 2))
arr.set_value(3, None,None,None, Element("3", 3))

bridges.set_data_structure(arr)
bridges.visualize()
