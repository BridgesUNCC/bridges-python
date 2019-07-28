from bridges.dl_element import *
from bridges.bridges import *
from tests.StudentInfo import *

def insert_front(front, new_el):
    if front is None:
        return new_el

    new_el.next = front
    front.prev = new_el

    return new_el

def main():

    # create the Bridges object, set credentials

    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

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
        head = insert_front(head, DLelement(label = "", e = students[i]))

    # add visual attributes
    curr = head
    while curr is not None:
        curr.label = curr.value.name
        curr.visualizer.color = curr.value.getDislikeColor()

        if curr.next is not None:
            next = curr.next
            curr.get_link_visualizer(next).color = curr.value.getDislikeColor()
            next.get_link_visualizer(curr).color = curr.value.getDislikeColor()

        curr = curr.next

    # set dat structure to be visualized
    bridges.set_data_structure(head)
    # visualize the data structure
    bridges.visualize()

if __name__ == "__main__":
    main()
