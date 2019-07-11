from bridges.bridges import *
from bridges.array import *

def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "testtest", "1243437903811")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    # for 2D array 4x4
    num_rows = 4
    num_cols = 4
    my_array = Array(x_dim = 4, y_dim = 4)

    #populate the array
    for row in range(num_rows):
        for col in range(num_cols):
            my_array.get_element(x=row, y=col).label = "El " + str(row*num_cols + col)

    #color some of the elements
    my_array.get_element(x=0, y=0).visualizer.color = "red"
    my_array.get_element(x=0, y=3).visualizer.color = "green"
    my_array.get_element(x=3, y=0).visualizer.color = "blue"
    my_array.get_element(x=3, y=3).visualizer.color = "magenta"
    my_array.get_element(x=1, y=1).visualizer.color = "cyan"
    my_array.get_element(x=2, y=2).visualizer.color = "yellow"

    #set visualizer type
    bridges.set_data_structure(my_array)

    #visualize tha array
    bridges.visualize()

if __name__ == "__main__":
    main()