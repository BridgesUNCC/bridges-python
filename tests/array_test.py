from bridges.bridges import *
from bridges.array import *
import os

def main():

    # create the Bridges object, set credentials
    user = os.environ.get("BRIDGES_USER_NAME")
    key = os.environ.get("BRIDGES_API_KEY")
    bridges = Bridges(100, user, key)
    bridges.set_visualize_JSON(True)
    #set array dimensions, allocate array fo elements
    arraySize = 10

    arr = Array(num_elements=arraySize)

    #populate the array with squares of indicies
    for i in range(arr.size):
        arr[i].label = i*i

    #color the array elements
    arr.get_element(0).visualizer.color = "red"
    arr.get_element(1).visualizer.color = "green"
    arr.get_element(2).visualizer.color = "blue"
    arr.get_element(3).visualizer.color = "cyan"
    arr.get_element(4).visualizer.color = "magenta"
    arr.get_element(5).visualizer.color = "yellow"
    arr.get_element(6).visualizer.color = "red"
    arr.get_element(7).visualizer.color = "green"
    arr.get_element(8).visualizer.color = "blue"
    arr.get_element(9).visualizer.color = "black"

    arr[5].color = "white"
    print(arr[5])

    # tell Bridges what data structure to visualize
    bridges.set_data_structure(arr)

    # visualize the list
    bridges.visualize()

if __name__ == "__main__":
    main()