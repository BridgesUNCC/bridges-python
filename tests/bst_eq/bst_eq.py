from bridges.bridges import *
from bridges.bst_element import *
from bridges.data_src_dependent.data_source import *
from tests.bst_eq.BST import *

def main():
    bridges = Bridges(0, "test", "")
    bridges.connector.set_server("local")
    bridges.set_title("Recent Earthquakes(USGIS Data}")

    eqlist = get_earthquake_usgs_data(1000)
    bst = BST()
    for i in range(eqlist.size()):
        if eqlist.get(i).get_magnitude() > 3:
            bst.insert(eqlist.get(i).get_magnitude(), eqlist.get(i))

    bridges.set_data_structure(bst.get_tree_root())
    bridges.visualize()