from bridges import *

def task1(bridges):
    lc = LineChart()
    lc.title = "Something"
    lc.x_label = "n"
    lc.y_label = "Time in seconds"

    xdata = []
    ydata = []

    for i in range(1, 100000, 1000):
        t = 10000 * i / (1000 * 1000)
        xdata.append(float(i))
        ydata.append(t)

    lc.set_data_series("10^4 n at 1MHz", xdata, ydata)

    print(lc.get_data_structure_representation())
    bridges.set_data_structure(lc)
    bridges.visualize()

def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    task1(bridges)


if __name__ == '__main__':
    main()