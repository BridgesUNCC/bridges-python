from bridges.bridges import *
from bridges.circ_dl_element import *
from tests.StudentInfo import *
import sys

#helper funtction
def insert_front(tailElement, newElement):
    tailNextElement = tailElement.next

    newElement.next = tailNextElement
    newElement.prev = tailElement

    tailNextElement.prev = newElement
    tailElement.next = newElement

    return tailElement


def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "833518929883")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    students = []

    # create a list of student data
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

    # init all student elements
    for i in range(len(students)):
        if i > 0:
            head = insert_front(head, CircDLelement(label = "", e = students[i]))
        else:
            head = CircDLelement(label = "", e = students[i])

    current = head

    # add visual attributes
    for i in range(len(students)):
        current.label = current.value.getName()
        current.visualizer.color = current.value.getLikeColor()

        current.get_link_visualizer(current.next).color = current.value.getDislikeColor()
        current.get_link_visualizer(current.next).thickness = current.value.getCreditHours()*.2

        current.get_link_visualizer(current.prev).color = current.value.getDislikeColor()
        current.get_link_visualizer(current.prev).thickness = current.value.getCreditHours()*.2

        current = current.next

    # set data structure to point to head
    bridges.set_data_structure(head)
    # visualize the circular list
    bridges.visualize()

if __name__ == "__main__":
    main()