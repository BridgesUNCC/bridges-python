#!/usr/bin/env python
## package: bridges.base
from SLelement import *

##
# 	@brief This class can be used to instantiate Multi-list Elements.
# 	This class extends SLelement (singly linked list element) to build multi-lists;
#	Multilist elements contain a tag that indicates if the element is a sublist or not;
#	If the element points to a sublist, then the sublist field is the beginning of
#	this sublist. If not, the data field contains the user specified data item and
#	list continues (getNext()/setNext()). As in singly linked elements, the next pointer
#	points to the following list element of the list or sublist.
#
# 	Multi-list elements contain a visualizer (ElementVisualizer) object for setting
#	visual attributes (color, shape, opacity, size), necessary for displaying
#	them in a web browser.
#
#	Elements also have a LinkVisualizer object, that is used when they are linked to
#	another element, appropriate for setting link attributes, for instance, between
#	the current element and its next element. In this case, the link in question is that
#  which connects the element to the following elements; a similar logic follows for
#	sublists.
#
# @author , Kalpathi Subramanian
#
# @date 5/24/17
#
# @param <E> The generic parameter object that is part of this element, representing
#			either application specific data, or a pointer to a sublist.
#
#	\sa Example Tutorial at <br> ??
#
class MLelement(SLelement):
    sub_list = None

    #  link to a sublist
    tag = False

    ##
    #
    # This constructor creates an SLelement object
    # and sets the next pointer to null
    #
    #
    def __init__(self, label = None, e = None, next = None, sublist = None):
        if label and e is not None:
            super(MLelement, self).__init__(e = e, label = label)
            self.sub_list = None
        if e is not None and label is None:
            super(MLelement, self).__init__(e = e, label = "")
        if next and sublist is not None:
            super(MLelement, self).__init__()
            self.set_next(next)
            self.sub_list = sublist
            if sublist is not None:
                self.tag = True
                self.set_link_visualizer(sublist)
        if label is None and e is None and next is None and sublist is None:
            super(MLelement, self).__init__()
            self.sub_list = None

    ##
    # Sets the start of a new sublist.
    # to the SLelement "next"
    #
    # @param sl the MLelement that is the beginning of a sublist
    #
    def set_sub_list(self, sl):
        self.sub_list = sl
        if sl is not None:
            self.tag = True
            self.set_link_visualizer(sl)
        #  by default, color and shape sublist nodes to distinguish them  from
        # 	remaining nodes
        self.get_visualizer().set_color("red")
        self.get_visualizer().set_shape("square")

    def get_sub_list(self):
        return self.sub_list

    def get_data_structure_type(self):
        return "MultiList"

    def get_next(self):
        return self.next

    def set_tag(self, t):
        self.tag = t

    def get_tag(self):
        return self.tag

    def get_data_structure_representation(self):
        nodes = []
        nodes.clear()
        self.get_list_elements(nodes)
        nodes_JSON = str()
        node_map = dict()
        k = 0
        while k < len(nodes):
            node_map[nodes[k]] = k
            nodes_JSON+=(nodes[k].get_element_representation())
            nodes_JSON+=(self.COMMA)
            k += 1
        if len(nodes) != 0:
            nodes_JSON = nodes_JSON[:-1]
        links_JSON = str()
        k = 0
        while k < len(nodes):
            par = nodes[k]
            if par.tag:
                chld = par.sub_list
                #  sub list
                if chld is not None:
                    #  add the link
                    links_JSON+=(self.get_link_representation(par.get_link_visualizer(chld), str(node_map.get(par)), str(node_map.get(chld))))
                    links_JSON+=(self.COMMA)
            chld = par.next
            if chld is not None:
                #  add the link
                links_JSON+=(self.get_link_representation(par.get_link_visualizer(chld), str(node_map.get(par)), str(node_map.get(chld))))
                links_JSON+=(self.COMMA)
            k += 1
        if len(links_JSON) > 0:
            links_JSON = links_JSON[:-1]
        json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX + nodes_JSON.__str__() + self.CLOSE_BOX + self.COMMA + self.QUOTE + "links" + self.QUOTE + self.COLON + self.OPEN_BOX + links_JSON.__str__() + self.CLOSE_BOX + self.CLOSE_CURLY
        return json_str

    def get_list_elements(self, nodes):
        self.get_list_elements_R(self, nodes)

    def get_list_elements_R(self, list, nodes):
        el = list
        while el is not None:
            nodes.append(el)
            if el.tag:
                self.get_list_elements_R(el.sub_list, nodes)
            el = el.get_next()
