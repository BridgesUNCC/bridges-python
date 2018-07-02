from Bridges import *
from Student import *
from CircSLelement import *

class CircSLtutorial:
    bridges = Bridges(26, "1343747370122", "test")

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
        current.set_next(CircSLelement(label = "", e = students[i]))

        if i is len(students)-1:
            current = current.get_next()

            current.set_next(head)

        current = current.get_next()

    current = head

    for i in range(len(students)):

        current.set_label(current.get_value().getName())
        current.get_visualizer().set_color(current.get_value().getLikeColor())

        current.get_link_visualizer(current.get_next()).set_color(current.get_value().getDislikeColor())

        current.get_link_visualizer(current.get_next()).set_thickness(current.get_value().getCreditHours() *.03)

        current = current.get_next()

    bridges.set_data_structure(head)
    bridges.visualize()
