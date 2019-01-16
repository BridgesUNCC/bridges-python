from bridges.bridges import *
from bridges.bst_element import *
from bridges.data_src_dependent.data_source import *
from tests.bst_eq.BST import *

def main():

    bridges = Bridges(0, "test", "")
    bridges.connector.set_server("local")
    bridges.set_title("Binary Search Tree with IGN Game Data")

    game_list = get_game_data()

    bst = BST()
    for i in range(5000):
        bst.insert(game_list[i].get_title(), game_list[i])

    bridges.set_data_structure(bst.get_tree_root())
    bridges.visualize()