from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
import sys
import random

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")

    my_list = get_earthquake_usgs_data(1000)

    quake1 = my_list[random.randrange(len(my_list))]

    print(quake1.get_latit())
    print(quake1.get_longit())
    print(quake1.get_location())
    print(quake1.get_title())
    print(quake1.get_magnitude())


if __name__ == '__main__':
    main()