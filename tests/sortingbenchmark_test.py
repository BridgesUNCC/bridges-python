from bridges.bridges import *
from bridges.line_chart import *
from bridges.sorting_benchmark import *

def sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_indx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_indx]:
                min_indx = j

        temp = arr[min_indx]
        arr[min_indx] = arr[i]
        arr[i] = temp

def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    plot = LineChart()
    plot.title = "Sort Runtime"
    bench = SortingBenchmark(plot)
    bench.linear_range(100, 10000, 20)
    bench.time_cap = 1000*1
    bench.run("insertsort", sort)
    bench.run("bubble sort", bubble_sort)
    bridges.set_data_structure(plot)
    bridges.visualize()

if __name__ == "__main__":
    main()