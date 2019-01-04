from bridges.dl_element import *
from bridges.bridges import *
from StudentInfo import *
import sys
import os



def insertFront(front, new_el):
    if front is None:
        return new_el

    new_el.set_next(front)
    front.set_prev(new_el)

    return new_el

def main():

    args = sys.argv[1:]

    # create the Bridges object, set credentials
    bridges = Bridges(1000, os.environ.get("BRIDGES_USER_NAME"), os.environ.get("BRIDGES_API_KEY"))

    if len(args) > 3:
        bridges.connector.set_server(args[3])

    students = []

    # load student info
    students.append(Student("00000000000",
                              "Gretel Chaney",
                              "CS",
                              "g.chaney@generated.com",
                              "magenta",
                              "blue",
                              9.0))

    students.append(Student("00000000001",
                              "Karol Soderman",
                              "SIS",
                              "k.soderman@generated.com",
                              "magenta",
                              "red",
                              11.0))

    students.append(Student("00000000002",
                              "Lamont Kyler",
                              "BIO",
                              "l.kyler@generated.com",
                              "yellow",
                              "green",
                              50.0))

    students.append(Student("00000000003",
                              "Gladys Serino",
                              "CS",
                              "g.serino@generated.com",
                              "green",
                              "magenta",
                              9.0))

    students.append(Student("00000000004",
                              "Starr Mcginn",
                              "CS",
                              "s.mcginn@generated.com",
                              "red",
                              "cyan",
                              15.0))

    # insert the students in front of the list
    head = None
    for i in range(len(students)):
        head = insertFront(head, DLelement(label = "", e = students[i]))

    # add visual attributes
    curr = head
    while curr is not None:
        curr.set_label(curr.get_value().getName())
        curr.get_visualizer().set_color(col_name=curr.get_value().getDislikeColor())

        if curr.get_next()is not None:
            next = curr.get_next()
            curr.get_link_visualizer(next).set_color(col_name=curr.get_value().getDislikeColor())
            next.get_link_visualizer(curr).set_color(col_name=curr.get_value().getDislikeColor())

        curr = curr.get_next()


    # set dat structure to be visualized
    bridges.set_data_structure(head)
    # visualize the data structure
    bridges.visualize()

if __name__ == "__main__":
    main()
