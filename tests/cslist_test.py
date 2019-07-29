from bridges.bridges import *
from bridges.circ_sl_element import *

def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")
    bridges.set_title("A Circle Singly Linked List Example")
    bridges.set_description("This example shows five nodes. Each node is linked only to its child node. "
            +	"Colors are: A green node with a yellow link size 12, a blue node with a magenta link size 9, "
            +	"a magenta node with a blue link size 9, a red node with a magenta link size 11, and a yellow node with "
            +	"a red link size 15.")

    # link the elements
    el1 = CircSLelement(e="Gretel Chaney", label="Gretel Chaney")
    el2 = CircSLelement(e="Gretel Chaney", label="Gretel Chaney")
    el3 = CircSLelement(e="Gretel Chaney", label="Gretel Chaney")
    el4 = CircSLelement(e="Gretel Chaney", label="Gretel Chaney")
    el5 = CircSLelement(e="Gretel Chaney", label="Gretel Chaney")

    el1.next = el2
    el2.next = el3
    el3.next = el4
    el4.next = el5

    el5.next = el1

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
