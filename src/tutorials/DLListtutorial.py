from DLelement import *
from Bridges import Bridges
from Student import *


def insertFront(front, new_el):
    if front is None:
        return new_el

    new_el.set_next(front)
    front.set_prev(new_el)

    return new_el

class DLListtutorial:
    bridges = Bridges(25, "1343747370122", "test")

    students = []

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

    head = None
    for i in range(len(students)):
        head = insertFront(head, DLelement(label = "", e = students[i]))

    curr = head
    while curr is not None:
        curr.set_label(curr.get_value().getName())
        curr.get_visualizer().set_color(curr.get_value().getDislikeColor())

        if curr.get_next()is not None:
            next = curr.get_next()
            curr.get_link_visualizer(next).set_color(curr.get_value().getDislikeColor())
            next.get_link_visualizer(curr).set_color(curr.get_value().getDislikeColor())

        curr = curr.get_next()

    bridges.set_data_structure(head)
    bridges.visualize()