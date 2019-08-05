from bridges.bridges import *
from bridges.array1d import *

def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")
    # set array dimensions, allocate array fo elements
    arraySize = 10
    arr =Array1D(arraySize)

    for k in range(0, arr.size):
        arr[k].value = k*k
        arr[k].label = str(k*k)

    arr[0].color = "red"
    arr[1].color = "green"

    # tell Bridges what data structure to visualize
    bridges.set_data_structure(arr)

    # visualize the list
    bridges.visualize()

if __name__ == "__main__":
    main()