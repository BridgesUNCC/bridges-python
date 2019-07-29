from bridges.bridges import *
from bridges.tree_element import *

def main():
    # create the Bridges object, set credentials

    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    #Title and Description
    bridges.set_title("A General Tree Example")
    bridges.set_description("A basic tree with seven nodes. Three on one side and three on the other. The root node is set to red with 0.3 opacity. "
            +	"The other six nodes are neutral color.")

    # create tree nodes
    t0 = TreeElement(e = "Hello")
    t1 = TreeElement(e= "this")
    t2 = TreeElement(e="is")
    t3 = TreeElement(e="a")
    t4 = TreeElement(e="generic")
    t5 = TreeElement(e="tree")
    t6 = TreeElement(e="representation")

    # put in labels for each node; simply use integers
    t0.label = "10"
    t1.label = "20"
    t2.label = "30"
    t3.label = "40"
    t4.label = "50"
    t5.label = "60"
    t6.label = "70"

    # add links to children
    t0.add_child(t1)
    t0.add_child(t2)
    t0.add_child(t5)
    t2.add_child(t4)
    t2.add_child(t5)
    t3.add_child(t6)

    # set some visual attributes
    t0.color = "red"
    t0.opacity = 0.3

    # set visualizer type
    bridges.set_data_structure(t0)

    # visualize the tree
    bridges.visualize()

if __name__ == "__main__":
    main()