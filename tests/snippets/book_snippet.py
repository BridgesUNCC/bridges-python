from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
import random

def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    book_list = get_gutenberg_book_data()

    book1 = book_list[random.randrange(len(book_list))]

    print(book1.title)
    print(book1.name)
    print(book1.genre)

if __name__ == '__main__':
    main()