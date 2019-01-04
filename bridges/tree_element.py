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
    # holds all children of the node
    children = []

    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    ##
    # Constructs an TreeElement
    # set to null.
    # @param e the generic object that TreeElement will hold
    # @param label the label of TreeElement that shows up on the bridges
    # @param left the TreeElement to be assigned to the child 0
    # @param right the TreeElement to be assigned to the child 1
    #
    def __init__(self, label=None, e=None, left=None, right=None):
        if label is None and e is None and left is None and right is None:
            super(TreeElement, self).__init__()
            self.children = []
        if e is not None and label is None and left is None and right is None:
            super(TreeElement, self).__init__(val = e)
            self.children = []
        elif e is not None and left is not None and right is not None:
            super(TreeElement, self).__init__(val = e)
            self.children = []
            self.children.append(left)
            self.children.append(right)
        elif e is None and left is not None and right is not None:
            super(TreeElement, self).__init__()
            self.children = []
            self.children.append(left)
            self.children.append(right)
        elif label is not None and e is not None and left is None and right is None:
            super(TreeElement, self).__init__(label = label, val = e)
            self.children = []
        elif e is not None and label is None and left is None and right is None:
            super(TreeElement, self).__init__(val = e)
            self.children = []



    ##
    # 	This method gets the data structure type
    #
    # 	@return  The date structure type as a string
    #
    def get_data_structure_type(self):
        return "Tree"

    ##
    #   Adds a child to the node

    def add_child(self, child):
        self.children.append(child)

    ##
    #
    #  Returns the number of children at this node
    #
    #  @return  number of children

    def get_number_of_children(self):
        return len(self.children)

    ##
    # 	adds a child to the node - will be added at the next open position
    #
    #  @param  child to be added
    #
    #  @return none
    def set_child(self, index, child):
        if index < len(self.children):
            self.children[index] = child

    ##
    # 	gets a child at a particular index
    #
    #  @param  index into the list of children
    #
    #  @return child to be returned
    #
    #
    def get_child(self, index):
        if index < len(self.children):
            return self.children[index]
        else:
            return None

    ##
    # 	Get  hierarchical JSON of the tree representation
    #
    # 	@return the JSON string
    #
    def get_data_structure_representation(self):
        json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_CURLY + self.pre_order(self) + self.CLOSE_CURLY + self.CLOSE_CURLY
        return json_str

    ##
    # 	Use a preorder traversal to directly extract a hierarchical JSON
    # 	representation of the tree.
    #
    #
    def pre_order(self, root):
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
                    json_str += self.pre_order(root.get_child(k))
                    json_str += self.CLOSE_CURLY + self.COMMA
                k += 1
            #  process its children
            #  remove last comma
            if len(json_str) > 0:
                json_str = json_str[0: len(json_str) - 1]
            #  end of children
            json_str += self.CLOSE_BOX
        return json_str
