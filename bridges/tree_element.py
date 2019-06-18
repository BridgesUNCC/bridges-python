#!/usr/bin/env python
from bridges.element import *
from bridges.link_visualizer import *


 ## @brief This class extends Element to represent general trees with
 #	arbitrary number of children.
 #
 # 	TreeElement nodes can have an arbitrary number of child nodes(held in
 # 	in a vector in the order in which they were added). The
 # 	visualization of trees assumes that the children are drawn in order
 # 	from left to right.
 #
 #  Tree Elements have labels (string) that are displayed on the visualization.
 #  Elements take an generic object E as a user defined parameter, which can be
 #  any native type or object.
 #
 #  Elements contain a visualizer (ElementVisualizer) object for setting visual
 #  attributes (color, shape, opacity, size), necessary for displaying them in a web
 #  browser.
 #
 #  Elements also have a LinkVisualizer object that is used when they are
 #  linked to another element, appropriate for setting link attributes, between parent
 # 	and child nodes.
 #
 # 	@author Matthew McQuaigue
 #
class TreeElement(Element):

    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    def __init__(self, **kwargs) -> None:
        """
        Constructor for Tree Element
        Kwargs:
            label: The label for the tree element that shows in visualization
            e: the generic object that the tree element will hold
            left: the tree element assigned to child 0
            right: the tree element assigned to child 1
        Returns:
            None
        """
        self.children = []
        if 'label' in kwargs and 'e' in kwargs:
            super(TreeElement, self).__init__(label = kwargs['label'], val = kwargs['e'])
        elif 'e' in kwargs:
            super(TreeElement, self).__init__(val = kwargs['e'])
        else:
            super(TreeElement, self).__init__()
        if 'left' in kwargs:
            self.children.append(kwargs['left'])
        if 'right' in kwargs:
            self.children.append(kwargs['right'])


    def _get_data_structure_type(self) -> str:
        """
        Gets the data structure type
        Returns:
            str
        """
        return "Tree"

    def add_child(self, child) -> None:
        """
        Adds a child to this parent node
        Args:
            child: the child node to add
        Returns:
            None
        """
        self.children.append(child)

    def get_number_of_children(self) -> int:
        """
        The number of children of this node
        Returns:
            int
        """
        return len(self.children)

    def set_child(self, index: int, child) -> None:
        """
        Adds a child to the node - will be added at the next open position
        Args:
            index: index to add child
            child: child to add to tree
        Returns:
            None
        Raises:
            value error
        """
        if index < len(self.children):
            self.children[index] = child
        else:
            raise ValueError("Index is higher than number of children")

    def get_child(self, index: int):
        """
        Gets a child at particular index
        Args:
            index: index to get child
        Returns:
            object
        Raises:
            value error
        """
        if index < len(self.children):
            return self.children[index]
        else:
            raise ValueError("Index is higher than number of children")

    def _get_data_structure_representation(self) -> str:
        """
        Get the hierarchical JSON of the tree representation
        Returns:
            str
        """
        json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_CURLY + self._pre_order(self) + self.CLOSE_CURLY + self.CLOSE_CURLY
        return json_str

    ##
    # 	Use a preorder traversal to directly extract a hierarchical JSON
    # 	representation of the tree.
    #
    #
    def _pre_order(self, root):
        k=0
        json_str = ""
        children = ""
        link_props = ""
        elem_rep = ""
        t_str = str()
        num = root.get_number_of_children()
        if root is not None:
            #  first get the node representation
            elem_rep = root.get_element_representation()
            #  remove surrounding curly braces
            t_str = elem_rep[1: len(elem_rep) - 1]
            json_str += t_str
            #  now get the children
            if root.get_number_of_children() > 0:
                json_str += self.COMMA + self.QUOTE + "children" + self.QUOTE + self.COLON + self.OPEN_BOX

            while k < root.get_number_of_children():

                if root.get_child(k) is None:
                    json_str += self.OPEN_CURLY + self.QUOTE + "name" + self.QUOTE + self.COLON + self.QUOTE + "NULL" + self.QUOTE + self.CLOSE_CURLY + self.COMMA
                else:
                    lv = LinkVisualizer()
                    lv = root.get_link_visualizer(root.get_child(k))
                    json_str += self.OPEN_CURLY
                    if lv is not None:
                        json_str += self.QUOTE + "linkProperties" + self.QUOTE + self.COLON + self.OPEN_CURLY + self.QUOTE + "color" + self.QUOTE + self.COLON + self.OPEN_BOX + str(lv.get_color().get_red()) + self.COMMA + str(lv.get_color().get_green()) + self.COMMA + str(lv.get_color().get_blue()) + self.COMMA + str(lv.get_color().get_alpha()) + self.CLOSE_BOX + self.COMMA + self.QUOTE + "thickness" + self.QUOTE + self.COLON + str(lv.get_thickness()) + self.CLOSE_CURLY + self.COMMA
                    else:
                        json_str += "linkProperties" + self.COLON + "{}" + self.COMMA
                    #  process its children
                    json_str += self._pre_order(root.get_child(k))
                    json_str += self.CLOSE_CURLY + self.COMMA
                k += 1
            #  process its children
            #  remove last comma
            if len(json_str) > 0:
                json_str = json_str[0: len(json_str) - 1]
            #  end of children
            json_str += self.CLOSE_BOX
        return json_str
