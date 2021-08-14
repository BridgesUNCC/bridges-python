#!/usr/bin/env python
from bridges.element import *
import json

class TreeElement(Element):
    """ 
    @brief This class extends Element to represent general trees with
    arbitrary number of children.
    
    TreeElement nodes can have an arbitrary number of child nodes(held in
    in a vector in the order in which they were added). The
    visualization of trees assumes that the children are drawn in order
    from left to right.
    
    Tree Elements have labels (string) that are displayed on the visualization.
    Elements take an generic object E as a user defined parameter, which can be
    any native type or object.
    
    Elements contain a visualizer (ElementVisualizer) object for setting visual
    attributes (color, shape, opacity, size), necessary for displaying them in a web
    browser.
    
    Elements also have a LinkVisualizer object that is used when they are
    linked to another element, appropriate for setting link attributes, between parent
    and child nodes.
    
    @author Matthew McQuaigue
    
    @date   2018, 7/23/19
    \sa Kd tree tutorial https://bridgesuncc.github.io/tutorials/KdTree.html
    """

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
            (0): The label for the tree element that shows in visualization
            (1): the generic object 'e' that the tree element will hold
            (2): the tree element assigned to child 0
            (3): the tree element assigned to child 1
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
        # json_dict = {
        #     "nodes": self._pre_order(self)
        #
        json_dict = ""
        json_dict += "{" + self.QUOTE + "nodes" + self.QUOTE + ":" + "{" + str(self._pre_order(self)) + "}" + "}"
        return json.loads(json_dict)

    def _pre_order(self, root) -> dict:
        """
        Use a preoreder traversal to directly extract a hierarchical
        JSON representation of the tree
        Args:
            root: the root of the tree structure
        Returns:
            dict: representing the json to be returned
        """
        json_str = ""
        children = ""
        link_props = ""
        elem_rep = ""
        t_str = str()
        num = root.get_number_of_children()
        if root is not None:
            elem_rep = root.get_element_representation()
            elem_rep = json.dumps(elem_rep)
            t_str = elem_rep[1:-1]
            json_str = t_str
            if root.get_number_of_children() > 0:
                json_str += "," + self.QUOTE + "children" + self.QUOTE + ":" + "["
            for k in range(0, root.get_number_of_children()):
                if root.get_child(k) is None:
                    json_str += "{" + self.QUOTE + "name" + self.QUOTE + ":" + \
                        self.QUOTE + "NULL" + self.QUOTE + "}" + ","
                else:
                    lv = root.get_link_visualizer(root.get_child(k))
                    json_str += "{"
                    if lv is not None:
                        json_str += self.QUOTE + "linkProperties" + self.QUOTE + ":" + "{" + \
                            self.QUOTE + "color" + self.QUOTE + ":" + \
                            "[" + \
                            str(lv.color.red) + "," + \
                            str(lv.color.green) + "," + \
                            str(lv.color.blue) + "," + \
                            str(lv.color.alpha) + "]" + "," + \
                            self.QUOTE + "thickness" + self.QUOTE + ":" + \
                            str(lv.thickness) + "}" + ","
                    else:
                        json_str += "linkProperties" + ":" + "{}" + ","

                    json_str += str(self._pre_order(root.get_child(k)))
                    json_str += "}" + ","
            if len(json_str) > 0:
                json_str = json_str[0:-1]
            json_str += "]"
        return json_str

        # k = 0
        # json_str = dict()
        # if root is not None:
        #     #  first get the node representationS
        #     elem_rep = root.get_element_representation()
        #     if root.get_number_of_children() > 0:
        #         elem_rep["children"] = []
        #     for i in range(0, root.get_number_of_children()):
        #         if root.get_child(i) is None:
        #             temp = {
        #                 "name": "NULL"
        #             }
        #             elem_rep["children"].append(temp)
        #         else:
        #             lv = root.get_link_visualizer(root.get_child(i))
        #             if lv is not None:
        #                 temp = {
        #                     "linkProperties": {
        #                         "color": [lv.color.red, lv.color.green, lv.color.blue, lv.color.alpha],
        #                         "thickness": lv.thickness
        #                     }
        #                 }
        #                 elem_rep["children"].append(temp)
        #             else:
        #                 temp = {
        #                     "linkProperties": {}
        #                 }
        #                 elem_rep["children"].append(temp)
        #             elem_rep['children'].append(self._pre_order(root.get_child(i)))
        #     json_str = elem_rep
        #
        # return json_str
