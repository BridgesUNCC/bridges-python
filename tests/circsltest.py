from bridges.bridges import *
from bridges.circ_sl_element import *
import sys

def main():
    # create the Bridges object, set credentials

#if TESTING
    # command line args provide credentials and server to test on
    bridges = Bridges(300, "test", "137842425086")
    bridges.connector.set_server("clone")
#endif


    # title, description
    bridges.set_title("A Circle Singly Linked List Example")
    bridges.set_description("This circular singly linked list example shows five nodes and attached visual attributes.")

    # create list elements
    el0 = CircSLelement(e="Gretel Chaney", label="Gretel Chaney")
    el1 = CircSLelement(e="Lamont Kyler", label="Lamont Kyler")
    el2 = CircSLelement(e="Gladys Serino", label="Gladys Serino")
    el3 = CircSLelement(e="Karol Soderman", label="Karol Soderman")
    el4 = CircSLelement(e="Starr McGinn", label="Starr McGinn")

    # link the elements
    el0.next = el1
    el1.next = el2
    el2.next = el3
    el3.next = el4

    # link last node back to first node
    el4.next = el0
    #using iterator
    myiter = el0.iterator()
    while myiter.has_next():
        print(myiter.next())

    # set visual attributes
    # el0.visualizer.color = "red"
    # el2.visualizer.color = 'aliceblue'
    #
    # el0.get_link_visualizer(el1).color = "green"
    # el3.get_link_visualizer(el4).color = "magenta"
    #
    # el0.get_link_visualizer(el1).thickness = 2.0
    #
    # el4.opacity = 0.5
    #
    # el0.size = 20
    #
    # el2.get_link_visualizer(el3).label = "Gladys_to_Karol"
    #
    # # visualize
    # bridges.set_data_structure(el0)
    # bridges.visualize()


if __name__ == "__main__":
    main()