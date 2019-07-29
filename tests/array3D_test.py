from bridges.bridges import *
from bridges.array import *
import os

def main():

    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    #speify array dimensions and create 3D array
    num_slices = 4
    num_rows = 4
    num_cols = 4

    my_array = Array(x_dim=num_slices, y_dim = num_rows, z_dim= num_cols)

    #populate the elements with their array postition
    n = 0
    for k in range(num_slices):
        for j in range(num_rows):
            for i in range(num_cols):
                my_array[i,j,k].label = "El " + str(n)
                n += n

    #color some of the elements
    my_array[0,0,0].visualizer.color = "red"
    my_array[0,3,0].visualizer.color = "green"
    my_array[3,0,0].visualizer.color = "blue"
    my_array[3,3,0].visualizer.color = "magenta"
    my_array[1,1,0].visualizer.color = "cyan"
    my_array[2,2,0].visualizer.color = "yellow"

    #set visualizer type
    bridges.set_data_structure(my_array)

    #visualize the list
    bridges.visualize()


if __name__ == "__main__":
    main()