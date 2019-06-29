#!/usr/bin/env python
from bridges.element_visualizer import *
from bridges.link_visualizer import *
import re
from decimal import Decimal
import traceback
import sys
# from bridges.kd_tree_element import *



##
# @brief This is the main superclass in BRIDGES for  deriving a number of
# 	objects used  in building arrays, lists, trees and graph data structures.
#  SLelement, DLelement, CircSLelement, CircDLelement, TreeElement, BinTreeElement,
#	BSTElement, CircSLelement, CircDLelement, AVLTreeElement are all subclasses
#  (see class hierarchy above).  Element contains  two
#	visualizer objects (ElementVisualizer, LinkVisualizer) for specifying
#	visual attributes for nodes and links respectively. It also contains a label that
#	that can be displayed in BRIDGES visualizations.
#
#  All the tutorials under
#
#	http://bridgesuncc.github.io/Hello_World_Tutorials/Overview.html
#
#  illustrate examples of using different types of Element objects and how to
#	manipulate their visual attributes.
#
# @author Mihai Mehedint, Kalpathi Subramanian
#
#
class Element():
    ids = 0

    #
    # 	this is the number of pattern matches where the new string
    #  	can be inserted; useful in case we insert line breaks at a
    #  	desired number of characters is the pattern is change to
    # 	white space this index can be changed to 2 words to insert a
    # 	line break every 2 words
    word_number = 0

    # this is the string value that replaces the pattern found in the label
    INSERT_STRING = "\\n"

    # 	for more complex patterns the key must be changed
    # 	like so "((John) (.+?))" returns "John firstWordAfterJohn":
    # 	John writes, John doe, John eats etc.
    # 	(\\w) matches any word (\\d) any digit (\\D) any non digit
    # 	(\\s) a white space (\\s*) zero or more whitespaces, (\\s+)
    # 	one or more
    DIVIDE_KEY = "(\r?\n)|(\n)|(\f)|(\r)|(%n)"

    def _get_data_structure_type(self) -> str:
        """
        Get the data structure representation
        Returns:
            str
        """
        return "Element"

    def __init__(self, **kwargs) -> None:
        """
        Element constructor
        creates an Element Visualizer and unique identifier for the current element
        kwargs:
            label: the string that is visible on the bridges Visualization
            val: generic parameter value used to construct Element
            original: element object to copy
        Returns:
            None
        """
        Element.ids += 1
        self._link_visualizer = dict()
        self._ids = Element.ids
        self._identifier = str(self._ids)
        self._label = "Default"
        self._visualizer = ElementVisualizer()
        if 'val' in kwargs:
            self._value = kwargs['val']
            if 'label' in kwargs:
                self._label = kwargs['label']
        elif 'original' in kwargs:
            self._visualizer = ElementVisualizer(kwargs['original'].get_visualizer())
            self._label = str(kwargs['original'].label)
            self.value = kwargs['original'].value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def identifier(self) -> str:
        """
        Getter for the element identifier
        Return:
            str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, id: int) -> None:
        """
        Setter for the element identifier
        Args:
            int id: the identifier
        Returns:
            None
        """
        self._identifier = id

    @property
    def visualizer(self) -> ElementVisualizer:
        return self._visualizer

    @visualizer.setter
    def visualizer(self, vis: ElementVisualizer) -> None:
        self._visualizer = vis

    def get_link_visualizer(self, el) -> LinkVisualizer:
        """
        Get the link visualizer object that links this element to another element specified by the argument.
        Args:
            el: the element terminating the link
        Returns:
            LinkVisualizer
        """
        #  if this is the first time, must create the
        #  link visualizer
        try:
            if (type(el) != Element):
                raise ValueError("Wrong type, Needs to be Element.")
        except Exception as e:
            #print stack if exception thrown
            tb = sys.exc_info()
            traceback.print_tb(tb)
        if el in self._link_visualizer:
            return self._link_visualizer[el]
        else:
            self._link_visualizer[el] = LinkVisualizer()
            return self._link_visualizer[el]

    def set_link_visualizer(self, el):
        self._link_visualizer[el] = LinkVisualizer()

    def remove_link_visualizer(self, el):
        self._link_visualizer.pop(el)

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    @property
    def size(self):
        return self.visualizer.get_size()

    @size.setter
    def size(self, sz):
        self.visualizer.set_size(sz)

    @property
    def color(self):
        return self.visualizer.get_color()

    @color.setter
    def color(self, col):
        self.visualizer.set_color(col)

    @property
    def opacity(self):
        return self.visualizer.get_opacity()

    @opacity.setter
    def opacity(self, o):
        self.visualizer.set_opacity(o)

    @property
    def shape(self):
        return self.visualizer.shape

    @shape.setter
    def shape(self, sh):
        self.visualizer.shape = sh

    def set_location(self, locX, locY):
        self.visualizer.set_location(locX, locY)

    def get_location(self):
        self.visualizer.get_locationX()

    def get_locationX(self):
        return self.visualizer.get_locationX()

    def get_locationY(self):
        return self.visualizer.get_locationY()

    def get_element_representation(self):
        json = {
            "name": str(self.label),
            "shape": str(self.visualizer.shape),
            "size": str(self.visualizer.get_size()),
            "color": [str(self.visualizer.get_color().get_red()), str(self.visualizer.get_color().get_green()),
                      str(self.visualizer.get_color().get_blue()), str(self.visualizer.get_color().get_alpha())]
        }
        loc_flag = not ((self.visualizer.get_locationX() == Decimal('Infinity')) or (self.visualizer.get_locationY() == Decimal('Infinity')))
        if loc_flag:
            json['location'] = [str(self.visualizer.get_locationX()), str(self.visualizer.get_locationY())]
        if self._get_data_structure_type() == "KDTree":
            kdt = self
            json['key'] = str(kdt.get_key())
            json['dimension'] = str(kdt.get_dimension())
            json['thickness'] = str(kdt.get_thickness())
        if self._get_data_structure_type() == "BinarySearchTree":
            bst = self
            json['key'] = str(bst.key)
        if self._get_data_structure_type() == "AVLTree":
            avl = self
            json['key'] = str(avl.key)
            json['height'] = str(avl.get_height())
            json['balance_factor'] = str(avl.get_balance_factor())
        return json

    def get_link_representation(self, lv, src, dest):
        link_json = lv.get_link_properties()
        link_json["source"] = src
        link_json["target"] = dest
        return link_json
