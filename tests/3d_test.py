from bridges.bridges import *
from bridges.array3d import *

def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    my_array = Array3D(dims=[4,4,4])
    my_array[0,0,0].color = "red"

    # tell Bridges what data structure to visualize
    bridges.set_data_structure(my_array)

    # visualize the list
    bridges.visualize()


if __name__ == "__main__":
    main()