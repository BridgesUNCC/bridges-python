#!/usr/bin/env python
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
#	@author Kalpathi Subramanian, Matthew McQuaigue
#
#	@date 6/22/16, 1/7/17, 5/17/17
#
#
class CircSLelement(SLelement):

    def __init__(self, **kwargs) -> None:
        """
        The constructor for a Circular Singly Linked Element
        Args:
            e: the generic object that this CircSLelement will hold
            label: The label of this CircSLelement
            next: The CircSLelement that should be assigned to the next pointer
        Returns:
            None
        """
        if 'e' in kwargs:
            if 'label' in kwargs:
                if 'next' in kwargs:
                    super(CircSLelement, self).__init__(e=kwargs['e'], label=kwargs['label'],
                                                        next = kwargs['next'])
                else:
                    super(CircSLelement, self).__init__(e=kwargs['e'], label=kwargs['label'])
            else:
                super(CircSLelement, self).__init__(e=kwargs['e'])
        else:
            super(CircSLelement, self).__init__()
            self.set_next(self)

    def _get_data_structure_type(self) -> str:
        """
        Gets the data structure type
        Returns:
            str
        """
        return "CircularSinglyLinkedList"

    @property
    def next(self):
        """
        Getter for the next element of this CircSLelement
        Returns:
            Generic object
        """
        return self.next