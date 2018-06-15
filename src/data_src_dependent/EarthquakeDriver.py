import Bridges
from SLelement import *
from data_src_dependent import DataSource

class EarthquakeDriver:

    bridges = Bridges.Bridges(10, "1343747370122", "test")

    ami = DataSource.getEarthquakeUSGSData(1000)

    head = None


    for im in ami:
        # print(im.get_Actor())
        newone = SLelement(im, im.getTitle())
        newone.set_next(head)
        print(float(im.getMagnitude()))
        if float(im.getMagnitude()) > 3.0:
            newone.get_visualizer().set_color("green")
        head = newone


    # print(head.get_data_structure_representation())

    bridges.set_data_structure(head)
    bridges.visualize()
