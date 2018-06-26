from Bridges import *
from Array import *
from Element import *


class Array1d():

    bridges = Bridges(23, "1343747370122", "test")

    arraySize = 10

    arr = Array(num_elements = arraySize)

    for i in range(arr.get_size()):
        arr.get_element(indx = i).set_label(i*i)

    arr.get_element(0).get_visualizer().set_color("red")

    bridges.set_data_structure(arr)
    bridges.visualize()
