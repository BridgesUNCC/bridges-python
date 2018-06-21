from SLelement import *
import Bridges
from data_src_dependent import DataSource


class GameDrive:

    bridges = Bridges.Bridges(11, "1343747370122", "test")

    ami = DataSource.getGameData()

    head = None

    for im in ami[:2000]:
        # print(im.get_Actor())
        newone = SLelement(im, im.getTitle())
        newone.set_next(head)
        head = newone

    # print(head.get_data_structure_representation())
    bridges.set_data_structure(head)
    bridges.visualize()