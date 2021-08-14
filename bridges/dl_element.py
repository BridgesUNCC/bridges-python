#!/usr/bin/env python
from bridges.sl_element import *

class DLelement(SLelement):
    """
    @brief This class is used to create doubly linked element objects.
    
    This class extends Element and takes a generic parameter <E> representing
    application specific data. This element forms the basic building block for
    doubly linked lists. Doubly linked elements have two links,
    "next" and "previous", that point to the previous and succeeding nodes along the list.
    
    Elements contain a visualizer (ElementVisualizer) object for setting visual
    attributes (color, shape, opacity, size), necessary for displaying them in a web
    browser.
    
    Elements also have a LinkVisualizer object that is used when they are linked to
    another element, appropriate for setting link attributes, such as in linked lists,
    between the current element and its next or previous nodes.
    
    @author Mihai Mehedint, Kalpathi Subramanian
    @date  2018, 6/24/19
    
    \sa Doubly Linked List tutorial : https://bridgesuncc.github.io/tutorials/DoublyLinkedList.html
    """


    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor for DLelement
        Kwargs:
            (object) e: the genereic application specific object that DLelement is holding
            next: the DLelement that should be assigned to the next pointer
            prev: the DLelement that should be assigned to the prev pointer
            (str) label: the label for this DLelement
        Return:
            None
        """
        super(DLelement, self).__init__(**kwargs)
        self._next = kwargs.get('next')
        self._prev = kwargs.get('prev')


    def get_data_structure_type(self) -> str:
        """
        This method gets the data structure type
        Returns:
            str: representing the data structure type
        """
        return "DoublyLinkedList"

    @property
    def next(self):
        """
        Getter for the next element in Dlelement
        Returns:
            element pointed to by this element
        """
        return self._next

    @next.setter
    def next(self, el):
        """
        Setter for the next element
        Args:
            el: element to be set 
        Returns:
            None
        """
        self._next = el

    @property
    def prev(self):
        """
        Getter for the prev element in Dlelement
        Returns:
            element that is prior to this element
        """
        return self._prev

    @prev.setter
    def prev(self, el):
        """
        Setter for the prev element
        Args:
            el: element to be set

        Returns:
            None
        """
        #remove any existing link visualizer from this node
        if self._prev is not None:
            self.remove_link_visualizer(self._prev)
        self._prev = el
        #  add a new link visualizer
        if el is not None:
            self.set_link_visualizer(el)

    def get_data_structure_representation(self) -> dict:
        """
        Getter for the json representation of this list
        Returns:
            dict: representing the JSON format
        """
        #  map to reorder the nodes for building JSON
        node_map = dict()
        #  get teh list nodes
        nodes = []
        SLelement.get_list_elements(self, nodes)
        #  generate the JSON of the list nodes
        nodes_JSON = []
        k = 0
        while k < len(nodes):
            node_map[nodes[k]] = k
            nodes_JSON.append(nodes[k].get_element_representation())
            k += 1
        links_JSON = []
        k = 0
        while k < len(nodes):
            par = nodes[k]
            nxt = par.next
            prv = par.prev
            if nxt is not None:
                #  add the link
                links_JSON.append(self.get_link_representation(par.get_link_visualizer(nxt), str(node_map.get(par)), str(node_map.get(nxt))))
            if prv is not None:
                #  add the link
                links_JSON.append(self.get_link_representation(par.get_link_visualizer(prv), str(node_map.get(par)), str(node_map.get(prv))))
            k += 1
        #  add the link
        json_dict = {
            "nodes": nodes_JSON,
            "links": links_JSON
        }
        return json_dict

    def reverse_iterator(self):
        """
        This iterator is used with range loops
        """
        return DLelementReverseIterator(self)

class DLelementReverseIterator():

    def __init__(self, current):
        self.current = current

    def has_next(self):
        return self.current is not None

    def next(self):
        ret = self.current.value
        self.current = self.current.prev
        return ret
