from Bridges import *
from AVLTreeElement import *


class AVLTreetutorial:

    bridges = Bridges(31, "1343747370122", "test")

    avl_root = AVLTreeElement(50, "Hello")

    avl_2 = AVLTreeElement(30, "This")
    avl_3 = AVLTreeElement(70, "is")
    avl_4 = AVLTreeElement(20, "an")
    avl_5 = AVLTreeElement(40, "AVL")
    avl_6 = AVLTreeElement(90, "Tree")


    avl_root.set_label("0")
    avl_2.set_label("0")
    avl_3.set_label("-1")
    avl_4.set_label("0")
    avl_5.set_label("0")
    avl_6.set_label("0")

    avl_root.set_left(avl_2)
    avl_root.set_right(avl_3)
    avl_2.set_left(avl_4)
    avl_2.set_right(avl_5)
    avl_3.set_right(avl_6)

    avl_root.get_visualizer().set_color("magenta")
    avl_root.get_visualizer().set_opacity(0.8)

    bridges.set_data_structure(avl_root)
    bridges.visualize()

