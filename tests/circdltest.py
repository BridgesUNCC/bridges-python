from bridges.circ_dl_element import *
from bridges.bridges import *
import sys


def main():
    # create the Bridges object, set credentials
#if TESTING
    # command line args provide credentials and server to test on
    bridges = Bridges(300, "test", "137842425086")
    bridges.connector.set_server("clone")
#endif

    # set title, description
    bridges.set_title("A doubly Linked List Example")
    bridges.set_description("This list has five nodes all linked to the nodes before and after them and illustrates visual attributes. ")

    # create list elements
    el0 = CircDLelement(e="Gretel Chaney", label="Gretel Chaney")
    el1 = CircDLelement(e="Lamont Kyler", label="Lamont Kyler")
    el2 = CircDLelement(e="Gladys Serino", label="Gladys Serino")
    el3 = CircDLelement(e="Karol Soderman", label="Karol Soderman")
    el4 = CircDLelement(e="Starr McGinn", label="Starr McGinn")

    # link elements
    el0.next = el1
    el1.prev = el0
    el1.next = el2
    el2.prev = el1
    el2.next = el3
    el3.prev = el2
    el3.next = el4
    el4.prev = el3

    el4.next = el0
    el0.prev = el4

    #regular iterator
    myiter = el0.iterator()
    while myiter.has_next():
        print(myiter.next())

    # reverse iterator
    myiter2 = el0.reverse_iterator()
    while myiter2.has_next():
        print(myiter2.next())


    # add visual attributes
    el0.color = "red"
    el2.color = "aliceblue"

    el0.get_link_visualizer(el1).color = "green"
    el1.get_link_visualizer(el0).color = "magenta"

    el3.get_link_visualizer(el4).thickness = 3.0
    el4.get_link_visualizer(el3).thickness = 6.0

    el2.get_link_visualizer(el3).label = "link label"

    el4.opacity = 0.5

    el0.size = 20

    # set dat structure to be visualized
    bridges.set_data_structure(el0)

    # visualize the data structure
    bridges.visualize()


if __name__ == "__main__":
    main()