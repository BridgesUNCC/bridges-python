from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
import sys
import random

def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    my_list = get_earthquake_usgs_data(1000)

    quake1 = my_list[random.randrange(len(my_list))]

    print(quake1.latit)
    print(quake1.longit)
    print(quake1.location)
    print(quake1.title)
    print(quake1.magnitude)


if __name__ == '__main__':
    main()