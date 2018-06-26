from Bridges import *
from Array import *
from Element import *


class Array1d():

    bridges = Bridges(23, "1343747370122", "test")

    dim = [10,1,1]

    arr = Array(1, dim)

    for i in range(arr.get_size()):
        arr.set_value(i, el = Element(str(i), i))

    arr.get

    bridges.set_data_structure(arr)
    bridges.visualize()
