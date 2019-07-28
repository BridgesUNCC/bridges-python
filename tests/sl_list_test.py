from bridges.bridges import *
from bridges.sl_element import *

def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")
    bridges.set_title("hello test")

    # link the elements
    el1 = SLelement(e="Gretel Chaney", label="Gretel Chaney")
    el2 = SLelement(e="Gretel Chaney", label="Gretel Chaney")
    el3 = SLelement(e="Gretel Chaney", label="Gretel Chaney")
    el4 = SLelement(e="Gretel Chaney", label="Gretel Chaney")
    el5 = SLelement(e="Gretel Chaney", label="Gretel Chaney")

    el1.next = el2
    el2.next = el3
    el3.next = el4
    el4.next = el5

    el1.visualizer.color = "red"
    el2.visualizer.color = 'magenta'

    bridges.set_data_structure(el1)
    bridges.visualize()

if __name__ == "__main__":
    main()
