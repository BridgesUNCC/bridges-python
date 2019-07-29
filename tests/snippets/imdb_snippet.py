from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
import sys
import random

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")

    my_list = get_actor_movie_imdb_data()

    pair1 = my_list[random.randrange(len(my_list))]

    print(pair1.actor)
    print(pair1.movie)

if __name__ == '__main__':
    main()