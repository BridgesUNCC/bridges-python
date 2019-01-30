from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
import sys
import random

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")

    book_list = get_gutenberg_book_data()

    book1 = book_list[random.randrange(len(book_list))]

    print(book1.get_title())
    print(book1.get_author_name())
    print(book1.get_genre())

if __name__ == '__main__':
    main()