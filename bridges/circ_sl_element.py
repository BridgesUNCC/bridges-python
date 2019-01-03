#!/usr/bin/env python
# package: bridges.base
from bridges.sl_element import *

##
# 	@brief This class can be used to instantiate Singly Linked
#	Circular List Elements.
#	Structurally they are the same as singly linked elements
#  except that each node constructed with the next point pointing to itself;
#  User's implementation of the circularly linked list needs to ensure that
#	the last node points to first node of the list, as the visualization generation is
#	dependent on this.
#
# 	Elements have labels (string) that are displayed on the visualization.
#  Elements take an generic object as a user defined parameter, E, which
#	can be any native type or object.
#
# 	Elements contains a visualizer (ElementVisualizer) object for setting visual
#	attributes (color, shape, opacity, size), necessary for displaying them in a web
#	browser.
#
#  Elements also have a LinkVisualizer object that is used when they are
#	linked to another element, appropriate for setting link attributes, between
#  an element and its next element.
#
#	@author Kalpathi Subramanian
#
#	@date 6/22/16, 1/7/17, 5/17/17
#
#
class CircSLelement(SLelement):
    ##
    #
    # 	This constructor creates an CircSLelement object
    # 	and sets its next pointer to itself
    # @param label the label of CircSLelement
    # @param e the generic object that this CircSLelement will hold
    # @param next the CircSLelement that should be assigned to the next pointer
    #
    def __init__(self, e = None, label = None, next = None):
        if e is not None and label is not None and next is None:
            super(CircSLelement, self).__init__(e = e, label = label)
            self.set_next(self)
        elif e is not None and label is None and next is not None:
            super(CircSLelement, self).__init__(e = e, next = next)
        elif e is None and label is None and next is not None:
            super(CircSLelement, self).__init__(next = next)
        else:
            super(CircSLelement, self).__init__()
            self.set_next(self)

    ##
    #
    #	This method gets the data structure type
    #
    #	@return  The date structure type as a string
    #
    #
    def get_data_structure_type(self):
        return "CircularSinglyLinkedList"

    ##
    #
    # Retrieves the next CircSLelement
    #
    # @return CircSLelement<E> assigned to next
    #
    #
    def get_next(self):
        return self.next

    #  (non-Javadoc)
    #
    # @see java.lang.Object#toString()
    #
    #
    def __str__(self):
        return "CircSLelement [next=" + self.next + ", getNext()=" + self.get_next() + ", getIdentifier()=" + self.get_identifier() + ", getVisualizer()=" + self.get_visualizer() + ", getClassName()=" + self.get_class_name() + ", getElementRepresentation()=" + self.get_element_representation() + ", getLabel()=" + self.get_label() + ", getValue()=" + self.get_value() + ", toString()=" + super(CircSLelement, self).__str__() + ", getClass()=" + self.get_class() + ", hashCode()=" + self.hash_code() + "]"
