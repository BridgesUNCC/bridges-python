from bridges.bridges import *
from bridges.bst_element import *
from bridges.data_src_dependent.data_source import *
from tests.bst_shakespeare.BST import *

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")
    bridges.set_title("Shakespeare Sonnets, Poems, PLays")
    bridges.json_flag = True
    shksp_list = get_shakespeare_data(textonly=True)

    bst = BST()

    for i in range(len(shksp_list)):
        bst.insert(shksp_list[i].get_title(), shksp_list[i])

    bridges.set_data_structure(bst.get_tree_root())
    bridges.visualize()

if __name__ == '__main__':
    main()