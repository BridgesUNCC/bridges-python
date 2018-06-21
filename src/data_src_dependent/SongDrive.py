
from data_src_dependent import DataSource
from SLelement import *
import Bridges

class SongDrive:

    bridges = Bridges.Bridges(20, "1343747370122", "test")

    ami = DataSource.getSong("Courtesy Call")

    element1 = SLelement(ami, ami.getSongTitle())

    ami2 = DataSource.getSong("Frontline")

    element2 = SLelement(ami2, ami2.getSongTitle())

    head = None

    element1.set_next(head)
    head = element1
    element2.set_next(head)
    head = element2

    # for im in ami:
    #     # print(im.get_Actor())
    #     newone = SLelement(im, im.getSongTitle())
    #     newone.set_next(head)
    #     head = newone

    # print(head.get_data_structure_representation())

    bridges.set_data_structure(head)
    bridges.visualize()