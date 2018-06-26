import Bridges
from SLelement import *
from BSTElement import *
from data_src_dependent import DataSource


def insertR(rt, newel):
    if (rt is None):
        return newel
    elif newel.get_key() < rt.get_key():
        rt.set_left(insertR(rt.get_left(), newel))
    else:
        rt.set_right(insertR(rt.get_right(), newel))
    return rt


class EarthquakeDriver():

    bridges = Bridges.Bridges(22, "1343747370122", "test")

    ami = DataSource.getEarthquakeUSGSData(1000)

    print(ami)

    root = None

    for i in range(len(ami)):
        bst_node = BSTElement(ami[i].getMagnitude(), ami[i])
        bst_node.set_label(ami[i].getTitle())
        # print(bst_node.get_key())
        root = insertR(root, bst_node)

    # print(head.get_data_structure_representation())

    bridges.set_data_structure(root)
    bridges.visualize()



