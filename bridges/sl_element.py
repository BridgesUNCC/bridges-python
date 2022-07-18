#!/usr/bin/env python
from bridges.element import *
import copy


class SLelement(Element):
    """
    @brief This class can be used to instantiate Singly Linked Elements.
    
    This class extends Element and takes a generic parameter <E>
    representing application specific data. This element forms the basic
    building block for singly linked lists. Singly linked elements have a field
    pointing to the next element along the list.
    
    Elements contain a visualizer (ElementVisualizer) object for setting visual
    attributes (color, shape, opacity, size), necessary for displaying them in a
    web browser.
    
    Elements also have a LinkVisualizer object, that is used when they are linked to
    another element, appropriate for setting link attributes, for instance, between
    the current element and its next element.
    
    @author Matthew Mcquaigue
    @date  2018, 6/24/19, 2021
    
    \sa Singly Linked List tutorial : https://bridgesuncc.github.io/tutorials/SinglyLinkedList.html
    """

    def __init__(self, **kwargs) -> None:
        """
        Conctructor for SLelement object
        Kwargs:
            (Generic) e: the generic object that this SLelement will hold
            (str) label: the label of the SLelement that shows up on the bridges visualization
            (Element) next: the element that should be assigned to the next pointer
        Returns:
            None
        """
        super(SLelement, self).__init__(val=kwargs.get('e'), label=kwargs.get('label'))
        self._next = kwargs.get('next')


    def get_data_structure_type(self) -> str:
        """
        Getter for the data structure type
        Returns:
            str: representing the data structure type
        """
        return "SinglyLinkedList"


    @property
    def next(self):
        """
        Getter for element following this element
        Returns:
            SLelement
        """
        return self._next

    @next.setter
    def next(self, n) -> None:
        """
        Setter for the element following this element
        Args:
            n: the element to be assigned to next
        Returns:
            None
        """
        self._next = n
        if n is not None:
            self.set_link_visualizer(n)

    @property
    def value(self):
        """
        Getter for the SLelement value to hold
        Returns:
            Element
        """
        return super(SLelement, self).value

    @value.setter
    def value(self, val):
        """
        Setter for the value that this SLelement will hold
        Args:
            val: the value that this SLelment will hold
        Returns:
            None
        """
        super(SLelement, self).value = val

    def list_helper(start):
        """
        helper method for graph adjacency list
        """
        if start is None:
            return
        node = start
        while node.next is not None:
            yield node.value
            node = node.next
        yield node.value

    def get_data_structure_representation(self) -> dict:
        """
        Getter for this data structure representation
        Returns:
            dict: representing the JSON before dumping
        """
        node_map = dict()# map to reorder the nodes for building JSON
        nodes = []# get the list nodes
        self.get_list_elements(nodes)
        nodes_JSON = []# generate the JSON of the list nodes
        k = 0
        while k < len(nodes):
            node_map[nodes[k]] = k
            nodes_JSON.append(nodes[k].get_element_representation())
            k += 1

        links_JSON = []
        k = 0
        while k < len(nodes):
            par = nodes[k]
            chld = par.next
            if chld is not None:
                #  add the link
                links_JSON.append(self.get_link_representation(par.get_link_visualizer(chld),
                                                               str(node_map.get(par)), str(node_map.get(chld))))
            k += 1
        #add the link
        json_dict = {
            "nodes": nodes_JSON,
            "links": links_JSON
        }
        return json_dict



    def get_list_elements(self, nodes):
        """
        Get the elements of the list (for  internal use only)
        Args:
            nodes: a vector of the nodes in the list
        Returns:
            elements of list
        """
        el = self
        #try to handle all lists in subclasses, except multilists
        nodes.clear()
        while el is not None:
            nodes.append(el)
            el = el.next
            #  handle circular lists
            if el == self:
                break

    def iterator(self):
        """
        used for range loops
        """
        return SLelementIterator(self)


class SLelementIterator():

    def __init__(self, current):
        self.current = current

    def has_next(self):
        return self.current is not None

    def next(self):
        if not self.has_next():
            raise StopIteration

        self.current = self.current.next
        return self.current
