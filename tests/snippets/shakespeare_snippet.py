from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
import sys
import random

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")

    my_list = get_shakespeare_data()

    work1 = my_list[random.randrange(len(my_list))]

    print(work1.get_title())
    print(work1.get_type())
    print(work1.get_text()[0:min(100, len(work1.get_text()))])


if __name__ == '__main__':
    main()