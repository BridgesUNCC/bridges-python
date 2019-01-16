from bridges.bridges import *
from bridges.bst_element import *
from bridges.data_src_dependent.data_source import *
from tests.bst_gutenburg.BST import *

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")
    bridges.set_title("GutenBerg book collection(meta data only)")

    book_list = get_gutenberg_book_data()

    bst = BST()

    for i in range(len(book_list)):
        bst.insert(book_list[i].get_title(), book_list[i])

    bridges.set_data_structure(bst.get_tree_root())
    bridges.visualize()

if __name__ == '__main__':
    main()