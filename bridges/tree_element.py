#!/usr/bin/env python
from bridges.element import *

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
 # @date   2018, 7/23/19
 #  \sa Kd tree tutorial http://bridgesuncc.github.io/tutorials/Tree.html
 #
class TreeElement(Element):

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


    def get_data_structure_type(self) -> str:
        """
        Gets the data structure type
        Returns:
            str: representing the data structure type
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
        Get the number of children at this node
        Returns:
            int: representing the number of children
        """
        return len(self.children)

    def set_child(self, index: int, child) -> None:
        """
        Adds a child to the node that will be added at the next open position
        Args:
            index: index to add child
            child: child to add to tree
        Returns:
            None
        Raises:
            ValueError: If the index is higher than the number of children
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
            the child element at this index
        Raises:
            ValueError: if the index is higher than the number of children
        """
        if index < len(self.children):
            return self.children[index]
        else:
            raise ValueError("Index is higher than number of children")

    def get_data_structure_representation(self) -> dict:
        """
        Get the hierarchical JSON of the tree representation (internal use only)
        Returns:
            dict: representing the data structures json 
        """
        json_dict = {
            "nodes": self._pre_order(self)
        }
        return json_dict

    def _pre_order(self, root) -> dict:
        """
        Use a preoreder traversal to directly extract a hierarchical
        JSON representation of the tree
        Args:
            root: the root of the tree structure
        Returns:
            dict: representing the json to be returned
        """
        k=0
        json_str = dict()
        t_str = str()

        if root is not None:
            #  first get the node representation
            elem_rep = root.get_element_representation()
            #  now get the children
            if root.get_number_of_children() > 0:
                json_str["children"] = []
            while k < root.get_number_of_children():
                if root.get_child(k) is None:
                    children_json = {
                        "name": "NULL",
                    }
                    json_str["children"].append(children_json)
                else:
                    lv = root.get_link_visualizer(root.get_child(k))
                    children_json = {}
                    if lv is not None:
                        children_json["linkProperties"] = {
                            "color": [str(lv.get_color().get_red()), str(lv.get_color().get_green()), str(lv.get_color().get_blue()), str(lv.get_color().get_alpha())],
                            "thickness": str(lv.get_thickness())
                        }
                        json_str["children"].append(children_json)
                    else:
                        children_json["linkProperties"] = {}
                        json_str["children"].append(children_json)
                    #  process its children
                    json_str.update(self._pre_order(root.get_child(k)))
            k += 1
        return json_str
