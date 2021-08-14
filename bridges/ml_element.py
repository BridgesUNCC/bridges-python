#!/usr/bin/env python
from bridges.sl_element import *

class MLelement(SLelement):
    """
    @brief This class can be used to instantiate Multi-list Elements.
    
    This class extends SLelement (singly linked list element) to build multi-lists;
    Multilist elements contain a tag (boolean) that indicates if the element 
    contains a sublist or not; if the tag is true, then there is a sublist beginning
    at this node and the starting point is the `sublist' field in the element. 
    If the tag is false, then the list continues as a normal singly linked list. 
    The sublists are re recursive: any sublist can have its own sublists and so on.
    As in singly linked elements, the next pointer points to the following list element and 
    each element contains a generic application specific object.
    
    Multi-list elements contain a visualizer (ElementVisualizer) object for setting
    visual attributes (color, shape, opacity, size), necessary for displaying
    them in a web browser.
    
    Elements also have a LinkVisualizer object, that is used when they are linked to
    another element, appropriate for setting link attributes, for instance, between
    the current element and its next element. In this case, the link in question is that
    which connects the element to the following elements; a similar logic follows for
    sublists.
    
    @author Kalpathi Subramanian, Matthew McQuaigue
    
    @date 2018, 7/23/19, 2021
    
    \sa There is a tutorial about Multi Lists : https://bridgesuncc.github.io/tutorials/MultiList.html
    """

    def __init__(self, **kwargs) -> None:
        """
        Constructor for MLelement
        Args:
            (str) label: the label the SLelement will hold and show on bridges visualization
            (object) e: the generic object/value that this SLelement will hold
            (object) next: the next element that will be assigned to this SLelement next pointer
            sublist: the MLelement that is the beginning of a sublist
        Returns:
            None
        """
        if 'e' in kwargs:
            if 'label' in kwargs:
                super(MLelement, self).__init__(e=kwargs['e'], label=kwargs['label'])
            else:
                super(MLelement, self).__init__(e=kwargs['e'])
        else:
            super(MLelement, self).__init__()
        if 'next' in kwargs:
            super(MLelement, self).next = kwargs['next']
        if 'sublist' in kwargs:
            self._sublist = kwargs['sublist']
            self._tag = True
            self.set_link_visualizer(kwargs['sublist'])
        else:
            self._sublist = None
            self._tag = False

    @property
    def sub_list(self):
        """
        Getter for the sublist at this node if exists
        Returns:
            Element: the sublist head element
        """
        return self._sub_list

    @sub_list.setter
    def sub_list(self, sl) -> None:
        """
        Setter for the start of a new sublist
        Args:
            sl: the MLelement that is the beginning of a sublist
        Returns:
            None
        """
        self._sub_list = sl
        if sl is not None:
            self._tag = True
            self.set_link_visualizer(sl)
        self._default_sub_list_nodes()

    def _default_sub_list_nodes(self) -> None:
        """
        function for setting sublist defaults
        Returns:
            None
        """
        #by default, color and shape sublist nodes to distinguish them  from
        #remaining nodes
        self.visualizer.color = "red"
        self.visualizer.shape = "square"

    def get_data_structure_type(self) -> str:
        """
        Getter for the data structure type
        Returns:
            str: representing the type
        """
        return "MultiList"

    @property
    def next(self):
        """
        Retrieves the element following this element
        Returns:
            MLelement
        """
        return super(MLelement, self).next

    @next.setter
    def next(self, n):
        SLelement.next.fset(self, n)

    @property
    def tag(self) -> bool:
        """
        Getter for the tag of the element
        Returns:
             bool
        """
        return self._tag

    @tag.setter
    def tag(self, t) -> None:
        """
        Setter for the tag of the element
        Args:
            t: boolean value
        Returns:
            None
        """
        self._tag = t

    def get_data_structure_representation(self) -> dict:
        """
        Getter for the data structure representation
        Returns:
            dict: representing the json structure before dumping
        """
        nodes = []
        nodes.clear()
        self.get_list_elements(nodes)
        nodes_JSON = []
        node_map = dict()
        for i in range(0, len(nodes)):
            node_map[nodes[i]] = i
            nodes_JSON.append(nodes[i].get_element_representation())
        links_JSON = []
        for j in range(0, len(nodes)):
            par = nodes[j]
            if par.tag:
                chld = par.sub_list
                #  sub list
                if chld is not None:
                    #  add the link
                    links_JSON.append(self.get_link_representation(par.get_link_visualizer(chld),
                                                                   str(node_map.get(par)), str(node_map.get(chld))))
            chld = par.next
            if chld is not None:
                #  add the link
                links_JSON.append(self.get_link_representation(par.get_link_visualizer(chld),
                                                               str(node_map.get(par)), str(node_map.get(chld))))
        json_dict = {
            "nodes": nodes_JSON,
            "links": links_JSON
        }
        return json_dict

    def get_list_elements(self, nodes):
        """
        Getter for the elements of the list
        Args:
            nodes: a list of the nodes
        Returns:
            element
        """
        self._get_list_elements_R(self, nodes)


    def _get_list_elements_R(self, list, nodes):
        el = list
        while el is not None:
            nodes.append(el)
            if el.tag:
                self._get_list_elements_R(el.sub_list, nodes)
            el = el.next
