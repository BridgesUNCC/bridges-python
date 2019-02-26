#!/usr/bin/env python
from bridges.element import *

##
# 	@brief This class can be used to instantiate Singly Linked Elements.
# 	This class extends Element and takes a generic parameter <E>
#	representing application specific data. This element forms the basic
#	building block for singly linked lists. Singly linked elements have a field
#	pointing to the next element along the list.
#
#
# 	Elements contain a visualizer (ElementVisualizer) object for setting visual
#	attributes (color, shape, opacity, size), necessary for displaying them in a
#	web browser.
#
#	Elements also have a LinkVisualizer object, that is used when they are linked to
#	another element, appropriate for setting link attributes, for instance, between
#	the current element and its next element.
#
#
class SLelement(Element):

    ##
    # This constructor creates an SLelement object
    # and sets the next pointer to null
    # @param label - the label of SLelement that shows up on the bridges visualization
    # @param e  - the generic object that this SLelement will hold
    # @param next - the element that should be assigned to the next pointer
    # 
    def __init__(self, e = None, label = None, next = None):
        if e is not None and label is not None:
            super(SLelement, self).__init__(val = e, label = label)
            self.next = None
        if e is not None and label is None and next is not None:
            super(SLelement, self).__init__(val = e)
            self.set_next(next)
        if e is not None and label is None and next is None:
            super(SLelement, self).__init__(val = e)
            self.next = None
        if e is None and label is None and next is not None:
            self.set_next(next)
        else:
            super(SLelement, self).__init__()
            self.next = next


    ##
    #
    #	This method gets the data structure type
    #
    #	@return  The date structure type as a string
    #
    #
    def get_data_structure_type(self):
        return "SinglyLinkedList"

    ##
    # Retrieves the element following this element
    #
    # @return - SLelement assigned to next
    #
    #
    def get_next(self):
        return self.next

    ##
    # Retrieves the value in the SLelement
    # @return - SLElement value held
    def get_value(self):
        return super(SLelement, self).get_value()
    ##
    # Sets the element to point to the next SLelement
    #
    # @param next - SLelement that should be assigned to the next pointer
    #
    def set_next(self, next):
        self.next = next
        if next is not None:
            self.set_link_visualizer(next)


    def __str__(self):
        return "SLelement [next=" + self.next + ", getNext()=" + self.get_next() + ", getIdentifier()=" + self.get_identifier() + ", getVisualizer()=" + self.get_visualizer() + ", getClassName()=" + self.get_class_name() + ", getElementRepresentation()=" + self.get_element_representation() + ", getLabel()=" + self.get_label() + ", getValue()=" + self.get_value() + ", toString()=" + super(SLelement, self).__str__() + ", getClass()=" + self.getClass() + ", hashCode()=" + self.hashCode() + "]"

    ##
    #	Get the JSON representation of the the data structure
    #
    def get_data_structure_representation(self):
        #  map to reorder the nodes for building JSON
        node_map = dict()
        #  get teh list nodes
        nodes = []
        self.get_list_elements(nodes)
        #  generate the JSON of the list nodes
        nodes_JSON = str()
        k = 0
        while k < len(nodes):
            node_map[nodes[k]] = k
            nodes_JSON += nodes[k].get_element_representation()
            nodes_JSON += self.COMMA
            k += 1
        #  remove the last comma
        if len(nodes) != 0:
            nodes_JSON = nodes_JSON[:-1]
        links_JSON = str()
        k = 0
        while k < len(nodes):
            par = nodes[k]
            chld = par.next
            if chld is not None:
                #  add the link
                links_JSON += (self.get_link_representation(par.get_link_visualizer(chld), str(node_map.get(par)), str(node_map.get(chld))))
                links_JSON += (self.COMMA)
            k += 1
        #  add the link
        if len(links_JSON) > 0:
            links_JSON = links_JSON[:-1]
        json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX + str(nodes_JSON) + self.CLOSE_BOX + self.COMMA + self.QUOTE + "links" + self.QUOTE + self.COLON + self.OPEN_BOX + str(links_JSON) + self.CLOSE_BOX + self.CLOSE_CURLY
        return json_str

    ##
    #	Get the elements of the list
    #
    #	@param nodes  a vector of the ndoes in the list
    #
    #
    def get_list_elements(self, nodes):
        el = self
        #  try to handld all lists in subclasses, except multilists
        nodes.clear()
        while el is not None:
            nodes.append(el)
            el = el.get_next()
            #  handle circular lists
            if el == self:
                break
