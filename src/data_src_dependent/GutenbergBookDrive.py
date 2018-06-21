from data_src_dependent import DataSource
from SLelement import *
import Bridges

class GutenbergBookDrive:

    bridges = Bridges.Bridges(13, "1343747370122", "test")

    ami = DataSource.getGutenBergBookData()

    head = None

    for im in ami:
        # print(im.get_Actor())
        newone = SLelement(im, im.getTitle())
        newone.set_next(head)
        head = newone

    # print(head.get_data_structure_representation())

    bridges.set_data_structure(head)
    bridges.visualize()