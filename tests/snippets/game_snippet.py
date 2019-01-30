from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
import sys
import random

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")

    my_list = get_game_data()

    game1 = my_list[random.randrange(len(my_list))]

    print(game1.get_title())
    print(game1.get_platform())
    print(game1.get_rating())
    print(game1.get_genre())



if __name__ == '__main__':
    main()