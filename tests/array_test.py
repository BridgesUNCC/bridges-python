from bridges.bridges import *
from bridges.array import *

def main():

    # create the Bridges object, set credentials
    bridges = Bridges(0, "testtest", "1243437903811")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    #set array dimensions, allocate array fo elements
    arraySize = 10

    arr = Array(num_elements=arraySize)

    #populate the array with squares of indicies
    for i in range(arr.size):
        arr.get_element(index = i).label = i*i

    #color the array elements
    arr.get_element(index = 0).visualizer.color = "red"
    arr.get_element(index = 1).visualizer.color = "green"
    arr.get_element(index = 2).visualizer.color = "blue"
    arr.get_element(index = 3).visualizer.color = "cyan"
    arr.get_element(index = 4).visualizer.color = "magenta"
    arr.get_element(index = 5).visualizer.color = "yellow"
    arr.get_element(index = 6).visualizer.color = "red"
    arr.get_element(index = 7).visualizer.color = "green"
    arr.get_element(index = 8).visualizer.color = "blue"
    arr.get_element(index = 9).visualizer.color = "black"

    # tell Bridges what data structure to visualize
    bridges.set_data_structure(arr)

    # visualize the list
    bridges.visualize()

if __name__ == "__main__":
    main()