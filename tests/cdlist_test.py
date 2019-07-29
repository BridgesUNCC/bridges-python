from bridges.bridges import *
from bridges.circ_dl_element import *

def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")
    bridges.set_title("A Circlar Doubly Linked List Example")
    bridges.set_description("This example shows five nodes each linked to their parent and child node. "
            +	"Colors are: Magenta node with blue links size 9, Red node with magenta links size 11, blue node with magenta links size 9, "
            +	"yellow node with red links size 15, and green node with yellow links size 12.")

    # link the elements
    el1 = CircDLelement(e="Gretel Chaney", label="Gretel Chaney")
    el2 = CircDLelement(e="Lamont Kyler", label="Lamont Kyler")
    el3 = CircDLelement(e="Gladys Serino", label="Gladys Serino")
    el4 = CircDLelement(e="Karol Soderman", label="Karol Soderman")
    el5 = CircDLelement(e="Starr McGinn", label="Starr McGinn")

    el1.next = el2
    el2.prev = el1
    el2.next = el3
    el3.prev = el2
    el3.next = el4
    el4.prev = el3
    el4.next = el5

    el5.next = el1
    el1.prev = el5

    el1.visualizer.color = "red"
    el2.visualizer.color = 'aliceblue'

    el1.get_link_visualizer(el2).color = "green"
    el3.get_link_visualizer(el4).color = "magenta"

    el3.get_link_visualizer(el4).thickness = 3.0
    el4.get_link_visualizer(el3).thickness = 6.0

    el4.opacity = 0.5

    el1.size = 20

    el2.get_link_visualizer(el3).label = "link label"

    bridges.set_data_structure(el1)
    bridges.visualize()

if __name__ == "__main__":
    main()