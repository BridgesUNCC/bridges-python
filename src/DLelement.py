#!/usr/bin/env python
# package: bridges.base
from SLelement import *


##
#
# 	@author Mihai Mehedint, Kalpathi Subramanian
#
#	@date 6/22/16, 1/7/17, 5/17/17
#
# 	@brief This class is used to create doubly linked element objects.
#
#	This class extends Element and takes a generic parameter <E> representing
#	application specific data. This element forms the basic building block for
#	doubly linked lists. Doubly linked elements have two links,
# 	"next" and "previous", that point to the previous and succeeding nodes along the list.
#
#	Elements contain a visualizer (ElementVisualizer) object for setting visual
#	attributes (color, shape, opacity, size), necessary for displaying them in a web
#	browser.
#
#	Elements also have a LinkVisualizer object that is used when they are linked to
#	another element, appropriate for setting link attributes, such as in linked lists,
#	between the current element and its next or previous nodes.
#
#	@param <E> The generic parameter object that is part of this element, representing
#          application specific data.
#
#	\sa Example Tutorial at <br>
#		http://bridgesuncc.github.io/Hello_World_Tutorials/DLL.html
#
class DLelement(SLelement):
    prev = object()

    ##
    #	Constructs an empty DLelement with next and prev pointers set to null.
    #
    def __init__(self, next = None, prev = None, e = None):
        if next is not None:
            SLelement.set_next(self, next)
        if prev is not None:
            self.set_prev(prev)
        if e is not None:
            super(DLelement, self).__init__(e)
        else:
            self.prev = None
            super(DLelement, self).__init__()

    ##
    #	This method gets the data structure type
    #
    #	@return  The date structure type as a string
    #
    def get_data_structure_type(self):
        return "DoublyLinkedList"

    ##
    # This method returns the pointer to the next DLelement
    #
    # @return the DLelement assigned to the next pointer
    #
    def get_next(self):
        return self.next

    ##
    # This method sets the pointer to the next DLelement
    #
    # @param next the DLelement that should be assigned to the next pointer
    #
    #
    #
    # 		public void setNext(DLelement<E> nxt) {
    # 			this.next = nxt;
    # 			if (nxt != null)
    # 				this.setLinkVisualizer(nxt);
    # 		}
    #
    #
    # This method returns the pointer to the previous DLelement
    #
    # @return the DLelement assigned to the prev pointer
    #
    def get_prev(self):
        return self.prev

    ##
    # This method sets the pointer to the previous DLelement
    #
    # @param prev the DLelement that should be assigned to the prev pointer
    #
    def set_prev(self, prv):
        #  first remove any existing link visualizer from this node
        # 	to its next node
        if self.prev is not None:
            self.remove_link_visualizer(self.prev)
        self.prev = prv
        #  add a new link visualizer
        if prv is not None:
            self.set_link_visualizer(prv)

    ##
    #	Get the JSON representation of the the data structure
    #
    def get_data_structure_representation(self):
        #  map to reorder the nodes for building JSON
        node_map = dict()
        #  get teh list nodes
        nodes = []
        SLelement.get_list_elements(self, nodes)
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
            nxt = par.next
            prv = par.prev
            if nxt is not None:
                #  add the link
                links_JSON += self.get_link_representation(par.get_link_visualizer(nxt),str(node_map.get(par)), str(node_map.get(nxt)))
                links_JSON += self.COMMA
            if prv is not None:
                #  add the link
                links_JSON += (self.get_link_representation(par.get_link_visualizer(prv), str(node_map.get(par)), str(node_map.get(prv))))
                links_JSON += (self.COMMA)
            k += 1
        #  add the link
        #  add the link
        if len(links_JSON) > 0:
            links_JSON = links_JSON[:-1]
        json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX + str(nodes_JSON) + self.CLOSE_BOX + self.COMMA + self.QUOTE + "links" + self.QUOTE + self.COLON + self.OPEN_BOX + str(links_JSON) + self.CLOSE_BOX + self.CLOSE_CURLY
        return json_str
