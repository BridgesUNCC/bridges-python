from bridges.bridges import *
from bridges.bst_element import *
from bridges.data_src_dependent.data_source import *


# recursive insert method to insert nodes into a binary search tree
def insertR(rt, newel):
    if (rt is None):
        return newel
    elif newel.key < rt.key:
        rt.left = insertR(rt.right, newel)
    else:
        rt.right = insertR(rt.right, newel)
    return rt


def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    # Retrieve a list of 10 earthquake records from USGS using the BRIDGES API
    ami = get_earthquake_usgs_data(10)

    root = None
    # create BST nodes and insert into a tree
    for i in range(len(ami)):
        bst_node = BSTElement(key=ami[i].magnitude, e=ami[i])
        # set label of the node
        bst_node.label = ami[i].title + ami[i].time

        root = insertR(root, bst_node)

    # set some visual attributes
    root.color = "red"

    # set visualizer type
    bridges.set_data_structure(root)
    # visualize the tree
    bridges.visualize()


if __name__ == "__main__":
    main()