from bridges.bridges import *
from bridges.array2d import *

def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    num_rows = 6
    num_cols = 6

    my_array = Array2D(num_rows, num_cols)

    my_array[0,0].color = "red"

    # tell Bridges what data structure to visualize
    bridges.set_data_structure(my_array)

    # visualize the list
    bridges.visualize()


if __name__ == "__main__":
    main()