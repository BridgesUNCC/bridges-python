from bridges.bridges import *
from bridges.bst_element import *
from bridges.data_src_dependent.data_source import *
from tests.bst_eq.BST import *

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")
    bridges.set_title("Recent Earthquakes(USGIS Data)")
    bridges.json_flag = True

    eqlist = get_earthquake_usgs_data(100)
    bst = BST()
    for i in range(len(eqlist)):
        if eqlist[i].get_magnitude() > 3:
            bst.insert(eqlist[i].get_magnitude(), eqlist[i])
            print(bst.node_count)

    bridges.set_data_structure(bst.get_tree_root())
    bridges.visualize()

if __name__ == '__main__':
    main()