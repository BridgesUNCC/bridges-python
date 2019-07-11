from bridges.bridges import *
from tests.StudentInfo import *
from bridges.circ_sl_element import *

def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "833518929883")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

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


    head = CircSLelement(label = "", e = students[0])
    current = head

    for i in range(1, len(students)):
        current.next = CircSLelement(label = "", e = students[i])

        # handle the last element
        if i is len(students)-1:
            # getting the last element
            current = current.next

            # point the last element to the first element
            # so the list becomes circular
            current.next = head
        # set the current element to be the next element
        current = current.next

    current = head

    # add visual attributes
    for i in range(len(students)):

        current.label = current.value.getName()
        current.visualizer.color = current.value.getLikeColor()

        current.get_link_visualizer(current.next).color = current.value.getDislikeColor()

        current.get_link_visualizer(current.next).thickness = current.value.getCreditHours() *.03

        current = current.next

    bridges.set_data_structure(head)
    bridges.visualize()

if __name__ == "__main__":
    main()
