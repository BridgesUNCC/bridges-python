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
    t0 = TreeElement(e ="Hello", label="Hello")
    t2 = TreeElement(e="this", label="this")
    t3 = TreeElement(e="is", label='is')
    t4 = TreeElement(e="a", label='a')
    t5 = TreeElement(e="generic", label="generic")
    t6 = TreeElement(e="tree", label='tree')
    t7 = TreeElement(e="representation", label = "representation")

    # add links to children
    t0.add_child(t2)
    t0.add_child(t3)
    t0.add_child(t4)
    t2.add_child(t5)
    t2.add_child(t6)
    t3.add_child(t7)

    # set some visual attributes
    t0.color = "red"
    t0.opacity = 0.3

    t0.get_link_visualizer(t2).color = "green"
    t0.get_link_visualizer(t2).thickness = 2.0
    t0.get_link_visualizer(t3).color = "blue"
    t0.get_link_visualizer(t3).thickness = 2.0
    t0.get_link_visualizer(t4).color = "orange"
    t0.get_link_visualizer(t4).thickness = 2.0

    # set visualizer type
    bridges.set_data_structure(t0)

    # visualize the tree
    bridges.visualize()

if __name__ == "__main__":
    main()