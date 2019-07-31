from bridges.bridges import *
from bridges.data_src_dependent.data_source import *

# Given an SLelement with an EarthquakeUSGS value, set various visual properties
def setProperties(el):
    # Get the magnitude of the earthquake from the SLelement
    # (the EarthquakeUSGS object stored as the value inside the SLelement
    magnitude = el.value.magnitude

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
    el.color = color

    # Set the size of the element based on the magnitude
    el.size = magnitude * 5

    # set the shape of the element based on the location
    if ("Alaska" in el.value.location):
        el.shape = "diamond"
    elif ("Hawaii" in el.value.location):
        el.shape = "cross"


class ListEQ:
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
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
        element.label = myList[i].title

        #Pass the element to a fucntion to set its visual properties
        setProperties(element)

        #add 'next pointer where appropriate
        if i > 0:
            prev.next = element
        else:
            #Set the head pointer
            head = element
        #Update the prev pointer
        prev = element

    #Pass the head of the list Bridges
    bridges.set_data_structure(head)

    #Visualize the list
    bridges.visualize()
