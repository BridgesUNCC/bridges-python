from bridges.bridges import *
from bridges.avl_tree_element import *


def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    #Title and Description
    bridges.set_title("AVL Tree Example")
    bridges.set_description("This AVL tree has six elements. "
                    + "The root is magenta color and has three nodes on its left "
                    + "and two nodes on its right. The values from lower left to the root, 20, 40, 30, 50. "
                    + "And from lower right to root, 90, 70, 50.")

    # create an AVL tree elements
    avl_root = AVLTreeElement(50, "Hello")

    avl_2 = AVLTreeElement(30, "This")
    avl_3 = AVLTreeElement(70, "is")
    avl_4 = AVLTreeElement(20, "an")
    avl_5 = AVLTreeElement(40, "AVL")
    avl_6 = AVLTreeElement(90, "Tree")


    # put in the balance factors - done manually here
    # for illustration, but in a real project, the user will
    # implement this as part of the insert/delete
    # operations on the tree to maintain a balanced tree
    avl_root.label = '0'
    avl_2.label = "0"
    avl_3.label = "-1"
    avl_4.label = "0"
    avl_5.label = "0"
    avl_6.label = "0"

    # add links between nodes
    avl_root.left = avl_2
    avl_root.right = avl_3
    avl_2.left = avl_4
    avl_2.right = avl_5
    avl_3.right = avl_6

    # add some visual attributes
    avl_root.visualizer.color = "magenta"
    avl_root.visualizer.opacity = 0.8


    # set visualizer type
    bridges.set_data_structure(avl_root)


    # visualize the tree
    bridges.visualize()


if __name__ == "__main__":
    main()
