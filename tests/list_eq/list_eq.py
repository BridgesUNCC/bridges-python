from bridges.bridges import *
from bridges.sl_element import *
from bridges.data_src_dependent.data_source import *

# Given an SLelement with an EarthquakeUSGS value, set various visual properties
def setProperties(el):
    # Get the magnitude of the earthquake from the SLelement
    # (the EarthquakeUSGS object stored as the value inside the SLelement
    magnitude = el.get_value().get_magnitude()

    # Pick the color depending on the magnitude
    if magnitude < 1.0:
        color = "blue"
    elif magnitude < 2.0:
        color = "green"
    elif magnitude < 3.0:
        color = "yellow"
    elif magnitude < 4.0:
        color = "orange"
    elif magnitude < 5.0:
        color = "red"
    elif magnitude < 6.0:
        color = "purple"
    else:
        color = "black"

    # Set the color of the element
    el.get_visualizer().set_color(color)

    # Set the size of the element based on the magnitude
    el.get_visualizer().set_size(magnitude * 5)

    # set the shape of the element based on the location
    if ("Alaska" in el.get_value().get_location()):
        el.get_visualizer().set_shape("diamond")
    elif ("Hawaii" in el.get_value().get_location()):
        el.get_visualizer().set_shape("cross")


class ListEQ:

    #Init a Bridges Connection with your credentials
    bridges = Bridges(36, "test", "211416381091")

    #Set assignment title
    bridges.set_title("ListEQ Example")

    bridges.connector.set_server("local")

    #Get a List od USGS Earthquake Tweet objects from Bridges
    myList = get_earthquake_usgs_data(150)

    #Set prev and head elements
    prev = SLelement()
    head = SLelement()

    for i in range(len(myList)):

        #Create each new SLelement
        element = SLelement(e = myList[i])

        #Set the element label equal to the Title (print it out for sanity check)
        element.set_label(myList[i].get_title())

        #Pass the element to a fucntion to set its visual properties
        setProperties(element)

        #add 'next pointer where appropriate
        if i > 0:
            prev.set_next(element)
        else:
            #Set the head pointer
            head = element
        #Update the prev pointer
        prev = element

    #Pass the head of the list Bridges
    bridges.set_data_structure(head)

    #Visualize the list
    bridges.visualize()
